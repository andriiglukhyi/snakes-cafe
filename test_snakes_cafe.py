import snakes_cafe

snakes_cafe.menu_items = snakes_cafe.default_items


def test_remove():
    """add 1 to the current value"""
    snakes_cafe.new_order.final_order['tea'] = 5
    snakes_cafe.new_order.remove('tea')
    assert snakes_cafe.new_order.final_order['tea'] == 4


def test_order_total():
    """count the total"""
    snakes_cafe.new_order.final_order['wings'] = 1
    snakes_cafe.new_order.final_order['tea'] = 3
    assert snakes_cafe.new_order.display_order() == 19.02

def test_bill():
    """count the bill for"""
    snakes_cafe.new_order.final_order['wings'] = 20
    snakes_cafe.new_order.final_order['tea'] = 20
    assert snakes_cafe.new_order._bill() == 289


def test_search():
    """search for spesick menu item and will print all item inside that
    menu item"""
    key = 'entrees'
    assert snakes_cafe.search(key) == sorted(['salmon', 'steak', 'country '
                                              'fried chicken', 'chopped '
                                              'grilled angus', 'crispy fish '
                                              'tacos', 'meat tornado', 'fish '
                                              'sticks', 'taylor swift',
                                              'nomnomnom'])


def test_remove_0():
    """check if function will remove one item from order."""
    snakes_cafe.new_order.final_order['tea'] = 1
    snakes_cafe.new_order.remove('tea')
    assert 'tea' not in snakes_cafe.new_order.final_order.keys()


def test_add_to_order_one_elemant():
    """Check current order if we add one element two identical items."""
    snakes_cafe.new_order.final_order = {}
    snakes_cafe.new_order.add_item('cake', 'cake')
    snakes_cafe.new_order.add_item('cake', 'cake')
    assert len(snakes_cafe.new_order.final_order) == 1


def test_add_to_order():
    """check if the current backet will change if we add one item."""
    snakes_cafe.new_order.final_order['wings'] = 10
    snakes_cafe.new_order.add_item('wings', 'wings')
    assert snakes_cafe.new_order.final_order['wings'] == 11

def test_add_to_order_couple_items():
    """check if the current backet will change if we add one item."""
    snakes_cafe.new_order.final_order['wings'] = 6
    snakes_cafe.new_order.add_item('wings', 'wings 4')
    assert snakes_cafe.new_order.final_order['wings'] == 10


def test_search_type_output():
    """check if output is list"""
    item = 'entrees'
    print(type(snakes_cafe.search(item)))
    assert 'salmon' in snakes_cafe.search(item)

def test_multi_order():
    """add o item to oted"""
    nam = 'tea'
    val = 'tea 2'
    snakes_cafe.new_order.add_item(nam,val)
    assert snakes_cafe.new_order.final_order[nam] == 2

def test_order_total_with_one_0():
    """count the total when 1 element is 0"""
    snakes_cafe.new_order.final_order = {}
    snakes_cafe.new_order.final_order['wings'] = 0
    snakes_cafe.new_order.final_order['tea'] = 3
    assert snakes_cafe.new_order.display_order() == 4.77

def test_bill_when_one_order_is_more_then_quantity():
    """check when items is out of stock"""
    snakes_cafe.new_order.final_order['cake'] = 40
    snakes_cafe.new_order.final_order['tea'] = 5
    assert snakes_cafe.new_order._bill() == 154.05

def test_find_item_in_menu():
    """find if menu exist"""
    item = 'tea'
    assert snakes_cafe.find(item) == 'drinks'

def test_find_item_not_in_menu():
    """when menu not exist"""
    item = 'notinmenu'
    assert snakes_cafe.find(item) == 0

def test_stock_if_not_enougth():
    """check if enougth items in stock"""
    name = 'tea'
    namber = 'tea 100'
    assert snakes_cafe.new_order._stock(name,namber) == False

def test_stock_if_enougth():
    """check if enougth items in stock"""
    name = 'tea'
    namber = 'tea 1'
    assert snakes_cafe.new_order._stock(name,namber) == True

def test_create_broken_path():
    """check if path is broken"""
    assert snakes_cafe.create('wdwdw.csv') == snakes_cafe.default_items
