#CONQUERED BY BERA KURT
#this was an exam prepared by meta

menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    print('Calculating bill subtotal...')

    items = []
    items = [item["price"] for item in order]
    subtotal_normal = sum(items)
    subtotal = round(subtotal_normal, 2)
    return subtotal

    raise NotImplementedError()

def calculate_tax(subtotal):

    print('Calculating tax from subtotal...')

    tax = subtotal * (15/100)
    tax_rounded = round(tax, 2)
    return tax_rounded
    raise NotImplementedError()

def summarize_order(order):
    
    items = []
    items = [item["price"] for item in order]
    subtotal = sum(items)

    tax = subtotal * (15/100)
    tax_rounded = round(tax, 2)

    total_normal = subtotal + tax_rounded
    total = round(total_normal, 2)

    names = []
    for item in order:
        names.append({"name":item["name"], "price":item["price"]})
    return (names, total)
    raise NotImplementedError()

def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order

def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    items, subtotal = summarize_order(order)
    print(items, subtotal)

if __name__ == "__main__":
    main()
