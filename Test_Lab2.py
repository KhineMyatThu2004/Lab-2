
import Lab2 as lab_two
def test_find_min_max():
    result=[]
    result=lab_two.find_min_max([0,1,99,3])
    test_arr=[0,99]
    assert(result==test_arr)
    
 
def test_calc_average():
    result=[]
    result=lab_two.calc_average([5,5,5,5,5,5])
    test_arr=5
    assert result==test_arr

def test_clac_median_temperature():
    result=[]
    result=lab_two.calc_median_temperature([1,2,3,4,5])
    test_arr=3
    assert result==test_arr
