if __name__ == '__main__':
    def cafe():
        appitizers = {
            'Wings': 0,
            'Cookies': 0,
            'Spring Rools': 0
        }
        entrees = {
            'Salmon': 0,
            'Steak': 0,
            'Meat tornado': 0,
        }
        desserts = {
           'Ice Cream': 0,
           'Cake': 0,
           'Pie': 0
        }
        drinks = {
            'Coffee': 0,
            'Tea': 0,
            'Blood': 0
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
        while True:
            order = input('> ')
            if (order in appitizers or order in entrees or order in desserts or
                    order in drinks):
                final_order[order] = 1 + final_order.get(order, 0)
                print('\n** ' + str(final_order[order]) + ' order(s) of ' +
                      str(order) + ' has been added to your meal **\n')
            elif order == 'Order':
                print('\n** You have ordered **')
                for key, val in final_order.items():
                    print('** {} order(s) {} **'.format(val, key))
            elif order == 'quit':
                break
            else:
                print('\n** That item is not on the menu **\n')

cafe()
