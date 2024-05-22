from flask import Flask, request, render_template, url_for
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
        unique_videocard.add(computer[4])
        unique_processor.add(computer[5])
        unique_ram.add(computer[6])
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
    return render_template('computers.html', computers=computers, page=page, total_pages=total_pages, has_prev=has_prev, has_next=has_next, prev_page=prev_page, next_page=next_page, unique_ram=unique_details[0], unique_processor=unique_details[1], unique_videocard=unique_details[2], max_price=max_price)


def get_filtered_computers(video_card, processor, ram, chosen_price, limit=9, offset=0):
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
        computers = get_filtered_computers(video_card, processor, ram, chosen_price, limit, offset)
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
        prev_page_url = request.url_root + 'search_computers/' + str(prev_page) + '?' + request.query_string.decode("utf-8")
    if has_next:
        next_page_url = request.url_root + 'search_computers/' + str(next_page) + '?' + request.query_string.decode("utf-8")

    current_page_computers = computers[offset: offset + limit]

    return render_template('search_results_computer.html', computers=current_page_computers, page=page, total_pages=total_pages,
                           has_prev=has_prev, has_next=has_next, prev_page=prev_page, next_page=next_page,
                           prev_page_url=prev_page_url, next_page_url=next_page_url)


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
    return render_template('accessories.html', accessories=accessories, page=page, total_pages=total_pages, has_prev=has_prev,
                           has_next=has_next, prev_page=prev_page, next_page=next_page, max_price=max_price, unique_types=unique[0], unique_companies=unique[1])

def get_filtered_accessories(acc_type, acc_company, chosen_price, limit=9, offset=0):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query_conditions = []
    query_parameters = []

    if acc_type:
        query_conditions.append("acc_type = ?")
        query_parameters.append(acc_type)
    if acc_company:
        query_conditions.append("acc_company = ?")
        query_parameters.append(acc_company)
    if chosen_price:
        query_conditions.append("PRICE <= ?")
        query_parameters.append(chosen_price)
    query = "SELECT * FROM accessories"
    if query_conditions:
        query += " WHERE " + " AND ".join(query_conditions)

    cursor.execute(query, tuple(query_parameters))
    all_accessories = cursor.fetchall()

    conn.close()
    print(all_accessories)
    return all_accessories

@app.route('/search_accessories', methods=['POST', "GET"])
@app.route('/search_accessories/<int:page>', methods=['POST', "GET"])
def search_accessories(page=1):
    acc_type = request.args.get('type', None)
    acc_company = request.args.get('company', None)
    chosen_price = request.args.get('price')
    limit = 9
    offset = (page - 1) * limit
    if acc_type or acc_company or chosen_price:
        accessories = get_filtered_accessories(acc_type, acc_company, chosen_price, limit, offset)
    else:
        accessories = get_accessories()
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

    return render_template('search_results_accessories.html', accessories=current_page_accessories, page=page,
                           total_pages=total_pages,
                           has_prev=has_prev, has_next=has_next, prev_page=prev_page, next_page=next_page,
                           prev_page_url=prev_page_url, next_page_url=next_page_url)



if __name__ == '__main__':
    app.run(debug=True)
