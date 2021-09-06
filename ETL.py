from Extract import extract_data, csv_path
from Transform_2 import Transform_transactions,Transform_Basket,Transform_payments,Transform_locations,Transform_products,General_Transformations
from Load_2 import load_locations,load_basket,load_payments,load_products,load_transactions

Transaction_data = extract_data(csv_path)
def etl(Transaction_data):
    Transaction_data = General_Transformations(Transaction_data)
    Individual_product_data = Transform_products(Transaction_data)
    card_data = Transform_payments(Transaction_data)
    locations_list = Transform_locations(Transaction_data)
    load_products(Individual_product_data)
    load_locations(locations_list)
    load_payments(card_data)
    Transaction_Final = Transform_transactions(Transaction_data)
    load_transactions(Transaction_Final)
    Basket = Transform_Basket(Transaction_data)
    load_basket(Basket)

etl(Transaction_data)