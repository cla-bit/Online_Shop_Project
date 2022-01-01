import pandas as pw
import datetime


pgoods = [
    {'Product': 'Fanta', 'Unit Price': 150, 'Quantity': 20}, {'Product': 'Gin', 'Unit Price': 150, 'Quantity': 30},
    {'Product': 'Hennessy', 'Unit Price': 2300, 'Quantity': 13},
    {'Product': 'Ginger', 'Unit Price': 150, 'Quantity': 20},
    {'Product': 'Cocacola', 'Unit Price': 150, 'Quantity': 30},
    {'Product': 'Paper', 'Unit Price': 2300, 'Quantity': 24},
    {'Product': 'Flower', 'Unit Price': 150, 'Quantity': 20}, {'Product': 'Milo', 'Unit Price': 150, 'Quantity': 30},
    {'Product': 'Bournvita', 'Unit Price': 150, 'Quantity': 20},
    {'Product': 'Skirt', 'Unit Price': 150, 'Quantity': 30}, {'Product': 'Short', 'Unit Price': 2300, 'Quantity': 56},
    {'Product': 'Chocolate', 'Unit Price': 150, 'Quantity': 20},
    {'Product': 'Biro', 'Unit Price': 150, 'Quantity': 30}, {'Product': 'Shirt', 'Unit Price': 2300, 'Quantity': 40},
    {'Product': 'Apple', 'Unit Price': 150, 'Quantity': 20}, {'Product': 'Pawpaw', 'Unit Price': 150, 'Quantity': 30},
    {'Product': 'Tangerine', 'Unit Price': 2300, 'Quantity': 84}, {'Product': 'Onion', 'Unit Price': 150, 'Quantity': 20},
    {'Product': 'Garlic', 'Unit Price': 150, 'Quantity': 30}, {'Product': 'Maggi', 'Unit Price': 2300, 'Quantity': 132},
    {'Product': 'Pepper', 'Unit Price': 150, 'Quantity': 20}, {'Product': 'Knorr', 'Unit Price': 150, 'Quantity': 30},
    {'Product': 'Tapiko', 'Unit Price': 2300, 'Quantity': 235}, {'Product': 'Tomato', 'Unit Price': 150, 'Quantity': 20},
    {'Product': 'Hollandia', 'Unit Price': 150, 'Quantity': 30}, {'Product': 'Chivita', 'Unit Price': 2300, 'Quantity': 124}
]

product = []
unit_price = []
quantity = []


def display_table():
    pd_name = []
    pd_price = []
    pd_quantity = []
    for i in pgoods:
        pd_name.append(i['Product'])
        pd_price.append(i['Unit Price'])
        pd_quantity.append(i['Quantity'])
    pd_goods = pw.DataFrame(
        {
            'Products': pd_name,
            'Price': pd_price,
            'Qty': pd_quantity
        }
    )
    pd_goods.index = pd_goods.index + 1
    print('------------ PRODUCTS IN STOCK -------------')
    print(pd_goods)


def qty_chk(qty):  # ensures the input is a digit
    while not qty.isdigit():
        qty = input('Enter a number: ')
    else:
        return qty


def display():
    print('*' * 100)
    print('*', ' ' * 35, 'Welcome to Benuriita Store', ' ' * 33, '*')
    print('*' * 100)


def u_item():
    zx = True
    while zx:
        display_table()
        prod_item = input('\nproduct? ')
        prod_item = prod_item.title()
        for i in pgoods:
            if prod_item.title() == i.get('Product'):
                print(f"--------Here is the product and unit price---------\nProduct: {prod_item.title()}"
                      f"\nPrice: {i.get('Unit Price')}\n")
                print('\nEnter the quantity that you want')
                qty_item = input('Qty: ')
                qty_chk(qty_item)

                while i.get('Quantity') != 0 and i.get('Quantity') >= int(qty_item):
                    print('Do you want to buy?')
                    w = input('>> ')
                    if w == 'yes':
                        print(f"{i.get('Product')} is added to your shop cart.")
                        a = i.get('Quantity') - int(qty_item)
                        i['Quantity'] = a
                        product.append(i.get('Product'))
                        unit_price.append(i.get('Unit Price'))
                        quantity.append(int(qty_item))
                        print(f"The quantity of {i.get('Product')} has been reduced to {a}")
                        i.update({'Quantity': a})
                        print('Do you want to stop purchasing?')
                        e = input('>> ')
                        if e == 'yes':
                            print('Purchased ended')
                            zx = False

                    break
                else:
                    if i.get('Quantity') == 0:
                        print(f"{i.get('Product')} is out of stock.")
                        break
                    elif int(qty_item) > i.get('Quantity'):
                        print(f"Your {qty_item} is greater than {i.get('Product')}'s quantity.")
                        break
                    zx = True


def tot():
    item = []
    price = []
    qty = []
    cost = []
    for i in product:
        item.append(i)
    for j in unit_price:
        price.append(j)
    for k in quantity:
        qty.append(k)
    for k in range(len(unit_price)):
        r = int(unit_price[k]) * int(quantity[k])
        cost.append(r)
    total_cost = sum(cost)
    td = pw.DataFrame(
        {
            'Item Bought': item,
            'Price': price,
            'Quantity': qty,
            'Cost': cost,
        }
    )
    td.index = td.index + 1
    print(td)
    print(f'Total Cost of items: {total_cost}')
    print(f'Date and Time of purchase: {datetime.datetime.now()}')

    if total_cost > 5000:
        c = (total_cost * 12) / 100
        print(f'Total Cost is more than 5000, pay {c}')
    elif total_cost == 3500:
        b = (total_cost * 10) / 100
        print(f'Total Cost is 3500, pay {b}')
    elif total_cost >= 2000:
        v = (total_cost * 5) / 100
        print(f'Total Cost is between 2000 and 3500, pay {v}')
    else:
        print(f'No discount, pay {total_cost}')

    td.to_csv('useritem.csv')


def benuritta_store():
    display()
    print('1. Purchase Menu\n2. Logout')
    print()
    q = input('> ')
    while not q.isdigit() or int(q) != 2 and int(q) != 1:
        q = input('>> ')
    else:
        if int(q) == 1:
            print('Come on in Shopper.\n')
            u_item()
            tot()
        else:
            print('goodbye')


benuritta_store()
