import operator
from data.data import loaded_test_data
from data.data import temp_dict
import data
from helpers.helpers import cls
import datetime
from time import strftime
import csv
import math
import sqlite3



choose = {'a.': 'Створити новий запис (додати заплановану справу)',
          'b.': 'Знайти запис за частиною назви та переглянути її деталі',
          'c.': 'Знайти та помітити справу, як виконану',
          'd.': 'Знайти справу та змінити її пріоритет',
          'e.': 'Знайти та видалити справу',
          'f.': 'Переглянути всі заплановані справи (тільки назви) у порядку їхнього додавання',
          'g.': 'Переглянути всі заплановані справи (тільки назви) у порядку спадання пріоритету',
          'h.': 'Переглянути всі невиконані справи (тільки назви)',
          'i.': 'Переглянути виконані справи (тільки назви)',
          'j.': 'Переглянути прострочені справи (тільки назви)',
          'k.': 'Переглянути статистику (загальна кількість справ, кількість виконаних/невиконаних/прострочених справ)',
          'l.': 'Зберегти список справ як csv файл.',
          'm.': 'Завантажити тестові дані',
          'n.': 'Вийти'
          }


def start():
    for line in choose:
        print(line + ' ' + choose[line])


def if_chosen_a():
    '''part of main function
    if user picked 'a''''
    print('Створить новий запис (додати заплановану справу)')



def if_chosen_b():
    '''part of main function
    if user picked 'b''''
    con = sqlite3.connect('./data/data.db')
    cur = con.cursor()
    chosen_b_my_input = input('Введіть назву: ')
    res = cur.execute("SELECT * FROM data where title like ? and title = ?",
                      ('%'+chosen_b_my_input+'%', chosen_b_my_input))
    return print(res.fetchall())


def if_chosen_c():
    '''part of main function
    if user picked 'c''''
    con = sqlite3.connect('./data/data.db')
    cur = con.cursor()

    my_input = input('Введіть назву: ')

    res = cur.execute("SELECT * FROM data where title like ? and title = ? and done = 0",
                      ('%'+my_input+'%', my_input))
    print(res.fetchall())


    while True:
        done_value_changer = input('Бажаєте помітити справу я виконану? (y/n): ')
        done_value_changer = done_value_changer.lower()

        if done_value_changer == 'y':
            res_change = cur.execute("UPDATE data SET done=1 where title like ? and title = ?",
                                     ('%'+my_input+'%', my_input))
            res_n = cur.execute("SELECT * FROM data where title like ? and title = ? and done = 1",
                                ('%' + my_input + '%', my_input))
            return print(res_n.fetchall())
        elif done_value_changer == 'n':
            print('Справа не була виконана')
        else:
            print('Не вірні данні')


def if_chosen_d():
    '''part of main function
    if user picked 'd''''
    con = sqlite3.connect('./data/data.db')
    cur = con.cursor()
    my_input = input('Введіть назву: ')

    res = cur.execute("SELECT * FROM data where title=?", (my_input,))
    print(res.fetchall())

    prio_value_changer = int(input('Виберіть число на яке хочете змінити приорітет (від 1-10): '))

    qwery_prio = cur.execute("SELECT priority FROM data where title=?", (my_input,))
    prio_str = [str(integer) for integer in qwery_prio]
    prio_string = "".join(prio_str)
    prio_ind = prio_string[1]
    prio_ind = int(prio_ind)
    qwery_prio_final = prio_ind

    if prio_value_changer > qwery_prio_final or prio_value_changer < qwery_prio_final:
        prio_value_changer = str(prio_value_changer)
        prio_change = cur.execute("UPDATE data SET priority = ? where title=?", (prio_value_changer, my_input))
        con.commit()
        qwery_prio_new = cur.execute("SELECT * FROM data where title=?", (my_input,))
        print(qwery_prio_new.fetchall())

    elif prio_value_changer == qwery_prio_final:
        print('Пріорітет не змінився')
    else:
        print('Не вірні данні')


'''Знайти та видалити справу'''
#
def if_chosen_e():
    '''part of main function
    if user picked 'e''''
    con = sqlite3.connect('./data/data.db')
    cur = con.cursor()
    my_input = str(input("Введіть назву:  "))

    res = cur.execute("SELECT * FROM data where title like ? and title = ?",
                      ('%'+my_input+'%', my_input))
    print(res.fetchall())
    verifier = input('Бажаєте видалити справу? (y/n): ')
    verifier = verifier.lower()
    while True:
        if verifier == 'y':
            res_del = cur.execute("DELETE FROM data where title like ? and title = ?",
                      ('%'+my_input+'%', my_input))
            con.commit()
            res = cur.execute("SELECT * FROM data where title like ? and title = ?",
                              ('%' + my_input + '%', my_input))
            return print(res.fetchall())
        elif verifier == 'n':
            print('Справа не була видалена!')
            quit()
        else:
            print('Не вірні данні')


#
def if_chosen_f():
    '''part of main function
    if user picked 'f''''
    con = sqlite3.connect('./data/data.db')
    cur = con.cursor()
    res = cur.execute("SELECT title FROM data ORDER by id ASC")
    print(res.fetchall())
#
#
def if_chosen_g():
    '''part of main function
    if user picked 'g''''
    con = sqlite3.connect('./data/data.db')
    cur = con.cursor()
    res = cur.execute("SELECT title FROM data ORDER by id DESC")
    print(res.fetchall())
#
#
def if_chosen_h():
    '''part of main function
    if user picked 'h''''
    con = sqlite3.connect('./data/data.db')
    cur = con.cursor()
    res = cur.execute("SELECT title FROM data WHERE done = 0")
    print(res.fetchall())
#
#
def if_chosen_i():
    '''part of main function
    if user picked 'i''''
    con = sqlite3.connect('./data/data.db')
    cur = con.cursor()
    res = cur.execute("SELECT title FROM data WHERE done = 1")
    print(res.fetchall())
#
#
# def if_chosen_j():
#     '''part of main function
#     if user picked 'j''''
#     for element in loaded_test_data:
#         for key, value in element.items():
#             if element['done'] == False and element['due_date'] < str(datetime.datetime.now()):
#                 print(element['title'])
#             break
#
#
# def if_chosen_k():
#     '''part of main function
#     if user picked 'k''''
#     con = sqlite3.connect('./data/data.db')
#     cur = con.cursor()
#     temp_list_undone = []
#     temp_list_done = []
#     for element in loaded_test_data:
#         for key, value in element.items():
#             if element['done'] == False:
#                 temp_list_undone.append(element['done'])
#             undone = len(temp_list_undone)
#             break
#
#         for key, value in element.items():
#             if element['done'] == True:
#                 temp_list_done.append(element['done'])
#             done = len(temp_list_done)
#             break
#     print('Ви маєте - ' + str(undone) + ' невиконаних й виконаних - ' + str(done))
#
#
def if_chosen_l():
    '''part of main funk
    if user picked 'l''''
    con = sqlite3.connect('./data/data.db')
    cur = con.cursor()
    with open('test_data.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='\n',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        res = cur.execute("SELECT * FROM data")
        spamwriter.writerow(res)

    with open('test_data.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
        for row in spamreader:
            ', '.join(row)
            print(row)
#
#
def if_chosen_m():
    '''part of main function
    if user picked 'm''''
    con = sqlite3.connect('./data/data.db')
    cur = con.cursor()
    res = cur.execute("SELECT * FROM data")
    print(res.fetchall())
