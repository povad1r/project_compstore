import sqlite3

connect = sqlite3.connect('database.db')
#
# connect.execute('''DROP TABLE users''')
# #
# connect.execute('''CREATE TABLE IF NOT EXISTS computers (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     computer_name TEXT NOT NULL,
#                     computer_desc TEXT NOT NULL,
#                     GPU TEXT NOT NULL,
#                     CPU TEXT NOT NULL,
#                     RAM INTEGER NOT NULL,
#                     price INTEGER NOT NULL
#                 )''')
#
cursor = connect.cursor()
# #
# #
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ('Gaming X35v41', 'Gaming X35v41 - магія інжернего мистецтва. Ефективне розміщення компонентів забезпечить максимальну продуктивність та естетичний вигляд', 'Nvidia GeForce RTX 3050', 'Intel Core i5-12400F', 16, 32000))
#
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ('Gaming X66v22', 'Gaming X66v22 побудований на платформі материнської плати ASUS PRIME B450M-A з роз\'ємом AM4 та підтримкою процесорів AMD всіх поколінь', 'GeForce RTX 3060 Ti', 'AMD Ryzen 5600X', 16, 42000))
#
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ('Gaming X59v33', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 81000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))

# #

# connect.execute('''CREATE TABLE IF NOT EXISTS computers (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     computer_name TEXT NOT NULL,
#                     computer_desc TEXT NOT NULL,
#                     GPU TEXT NOT NULL,
#                     CPU TEXT NOT NULL,
#                     RAM INTEGER NOT NULL,
#                     price INTEGER NOT NULL
#                 )''')
#
# connect.execute('''CREATE TABLE IF NOT EXISTS accessories (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     acc_image TEXT NOT NULL,
#                     acc_type TEXT NOT NULL,
#                     acc_name TEXT NOT NULL,
#                     acc_desc TEXT NOT NULL,
#                     acc_price INTEGER NOT NULL,
#                     acc_company TEXT NOT NULL
#                 )''')
#
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    phone_number TEXT UNIQUE NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    favorite_computers TEXT,
                    favorite_accessories TEXT,
                    accessories_cart TEXT,
                    computers_cart TEXT        
                  )''')

# cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
#                 ('https://content2.rozetka.com.ua/goods/images/big/272938087.jpg', 'Миша', 'Миша Razer DeathAdder Essential USB', 'Razer DeathAdder є основною в кіберспорті.', 1200, 'Razer'))
#
# cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
#             ('https://hotline.ua/img/tx/265/2652527685.jpg', 'Миша', 'Миша Logitech G Pro X', 'Найлегша бездротова мишка у світі!', 6699, 'Logitech'))
#
#
# cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
#                ('https://i.citrus.world/imgcache/size_800/uploads/shop/a/d/adf22f646228467a2e9359299268c79e.jpg', 'Миша', 'Миша HyperX Pulsefire Dart Wireless', 'Чудова бездротова мишка з великою батареєю.', 4299, 'HyperX'))
# cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
#                ('https://content2.rozetka.com.ua/goods/images/big/361181038.jpg', 'Миша', 'Миша Logitech G502 X', 'Найкраща миша у своєму ціновому сегменті.', 2599, 'Logitech'))
# cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
#                ('https://i.citrus.world/imgcache/size_800/uploads/shop/b/2/b22d28b08451eeaa5b9f95e6e64a7ed4.jpg', 'Навушники', 'Навушники Razer Kraken Multi Platform', 'Топові навушники за дуже топову ціну', 2499, 'Razer'))
#
# cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
#                ('https://i.citrus.world/imgcache/size_800/uploads/shop/1/6/1691741570-hypergang-2-hta-910-black-003.jpg', 'Навушники', 'Навушники HATOR Hypergang 2', 'Навушники від топового українського бренду.', 1999, 'Hator'))
#
#
# cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
#                ('https://content2.rozetka.com.ua/goods/images/big/336444973.jpg', 'Навушники', 'Навушники Logitech G Pro', 'Найкрутіші навушники в сфері кіберспорту.', 8999, 'Logitech'))
# cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
#                ('https://i.citrus.world/imgcache/size_800/uploads/shop/1/6/1694419919-hyperx-cloud-ii-core-wireless-6y2g8aa-angle-2.jpg', 'Навушники', 'Навушники HyperX Cloud II Core', 'Чудові бездротові навушники від HyperX.', 5499, 'HyperX'))
# cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
#                ('https://content2.rozetka.com.ua/goods/images/big/392106442.jpg', 'Клавіатура', 'Клавіатура Varmilo VEA87 Panda R2', 'Дуже гарна клавіатура з неймовірним кольором.', 6499, 'Varmilo'))
#
# cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
#                ('https://content1.rozetka.com.ua/goods/images/big/412326412.jpg', 'Клавіатура', 'Клавіатура HATOR Rockfall 2', 'Чудова дротова клавіатура від бренду Hator.', 7999, 'Hator'))
# cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
#                ('https://content1.rozetka.com.ua/goods/images/big/392116955.jpg', 'Клавіатура', 'Клавіатура Varmilo VEM87 Beijing Opera', 'Дизайн клавіатури зроблений у азіатському стилі.', 8099, 'Varmilo'))
# cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
#                ('https://content.rozetka.com.ua/goods/images/big/188638110.jpg', 'Клавіатура', 'Клавіатура HyperX Alloy Origins', 'Неймовірна клавіатура за дуже приємну ціну.', 3299, 'HyperX'))
#

#
# cursor.execute('''DROP TABLE users''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     phone_number TEXT UNIQUE NOT NULL,
#                     username TEXT NOT NULL,
#                     password TEXT NOT NULL,
#                     favorite_computers TEXT DEFAULT,
#                     favorite_accessories TEXT DEFAULT
#                   )''')

# cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     phone_number TEXT UNIQUE NOT NULL,
#                     username TEXT NOT NULL,
#                     password TEXT NOT NULL,
#                     favorite_computers TEXT,
#                     favorite_accessories TEXT
#                   )''')


# cursor.execute("SELECT * from users")
# c111 = cursor.fetchone()
# print(c111)

#
# cursor.execute("INSERT INTO users(phone_number, username, password) VALUES(?,?,?)",
# ('+380509253658', 'povad1r', '123'))
#
connect.commit()


connect.close()
