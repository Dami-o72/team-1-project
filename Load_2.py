from connect import execute

def load_payments(card_data):
# 1) Formats Card details into string correctly and then loads to SQL database
    Payments_string = ""

    for x in card_data:
        Payments_string += "(" + f"'{x}'" + ")" + ","

    Payments_string = Payments_string.rstrip(Payments_string[-1])

    print(Payments_string)
    execute(
        [f"""
        INSERT INTO payments (payment_type) VALUES {Payments_string}
        ;"""]
    )
def load_locations(locations_list):
# 2) Formats Location Data into string correctly and then loads to SQL database
    Location_string = ""

    for x in locations_list:
        Location_string += "(" + f"'{x}'" + ")" + ","
    Location_string = Location_string.rstrip(Location_string[-1])

    print(Location_string)
    execute(
        [f"""
        INSERT INTO locations (location) VALUES {Location_string}
        ;"""]
    )

def load_products(Individual_product_data):
# 3) Formats Product Data into string correctly and then loads to SQL database
    Item_string = ""

    for x in Individual_product_data:
        Item_string += "('" + x["Size"].lower() + "','" + x["Name"].lower() + "','" + x["Price"] + "')" + ","

    Item_string = Item_string.rstrip(Item_string[-1])

    execute(
        [f"""
        INSERT INTO Items (size,item_name,price) VALUES {Item_string}
        ;"""]
    )
def load_transactions(Transaction_Final):
# 4) Formats Transaction Data into string correctly and then loads to SQL database
    Transaction_string = ""

    for T in Transaction_Final:
        Transaction_string += "('" + f"{T['Date_time']}" + "','" + f"{T['Location_id']}" + "','" + f"{T['Total']}" + "','" + f"{T['Payment_id']}" + "')" + ","

    Transaction_string = Transaction_string.rstrip(Transaction_string[-1])

    execute(
        [f"""
        INSERT INTO Transactions (date_time,location_id,total,payment_id) VALUES {Transaction_string}
        ;"""]
    )

def load_basket(Basket):
# 5) Formats Basket Data into string correctly and then loads to SQL database
    Basket_string = ""

    for B in Basket:
        Basket_string += "('" + f"{B['transaction_id']}" + "','" + f"{B['item_id']}" + "','" + f"{B['no_of_items']}" + "')" + ","

    Basket_string = Basket_string.rstrip(Basket_string[-1])

    execute(
        [f"""
        INSERT INTO basket (transaction_id,item_id,no_of_items) VALUES {Basket_string}
        ;"""]
    )
