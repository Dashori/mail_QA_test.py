from functions import *
import pytest

##type int
##позитивный тест на умножение чисел
def test_multiplication():
    a = 20
    b = 30
    res = 600
    assert multiplication(a,b) == res

    
##тест через параметризацию на сложение чисел   
@pytest.mark.parametrize("a, b, res", [(5, 5, 10), (10, -10, 0), (0, 1, 1)])

def test_addition(a, b, res):
    assert addition(a, b) == res

##негативный тест на возведение числа в степень
def test_power():
    a = 200
    b = '3'
    res = TypeError
    try:
        a = a ** b
    except TypeError:
        print('Exit TypeError')
        pass


##type tuple
##тест на нахождение индекса элемента в кортеже
def test_find_el():
    a = (0, -1, -2, 3, 5)
    b = 3
    res = 3
    assert find_el(a, b) == res


##тест на параметризацию - сортировка элементов кортежа
@pytest.mark.parametrize("a, res", [((5,4,2,1), [1,2,4,5]), ((-12, 123,0 ), [-12, 0, 123])])
def test_sorted_tuple(a, res):
    assert sorted_tuple(a) == res

##негативный тест на удаление элемента из кортежа
def test_delete_el():
    a = (0, 1, 2, 3, 4)
    res = TypeError
    try:
        delete_el(a, 3)
    except res:
        print('Exit TypeError')
        pass
