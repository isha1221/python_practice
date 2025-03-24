import numpy as np

def calculate(list):
    if len(list)<9 :
        raise ValueError("List must contain nine numbers.") #raised an exception here
    
    num_array = np.array(list) #convert list to numpy array
    num_array=num_array.reshape(3,3) #redefining array size
   
    calculations={'mean':[num_array.mean(axis=0).tolist(),num_array.mean(axis=1).tolist(),num_array.mean().tolist()],
    'variance':[num_array.var(axis=0).tolist(),num_array.var(axis=1).tolist(),num_array.var().tolist()],
    'standard deviation':[num_array.std(axis=0).tolist(),num_array.std(axis=1).tolist(),num_array.std().tolist()],
    'max':[num_array.max(axis=0).tolist(),num_array.max(axis=1).tolist(),num_array.max().tolist()],
    'min':[num_array.min(axis=0).tolist(),num_array.min(axis=1).tolist(),num_array.min().tolist()],
    'sum':[num_array.sum(axis=0).tolist(),num_array.sum(axis=1).tolist(),num_array.sum().tolist()]
    }
    #tolist--> converts numpy array to list 
    #calculations is a dictionary
    return calculations
# num_list = [2,6,2,8,4,0,1,5,7] 
user_input=input('Enter nine digits: ').split() #takes the input string
num_list = [float(x) for x in user_input] #converts string to integer 
print(calculate(num_list))