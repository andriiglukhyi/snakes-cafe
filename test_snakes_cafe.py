import snakes_cafe

def test_remove ():

    # ***
    # test should lover current value by 1 ppont
    # ***

    snakes_cafe.final_order['tea'] = 5
    snakes_cafe.remove('tea')
    assert snakes_cafe.final_order['tea'] == 4

def test_order_total():
    snakes_cafe.final_order['wings'] = 1
    snakes_cafe.final_order['tea'] = 3
    assert snakes_cafe.order_total() == 19.02

def test_bill():
    snakes_cafe.final_order['wings'] = 20
    snakes_cafe.final_order['tea'] = 20
    assert snakes_cafe.bill() == 289

def test_search():
    key = 'entrees'
    assert snakes_cafe.search(key) == ['salmon', 'steak', 'country fried chicken', 'chopped grilled angus', 'crispy fish tacos', 'meat tornado'].sort()

def test_remove_0():
    snakes_cafe.final_order['tea'] = 1
    snakes_cafe.remove('tea')
    # import pdb; pdb.set_trace()
    assert ['tea'] not in snakes_cafe.final_order.keys()

def test_add_to_order_one_elemant():
    snakes_cafe.final_order = {}
    snakes_cafe.add_to_order('cake')
    snakes_cafe.add_to_order('cake')
    assert len(snakes_cafe.final_order)==1


def test_add_to_order():
    snakes_cafe.final_order['wings'] = 10
    snakes_cafe.add_to_order('wings')
    assert snakes_cafe.final_order['wings'] == 11
    
