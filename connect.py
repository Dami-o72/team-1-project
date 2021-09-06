import psycopg2

# parameters for postgres server
db = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'root',
    'password': 'password'
}


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        # print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**db)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        # print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        # print(db_version)
        # close the communication with the PostgreSQL
        cur.close()
        print("Database connection check pass")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            # print('Database connection closed.')


def execute(commands):
    """ create tables in the PostgreSQL database"""
    result = []
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**db)
        # create a cursor
        cur = conn.cursor()
        # execute each command in commands
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def execute_store_var(commands):
    result = []
    """ create tables in the PostgreSQL database"""
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**db)
        # create a cursor
        cur = conn.cursor()
        # execute each command in commands
        for command in commands:
            cur.execute(command)
            result = cur.fetchone()
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            return result



def check(commands):
    """ create tables in the PostgreSQL database"""
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**db)
        # create a cursor
        cur = conn.cursor()
        # execute each command in commands
        for command in commands:
            cur.execute(command)
        print(cur.fetchone)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


connect()

tables = \
    ["""
    CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    size VARCHAR(255) NOT NULL,
    price decimal(12,2) NOT NULL
    )
    """,
    """
    CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    payment_type VARCHAR(255)
    )
    """,
    """
    CREATE TABLE locations (
    location_id SERIAL PRIMARY KEY,
    location varchar(255) NOT NULL
    )
    """,
    """
    CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    date_time TIMESTAMP,
    location_id INT REFERENCES locations(location_id),
    total decimal(12,2),
    payment_id INT REFERENCES payments(payment_id)
    )
    """,
    """
    CREATE TABLE basket (
    transaction_id INT REFERENCES transactions(transaction_id),
    item_id INT REFERENCES items(item_id),
    no_of_items INT NOT NULL
    )
    """]


drop_tables = \
    ["""
    drop table basket;
    drop table transactions;
    drop table locations;
    drop table payments;
    drop table items
    """]

# execute(drop_tables)
execute(tables)


# test_row = \
#     ["""
#     INSERT INTO Orders (date_time, location, customer_name, basket_id, card_number)
#     VALUES ('2021-02-23 09:01:45', 'Isle of Wight', 'William Perdomo', NULL, 'discover,6011776257398866')
#     """]
#
# # execute(test_row)
#
#
# check_tables = \
#     ["""SELECT EXISTS(SELECT 1 from Transactions)"""]

# check(check_tables)
