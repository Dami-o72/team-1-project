import boto3, csv, psycopg2
from src.Extract import extract_data
from src.Transform import General_Transformations, Transform_products, Transform_locations, Transform_transactions, \
    Transform_Basket
from src.Connect import execute, execute_store_var, drop, create, tables, drop_tables
from src.Load import load_products, load_locations, load_transactions, load_basket


def handler(event, context):
    Transaction_data = extract_data(event, context)
    Transaction_data = General_Transformations(Transaction_data)
    Individual_product_data = Transform_products(Transaction_data)
    locations_list = Transform_locations(Transaction_data)
    load_products(Individual_product_data)
    load_locations(locations_list)
    Transaction_Final = Transform_transactions(Transaction_data)
    load_transactions(Transaction_Final)
    Basket = Transform_Basket(Transaction_Data)
    load_basket(Basket)


