import sqlite3

def seed(): 

    with sqlite3.connect('data.db') as conn: 
            cursor = conn.cursor()
            SQL = """ INERT INTO accounts (email_address, password_hash, first_name, last_name, token)
            VALUES ("caroline.gbowski@gmail.com", "password_hash", "Caroline", "Grabowski", "1111111111");"""
            cursor.execute(SQL)
            SQL = """ INERT INTO recipes (recipe_api)
            VALUES ("query");"""
            cursor.execute(SQL)
            SQL = """ INSERT INTO accounts_recipes (account_id, recipe_id)
            VALUES (1, 1);"""
            cursor.execute(SQL)
        


if __name__ == "__main__":
    seed()