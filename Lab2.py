def display_main_menu():
    print("display_main_menu")
    print("\nEnter some numbers separated by commas(e.g.5,67,32)")
# All the inputs are string 
def get_user_input():
    print("\nget_user_input")
    print("\n Enter the number : ")
    x=input()
    x_split=x.split(',') # split the number by comma 
    input_list=[float(item) for item in x_split] # Convert the input string into float
    return input_list

def calc_average(input_list):
    print("calc_average")
    total=sum(input_list)
    count=len(input_list)
    average=total/count
    return average


def find_min_max(input_list):
    print("find_min_max")
    minimum=min(input_list)
    maximum=max(input_list)
    return [minimum,maximum]

def sort_temperature(input_list):
    print("sort_temperature")
    return sorted(input_list)

def calc_median_temperature(input_list):
    print("calc_median_temperature")
    sorted_list=sorted(input_list)
    n=len(input_list)
    if n%2==0:
        num1=sorted_list[n//2-1]
        num2=sorted_list[n//2]
        median=(num1+num2)/2
        
        
    else:
         median=sorted_list[n//2]
         return round (median)

def main():
    print("ET0735(DeVops for AIoT)-Lab2-Introduction to Python")
    display_main_menu()
    input_list=calc_average()
    print("\nThe average temperature is "+str(calc_average(input_list)))
    print("\nThe min and max are"+str(find_min_max(input_list)))
    print("\nSorted temperature is "+str(sort_temperature(input_list)))
    print("The median temperature is "+str(calc_median_temperature(input_list)))

#Function calls for testing purpose
if __name__=="__main__":
    main()