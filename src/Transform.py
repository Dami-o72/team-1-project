from src.connect import execute_store_var

def General_Transformations(Transaction_data):
    for data in Transaction_data:
        del data['Name']
        del data['Card_Details']
        for product in data['Products']:
            if product['Size'] == '' or product['Size'] == ' ':
                product['Size'] = 'NULL'
        date = data['Date_time'].split()[0]
        time = data['Date_time'].rsplit()[-1]
        day = date.split('/')[0]
        month = date.split('/')[1]
        year = date.split('/')[2]
        new_dt = str(year + '/' + month + '/' + day + ' ' + time)
        data['Date_time'] = new_dt
    return Transaction_data

def Transform_products(Transaction_data):
    Individual_product_data = []
    for data in Transaction_data:
        for product in data['Products']:
            if product not in Individual_product_data:
                Individual_product_data.append(product)
    return Individual_product_data

def Transform_locations(Transaction_data):
    locations_list = []
    for Item in Transaction_data:
        if Item['Location'] not in locations_list:
            locations_list.append(Item['Location'])
    return locations_list

def Transform_transactions(Transaction_data):
    Transaction_Final = []
    for Item in Transaction_data:
        Loc_string = f"'{Item['Location']}'"
        Loc_id = execute_store_var([f"""SELECT location_id FROM locations WHERE location = {Loc_string} Limit 1"""])
        New_T = {'Date_time': Item['Date_time'], 'Location_id': Loc_id[0], 'Total': Item['Price'], 'Payment_type': Item['Payment_type']}
        Transaction_Final.append(New_T)
    return Transaction_Final

def Transform_Basket(Transaction_data):
    Basket = []
    for Item in Transaction_data:
        T_string = f"'{Item['Date_time']}'"
        T_id = execute_store_var([f"""SELECT transaction_id FROM transactions WHERE date_time = {T_string}"""])
        for product in Item['Products']:
            name_string = f"'{product['Name'].lower()}'"
            size_string = f"'{product['Size'].lower()}'"
            price_string = f"'{product['Price'].lower()}'"
            I_id = execute_store_var([f"""SELECT item_id FROM items WHERE item_name = {name_string} AND size = {size_string} AND price = {price_string}"""])
            no_of_items = Item['Products'].count(product)
            New_B = {'transaction_id': T_id[0], 'item_id': I_id[0], "no_of_items": no_of_items}
            Basket.append(New_B)
    return Basket