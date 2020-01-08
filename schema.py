import sqlite3

def schema():
    CREATE_SQL_ACCOUNTS = """
    CREATE TABLE accounts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(50),
        password VARCHAR(30),
        token VARCHAR
    ); """

    CREATE_SQL_RECIPES = """
    CREATE TABLE recipes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipe_id INTEGER,
        recipe_image VARCHAR,
        recipe_title VARCHAR,
        account_id INTEGER,
        FOREIGN KEY("account_id") REFERENCES accounts(id)
    ); """
    


    DROPSQL_ACCOUNTS = "DROP TABLE IF EXISTS accounts;"
    DROPSQL_RECIPES = "DROP TABLE IF EXISTS recipes;"
    DROPSQL_ACCOUNTS_RECIPES = "DROP TABLE IF EXISTS accounts_recipes;"


    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()
        cursor.execute(DROPSQL_ACCOUNTS)
        cursor.execute(DROPSQL_RECIPES)
        cursor.execute(DROPSQL_ACCOUNTS_RECIPES)
        cursor.execute(CREATE_SQL_ACCOUNTS)
        cursor.execute(CREATE_SQL_RECIPES)

if __name__ == "__main__":
    schema()