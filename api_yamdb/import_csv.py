import csv
import sqlite3


connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

create_table = '''CREATE TABLE api_category(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                slug TEXT NOT NULL);
                '''
cursor.execute(create_table)
with open('static/data/category.csv', 'r') as csvfile:
    dr = csv.DictReader(csvfile)
    contents = [(i['name'], i['slug']) for i in dr]
insert_records = "INSERT INTO api_category (name, slug) VALUES(?, ?)"
cursor.executemany(insert_records, contents)


create_table = '''CREATE TABLE api_genre(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                slug TEXT NOT NULL);
                '''
cursor.execute(create_table)
with open('static/data/genre.csv', 'r') as csvfile:
    dr = csv.DictReader(csvfile)
    contents = [(i['name'], i['slug']) for i in dr]
insert_records = "INSERT INTO api_genre (name, slug) VALUES(?, ?)"
cursor.executemany(insert_records, contents)


create_table = '''CREATE TABLE api_title(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                year INTEGER NOT NULL,
                category INTEGER);
                '''
cursor.execute(create_table)
with open('static/data/titles.csv', 'r') as csvfile:
    dr = csv.DictReader(csvfile)
    contents = [(i['name'], i['year'], i['category']) for i in dr]
insert_records = "INSERT INTO api_title (name, year, category) VALUES(?, ?, ?)"
cursor.executemany(insert_records, contents)


create_table = '''CREATE TABLE api_title_genre(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title_id INTEGER NOT NULL,
                genre_id INTEGER NOT NULL);
                '''
cursor.execute(create_table)
with open('static/data/genre_title.csv', 'r') as csvfile:
    dr = csv.DictReader(csvfile)
    contents = [(i['title_id'], i['genre_id']) for i in dr]
insert_records = '''INSERT INTO api_title_genre 
                 (title_id, genre_id) VALUES(?, ?)
                 '''
cursor.executemany(insert_records, contents)


create_table = '''CREATE TABLE users_user(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                role TEXT NOT NULL,
                bio TEXT,
                first_name TEXT,
                last_name TEXT);
                '''
cursor.execute(create_table)
with open('static/data/users.csv', 'r') as csvfile:
    dr = csv.DictReader(csvfile)
    contents = [(i['username'], i['email'], i['role'], i['bio'],
                 i['first_name'], i['last_name']) for i in dr]
insert_records = '''INSERT INTO users_user 
                 (username, email, role, bio, first_name, last_name) 
                 VALUES(?, ?, ?, ?, ?, ?)
                 '''
cursor.executemany(insert_records, contents)

connection.commit()
connection.close()
