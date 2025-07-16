# calculate bmi of a person and find if overweight or not


# name="isha"
height=157#in centimeters
weight=60 #in kgs

def bmi(height,weight):
    req_weight=weight*10000
    req_height=height**2
    
    bmi_calculation=req_weight/req_height
    print(f"your bmi is: {bmi_calculation}")
    if(bmi_calculation<19):
        return "you are underweight"
        
    elif(18<bmi_calculation<25):
        return "normal"
    else:
        return "obese"
isha=bmi(157,60)
print(isha)