import sys
import uuid 

def cafe():
        appitizers = {
            'wings': 13,
            'cookies': 17.22,
            'spring rolls': 13.56,
            'pasta chips' : 2.56,
            'lasagna':24.14,
            'mozzarella':12.45
        }
        entrees = {
            'salmon': 23.55,
            'steak': 11.56,
            'country fried chicken' : 24.05,
            'chopped grilled angus' : 16.94,
            'crispy fish tacos' : 23.67,
            'meat tornado': 11.45
        }
        desserts = {
           'ice cream': 2.17,
           'cake': 3.67,
           'molten chocolate cake': 12.45,
           'cheesecake': 24.37,
           'chip cookie': 10.46,
           'pie': 23.45
        }
        drinks = {
            'coffee': 2.24,
            'tea': 1.45,
            'milk': 2,
            'vodka':4.45,
            'water': 2.35,
            'blood': 10
        }
        sides = {
            'onion rings' : 10.45,
            'gristmill fries' : 11,
            'gruene beans' : 30.45,
            'yellow & green squash' : 30,
            'homemade mashed potatoes' : 25,
            'steamed fresh veggies' : 40
            }
        final_order = {}
        order_number = str(uuid.uuid1())

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
        print('\nSides'+'\n' + '-------------')
        for key in sides.keys():
            print(key)

        print('\n' + '*' * 35 + '\n' + '** What would you like to order?**\n' +
              '*' * 35)
        while True:
                order = input('> ').lower()
                if (order in appitizers or order in entrees or order in
                        desserts or order in drinks):
                    final_order[order] = 1 + final_order.get(order, 0)
                    print('\n** ' + str(final_order[order]) + ' order(s) of ' +
                          str(order) + ' has been added to your meal **\n')

                elif order.lower() == 'order':
                    subtotal = 0
                    print('*'*35 + '\n' + 'The Snakes Cafe' + '\n'+ 'Oreder ' + order_number)
                    for key,val in final_order.items():
                        if key in appitizers:
                            price = appitizers.get(key)*val
                            subtotal += price
                        elif key in entrees: 
                            price = entrees.get(key)*val
                            subtotal += price
                        elif key in desserts:
                            price = desserts.get(key)*val
                            subtotal += price
                        elif key in drinks:
                            price = drinks.get(key)*val
                            subtotal += price
                        to_output = ('{} x {}'.format(key,val ))

                elif order.lower() == 'quit':
                    break
                else:
                    print('\n** That item is not on the menu **\n')


if __name__ == '__main__':
    cafe()
    
    
