from Extract import extract_data, csv_path
from connect import execute_store_var

Transaction_data = extract_data(csv_path)

for data in Transaction_data:
    del data['Name']

for data in Transaction_data:
    if data['Card_Details'] == 'None':
        data['Card_Details'] = 'CASH'
    else:
        data['Card_Details'] = data['Card_Details'].split(',')[0]

for data in Transaction_data:
    data['Products'] = data['Products'].split(',')


Individual_product_data = []

for data in Transaction_data:
    products_list = []
    for line in ([data['Products'][i:i + 3] for i in range(0, len(data['Products']), 3)]):
        New_Data = {'Size': line[0], 'Name': line[1], 'Price': line[2]}
        products_list.append(New_Data)
        data['Products'] = products_list
        if New_Data not in Individual_product_data:
            Individual_product_data.append(New_Data)

for Item in Individual_product_data:
    if Item['Size'] == '' or Item['Size'] == ' ':
        Item['Size'] = 'Null'

card_data = []
for item in Transaction_data:
    if item['Card_Details'] not in card_data:
        card_data.append(item['Card_Details'])

locations_list = []
for Item in Transaction_data:
    if Item['Location'] not in locations_list:
        locations_list.append(Item['Location'])

Transaction_Final = []
for Item in Transaction_data:
    Loc_string = f"'{Item['Location']}'"
    Loc_id = execute_store_var([f"""SELECT location_id FROM locations WHERE location = {Loc_string} Limit 1"""])
    Pay_string = f"'{Item['Card_Details']}'"
    Pay_id = execute_store_var([f"""SELECT payment_id FROM payments WHERE payment_type = {Pay_string}"""])
    New_T = {'Date_time': Item['Date_time'], 'Location_id': Loc_id[0], 'Total': Item['Price'], 'Payment_id': Pay_id[0]}
    Transaction_Final.append(New_T)

for data in Transaction_data:
    for product in data['Products']:
        if product['Size'] == '' or product['Size'] == ' ':
            product['Size'] = 'NULL'

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

print(Basket)