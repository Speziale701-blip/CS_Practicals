#Q1
# given_input = input("Enter Phone Number (XXX-XXX-XXXX): ")

# if (len(given_input) == 12):
#     if (given_input[3] == "-" and given_input[7] == "-"):
#         if ((given_input[0: 2 + 1] + given_input[4: 6 + 1] + given_input[8: 11 + 1]).isdigit() == True):
#             print("Phone Number is valid.")
#         else:
#             print("Phone Number is not valid.")
#     else:
#         print("Phone Number is not valid.")
# else:
#     print("Phone Number is not valid.")


#Q2
# given_input = input(">>> ")
# word_count = 0
# character_count = 0
# alnum_character_count = 0

# for i in given_input:
#     character_count += 1
    
#     if (i == " "):
#         word_count += 1

#     if (i.isalnum() == True):
#         alnum_character_count += 1
# else:
#     print(f"Number of Words: {word_count}")
#     print(f"Number of Characters: {character_count}")
#     print(f"Alpha Numeric Characters (%): {(alnum_character_count/character_count) * 100}")


#Q3
# L = eval(input("Enter List_1: "))
# M = eval(input("Enter List_2: "))
# N = []

# if len(L) != len(M):
#     if len(L) > len(M):
#         L.pop()
#     elif len(L) < len(M):
#         M.pop()
#     else:
#         pass

# for i in range(0, len(L)):
#     N.append(L[i] + M[i])
# else:
#     print(N)


#Q4
# given_input = eval(input("Enter a List: "))
# given_input = given_input[-1: len(given_input)] + given_input[0: -1]
# print(given_input)


#Q5
# given_input = input(">>> ").split()
# longest_word = given_input[0]

# for i in given_input:
#     if len(i) > len(longest_word):
#         longest_word = i
#     else:
#         pass
# else:
#     print(f"Longest Word is: {longest_word}")


#Q6
# L = []

# for i in range(0, 100 + 1):
#     if (i % 3 == 0 or i % 5 == 0):
#         L.append(i)
#     else:
#         pass
# else:
#     print(L)


#Q7
# first = "Jimmy"
# second = "Johny"

# first, second = second, first
# print(first, second)


#Q8
# L = []

# for i in range(0, 9):
#     if len(L) < 2:
#         L.append(i)
#     else:
#         i = L[(i - 1)] + L[(i - 2)]
#         L.append(i)
# else:
#     print(f"First 9 terms of Fibonacci series are: {tuple(L)}") 


#Q9
# D = {"January" : 31, "February" : 28, "March" : 31, "April" : 30, "May" : 31,
#      "June" : 30, "July" : 31, "August" : 31, "September" : 30, "October" : 31,
#      "November" : 30, "December" : 31}
# given_input = input("Enter a Month Name: ")

# if given_input in D:
#     print(f"The number of days in {given_input} are: {D[given_input]}")
# else:
#     print(f"There is no month by the name of {given_input}.")

# print(sorted(D.keys()))

# for i in D:
#     if (D[i] == 31):
#         print(i)

#TO-DO --> Q9.(d)