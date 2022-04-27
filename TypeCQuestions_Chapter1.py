#Q1
# input = float(input(">>> "))

# if (input < 0):
#     print(f"The number {input} is Negative.")
# elif (input == 0):
#     print(f"The number {input} is Zero.")
# elif (input > 0):
#     print(f"The number {input} is Positive.")


#Q2
# input = float(input(">>> "))

# if (input % 2 == 0):
#     print("True")
# else:
#     print("False")


#Q3
# input = int(input(">>> "))

# if (input % 4 == 0 and input%100 != 0):
#     print(f"The number of seconds in year {input} is 31622400.")
# elif (input % 400 == 0):
#     print(f"The number of seconds in year {input} is 31622400.")
# else:
#     print(f"The number of seconds in year {input} is 31536000.")


#Q4
# input_1 = int(input(">>> "))
# input_2 = int(input(">>> "))

# if (input_1 % input_2 == 0):
#     print(f"{input_1} is divisible by {input_2}.")
# else:
#     print(f"{input_1} is not divisible by {input_2}.")


#Q5


#Q6
# def compute(feet):
#     return feet * 12

# def get_input():
#     feet = float(input("Enter Length (feet): "))
#     return feet

# def give_output(inches):
#     print(f"Given feet in inches are: {inches}")

# give_output(compute(get_input()))


#Q7
# N = int(input(">>> "))
# total = 0

# if (N > 0):
#     for i in range(N, 2 * N + 1):
#         total += i
#     else:
#         print(total)
# elif (N < 0):
#     for i in range(2 * N, N + 1):
#         total += i
#     else:
#         print(total)


#Q8
# months_of_a_year = ["January", "February", "March", "April", "May", "June",
# "July", "August", "September", "October", "November", "December"]

# input = input("Enter date (MMDDYYYY): ")
# print(f"{months_of_a_year[int(input[0 : 1 + 1]) - 1]} {input[2 : 3 + 1]}, {input[4 : ]}")


#Q9
# print("Miles \tKilometers")

# for i in range(1, 10):
#     if (i != 10):
#         print(f"{i} \t{round(i * 1.609344, 3)}")


#Q10
# print("Pounds \tKilograms")

# for i in range(1, 10):
#     if (i != 10):
#         print(f"{i} \t{round(i * 0.45359237, 3)}")


#Q11
# input_1 = input("Time_1 = ")
# input_2 = input ("Time_2  = " )
# print (f"{int(t2[: 2]) - int(t1[: 2])} hours {int(t2[2: ]) - int(t1[2: ])} minutes")