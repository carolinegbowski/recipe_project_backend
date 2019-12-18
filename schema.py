import sqlite3

def schema():
    CREATE_SQL_ACCOUNTS = """
    CREATE TABLE accounts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email_address VARCHAR(50),
        password_hash VARCHAR(30),
        first_name VARCHAR(200),
        last_name VARCHAR(200),
        token VARCHAR
    ); """

    CREATE_SQL_RECIPES = """
    CREATE TABLE recipes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipe_api VARCHAR
    ); """
    
    CREATE_SQL_ACCOUNTS_RECIPES = """
    CREATE TABLE accounts_recipes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER,
        recipe_id INTEGER,
        FOREIGN KEY ("account_id") REFERENCES accounts(id),
        FOREIGN KEY ("recipe_id") REFERENCES recipes(id)
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
        cursor.execute(CREATE_SQL_ACCOUNTS_RECIPES)


if __name__ == "__main__":
    schema()