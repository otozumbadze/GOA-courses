# >, <, >=, <=, ==, !=.


print(5 > 4)
print(6 > 7)
print(10 < 12)
print(20 < 10)
print(50 >= 40)
print(60 >= 60)
print(10 <= 20)
print(30 <= 30)
print(40 == 40)
print(80 == 90)
print(40 != 30)
print(70 != 70)


# logical operator - ში შედის and და or, and - არის (და) და თუ ჩვენ დავწერთ (True and False) მაშინ ეს გამოგვიტანს False რადგან and - ის დროს სადაც იქნება (True and False) მანდ სულ False გამოვა მაგრამ თუ იყო ასე (True and True) მაშინ ეს True გამოგვიტანს.

# Logical operator - ში გვაქვს კიდევ or როგორც (ან) და თუ ჩვენ დავწერთ (True or False) მაშინ ეს გამოგვიტანს ჭეშმარიტს ანუ True - ს, იმიტომ რომ მანდ გვეუბნებიან ან ეს ან ის ამიტომ მანდა სულ ჭეშმარიტი გამოვა.


print(True and False)
print(True and True)
print(False and False)
print(True or False)
print(True or True)
print(False or False)


user_number = int(input("enter your number: "))

print(user_number > 6)


user_name = input("enter your name: ")

print(user_name == "Oto")


user_age = int(input("enter your age: "))

print(user_age >= 18)