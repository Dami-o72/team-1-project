import csv, boto3


# Extracts data from csv at path into dictionary
def extract_data(event, context):
    # Get key and bucket informaition
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']

    # use boto3 library to get object from S3
    s3 = boto3.client('s3')
    s3_object = s3.get_object(Bucket=bucket, Key=key)
    data = s3_object['Body'].read().decode('utf-8')

    fieldnames = ['Date_time', 'Location', 'Name', 'Products', 'Price', 'Payment_type', 'Card_Details']
    csv_data = csv.DictReader(data.splitlines(), fieldnames=fieldnames)
    Transaction_data = list(csv_data)
    for line in Transaction_data:
        line['Products'] = list(line['Products'].split(','))
        products_list = []
        for data in line['Products']:
            size = data.split()[0]
            price = data.rsplit(' - ')[-1]
            x = len(size)
            y = len(price) + 2
            name = data[(x + 1): (-y)].strip()
            product = {"Size": size, "Name": name, "Price": price}
            products_list.append(product)
            line['Products'] = products_list

    return Transaction_data