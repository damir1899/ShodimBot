import psycopg2
from core.config import *


def PGconnection():
    with psycopg2.connect(
        host = PGHOST,
        database = PGDATABASE,
        user = PGUSER,
        password = PGPASSWORD,
        port = PGPORT ) as connection:
        connection.autocommit = True
    return connection


def CheckRegistration(user_id):
    with PGconnection().cursor() as cursor:
        cursor.execute(f"SELECT * FROM users WHERE userid = {user_id}")
        usercheck = cursor.fetchone()
        return usercheck


def RegistrationUserPG(user_id, username, first_name, last_name, phone):
    with PGconnection().cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS users(\
                        id SERIAL PRIMARY KEY,\
                        userid BIGINT NOT NULL,\
                        username VARCHAR(50) DEFAULT 'Not username',\
                        first VARCHAR(250) DEFAULT 'Not first_name',\
                        last VARCHAR(250) DEFAULT 'Not first_name',\
                        phone VARCHAR(20) NOT NULL,\
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        if CheckRegistration(user_id) is None:
            cursor.execute(
                "INSERT INTO users(userid, username, first, last, phone)\
                VALUES (%s, %s, %s, %s, %s)", (user_id, username, first_name, last_name, phone)
            )
        else:
            pass
        

def add_information_places(category, title, information, url, photo):
    with PGconnection().cursor() as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS places(\
            id SERIAL PRIMARY KEY,\
            category VARCHAR(150) NOT NULL,\
            title VARCHAR(150) NOT NULL,\
            information VARCHAR(255) NOT NULL,\
            url TEXT NOT NULL,\
            photo TEXT NOT NULL,\
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
        ) 
        cursor.execute(
            f"SELECT * from places WHERE title = '{title}'\
            and information = '{information}' and url = '{url}'"
        )
        CheckPlaces = cursor.fetchone()
        if CheckPlaces is None:
            cursor.execute(
                "INSERT INTO places(category, title, information, url, photo)\
                VALUES (%s, %s, %s, %s, %s)", (category, title, information, url, photo)
            )
        else:
            pass