import sys
import uuid

menu_items = {
    'appitizers': {
        'wings': 13.00,
        'cookies': 17.22,
        'spring rolls': 13.56,
        'pasta chips': 2.56,
        'lasagna': 24.14,
        'mozzarella': 12.45
    },
    'entrees': {
        'salmon': 23.55,
        'steak': 11.56,
        'country fried chicken': 24.05,
        'chopped grilled angus': 16.94,
        'crispy fish tacos': 23.67,
        'meat tornado': 11.45
    },
    'desserts': {
        'ice cream': 2.17,
        'cake': 3.67,
        'molten chocolate cake': 12.45,
        'cheesecake': 24.37,
        'chip cookie': 10.46,
        'pie': 23.45
    },
    'drinks': {
        'coffee': 2.24,
        'tea': 1.45,
        'milk': 2.00,
        'vodka': 4.45,
        'water': 2.35,
        'blood': 10.00
    },
    'sides': {
        'onion rings': 10.45,
        'gristmill fries': 11.00,
        'gruene beans': 30.45,
        'yellow & green squash': 30.00,
        'homemade mashed potatoes': 25.00,
        'steamed fresh veggies': 40.00
    }
}
final_order = {}
order_number = str(uuid.uuid1())


def menu():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************''')
    print('\nAppitizers' + '\n' + '-------------')
    for key in menu_items['appitizers'].keys():
        print(key)
    print('\nEntrees' + '\n' + '-------------')
    for key in menu_items['entrees'].keys():
        print(key)
    print('\nDesserts' + '\n' + '-------------')
    for key in menu_items['desserts'].keys():
        print(key)
    print('\nDrinks' + '\n' + '-------------')
    for key in menu_items['drinks'].keys():
        print(key)
    print('\nSides' + '\n' + '-------------')
    for key in menu_items['sides'].keys():
        print(key)
    print('\n' + '*' * 35 + '\n' + '** What would you like to order?**\n' +
          '*' * 35)


def search(key):
    for food in menu_items[key].keys():
        print(food)


def add_to_order(food):
    final_order[food] = 1 + final_order.get(food, 0)
    print('\n** ' + str(final_order[food]) + ' order(s) of ' +
          str(food) + ' has been added to your meal **\n')


def order_total():
    subtotal = 0
    print('\n' + '*' * 61 + '\n' + 'The Snakes Cafe' + '\n' + 'Order ' +
          order_number + '\n' + '=' * 61)
    for key, val in final_order.items():
        if key in menu_items['appitizers']:
            price = menu_items['appitizers'].get(key)*val
            subtotal += price
        elif key in menu_items['entrees']:
            price = menu_items['entrees'].get(key)*val
            subtotal += price
        elif key in menu_items['desserts']:
            price = menu_items['desserts'].get(key)*val
            subtotal += price
        elif key in menu_items['drinks']:
            price = menu_items['drinks'].get(key)*val
            subtotal += price
        elif key in menu_items['sides']:
            price = menu_items['sides'].get(key) * val
            subtotal += price
        to_output = ('{} x {}'.format(key, val))
        print('{:<30} {:>30.2f}'.format(to_output, price))
    tax = subtotal * 0.096
    print('-' * 61 + '\nSubtotal {:>52.2f}'.format(subtotal))
    print('Sales Tax {:>51.2f}'.format(tax))
    print('-' * 10 + '\nTotal Due {:>51.2f}\n'.format(subtotal + tax))


def remove(key):
    if key in final_order:
        final_order[key] -= 1
        if final_order[key] == 0:
            del final_order[key]
    order_total()


def cafe():
    menu()
    while True:
        order = input('> ').lower()
        if (order in menu_items['appitizers'] or order in
            menu_items['entrees'] or order in menu_items['desserts'] or
           order in menu_items['drinks'] or order in menu_items['sides']):
            add_to_order(order)
        elif order.lower() in menu_items.keys():
            search(order.lower())
        elif order.lower() == 'order':
            order_total()
        elif order.lower().split(' ')[0] == 'remove':
            remove(order.lower().split(' ', 1)[1])
        elif order.lower() == 'menu':
            menu()
        elif order.lower() == 'quit':
            break
        else:
            print('\n** That item is not on the menu **\n')


if __name__ == '__main__':
    try:
        cafe()
    except KeyboardInterrupt:
        sys.exit(0)
