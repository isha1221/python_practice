import random
num = random.randint(1,100)
count=0
print('guess a number: ')
guessed_num = int(input())

flg=1

while(count<10 and flg==1):
    if(guessed_num>num):
        print('guess a smaller number:')
        guessed_num = int(input())
        if(count==9):
            print('do you want to continue enter 0 or 1: ')
            flg_inpt = int(input())
            if(flg_inpt==0):
             break 
            else:
                count=0
                flg=1
                num = random.randint(1,100)

    elif (guessed_num<num):
        print('guess a geater number:')
        guessed_num = int(input())
        if(count==9):
            print('do you want to continue enter 0 or 1: ')
            flg_inpt = int(input())
            if(flg_inpt==0):
             break 
            else:
                count=0
                flg=1
                num = random.randint(1,100)
            
    elif(guessed_num==num):
        print('Bravoo correct guess') 
        print('your score is:',count)
        print('do you want to continue enter 0 or 1: ')
        flg_inpt = int(input())
        if(flg_inpt==0):
          break 
        else:
            count=0
            flg=1
            num = random.randint(1,100)
    
    count+=1  
            

          

    