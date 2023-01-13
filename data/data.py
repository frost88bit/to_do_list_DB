import datetime
import csv
import sqlite3


loaded_test_data = []

temp_dict = {
            'title': "str1",
            'description': "str2",
            'priority': 3,
            'due_date': "str",
            'done': True
            }

temp_list = list(temp_dict.values())

con = sqlite3.connect('data.db')
cur = con.cursor()

def create_table():
    cur.execute("""CREATE TABLE if not exists data 
                (
                id INTEGER primary key autoincrement,
                title TEXT,
                description TEXT,
                priority INTEGER,
                due_date TEXT,
                done INTEGER
                )
                """)
    con.commit()

create_table()


# cur.execute("""
#     INSERT INTO data(title, description, priority, due_date, done) VALUES
#         ('Shopping', 'Shopping day', 8, '5.01.2023', True),
#         ('Shopping2', 'Shopping day2', 7, '10.01.2023', False),
#         ('Shopping3', 'Shopping day3', 7, '11.01.2023', False)
# """)
# con.commit()

if __name__ == '__main__':
    res = cur.execute("SELECT * FROM data ",)
    print(res.fetchall())












