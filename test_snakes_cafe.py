import snakes_cafe

snakes_cafe.menu_items = snakes_cafe.default_items


def test_remove():
    """add 1 to the current value"""
    snakes_cafe.final_order['tea'] = 5
    snakes_cafe.remove('tea')
    assert snakes_cafe.final_order['tea'] == 4


def test_order_total():
    """count the total"""
    snakes_cafe.final_order['wings'] = 1
    snakes_cafe.final_order['tea'] = 3
    assert snakes_cafe.order_total() == 19.02


def test_bill():
    """count the bill for"""
    snakes_cafe.final_order['wings'] = 20
    snakes_cafe.final_order['tea'] = 20
    assert snakes_cafe.bill() == 289


def test_search():
    """search for spesick menu item and will print all item inside that
    menu item"""
    key = 'entrees'
    assert snakes_cafe.search(key) == sorted(['salmon', 'steak', 'country fried '
                                       'chicken', 'chopped grilled angus',
                                       'crispy fish tacos', 'meat'                                        'tornado'])


def test_remove_0():
    """check if function will remove one item from order."""
    snakes_cafe.final_order['tea'] = 1
    snakes_cafe.remove('tea')
    assert 'tea' not in snakes_cafe.final_order.keys()


def test_add_to_order_one_elemant():
    """Test will check current order if we add one element two identical items."""
    snakes_cafe.final_order = {}
    snakes_cafe.add_to_order('cake')
    snakes_cafe.add_to_order('cake')
    assert len(snakes_cafe.final_order) == 1


def test_add_to_order():
    """check if the current backet will change if we add one item."""
    snakes_cafe.final_order['wings'] = 10
    snakes_cafe.add_to_order('wings')
    assert snakes_cafe.final_order['wings'] == 11


def test_search_type_output():
    """check if output is list"""
    item = 'entrees'
    print(type(snakes_cafe.search(item)))
    assert 'salmon' in snakes_cafe.search(item)

# def test_search_not_in_menu():
#     """check if item not in menu"""
#     item = 'something'
#     assert snakes_cafe.search(item) == []

# def test_multi_order():
#     """add o item to oted"""
#     snakes_cafe.add_to_order(num)
