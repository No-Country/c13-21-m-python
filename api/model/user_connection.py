import psycopg
import os

#Constants from environment variables
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")



class UserConnection():
    conn = None

    #constructor class
    def __init__(self):
        try:
            self.conn = psycopg.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password = DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT
            )
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()

    #mostrar publicaciones segun pais de usuario
    def read_publications_by_country(self, country):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM publications INNER JOIN users ON publications.id = users.id WHERE country = %s
            """, (country,))
            return data.fetchall()

    #destructor class
    def __def__(self):
        self.conn.close()
    
    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                            INSERT INTO "users"(email, pass_user, country) VALUES(%(email)s, %(password)s, %(country)s)
                        """, data)
        self.conn.commit()
    #destructor class
    def __def__(self):
        self.conn.close()

