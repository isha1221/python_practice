# # 268. Missing Number
# # Given an array nums containing n distinct numbers in the range [0, n], 
# # return the only number in the range that is missing from the array.


# # given:
# # -1. array(list)= nums which will have n distinct numbers,
# # -2. range will (0,n) therfore n=len(nums)
# # -3. count of missing number==1
# # to find:    
# #    the missing number from the list 
    
    
# # defining function
#     # a.initialize
#     # b.call
    
    
# # method 1    
# def missing_number(nums):  # initialize
#     nums=sorted(nums) #for sorting using sort doesnot work because it modifies the self while sorted creates a new sorted element
#     n=len(nums)
#     for i in range(n):
#         if i not in nums:
#             print(i)
#             return i
                
# nums=[1,2,3,4,5,6,7,9,0] 
# missing_number(nums) # call

# # method 2
# def missing_num2(nums):
#     n=len(nums)
#     ans= sum(range(n) )- sum(nums) # sum(range(n)) here displayes sum of all numbers in the range n starting from 0 i.e 0,n
#     print(ans)
# nums=[1,2,3,4,5,6,7,9,0] 
# missing_number(nums)     
    

# method 3
def missing_num3(nums):
    n=len(nums)
    nums=sorted(nums)
    for index, value in enumerate(nums): #herer you are using enumerate so that we can iterrate simulteneusly through index and values of nums
         if(index!=value):
             return value-1
         if(value==n):
             return value+1

nums=[1, 2, 0, 4, 5, 6, 7, 8, 9]
 
print(missing_num3(nums))                         
    