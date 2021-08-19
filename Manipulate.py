from Extract import extract_data, csv_path


Transaction_data = extract_data(csv_path)


#Removes all names from data as it is sensitive
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
        data['Card_Details'] = 'NULL'
    else:
        data['Card_Details'] = data['Card_Details'].split(',')[0]


Store_items = list()


#Iterates through all 'Product_data' and cleans it, leaving just products
for data in products_list:
    for x in data:
        if x.lower() not in Store_items:
            if x == ' ' or x == '':
                continue
            if x.lower() in ['large', 'small', 'regular', 'medium']:
                continue
            try:
                float(x)
            except ValueError:
                Store_items.append(x.lower())


#Creates Enumerated dictionary of each Product sold by cafe
Items = {}
for products in Store_items:
    Items[Store_items.index(products)] = products