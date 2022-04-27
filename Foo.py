# 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

# # #Declare Stuff
# months = {"January" : 0, "February" : 1, "March" : 2, "April" : 3, "May" : 4,
#           "June" : 5, "July" : 6, "August" : 7, "September" : 8, "October" : 9,
#           "November" : 10, "December" : 11}
# days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# #Adjust the Days in list if the Year is a Leap Year
# print("Enter a Year of your Choice")
# given_year = int(input(">>> "))

# if given_year % 4 == 0:
#     if given_year % 100 == 0:
#         if given_year % 400 == 0:
#             days_in_months[1] += 1
#         else:
#             pass
#     else:
#         days_in_months[1] += 1
# else:
#     pass

# #Logic
# print("Enter a Month of your Choice")
# given_month = input(">>> ")
# given_month = given_month.title()

# if given_month in months:
#     print("Enter a Day of your Choice")
#     given_day = int(input(">>> "))
#     if given_day <= days_in_months[months[given_month]]:
#         day_of_the_year = str(sum(days_in_months[0 : months[given_month]], given_day))
#         if "1" in day_of_the_year[-1]:
#             day_of_the_year += "st"
#         elif "2" in day_of_the_year[-1]:
#                 day_of_the_year += "nd"
#         elif "3" in day_of_the_year[-1]:
#                 day_of_the_year += "rd"
#         else:
#                 day_of_the_year += "th"
#         print(f"The Day you seek is {day_of_the_year} day of the Year!")
#     else:
#         print("The Data is Invaild")
# else:
#     print("The Data is Invalid")


# from random import randint
# from statistics import mode

# score_throughout_game = []

# computer_input = 0
# user_input = 1
# user_inputs = []


# def gameLogic(input_1, input_2):
    
#     if input_1 != input_2:
#         print(f"Computer Input : {input_2}")
#         score = input_1 + input_2
#         score_throughout_game.append(score)
#         print(f"Points won this round : {score}")
#     else:
#         print(f"Computer Input : {input_2}")
#         print("You Lose!")
#         print(f"The Total Score is {sum(score_throughout_game)}")
#         # score = input_1 + input_2
#         # print(f"Points won this round : {score}")


# while user_input != computer_input:
#     computer_input = randint(1, 6)
#     print()
#     print("What is your action?")
#     user_input = int(input(">>> "))
#     if user_input in range(1, 7):
#         user_inputs.append(user_input)
#         if len(user_inputs) >= 6:
#                 computer_input = mode(user_inputs)
#                 user_inputs.clear()
#         else:
#             pass
#         gameLogic(user_input, computer_input)
#     else:
#         print("Invalid Input")