import sqlite3
connection = sqlite3.connect("paraugs.db")
curs = connection.cursor()

# curs.execute("CREATE TABLE dalibnieki (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
# curs.execute("INSERT INTO dalibnieki VALUES (2244560, 'Janis Platais', 32)")
# curs.execute("INSERT INTO dalibnieki VALUES (2243560, 'Janis Resnais', 12)")
# curs.execute("INSERT INTO dalibnieki VALUES (2244540, 'Janis Šaurais', 22)")
# curs.execute("INSERT INTO dalibnieki VALUES (2244561, 'Janis Līkais', 42)")

# new_persons = [(2233223, 'Linda Priede', 32),
#  (2233224, 'Olafs Kalnins', 10),
#  (2233225, 'Ance Ozola', 21),
#  (2233226, 'Indra Abele', 41),
#  (2233227, 'Zigmars Liepins', 25)
#  ]
# # Insert values into the students table
# curs.executemany('''INSERT INTO dalibnieki VALUES (?,?,?)''', new_persons)

connection.commit()
connection.close()