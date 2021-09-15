from src.connect import execute, execute_store_var


def load_locations(locations_list):
    # 2) Formats Location Data into string correctly and then loads to SQL database
    for x in locations_list:
        print('location', x)
        Verify_loc = execute_store_var([f"""SELECT location FROM locations WHERE location = '{x}'"""])
        print(Verify_loc)
        if x == Verify_loc[0]:
            continue
        else:
            Location_string = "(" + f"'{x}'" + ")"
            execute([f"""INSERT INTO locations (location) VALUES {Location_string}"""])


def load_products(Individual_product_data):
    # 3) Formats Product Data into string correctly and then loads to SQL database
    for x in Individual_product_data:
        print('item', x)
        Verify_prod = execute_store_var([f"""SELECT * FROM items WHERE item_name = '{x['Name'].lower()}' AND size = '{x['Size'].lower()}' AND price = {x['Price']}"""])
        print(Verify_prod)
        if len(Verify_prod) == 0:
            continue
        elif x['Size'].lower() == Verify_prod[2] and x['Name'].lower() == Verify_prod[1]:
            continue
        else:
            Item_string = "('" + x["Size"].lower() + "','" + x["Name"].lower() + "','" + x["Price"] + "')"
            execute([f"""INSERT INTO Items (size,item_name,price) VALUES {Item_string}"""])


def load_transactions(Transaction_Final):
    # 4) Formats Transaction Data into string correctly and then loads to SQL database
    Transaction_string = ""

    for T in Transaction_Final:
        Transaction_string += "('" + f"{T['Date_time']}" + "','" + f"{T['Location_id']}" + "','" + f"{T['Total']}" + "','" + f"{T['Payment_type']}" + "')" + ","

    Transaction_string = Transaction_string.rstrip(Transaction_string[-1])

    execute(
        [f"""
        INSERT INTO Transactions (date_time,location_id,total,payment_type) VALUES {Transaction_string}
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