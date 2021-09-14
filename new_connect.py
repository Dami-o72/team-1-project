import psycopg2
import boto3



def generate_db():
    client = boto3.client('redshift', region_name='eu-west-1')
    
    REDSHIFT_USER = "awsuser"
    REDSHIFT_CLUSTER = "redshiftcluster-jlqz8zhcuit6"
    REDSHIFT_HOST = "redshiftcluster-jlqz8zhcuit6.cc3hslvy2bfm.eu-west-1.redshift.amazonaws.com"
    REDSHIFT_DATABASE = "team-5-db"

    print('getting user credentials')     
    creds = client.get_cluster_credentials(
    DbUser=REDSHIFT_USER,
    DbName=REDSHIFT_DATABASE,
    ClusterIdentifier=REDSHIFT_CLUSTER,
    DurationSeconds=3600
    )

    print('pyscopg2 is conntecting') 
    connectdb = psycopg2.connect(
    user=creds['DbUser'], 
    password=creds['DbPassword'],
    host=REDSHIFT_HOST,
    database=REDSHIFT_DATABASE, 
    port=5439
    )

    # connectdb = database_connection(database=database)
    connectdb.autocommit = True

    print('creating cursor') 
    cursor = connectdb.cursor()

    print('creating items table')
    create_items_table = \
        """
        DROP TABLE IF EXISTS Items;
        CREATE TABLE Items(
            item_id INT IDENTITY(0, 1),
            item_name VARCHAR NOT NULL,
            item_price DECIMAL,
            PRIMARY KEY(item_id)
        );"""

    print('Creating stores table')
    create_stores_table = \
    """
    DROP TABLE IF EXISTS Stores;
    CREATE TABLE Stores(
    store_id INT IDENTITY(0, 1),
    store_name VARCHAR NOT NULL,
    PRIMARY KEY(store_id)
    );"""
    
    print('Creating orders table')
    create_orders_table = \
    """
    DROP TABLE IF EXISTS Orders;
    CREATE TABLE Orders(
    order_id  INT IDENTITY(0, 1),
    transaction_id INTEGER,
    item_id INTEGER,
    quantity INTEGER,
    PRIMARY KEY(order_id),
    FOREIGN KEY(transaction_id) references Transactions(transaction_id),
    FOREIGN KEY(item_id) REFERENCES Items(item_id)
    );"""
    # PostgreSQL uses the  yyyy-mm-dd
    
    print('Creating transactions table')
    create_transactions_table = \
    """
    DROP TABLE IF EXISTS Transactions;
    CREATE TABLE Transactions(
    transaction_id INT IDENTITY(0, 1),
    date DATE, 
    time TIME NOT NULL,
    store_id INTEGER,
    total_price INTEGER,
    cash_or_card VARCHAR NOT NULL,
    PRIMARY KEY(transaction_id),
    FOREIGN KEY(store_id) REFERENCES Stores(store_id)
    );"""
    
    print("creating items table...")
    cursor.execute(create_items_table)
    print('success')
    print("creating stores table..."
    cursor.execute(create_stores_table)
    print('success')
    print("creating transactions table...")
    cursor.execute(create_transactions_table)
    print('success')
    print("creating orders table...")
    cursor.execute(create_orders_table)
    print('success')

    connectdb.close()
    
# database_connection()
# table_creation(database="root")

# def generate_db():
#     table_creation(database="root")