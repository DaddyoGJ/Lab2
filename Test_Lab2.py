import Lab2.lab2 as lab2

def test_find_min_max():
    inputno = [70, 50, 80, 90, 100]
    result = lab2.sort_temperature(inputno)
    min = result[0]
    max = result [-1]

    assert (min == 50)
    assert (max == 100)

def test_calc_average():
    inputno = [70, 50, 80, 90, 100]
    result = lab2.calc_average(inputno)

    assert (result == 78)

def test_calc_median_temperature():
    inputno = [70, 50, 80, 110, 90, 100]
    result = lab2.calc_median_temperature(inputno)
    
    assert (result == 85)