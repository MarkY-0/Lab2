import Lab2 as lab2

def test_find_min_max():

    test_list = [5, 67, 32]
    expected_result = [5, 67]
    assert lab2.calc_min_max_temperature(test_list) == expected_result

def test_calc_average():
    test_list = [4.0, 4.0, 4.0, 5.0, 6.0]
    expected_result = 4.6
    assert lab2.calc_average_temperature(test_list) == expected_result

def test_calc_median_temperature():
    test_list = [2, 4, 8]
    expected_result = 4
    assert lab2.calc_median_temperature(test_list) == expected_result