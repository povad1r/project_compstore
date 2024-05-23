import sqlite3

connect = sqlite3.connect('database.db')

connect.execute('''DROP TABLE accessories''')

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

cursor = connect.cursor()
#
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('Gaming X35v41.jpg', 'Gaming X35v41', 'Gaming X35v41 - магія інжернего мистецтва. Ефективне розміщення компонентів забезпечить максимальну продуктивність та естетичний вигляд', 'Nvidia GeForce RTX 3050', 'Intel Core i5-12400F', 16, 32000))
#
#
# cursor.execute("INSERT INTO computers (image, computer_name, computer_desc, GPU, CPU, RAM, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
#                ('Gaming X66v22.jpg', 'Gaming X66v22', 'Gaming X66v22 побудований на платформі материнської плати ASUS PRIME B450M-A з роз\'ємом AM4 та підтримкою процесорів AMD всіх поколінь', 'GeForce RTX 3060 Ti', 'AMD Ryzen 5600X', 16, 42000))
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
                ('https://content.rozetka.com.ua/goods/images/big_tile/12934309.jpg', 'Миша', 'Миша Razer DeathAdder Essential USB Black', 'Razer DeathAdder є основною в кіберспорті.', 1200, 'Razer'))

cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
            ('https://hotline.ua/img/tx/265/2652527685.jpg', 'Миша', 'Миша Logitech G Pro X', 'Найлегша бездротова мишка у світі!', 6699, 'Logitech'))


cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
               ('https://i.citrus.world/imgcache/size_800/uploads/shop/a/d/adf22f646228467a2e9359299268c79e.jpg', 'Миша', 'Миша HyperX Pulsefire Dart Wireless', 'Чудова бездротова мишка, яка може працювати більше 3 днів.', 4299, 'HyperX'))
cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
               ('data:image/jpeg;base64,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', 'Миша', 'Миша Logitech G502 X', 'Найкраща миша у своєму ціновому сегменті.', 2599, 'Logitech'))
cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
               ('https://i.citrus.world/imgcache/size_800/uploads/shop/b/2/b22d28b08451eeaa5b9f95e6e64a7ed4.jpg', 'Навушники', 'Навушники Razer Kraken Multi Platform', 'Топові навушники за дуже топову ціну', 2499, 'Razer'))

cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
               ('https://i.citrus.world/imgcache/size_800/uploads/shop/1/6/1691741570-hypergang-2-hta-910-black-003.jpg', 'Навушники', 'Навушники HATOR Hypergang 2', 'Навушники від топового українського бренду.', 1999, 'Hator'))


cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
               ('https://content2.rozetka.com.ua/goods/images/big/336444973.jpg', 'Навушники', 'Навушники Logitech G Pro', 'Найкрутіші навушники в сфері кіберспорту.', 8999, 'Logitech'))
cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
               ('https://i.citrus.world/imgcache/size_800/uploads/shop/1/6/1694419919-hyperx-cloud-ii-core-wireless-6y2g8aa-angle-2.jpg', 'Навушники', 'Навушники HyperX Cloud II Core Wireless', 'Чудові бездротові навушники від HyperX.', 5499, 'HyperX'))
cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
               ('https://content2.rozetka.com.ua/goods/images/big/392106442.jpg', 'Клавіатура', 'Клавіатура Varmilo VEA87 Panda R2', 'Дуже гарна клавіатура з неймовірним кольором.', 6499, 'Varmilo'))

cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
               ('https://content1.rozetka.com.ua/goods/images/big/412326412.jpg', 'Клавіатура', 'Клавіатура HATOR Rockfall 2', 'Чудова дротова клавіатура від бренду Hator.', 7999, 'Hator'))
cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
               ('https://content1.rozetka.com.ua/goods/images/big/392116955.jpg', 'Клавіатура', 'Клавіатура Varmilo VEM87 Beijing Opera', 'Дизайн клавіатури виповнений у китайському стилі.', 8099, 'Varmilo'))
cursor.execute("INSERT INTO accessories(acc_image, acc_type, acc_name, acc_desc, acc_price, acc_company) VALUES (?,?,?,?,?,?)",
               ('https://content.rozetka.com.ua/goods/images/big/188638110.jpg', 'Клавіатура', 'Клавіатура HyperX Alloy Origins', 'Неймовірна клавіатура за дуже приємну ціну.', 3299, 'HyperX'))


connect.commit()


connect.close()
