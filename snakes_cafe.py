import uuid


class Order:
    """Class for new orders."""
    def __init__(self):
        """Initialize ID and dictionary of items ordered."""
        self.id = str(uuid.uuid1())
        self.final_order = {}

    def __repr__(self):
        """Represent user's order."""
        print('Order {} | items : {} | total : {:.2f}'.format(self.id,
              self.__len__(), self.display_order()))

    def __len__(self):
        """Number of items in order."""
        return sum(self.final_order.values())

    def add_item(self, food, multifood):
        """Add a food item to the running order."""
        if food == multifood and self._stock(food, multifood) is True:
            self.final_order[food] = 1 + self.final_order.get(food, 0)
            print('\n ** {} total order(s) of {} has been added to your meal *'
                  '*\n **Your order cost is {:.2f} **\n'
                  .format(self.final_order[food], food, self.display_order()))
        elif self._stock(food, multifood) is True:
            self._multi_order(food, multifood)

    def print(self):
        """Create or overwrite file with reciept of current order."""
        a = ''
        a += ('\n' + '*' * 61 + '\n' + 'The Snakes Cafe' + '\n' + 'Order ' +
              self.id + '\n' + '=' * 61)
        subtotal = self.display_order()
        for key, val in self.final_order.items():
            if key in menu_items['appitizers']:
                price = menu_items['appitizers'].get(key)[0]*val
            elif key in menu_items['entrees']:
                price = menu_items['entrees'].get(key)[0]*val
            elif key in menu_items['desserts']:
                price = menu_items['desserts'].get(key)[0]*val
            elif key in menu_items['drinks']:
                price = menu_items['drinks'].get(key)[0]*val
            elif key in menu_items['sides']:
                price = menu_items['sides'].get(key)[0] * val
            to_output = ('{} x {}'.format(key, val))
            a += ('\n{:<30} {:>30.2f}'.format(to_output, price))
        tax = subtotal * 0.096
        a += ('\n' + '-' * 61 + '\nSubtotal {:>52.2f}'.format(subtotal))
        a += ('\nSales Tax {:>51.2f}'.format(tax))
        a += ('\n' + '-' * 10 + '\nTotal Due {:>51.2f}\n'.format(subtotal +
              tax))
        with open('receipts/' + self.id + '.txt', 'w') as f:
            f.write(a)

    def remove_item(self, key):
        """Remove a food item from the order."""
        key = key.rsplit(' ', 1)
        if len(key) == 1 or type(int(key[1])) is not int:
            key = key[0]
            if key in self.final_order:
                self.final_order[key] -= 1
                if self.final_order[key] == 0:
                    del self.final_order[key]
                menu_items[find(key)][key][1] += 1
            print('Your current total is ${:.2f}\n'.format(self.display_order()))
        else:
            if key[0] in self.final_order:
                self.final_order[key[0]] -= int(key[1])
                if self.final_order[key[0]] == 0:
                    del self.final_order[key[0]]
                menu_items[find(key[0])][key[0]][1] += int(key[1])
            print('Your current total is ${:.2f}\n'.format(self.display_order()))

    def print_receipt(self):
        """Display reciept of current order."""
        print('\n' + '*' * 61 + '\n' + 'The Snakes Cafe' + '\n' + 'Order ' +
              self.id + '\n' + '=' * 61)
        subtotal = self.display_order()
        for key, val in self.final_order.items():
            if key in menu_items['appitizers']:
                price = menu_items['appitizers'].get(key)[0]*val
            elif key in menu_items['entrees']:
                price = menu_items['entrees'].get(key)[0]*val
            elif key in menu_items['desserts']:
                price = menu_items['desserts'].get(key)[0]*val
            elif key in menu_items['drinks']:
                price = menu_items['drinks'].get(key)[0]*val
            elif key in menu_items['sides']:
                price = menu_items['sides'].get(key)[0] * val
            to_output = ('{} x {}'.format(key, val))
            print('{:<30} {:>30.2f}'.format(to_output, price))
        tax = subtotal * 0.096
        print('-' * 61 + '\nSubtotal {:>52.2f}'.format(subtotal))
        print('Sales Tax {:>51.2f}'.format(tax))
        print('-' * 10 + '\nTotal Due {:>51.2f}\n'.format(subtotal + tax))
        return round(subtotal+tax, 2)

    def _stock(self, name, number):
        """Check if item is in stock."""
        category = find(name)
        num = 1
        if name != number:
            try:
                num = int(number.rsplit(' ', 1)[1])
            except ValueError:
                pass
        if num <= menu_items[category][name][1]:
            menu_items[category][name][1] -= num
            return True
        else:
            print('Not enough stock')
            return False

    def _multi_order(self, name, item):
        """Add multiple items to the order."""
        quant = 0
        try:
            quant = int(item.rsplit(' ', 1)[1])
        except ValueError:
            pass
        if quant <= 0:
            print('Sorry it\'s not a value')
            return 1
        else:
            self.final_order[name] = quant + self.final_order.get(name, 0)
            print('\n ** {} total order(s) of {} has been added to your meal *'
                  '* \n** Your order cost is {:.2f} **\n'
                  .format(self.final_order[name], name, self.display_order()))

    def display_order(self):
        """Sum a subtotal of selected menu items prices."""
        subtotal = 0
        for key, val in self.final_order.items():
            if key in menu_items['appitizers']:
                subtotal += menu_items['appitizers'].get(key)[0] * val
            elif key in menu_items['entrees']:
                subtotal += menu_items['entrees'].get(key)[0]*val
            elif key in menu_items['desserts']:
                subtotal += menu_items['desserts'].get(key)[0]*val
            elif key in menu_items['drinks']:
                subtotal += menu_items['drinks'].get(key)[0]*val
            elif key in menu_items['sides']:
                subtotal += menu_items['sides'].get(key)[0] * val
        return subtotal


def find(inner_key):
    """Find menu categories."""
    for key in menu_items.keys():
        if inner_key in menu_items[key]:
            return key
    return 0


new_order = Order()

default_items = {
    'appitizers': {
        'wings': [13.00, 10],
        'cookies': [17.22, 14],
        'spring rolls': [13.56, 24],
        'pasta chips': [2.56, 22],
        'lasagna': [24.14, 10],
        'mozzarella': [12.45, 11],
        'small salad': [6.00, 40],
        'bread': [5.50, 100],
        'baby legs': [0.99, 2],
        'sliders': [10.00, 10],
        'chips': [3.50, 400],
        'salsa': [1.24, 400]
    },
    'entrees': {
        'salmon': [23.55, 20],
        'steak': [11.56, 12],
        'country fried chicken': [24.05, 11],
        'chopped grilled angus': [16.94, 12],
        'crispy fish tacos': [23.67, 10],
        'meat tornado': [11.45, 13],
        'fish sticks': [12.32, 10],
        'taylor swift': [89.21, 1],
        'nomnomnom': [1.00, 50],
        'pasta': [16.00, 30],
        'roast': [24.34, 20],
        'pig feet': [10.99, 4]
    },
    'desserts': {
        'ice cream': [2.17, 12],
        'cake': [3.67, 23],
        'molten chocolate cake': [12.45, 12],
        'cheesecake': [24.37, 45],
        'chip cookie': [10.46, 23],
        'pie': [23.45, 34],
        'more pie': [23.46, 35],
        'burger shake': [16.20, 20],
        'snack': [3.50, 350],
        'cream': [0.50, 1000],
        'popsicle': [1.00, 50],
        'tongues': [0.69, 69]
    },
    'drinks': {
        'coffee': [2.24, 34],
        'tea': [1.45, 12],
        'milk': [2.00, 11],
        'vodka': [4.45, 34],
        'water': [2.35, 10],
        'blood': [10.00, 23],
        'tequila': [20.00, 20],
        'tears': [100.99, 1000],
        'swamp juice': [0.23, 23],
        'whiskey': [10.99, 99],
        'beer': [5.00, 500],
        'wine': [6.00, 500]
    },
    'sides': {
        'onion rings': [10.45, 12],
        'gristmill fries': [11.00, 23],
        'gruene beans': [30.45, 23],
        'yellow & green squash': [30.00, 23],
        'homemade mashed potatoes': [25.00, 23],
        'steamed fresh veggies': [40.00, 40],
        'rice': [1.20, 120],
        'cheese': [17.38, 30],
        'an on fire garbage can': [0.01, 9001],
        'angels': [99999.99, 2],
        'devils': [0.00, 100000],
        'me': [1000000000.00, 1]
    }
}


def menu():
    """Prints the menu."""
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
**    A filepath ending in .csv     **
**      can be used as a menu       **
**
**     "order" will show bill       **
**    "print" print your reciept    **
**
** To quit at any time, type "quit" **
**************************************''')
    print('\nAppitizers' + '\n' + '-------------')
    for key, value in menu_items['appitizers'].items():
        print('{} - ${:.2f}'.format(key, value[0]))
    print('\nEntrees' + '\n' + '-------------')
    for key, value in menu_items['entrees'].items():
        print('{} - ${:.2f}'.format(key, value[0]))
    print('\nDesserts' + '\n' + '-------------')
    for key, value in menu_items['desserts'].items():
        print('{} - ${:.2f}'.format(key, value[0]))
    print('\nDrinks' + '\n' + '-------------')
    for key, value in menu_items['drinks'].items():
        print('{} - ${:.2f}'.format(key, value[0]))
    print('\nSides' + '\n' + '-------------')
    for key, value in menu_items['sides'].items():
        print('{} - ${:.2f}'.format(key, value[0]))
    print('\n' + '*' * 35 + '\n' + '** What would you like to order?**\n' +
          '*' * 35)


def search(key):
    """Search the dictionary to print the set of keys from a specific meal."""
    a = []
    for food in menu_items[key].keys():
        a.append(food)
        print(food)
    return sorted(a)


def open_and_read(path):
    """Create menu from csv."""
    menu_csv = {}
    with open(path, 'r') as f:
        test = f.read().split('\n')
        for item in test:
            item = item.split(',')
            if item[0] not in menu_csv:
                menu_csv[item[0]] = {}
                menu_csv[item[0]][item[1]] = [float(item[2]), int(item[3])]
            else:
                menu_csv[item[0]].update({item[1]: [float(item[2]),
                                         int(item[3])]})
    return menu_csv


def create(filepath):
    """Use csv menu if possible."""
    try:
        global menu_items
        menu_items = open_and_read(filepath)
    except (FileNotFoundError, TypeError):
        return default_items


def cafe():
    """Handle user input to call correct methods and functions."""
    while True:
        user_order = input('> ').lower()
        try:
            int(user_order[-1:])
            order = user_order.rsplit(' ', 1)[0]
            print(order)
        except ValueError:
            order = user_order
        if (order in menu_items['appitizers'] or order in
            menu_items['entrees'] or order in menu_items['desserts'] or
           order in menu_items['drinks'] or order in menu_items['sides']):
            new_order.add_item(order, user_order)
        elif user_order in menu_items.keys():
            search(order)
        elif user_order == 'order':
            new_order.print_receipt()
        elif user_order.split(' ')[0] == 'remove':
            new_order.remove_item(user_order.split(' ', 1)[1])
        elif user_order[-4:] == '.csv':
            create(user_order)
            menu()
            new_order.final_order.clear()
        elif user_order == 'menu':
            menu()
        elif user_order == 'print':
            new_order.print()
        elif user_order == 'quit':
            break
        else:
            print('\n** That item is not on the menu **\n')
            return False


if __name__ == '__main__':
    """Run the app."""
    try:
        menu_items = create(None)
        menu()
        cafe()

    except KeyboardInterrupt:
        print('Have a nice day!')
