def calculate_bmi(height,weight):
    print("Height="+str(height))
    print("Weight="+str(weight))
    bmi=(weight/(height*height))
    print("\nBMI="+str(bmi))
    status=""
    if bmi<18.5:
        status="Under Weight"
        return 1
    elif 18.5<=bmi<=25.0:
        status="Normal Weight"
        return 0
    else:
        status="Over Weight"
        return -1
      




calculate_bmi (weight=57,height=1.73)
