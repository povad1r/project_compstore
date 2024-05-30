from flask import Flask, request, render_template, redirect, url_for, session
import sqlite3

app = Flask(__name__)


def get_computers():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM computers")
    computers = cursor.fetchall()
    conn.close()
    return computers


@app.route('/')
def home():
    computers = get_computers()[0:3]
    return render_template('base.html', computers=computers)


def get_page_computers(offset=0, limit=9):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM computers LIMIT ? OFFSET ?", (limit, offset))
    computers = cursor.fetchall()
    conn.close()
    return computers


def get_max_price():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(price) FROM computers")
    max_price = cursor.fetchone()[0]
    conn.close()
    return max_price


def count_computers():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM computers")
    count = cursor.fetchone()[0]
    conn.close()
    return count


def get_unique_pc():
    computers = get_computers()
    unique_videocard = set()
    unique_processor = set()
    unique_ram = set()
    for computer in computers:
        unique_videocard.add(computer[3])
        unique_processor.add(computer[4])
        unique_ram.add(computer[5])
    return unique_ram, unique_processor, unique_videocard


@app.route('/computers')
@app.route('/computers/<int:page>')
def computers(page=1):
    limit = 9
    offset = (page - 1) * limit
    computers = get_page_computers(offset, limit)
    total_computers = count_computers()
    total_pages = (total_computers + limit - 1) // limit
    has_prev = page > 1
    has_next = page < total_pages
    prev_page = page - 1
    next_page = page + 1
    unique_details = get_unique_pc()
    max_price = get_max_price()

    user_favorite_computers = []
    if 'logged_in' in session and session['logged_in']:
        user_id = session['user_id']
        user_favorite_computers = get_user_favorite_computers(user_id)

    return render_template('computers.html', computers=computers, page=page, total_pages=total_pages, has_prev=has_prev,
                           has_next=has_next, prev_page=prev_page, next_page=next_page, unique_ram=unique_details[0],
                           unique_processor=unique_details[1], unique_videocard=unique_details[2], max_price=max_price,
                           user_favorite_computers=user_favorite_computers)


def get_filtered_computers(video_card, processor, ram, chosen_price):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query_conditions = []
    query_parameters = []

    if video_card:
        query_conditions.append("GPU = ?")
        query_parameters.append(video_card)
    if processor:
        query_conditions.append("CPU = ?")
        query_parameters.append(processor)
    if ram:
        query_conditions.append("RAM = ?")
        query_parameters.append(ram)
    if chosen_price:
        query_conditions.append("PRICE <= ?")
        query_parameters.append(chosen_price)
    query = "SELECT * FROM computers"
    if query_conditions:
        query += " WHERE " + " AND ".join(query_conditions)

    cursor.execute(query, tuple(query_parameters))
    all_computers = cursor.fetchall()

    conn.close()
    print(all_computers)
    return all_computers


@app.route('/search_computers', methods=['POST', "GET"])
@app.route('/search_computers/<int:page>', methods=['POST', "GET"])
def search_computers(page=1):
    video_card = request.args.get('videoCard', None)
    processor = request.args.get('processor', None)
    ram = request.args.get('ram', None)
    chosen_price = request.args.get('priceRange', None)

    limit = 9
    offset = (page - 1) * limit

    if video_card or processor or ram or chosen_price:
        computers = get_filtered_computers(video_card, processor, ram, chosen_price)
    else:
        computers = get_computers()

    total_computers = len(computers)
    total_pages = (total_computers + limit - 1) // limit

    has_prev = page > 1
    has_next = page < total_pages
    prev_page = page - 1
    next_page = page + 1

    prev_page_url = None
    next_page_url = None

    if has_prev:
        prev_page_url = request.url_root + 'search_computers/' + str(prev_page) + '?' + request.query_string.decode(
            "utf-8")
    if has_next:
        next_page_url = request.url_root + 'search_computers/' + str(next_page) + '?' + request.query_string.decode(
            "utf-8")

    current_page_computers = computers[offset: offset + limit]

    user_favorite_computers = []
    if 'logged_in' in session and session['logged_in']:
        user_id = session['user_id']
        user_favorite_computers = get_user_favorite_computers(user_id)

    return render_template('search_results_computer.html', computers=current_page_computers, page=page,
                           total_pages=total_pages,
                           has_prev=has_prev, has_next=has_next, prev_page=prev_page, next_page=next_page,
                           prev_page_url=prev_page_url, next_page_url=next_page_url,
                           user_favorite_computers=user_favorite_computers)


def get_accessories():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accessories")
    accessories = cursor.fetchall()
    conn.close()
    return accessories


def get_page_accessories(offset=0, limit=9):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accessories LIMIT ? OFFSET ?", (limit, offset))
    accessories = cursor.fetchall()
    conn.close()
    return accessories


def get_unique_accessories():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accessories")
    accessories = cursor.fetchall()
    conn.close()
    unique_types = set()
    unique_companies = set()
    for accesory in accessories:
        unique_types.add(accesory[2])
        unique_companies.add(accesory[6])
    return unique_types, unique_companies


def get_max_price_accessories():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(acc_price) FROM accessories")
    max_price_accessories = cursor.fetchone()[0]
    return max_price_accessories


def get_count_accessories():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM accessories")
    count = cursor.fetchone()[0]
    conn.close()
    return count


@app.route('/accessories')
@app.route('/accessories/<int:page>')
def accessories(page=1):
    unique = get_unique_accessories()
    limit = 9
    offset = (page - 1) * limit
    accessories = get_page_accessories(offset, limit)
    total_accessories = get_count_accessories()
    total_pages = (total_accessories + limit - 1) // limit
    has_prev = page > 1
    has_next = page < total_pages
    prev_page = page - 1
    next_page = page + 1
    max_price = get_max_price_accessories()
    user_favorite_accessories = []
    if 'logged_in' in session and session['logged_in']:
        user_id = session['user_id']
        user_favorite_accessories = get_user_favorite_accessories(user_id)
    return render_template('accessories.html', accessories=accessories, page=page, total_pages=total_pages,
                           has_prev=has_prev,
                           has_next=has_next, prev_page=prev_page, next_page=next_page, max_price=max_price,
                           unique_types=unique[0], unique_companies=unique[1],
                           user_favorite_accessories=user_favorite_accessories)


def get_filtered_accessories(acc_types, acc_companies, chosen_price):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query_conditions = []
    query_parameters = []

    if acc_types:
        query_conditions.append("acc_type IN ({})".format(','.join('?' * len(acc_types))))
        query_parameters.extend(acc_types)
    if acc_companies:
        query_conditions.append("acc_company IN ({})".format(','.join('?' * len(acc_companies))))
        query_parameters.extend(acc_companies)
    if chosen_price:
        query_conditions.append("acc_price <= ?")
        query_parameters.append(chosen_price)

    query = "SELECT * FROM accessories"
    if query_conditions:
        query += " WHERE " + " AND ".join(query_conditions)

    cursor.execute(query, tuple(query_parameters))
    all_accessories = cursor.fetchall()

    conn.close()
    return all_accessories


@app.route('/search_accessories', methods=['POST', "GET"])
@app.route('/search_accessories/<int:page>', methods=['POST', "GET"])
def search_accessories(page=1):
    acc_types = request.args.getlist('type')
    acc_companies = request.args.getlist('company')
    chosen_price = request.args.get('price')
    limit = 9
    offset = (page - 1) * limit

    accessories = get_filtered_accessories(acc_types, acc_companies, chosen_price)

    total_accessories = len(accessories)
    total_pages = (total_accessories + limit - 1) // limit

    has_prev = page > 1
    has_next = page < total_pages
    prev_page = page - 1
    next_page = page + 1

    prev_page_url = None
    next_page_url = None

    if has_prev:
        prev_page_url = request.url_root + 'search_accessories/' + str(prev_page) + '?' + request.query_string.decode(
            "utf-8")
    if has_next:
        next_page_url = request.url_root + 'search_accessories/' + str(next_page) + '?' + request.query_string.decode(
            "utf-8")

    current_page_accessories = accessories[offset: offset + limit]
    user_favorite_accessories = []
    if 'logged_in' in session and session['logged_in']:
        user_id = session['user_id']
        user_favorite_accessories = get_user_favorite_accessories(user_id)
    return render_template('search_results_accessories.html', accessories=current_page_accessories, page=page,
                           total_pages=total_pages,
                           has_prev=has_prev, has_next=has_next, prev_page=prev_page, next_page=next_page,
                           prev_page_url=prev_page_url, next_page_url=next_page_url,
                           user_favorite_accessories=user_favorite_accessories)


app.secret_key = 'my_secret_key_1234567890'


def check_login(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
    user_id = cursor.fetchone()
    conn.close()
    return user_id


def update_user_favorites(user_id, item_id, action, table_name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    favorites_column = 'favorite_accessories' if table_name == 'accessories' else 'favorite_computers'

    cursor.execute(f"SELECT {favorites_column} FROM users WHERE id = ?", (user_id,))
    favorite_items = cursor.fetchone()[0]

    if favorite_items:
        favorites_list = favorite_items.split(',')
    else:
        favorites_list = []

    if action == 'add' and str(item_id) not in favorites_list:
        favorites_list.append(str(item_id))
    elif action == 'remove' and str(item_id) in favorites_list:
        favorites_list.remove(str(item_id))

    new_favorites = ','.join(favorites_list)
    cursor.execute(f"UPDATE users SET {favorites_column} = ? WHERE id = ?", (new_favorites, user_id))
    conn.commit()
    conn.close()


@app.route('/add_favorite/<item_type>/<int:item_id>', methods=['POST'])
def add_favorite(item_type, item_id):
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('register'))

    user_id = session['user_id']
    table_name = 'accessories' if item_type == 'accessory' else 'computers'
    update_user_favorites(user_id, item_id, 'add', table_name)
    return redirect(request.referrer)


@app.route('/remove_favorite/<item_type>/<int:item_id>', methods=['POST'])
def remove_favorite(item_type, item_id):
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('register'))

    user_id = session['user_id']
    table_name = 'accessories' if item_type == 'accessory' else 'computers'
    update_user_favorites(user_id, item_id, 'remove', table_name)
    return redirect(request.referrer)


def get_user_favorite_computers(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT favorite_computers FROM users WHERE id = ?", (user_id,))
    favorite_computers = cursor.fetchone()[0]

    if favorite_computers:
        favorite_computers_list = [int(item) for item in favorite_computers.split(',') if item]
    else:
        favorite_computers_list = []

    conn.close()

    return favorite_computers_list


def get_user_favorite_accessories(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT favorite_accessories FROM users WHERE id = ?", (user_id,))
    favorite_accessories = cursor.fetchone()[0]

    if favorite_accessories:
        favorite_accessories_list = [int(item) for item in favorite_accessories.split(',') if item]
    else:
        favorite_accessories_list = []

    conn.close()

    return favorite_accessories_list


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('login'))
    show_password = session.get('show_password', False)
    user_id = session['user_id']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user_data = cursor.fetchone()

    user_favorite_computers = get_user_favorite_computers(user_id)
    user_favorite_accessories = get_user_favorite_accessories(user_id)

    if user_favorite_computers:
        favorite_computers_query = f'SELECT * FROM computers WHERE id IN ({",".join("?" * len(user_favorite_computers))})'
        favorite_computers = cursor.execute(favorite_computers_query, user_favorite_computers).fetchall()
    else:
        favorite_computers = []

    if user_favorite_accessories:
        favorite_accessories_query = f'SELECT * FROM accessories WHERE id IN ({",".join("?" * len(user_favorite_accessories))})'
        favorite_accessories = cursor.execute(favorite_accessories_query, user_favorite_accessories).fetchall()
    else:
        favorite_accessories = []

    conn.close()

    return render_template('profile.html', user=user_data, favorite_computers=favorite_computers,
                           favorite_accessories=favorite_accessories, show_password=show_password)


@app.route('/toggle_password', methods=['POST'])
def toggle_password():
    session['show_password'] = not session.get('show_password', False)
    return redirect(url_for('profile'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user_id = check_login(username, password)
        if user_id:
            session['logged_in'] = True
            session['user_id'] = user_id[0]
            return redirect(url_for('profile'))
        else:
            error = 'Неправильний логін чи пароль. Спробуйте ще раз!'
            return render_template('login.html', error=error)

    return render_template('login.html', error=None)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        phone_number = request.form['phone_number']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            error = 'Ви ввели різні паролі. Спробуйте ще раз.'
            return render_template('register.html', error=error)

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE phone_number=?", (phone_number,))
        existing_user = cursor.fetchone()

        if existing_user:
            error = 'Профіль з таким номером телефона вже існує.'
            conn.close()
            return render_template('register.html', error=error)

        cursor.execute("INSERT INTO users (phone_number, username, password) VALUES (?, ?, ?)",
                       (phone_number, username, password))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template('register.html', error=None)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

def add_to_cart(user_id, item_type, item_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    if item_type == 'computer':
        cursor.execute("SELECT * FROM computers WHERE id=?", (item_id,))
    elif item_type == 'accessory':
        cursor.execute("SELECT * FROM accessories WHERE id=?", (item_id,))

    item = cursor.fetchone()

    if item:
        cursor.execute("SELECT computers_cart FROM users WHERE id=?", (user_id,))
        cart = cursor.fetchone()[0]
        if cart:
            cart = eval(cart)
            cart.append({'item_type': item_type, 'item_id': item_id})
            cursor.execute("UPDATE users SET computers_cart=? WHERE id=?", (str(cart), user_id))
        else:
            cursor.execute("UPDATE users SET computers_cart=? WHERE id=?", (str([{'item_type': item_type, 'item_id': item_id}]), user_id))

        conn.commit()
        conn.close()

@app.route('/add_to_cart/<item_type>/<item_id>', methods=['POST'])
def add_to_cart_route(item_type, item_id):
    if 'logged_in' in session and session['logged_in']:
        user_id = session['user_id']
        add_to_cart(user_id, item_type, item_id)
        return redirect(url_for('cart'))
    else:
        return redirect(url_for('register'))
def get_cart_items(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT computers_cart FROM users WHERE id=?", (user_id,))
    cart = cursor.fetchone()[0]

    computers = []
    accessories = []
    if cart:
        cart = eval(cart)
        for item in cart:
            if item['item_type'] == 'computer':
                cursor.execute("SELECT * FROM computers WHERE id=?", (item['item_id'],))
                computers.append(cursor.fetchone())
            elif item['item_type'] == 'accessory':
                cursor.execute("SELECT * FROM accessories WHERE id=?", (item['item_id'],))
                accessories.append(cursor.fetchone())

    conn.close()
    return computers, accessories

def remove_from_cart(user_id, item_type, item_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT computers_cart FROM users WHERE id=?", (user_id,))
    cart = cursor.fetchone()[0]

    if cart:
        cart = eval(cart)
        updated_cart = [item for item in cart if not (item['item_type'] == item_type and item['item_id'] == item_id)]
        cursor.execute("UPDATE users SET computers_cart=? WHERE id=?", (str(updated_cart), user_id))

    conn.commit()
    conn.close()

@app.route('/remove_from_cart/<item_type>/<item_id>', methods=['POST'])
def remove_from_cart_route(item_type, item_id):
    if 'logged_in' in session and session['logged_in']:
        user_id = session['user_id']
        remove_from_cart(user_id, item_type, item_id)
        return redirect(url_for('cart'))
    else:
        return redirect(url_for('register'))
@app.route('/cart')
def cart():
    if 'logged_in' in session and session['logged_in']:
        user_id = session['user_id']
        computers, accessories = get_cart_items(user_id)
        return render_template('cart.html', computers=computers, accessories=accessories)
    else:
        return redirect(url_for('register'))


if __name__ == '__main__':
    app.run(debug=True)
