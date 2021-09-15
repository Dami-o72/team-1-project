import psycopg2
import boto3

tables = \
    """
    CREATE TABLE items (
    item_id INT IDENTITY(0,1) PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    size VARCHAR(255) NOT NULL,
    price decimal(12,2) NOT NULL
    );
    CREATE TABLE locations (
    location_id INT IDENTITY(1,1) PRIMARY KEY,
    location varchar(255) NOT NULL
    );
    CREATE TABLE transactions (
    transaction_id INT IDENTITY(1,1) PRIMARY KEY,
    date_time DATETIME,
    location_id INT REFERENCES locations(location_id),
    total decimal(12,2),
    payment_type varchar(255)
    );
    CREATE TABLE basket (
    transaction_id INT REFERENCES transactions(transaction_id),
    item_id INT REFERENCES items(item_id),
    no_of_items INT NOT NULL
    )
    """

drop_tables = \
    """
    drop table basket;
    drop table transactions;
    drop table locations;
    drop table items
    """


def execute(commands):
    client = boto3.client('redshift', region_name='eu-west-1')

    REDSHIFT_USER = "awsuser"
    REDSHIFT_CLUSTER = "redshiftcluster-jlqz8zhcuit6"
    REDSHIFT_HOST = "redshiftcluster-jlqz8zhcuit6.cc3hslvy2bfm.eu-west-1.redshift.amazonaws.com"
    REDSHIFT_DATABASE = "team-1-db"

    creds = client.get_cluster_credentials(
        DbUser=REDSHIFT_USER,
        DbName=REDSHIFT_DATABASE,
        ClusterIdentifier=REDSHIFT_CLUSTER,
        DurationSeconds=3600)

    conn = psycopg2.connect(
        user=creds['DbUser'],
        password=creds['DbPassword'],
        host=REDSHIFT_HOST,
        database=REDSHIFT_DATABASE,
        port=5439
    )

    cursor = conn.cursor()
    for command in commands:
        cursor.execute(command)

    cursor.close()
    conn.commit()
    conn.close()


def execute_store_var(commands):
    result = []
    client = boto3.client('redshift', region_name='eu-west-1')

    REDSHIFT_USER = "awsuser"
    REDSHIFT_CLUSTER = "redshiftcluster-jlqz8zhcuit6"
    REDSHIFT_HOST = "redshiftcluster-jlqz8zhcuit6.cc3hslvy2bfm.eu-west-1.redshift.amazonaws.com"
    REDSHIFT_DATABASE = "team-1-db"

    creds = client.get_cluster_credentials(
        DbUser=REDSHIFT_USER,
        DbName=REDSHIFT_DATABASE,
        ClusterIdentifier=REDSHIFT_CLUSTER,
        DurationSeconds=3600)

    conn = psycopg2.connect(
        user=creds['DbUser'],
        password=creds['DbPassword'],
        host=REDSHIFT_HOST,
        database=REDSHIFT_DATABASE,
        port=5439
    )

    cursor = conn.cursor()
    for command in commands:
        cursor.execute(command)
        fetch = cursor.fetchone()
        if fetch != None:
            result += fetch

    cursor.close()
    conn.commit()
    conn.close()
    return result


def drop(drop_tables):
    execute(drop_tables)


def create(tables):
    execute(tables)