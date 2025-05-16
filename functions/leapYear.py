# def is_leap(year):
#     leap = False
#     if(year%4==0 and year%400==0):
#         leap=True 
#     elif(year%4==0 and year%100==0):
#         leap=False
     
 
    
#     return leap

# year = int(input())
# print(is_leap(year))

##failing at 1992
# def is_leap(year):
#     leap = False
#     if(year%4==0):
#         if(year%100==0):
#             if(year%400==0):
#                  leap=True    
     
 
    
#     return leap

# year = int(input())
# print(is_leap(year))

def is_leap(year):
    leap = False
     
    if(year>1999):
        if(year%4==0):
            if(year%100==0):
                if(year%400==0):
                    leap=True
    else:
        if(year%4==0 and year%100!=0):
            leap=True                
     
 
    
    return leap

year = int(input())
print(is_leap(year))