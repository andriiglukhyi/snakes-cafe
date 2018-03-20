    import sys

def cafe():
        appitizers = {
            'wings': 0,
            'cookies': 0,
            'spring rolls': 0
        }
        entrees = {
            'salmon': 0,
            'steak': 0,
            'meat tornado': 0,
        }
        desserts = {
           'ice cream': 0,
           'cake': 0,
           'pie': 0
        }
        drinks = {
            'coffee': 0,
            'tea': 0,
            'blood': 0
        }
        final_order = {}

        print('*' * 38 + '\n' + '**    Welcome to the Snakes Cafe!   **' +
              '\n' + '**    Please see our menu below.    **' + '\n' +
              '\n' + '**    Type Order to see your current order.    **' +
              '\n' + '** To quit at any time, type "quit" **' + '\n' +
              '*' * 38)
        print('\nAppitizers'+'\n' + '-------------')
        for key in appitizers.keys():
            print(key)
        print('\nEntrees'+'\n' + '-------------')
        for key in entrees.keys():
            print(key)
        print('\nDesserts' + '\n' + '-------------')
        for key in desserts.keys():
            print(key)
        print('\nDrinks'+'\n' + '-------------')
        for key in drinks.keys():
            print(key)

        print('\n' + '*' * 35 + '\n' + '** What would you like to order?**\n' +
              '*' * 35)
        while True
                order = input('> ').lower()
                if (order in appitizers or order in entrees or order in
                        desserts or order in drinks):
                    final_order[order] = 1 + final_order.get(order, 0)
                    print('\n** ' + str(final_order[order]) + ' order(s) of ' +
                          str(order) + ' has been added to your meal **\n')
                elif order.lower() == 'order':
                    print('\n** You have ordered **')
                    for key, val in final_order.items():
                        print('** {} order(s) {} **'.format(val, key))
                elif order.lower() == 'quit':
                    break
                else:
                    print('\n** That item is not on the menu **\n')


if __name__ == '__main__':
    cafe()
    
