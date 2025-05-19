def list_comp(x,y,z,n):
   
    
    # ans=[]    
    # for i in range(x+1):
    #     # print("i",i)
    #     for j in range(y+1):
    #         # print("j",j)
    #         for k in range(z+1):
    #             # print("K",k)
    #             sum=(i+j+k)
    #             # print(sum)
    #             if sum!=n:
    #                 ans.append([i, j, k])
    # print(ans)


    ##using list compression:
    ans=[[i, j, k]
    for i in range(x+1)
    for j in range(y+1)
    for k in range(z+1) 
    if (i+j+k)!=n]
    
    print(ans)

x = int(input())
y = int(input())
z = int(input())
n = int(input())

list_comp(x,y,z,n)



#NOTE:ans = [expression(the required output) for item in iterable(all the required for loops) if condition == True(all the if loops)]  
           
            
            
            