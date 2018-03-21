import snakes_cafe


def test_remove():
    """
    Test will test remove function. It the add 1 to the current value
    """
    snakes_cafe.final_order['tea'] = 5
    snakes_cafe.remove('tea')
    assert snakes_cafe.final_order['tea'] == 4


def test_order_total():
    """
    Test will count the total dependence on the current order backet('final
    order')
    """
    snakes_cafe.final_order['wings'] = 1
    snakes_cafe.final_order['tea'] = 3
    assert snakes_cafe.order_total() == 19.02


def test_bill():
    """
    Test will count the bill dependence on the current order backet('final
    order')
    """
    snakes_cafe.final_order['wings'] = 20
    snakes_cafe.final_order['tea'] = 20
    assert snakes_cafe.bill() == 289


def test_search():
    """
    Test will search for spesick menu item and will print all item inside that
    menu item
    """
    key = 'entrees'
    assert snakes_cafe.search(key) == ['salmon', 'steak', 'country fried '
                                       'chicken', 'chopped grilled angus',
                                       'crispy fish tacos', 'meat'
                                       'tornado'].sort()


def test_remove_0():
    """
    Test will check if function will remove one item from current order
    """
    snakes_cafe.final_order['tea'] = 1
    snakes_cafe.remove('tea')
    assert ['tea'] not in snakes_cafe.final_order.keys()


def test_add_to_order_one_elemant():
    """
    Test will check current order if we add one element two identical items
    """
    snakes_cafe.final_order = {}
    snakes_cafe.add_to_order('cake')
    snakes_cafe.add_to_order('cake')
    assert len(snakes_cafe.final_order) == 1


def test_add_to_order():
    """
    Test will check if the current backet will change if we add one item to our
    order
    """
    snakes_cafe.final_order['wings'] = 10
    snakes_cafe.add_to_order('wings')
    assert snakes_cafe.final_order['wings'] == 11
