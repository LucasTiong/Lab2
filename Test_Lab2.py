import LAB2

def test_calc_min_max():
    # test number list: 19, 5, 10, 1, 3
    minmax = LAB2.calc_min_max_temperature()
    assert (minmax == [1, 19])

def test_calc_average():
    # test number list: 19, 5, 10, 1, 3
    avg = LAB2.calc_average_temperature()
    assert (avg == 7.6)

def test_calc_median_temperature():
    # test number list: 19, 5, 10, 1, 3
    median = LAB2.calc_median_temperature()
    assert (median == 5.0)