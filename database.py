import sqlite3

connect = sqlite3.connect('database.db')
#
# connect.execute('''DROP TABLE computers''')
# connect.execute('''DROP TABLE users''')
# connect.execute('''DROP TABLE orders''')
#
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
#                ('Gaming X35v41', 'Gaming X35v41 - магія інжернего мистецтва. Ефективне розміщення компонентів забезпечить максимальну продуктивність та естетичний вигляд', 'Nvidia GeForce RTX 3050', 'Intel Core i5-12400', 16, 32000))
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
#                ( 'Overlord HYPERIONv12', 'Overlord HYPERIONv12 - Це висококласна ігрова станція, створена із застосуванням найпередовіших технологій та компонентів.', 'GeForce RTX 4090', 'Intel Core i9-13900', 32, 220000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord DRAGONv38CH', 'Overlord DRAGONv38CH - це високопродуктивний комп\'ютер, що має найбільш топову «начинку» від відомих брендів, у тому числі від компанії MSI.', 'Radeon RX 6600 XT', 'AMD Ryzen 5 3600', 32, 40900))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Gaming X48v15', 'Gaming X48v15 - є відмінним вибором для користувача, який шукає продуктивний процесор та відеокарту за бюджетною ціною.', 'Radeon RX 6600 XT', 'AMD Ryzen 5 3600', 16, 31000))
# #
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Gaming X66v30', 'Gaming X66v30 - геймерська пам\'ять DDR4 на 32 ГБ з ефективною робочою частотою 3200 МГц забезпечить швидку і стабільну роботу ПК.', 'Radeon RX 6600 XT', 'AMD Ryzen 5600X', 32, 43000))
# #
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Gaming X38v23', 'Gaming X38v23 - Ігровий комп\'ютер з ефективним охолодженням та потужною графікою, ідеальний для запальних геймерських битв.', 'Radeon RX 6600 XT', 'Intel Core i5-12400', 16, 34500))
# #
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Gaming X53WHITEv33', 'Gaming X53WHITEv33 - гігантський ігровий монстр із потужним процесором та відмінною графікою, створений для найекстремальніших геймерських випробувань.', 'GeForce RTX 3050', 'Intel Core i5-12400', 32, 38500))
# #
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Gaming X43v31', 'Gaming X43v31 - компактний ігровий ПК з портативним дизайном, ідеальний для геймерів, що постійно перебувають в русі.', 'GeForce RTX 3050', 'AMD Ryzen 5 3600', 16, 28000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord STRIXv111', 'Overlord STRIXv111 - ігрова робоча станція, спроектована для великих мультиплеерних ігор та стрімінгу високої якості без будь-яких затримок.', 'GeForce RTX 4090', 'Intel Core i9-13900', 32, 207000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Gaming X99v55', 'Gaming X99v55 - комп\'ютер з вражаючою графікою та звуком, який занурює гравця в атмосферу віртуальної реальності з першої миті гри.', 'GeForce RTX 4090', 'Intel Core i9-13900', 32, 163000))
# #
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord GIGAv38', 'Overlord GIGAv38 - ігровий ПК з інноваційним жидкісним охолодженням, що забезпечує стабільну температуру під час найінтенсивніших ігрових сесій.', 'GeForce RTX 4070 Ti', 'Intel Core i9-13900', 64, 117000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord GT502v16', 'Overlord GT502v16 - ігровий комп\'ютер з потужними відрахунковими можливостями, який забезпечує неперевершений досвід гри в найсучасніші та найпопулярніші ігри.', 'GeForce RTX 4090', 'Intel Core i9-13900', 32, 195500))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Gaming HGWRTSv14', 'Gaming HGWRTSv14 - ігрова робоча станція, що вражає не тільки потужністю, але й стабільністю під час найдовших ігрових марафонів.', 'Radeon RX 6600 XT', 'Intel Core i5-12400', 16, 39300))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord FROSTBITEv01', 'Overlord FROSTBITEv01 - комп\'ютер, що здатний забезпечити найвищу швидкість фреймрейту та мінімальну лагодрому під час ігрових баталій.', 'GeForce RTX 4070 Ti', 'Intel Core i5-13500', 32, 91500))
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Overlord ANOMALYv02', 'Overlord ANOMALYv02 - комп\'ютер з унікальним дизайном та бездоганною продуктивністю, який допомагає кожному гравцеві розкрити свій потенціал.', 'GeForce RTX 3060 Ti', 'AMD Ryzen 5600X', 16, 57500))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Gaming X99v56', 'Gaming X99v56 -  ігровий комп\'ютер з вражаючими космічними можливостями, який веде гравців у захоплюючі подорожі по найвіддаленіших галактиках.', 'GeForce RTX 4090', 'Intel Core i9-13900', 64, 168000))
#
# cursor.execute("INSERT INTO computers (computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?)",
#                ( 'Gaming DRGN', 'Gaming DRGN - ігрова робоча станція з кристальною якістю графіки та звуку, яка перетворює кожну гру на захоплюючий кінематографічний досвід.', 'GeForce RTX 4060 Ti', 'Intel Core i5-13500', 32, 56500))
# # #

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
# connect.execute('''DROP TABLE accessories''')
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
# cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     phone_number TEXT UNIQUE NOT NULL,
#                     username TEXT NOT NULL,
#                     password TEXT NOT NULL,
#                     favorite_computers TEXT,
#                     favorite_accessories TEXT,
#                     accessories_cart TEXT,
#                     computers_cart TEXT
#                   )''')
# # cursor.execute('''DROP TABLE orders''')
# cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     user_id INTEGER NOT NULL,
#     name TEXT NOT NULL,
#     surname TEXT NOT NULL,
#     address TEXT NOT NULL,
#     phone TEXT NOT NULL,
#     FOREIGN KEY(user_id) REFERENCES users(id)
# )''');
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
