from connect import db, execute
from Transform import Items, Transaction_data
import pandas as pd

Item_string = ""


for x in Items:
    Item_string += "('" + x["Size"] + "','" + x["name"] + "','" + x["Price"] + "')" + ","

Item_string = Item_string.rstrip(Item_string[-1])


execute(
    [f"""
    INSERT INTO Items (size,item_name,price) VALUES {Item_string}
    ;"""]
)

locations_list = []
for Item in Transaction_data:
    if Item['Location'] not in locations_list:
        locations_list.append(Item['Location'])

print(locations_list)

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

card_data = []
for item in Transaction_data:
    if item['Card_Details'] not in card_data:
        card_data.append(item['Card_Details'])

print(card_data)
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


execute(
    ["""INSERT INTO transactions(transaction_id, date_time, location_id, basket_id, total, payment_id) VALUES ("""]
