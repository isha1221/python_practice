# if __name__ == '__main__':
#     my_dict = {}
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         my_dict[name] = score
 
# minScore=1000 
# secondMin=0
# temp = 0
# for key, value in my_dict.items():
#     if(value < minScore):
#         temp = minScore
#         secondMin = temp
#         minScore = value
# print(secondMin)
# my_dict_sor=dict(sorted(my_dict.items()))
# print(my_dict_sor)  
  
# for key, value in my_dict_sor.items():
#             if value == secondMin:
#                 print(key) 

def find_second_lowest_students():
    my_dict = {}
    for _ in range(int(input("Enter number of students: "))):
        name = input("Enter name: ")
        score = float(input("Enter score: "))
        my_dict[name] = score

    unique_scores = sorted(set(my_dict.values()))
    if len(unique_scores) < 2:
        print("No second lowest score found.")
        return

    second_lowest = unique_scores[1]
    result = [name for name in my_dict if my_dict[name] == second_lowest]

    for name in sorted(result):
        print(name)


if __name__ == '__main__':
    find_second_lowest_students()


# def second_small()
#     my_dict = {}
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         my_dict[name] = score

#     # Step 1: Extract all unique scores
#     unique_scores = sorted(set(my_dict.values()))

#     # Step 2: Find second lowest score
#     second_lowest = unique_scores[1]

#     # Step 3: Find names with second lowest score
#     result = [name for name in my_dict if my_dict[name] == second_lowest]

#     # Step 4: Sort names and print
#     for name in sorted(result):
#         print(name)
