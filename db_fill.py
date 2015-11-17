import csv
from app import db, models

reader = csv.reader(open('GNC-Similar-Data-Reduced.csv'), delimiter=',', quotechar='"')
valid = [0, 1, 2]
count = 0
for row in reader:
    count += 1
    if row[0] != 'BinLocation':
        product = models.Product()
        if len(row) >= 8 and row[8] is not '':
            product.description = row[8].decode('unicode_escape').encode('ascii','ignore')
        if len(row) >= 18 and row[18] is not '':
            product.item_id = int(row[18])
        if len(row) >= 19 and row[19] is not '':
            product.item_lookup_code = row[19]
        if len(row) >= 23 and row[23] is not '':
            if row[23] == "NULL":
                product.price = None
            else:
                product.price = float(row[23])
        if len(row) >= 32 and row[32] is not '':
            if row[32] == "NULL":
                reader.next()
                continue

            if int(row[32]) not in valid:
                reader.next()
                continue
            product.item_type = int(row[32])
        if len(row) >= 33 and row[33] is not '':
            product.cost = float(row[33])
        if len(row) >= 34 and row[34] is not '':
            product.quantity = float(row[34])
        if len(row) >= 35 and row[35] is not '':
            product.reorder_point = float(row[35])
        if len(row) >= 37 and row[37] is not '':
            product.restock_level = int(row[36])
        if len(row) >= 41 and row[41] is not '':
            product.parent_item = int(row[41])
        if len(row) >= 48 and row[48] is not '':
            product.extended_description = row[48]
        if len(row) >= 70 and row[70] is not '':
            product.inactive = int(row[70])
        if len(row) >= 73 and row[73] is not '' and row[73] != "NULL":
            product.msrp = float(row[73])
        if len(row) >= 74 and row[74] is not '':
            product.date_created = row[74]

        #Add the created entry to the table
        db.session.add(product)

db.session.commit()
