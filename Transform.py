from Extract import extract_data, csv_path

Transaction_data = extract_data(csv_path)

#Removes all names from data as it is sensitive, turns products into a list
products_list = []
for data in Transaction_data:
    del data['Name']
    products_list.append(data['Products'].split(','))


#Creates an individual list for product data
for data in Transaction_data:
    for products in products_list:
        data['Products'] = products


#Cleans 'Card_Details' removing personal data and Changes none to null for cash payments
for data in Transaction_data:
    if data['Card_Details'] == 'None':
        data['Card_Details'] = 'CASH'
    else:
        data['Card_Details'] = data['Card_Details'].split(',')[0]


#Iterates through all 'Product_data' and cleans it, leaving just products

Store_items = list()

for data in products_list:
    for x in data:
        if x.lower() not in Store_items:
            if x == ' ' or x == '':
                continue
            elif x.lower() in ['large', 'small', 'regular', 'medium']:
                continue
            try:
                float(x)
            except ValueError:
                Store_items.append(x)


#Creates Enumerated dictionary of each Product sold by cafe
Individual_product_data = []

while len(Individual_product_data) < (len(products_list) / 3):
    for line in products_list:
        New_Data = line[:3]
        Individual_product_data.append(New_Data)


Items = []

for data in Individual_product_data:
    Item = {'Size': data[0].lower(), 'name': data[1].lower(), 'Price': data[2]}
    if Item in Items:
        continue
    Items.append(Item)

for x in Items:
    if x['Size'] == '' or x['Size'] == ' ':
        x['Size'] = 'Null'
