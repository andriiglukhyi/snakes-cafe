if __name__ =='__main__':
    def cafe():
        Appitizers ={
            'Wings' : 0,
            'Cookies' : 0,
            'Spring Rools' : 0
            }
        Entrees = {
            'Salmon' : 0,
            'Steak' : 0,
            'Meat tornado' : 0,
            }        
        Desserts = { 
           'Ice Cream' : 0,
           'Cake' : 0,
           'Pie' : 0
            }
        Drinks = {
            'Coffee' : 0, 
            'Tea' : 0, 
            'Blood' : 0
            }
        
        meals = [Appitizers, Entrees, Desserts, Drinks]
        meals2 = ['Appitizers', 'Entrees', 'Desserts', 'Drinks']

        print('*'*38)
        print('**    Welcome to the Snakes Cafe!   **')
        print('**    Please see our menu below.    **')
        print('** To quit at any time, type "quit" **')
        print('*'*38)
        print('Appitizers'+'\n'+ '-------------')
        for key in Appitizers.keys():
            print(key)
        print('\n'+'Entrees'+'\n'+ '-------------')
        for key in Entrees.keys():
            print(key)
        print('\n'+'Desserts' +'\n'+ '-------------')
        for key in Desserts.keys():
            print(key)
        print('\n'+'Drinks'+'\n'+ '-------------')
        for key in Drinks.keys():
            print(key)

        
        
cafe()

