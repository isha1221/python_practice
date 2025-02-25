# NOTE:Practice Questions



### **1. What is `[]`?**  
# `[]` represents an **empty list** in .



### **2. How would you assign the value `'hello'` as the third value in a 
# list stored in a variable named `spam`? (Assume `spam` contains `[2, 4, 6, 8, 10]`.)**  

spam[2] = 'hello'

# Explanation:  
# - Lists are **zero-indexed**, so the third value (index `2`) is `6`.  
# - This statement replaces `6` with `'hello'`.  
# - After execution, `spam` becomes `[2, 4, 'hello', 8, 10]`.



### **For the following three questions, let’s say `spam` contains the list `['a', 'b', 'c', 'd']`.**  

#### **3. What does `spam[int(int('3' * 2) // 11)]` evaluate to?**  
# Step-by-step breakdown:

# 'int('3' * 2) // 11'  
int('33') // 11  
33 // 11  
3

# So, `spam[3] = 'd'`.  
## **Answer:** `'d'`



#### **4. What does `spam[-1]` evaluate to?**  
# - Negative indexing starts counting from the right (`-1` refers to the last element).  
## **Answer:** `'d'`



#### **5. What does `spam[:2]` evaluate to?**  
# - `[:2]` means "slice from the beginning up to (but not including) index `2`".  
# - `spam[:2]` → `['a', 'b']`  
## **Answer:** `['a', 'b']`



### **For the following three questions, let’s say `bacon` contains the list `[3.14, 'cat', 11, 'cat', True]`.**  

#### **6. What does `bacon.index('cat')` evaluate to?**  
# - `index('cat')` returns the **first occurrence** of `'cat'`.  
## **Answer:** `1`



#### **7. What does `bacon.append(99)` make the list value in `bacon` look like?**  
# - `append(99)` **adds `99` to the end** of the list.  
## **Updated list:** `[3.14, 'cat', 11, 'cat', True, 99]`



#### **8. What does `bacon.remove('cat')` make the list value in `bacon` look like?**  
# - `remove('cat')` **removes only the first occurrence** of `'cat'`.  
## **Updated list:** `[3.14, 11, 'cat', True]`



### **9. What are the operators for list concatenation and list replication?**  
## **Concatenation:** `+` (joins two lists)  
## **Replication:** `*` (repeats elements)  



[1, 2] + [3, 4]  # → [1, 2, 3, 4]
[1, 2] * 3       # → [1, 2, 1, 2, 1, 2]




### **10. What is the difference between the `append()` and `insert()` list methods?**  
## `append(value)` → **Adds value to the end** of the list.  
## `insert(index, value)` → **Inserts value at a specific index** in the list.  



lst = [1, 2, 3]
lst.append(4)    # → [1, 2, 3, 4]
lst.insert(1, 99)  # → [1, 99, 2, 3, 4]




### **11. What are two ways to remove values from a list?**  
# 1. **Using `remove(value)`** → Removes the **first occurrence** of `value`.
   
lst = [1, 2, 3, 2]
lst.remove(2)  # → [1, 3, 2]
   
# 2. **Using `del` statement** → Removes by **index**.
   
lst = [1, 2, 3]
del lst[1]  # → [1, 3]
   



### **12. Name a few ways that list values are similar to string values.**  
## **Both are sequences**  
## **Both support indexing and slicing**  
## **Both support `len()` function**  
## **Both support iteration using `for` loops**  



s = "hello"
l = ['h', 'e', 'l', 'l', 'o']

print(s[1])  # 'e'
print(l[1])  # 'e'

print(s[:3])  # 'hel'
print(l[:3])  # ['h', 'e', 'l']




### **13. What is the difference between lists and tuples?**  
## **Lists are mutable** (can be changed).  
## **Tuples are immutable** (cannot be changed).  



lst = [1, 2, 3]
lst[0] = 99  # Allowed

tup = (1, 2, 3)
tup[0] = 99  # ❌ Error! Tuples cannot be modified




### **14. How do you type the tuple value that has just the integer value `42` in it?**  
## **Answer:** `(42,)` (with a comma)  



t = (42,)  # Correct
t = (42)   # ❌ Wrong (this is just an integer)




### **15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?**  
## **Convert list → tuple:** `tuple(my_list)`  
## **Convert tuple → list:** `list(my_tuple)`



lst = [1, 2, 3]
tup = tuple(lst)  # → (1, 2, 3)

tup = (4, 5, 6)
lst = list(tup)  # → [4, 5, 6]




### **16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?**  
## **Answer:** A **reference** (memory address) to the list, not the list itself.



a = [1, 2, 3]
b = a  # Both a and b point to the same list
b.append(4)  # Modifies the same list
print(a)  # → [1, 2, 3, 4]

# Since `b` is just a reference to `a`, modifying `b` also affects `a`.



### **17. What is the difference between `copy.copy()` and `copy.deepcopy()`?**  
## **`copy.copy()` (shallow copy)** → Creates a new object but keeps references to nested objects.  
## **`copy.deepcopy()` (deep copy)** → Creates a completely independent copy, including nested objects.



import copy

a = [[1, 2], [3, 4]]
shallow = copy.copy(a)
deep = copy.deepcopy(a)

shallow[0][0] = 99  # Changes original list!
print(a)  # → [[99, 2], [3, 4]]

deep[0][0] = 42  # Does NOT change original list
print(a)  # → [[99, 2], [3, 4]]

## **Use `deepcopy()` if modifying nested lists is a concern.**



