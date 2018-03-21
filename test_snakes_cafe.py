import snakes_cafe

def test_remove ():

    # ***
    # test should lover current value by 1 ppont
    # ***

    snakes_cafe.final_order['tea'] = 5
    snakes_cafe.remove('tea')
    assert snakes_cafe.final_order['tea'] == 4

# def test_remove_fail():
#     snakes_cafe.final_order['tea'] = 5
#     snakes_cafe.remove('tea')
#     assert snakes_cafe.final_order['tea'] != 4

def test_add_to_order():
    snakes_cafe.final_order['wings'] = 10
    snakes_cafe.add_to_order('wings')
    assert snakes_cafe.final_order['wings'] == 11
    
def test_order_total():
    snakes_cafe.final_order['wings'] = 1
    snakes_cafe.final_order['tea'] = 3
    assert snakes_cafe.order_total() == 19.02