import contextlib

from data.data import *
from source.source import *
from helpers.helpers import *
import datetime
import json
from time import strftime
import csv
import os
import sqlite3


con = sqlite3.connect('./data/data.db')
cur = con.cursor()

print('Доступні функціі')
start()
picker = input('Виберіть функцію, введіть відповідну букву: ')

while True:
    if picker == 'a':
        cls()
        if_chosen_a()
        chosen_a_name()
        chosen_a_descrip()
        chosen_a_prio()
        chosen_a_datetime()
        chosen_a_done()
        temp_list = list(temp_dict.values())
        cur.execute('INSERT INTO data (title, description, priority, due_date, done) VALUES (?, ?, ?, ?,?)', temp_list)
        con.commit()
        con.close()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')


    elif picker == 'b':
        cls()
        if_chosen_b()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'c':
        cls()
        if_chosen_c()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'd':
        cls()
        if_chosen_d()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'e':
        cls()
        if_chosen_e()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'f':
        cls()
        if_chosen_f()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'g':
        cls()
        if_chosen_g()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'h':
        cls()
        if_chosen_h()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'i':
        cls()
        if_chosen_i()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'j':
        cls()
        # if_chosen_j()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'k':
        cls()
        if_chosen_k()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'l':
        cls()
        if_chosen_l()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'm':
        cls()
        if_chosen_m()
        start()
        picker = input('Виберіть функцію, введіть відповідну букву: ')

    elif picker == 'n':
        quit()

    else:
        start()
        picker = input('Виберіть функцію та введіть відповідну букву: ')
