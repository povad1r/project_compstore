import sqlite3

connect = sqlite3.connect('database.db')

# connect.execute('''DROP TABLE computers''')

# connect.execute('''CREATE TABLE IF NOT EXISTS computers (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     image TEXT NOT NULL,
#                     computer_name TEXT NOT NULL,
#                     computer_desc TEXT NOT NULL,
#                     GPU TEXT NOT NULL,
#                     CPU TEXT NOT NULL,
#                     RAM INTEGER NOT NULL,
#                     price INTEGER NOT NULL
#                 )''')
#
cursor = connect.cursor()
#
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('Gaming X35v41.jpg', 'Gaming X35v41', 'Gaming X35v41 - магія інжернего мистецтва. Ефективне розміщення компонентів забезпечить максимальну продуктивність та естетичний вигляд', 'Nvidia GeForce RTX 3050', 'Intel Core i5-12400F', 16, 32000))
#
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('Gaming X66v22.jpg', 'Gaming X66v22', 'Gaming X66v22 побудований на платформі материнської плати ASUS PRIME B450M-A з роз\'ємом AM4 та підтримкою процесорів AMD всіх поколінь Ryzen', 'GeForce RTX 3060 Ti', 'AMD Ryzen 5600X', 16, 42000))
#
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('Gaming X59v33.jpg', 'Gaming X59v33', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 81000))
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('https://artline.ua/storage/images/products/14748/gallery/180612/1400_gallery_1692255799633702_0.webp', 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('https://artline.ua/storage/images/products/14748/gallery/180612/1400_gallery_1692255799633702_0.webp', 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('https://artline.ua/storage/images/products/14748/gallery/180612/1400_gallery_1692255799633702_0.webp', 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('https://artline.ua/storage/images/products/14748/gallery/180612/1400_gallery_1692255799633702_0.webp', 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('https://artline.ua/storage/images/products/14748/gallery/180612/1400_gallery_1692255799633702_0.webp', 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('https://artline.ua/storage/images/products/14748/gallery/180612/1400_gallery_1692255799633702_0.webp', 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('https://artline.ua/storage/images/products/14748/gallery/180612/1400_gallery_1692255799633702_0.webp', 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('https://artline.ua/storage/images/products/14748/gallery/180612/1400_gallery_1692255799633702_0.webp', 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('https://artline.ua/storage/images/products/14748/gallery/180612/1400_gallery_1692255799633702_0.webp', 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('https://artline.ua/storage/images/products/14748/gallery/180612/1400_gallery_1692255799633702_0.webp', 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('https://artline.ua/storage/images/products/14748/gallery/180612/1400_gallery_1692255799633702_0.webp', 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('https://artline.ua/storage/images/products/14748/gallery/180612/1400_gallery_1692255799633702_0.webp', 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('https://artline.ua/storage/images/products/14748/gallery/180612/1400_gallery_1692255799633702_0.webp', 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('https://artline.ua/storage/images/products/14748/gallery/180612/1400_gallery_1692255799633702_0.webp', 'Overlord HYPERIONv12', 'Gaming X59v33 - чудовий ігровий комп\'ютер з неймовірними комплектуючими, які дозволяють грати в сучасні ігри з великим задоволенням', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 220000))
#
#


connect.execute('''CREATE TABLE IF NOT EXISTS accessories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    acc_image TEXT NOT NULL,
                    acc_type TEXT NOT NULL,
                    acc_name TEXT NOT NULL,
                    acc_desc TEXT NOT NULL,
                    acc_price INTEGER NOT NULL,
                    acc_company TEXT NOT NULL
                )''')


cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
                ('https://content.rozetka.com.ua/goods/images/big_tile/12934309.jpg', 'mouse', 'Миша Razer DeathAdder Essential USB Black', 'Вже більше десяти років серія Razer DeathAdder є основною на світовий кіберспортивній арені.', 1200, 'Razer'))

cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
            ('https://content.rozetka.com.ua/goods/images/big_tile/12934309.jpg', 'mouse', 'Миша Logitech DeathAdder Essential USB Black', 'Вже більше десяти років серія Razer DeathAdder є основною на світовий кіберспортивній арені.', 2500, 'Logitech'))


cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)", ('https://content.rozetka.com.ua/goods/images/big_tile/12934309.jpg', 'mouse', 'Миша HyperX DeathAdder Essential USB Black', 'Вже більше десяти років серія Razer DeathAdder є основною на світовий кіберспортивній арені.', 1500, 'Hyperx'))
cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)", ('https://content.rozetka.com.ua/goods/images/big_tile/12934309.jpg', 'mouse', 'Миша Logitech DeathAdder Essential USB Black', 'Вже більше десяти років серія Razer DeathAdder є основною на світовий кіберспортивній арені.', 5000, 'Logitech'))
cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)", ('https://content.rozetka.com.ua/goods/images/big_tile/12934309.jpg', 'headphones', 'Миша Razer DeathAdder Essential USB Black', 'Вже більше десяти років серія Razer DeathAdder є основною на світовий кіберспортивній арені.', 11334, 'Razer'))

cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)", ('https://content.rozetka.com.ua/goods/images/big_tile/12934309.jpg', 'headphones', 'Миша Logitech DeathAdder Essential USB Black', 'Вже більше десяти років серія Razer DeathAdder є основною на світовий кіберспортивній арені.', 1453, 'Logitech'))


cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)", ('https://content.rozetka.com.ua/goods/images/big_tile/12934309.jpg', 'headphones', 'Миша HyperX DeathAdder Essential USB Black', 'Вже більше десяти років серія Razer DeathAdder є основною на світовий кіберспортивній арені.', 4633, 'Hyperx'))
cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)", ('https://content.rozetka.com.ua/goods/images/big_tile/12934309.jpg', 'headphones', 'Миша Logitech DeathAdder Essential USB Black', 'Вже більше десяти років серія Razer DeathAdder є основною на світовий кіберспортивній арені.', 6768, 'Logitech'))
cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)", ('https://content.rozetka.com.ua/goods/images/big_tile/12934309.jpg', 'keyboard', 'Миша Razer DeathAdder Essential USB Black', 'Вже більше десяти років серія Razer DeathAdder є основною на світовий кіберспортивній арені.', 8797, 'Razer'))

cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)", ('https://content.rozetka.com.ua/goods/images/big_tile/12934309.jpg', 'keyboard', 'Миша Logitech DeathAdder Essential USB Black', 'Вже більше десяти років серія Razer DeathAdder є основною на світовий кіберспортивній арені.', 2357, 'Logitech'))


cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)", ('https://content.rozetka.com.ua/goods/images/big_tile/12934309.jpg', 'keyboard', 'Миша HyperX DeathAdder Essential USB Black', 'Вже більше десяти років серія Razer DeathAdder є основною на світовий кіберспортивній арені.', 8643, 'Hyperx'))
cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)", ('https://content.rozetka.com.ua/goods/images/big_tile/12934309.jpg', 'keyboard', 'Миша Logitech DeathAdder Essential USB Black', 'Вже більше десяти років серія Razer DeathAdder є основною на світовий кіберспортивній арені.', 7589, 'Logitech'))




connect.commit()


connect.close()
