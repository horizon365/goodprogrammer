# coding: utf-8
import subprocess

PREFIX = "mysql -u root -h djangodb -p'123456' -e '{}'"
CREATETABLE = 'use mysql ;create table registry (name varchar(100), tag varchar(100))'
INSERT = 'use mysql;insert into registry (name, tag) values ("{}", "{}")'


def operation(name, tag):
    try:
        print(PREFIX.format(CREATETABLE))
        subprocess.check_call(PREFIX.format(CREATETABLE), shell=True)
    except Exception as e1:
        print('table already exist!', e1)

    try:
        subprocess.check_call(PREFIX.format(INSERT.format(name, tag)), shell=True)
    except Exception as e2:
        print('insert fail, may already exist!', e2)

