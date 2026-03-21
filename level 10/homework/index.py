# boolean შეიცავს True და False და ამით ვამოწმებთ იმას თუ ჭეშმარიტია თუ არა რაიმე.


print(5 > 6) #False
print(5 < 6) #True
print(2 >= 2) #True
print(2 <= 9) #True
print(2 != 2) #False
print(2 == 2) #True 


# binary code არის კომპიუტერების ფუნდამენტური ენა რომელიც მონაცემებსა და ინსტრუქციებს წარმოადგენს, მხოლოდ ორი ციფრის გამპოყენებით 0 და 1 (ბიტები). 1 აღნიშნავს ჩართულს ხოლო 0 აღნიშნავს გამორთულს.


# bool() ფუნქცია გამპოიყენება მნიშვნელობების ლოგიკურ მნიშვნელობად True ან False გადასაყვანად.


print(bool(5)) #True
print(bool(0)) #False

print(bool("oto")) #True
print(bool("")) #False

print(bool([1,2])) #True
print(bool([])) #False



a = 5
b = 5

print(a == b )



d = int(input("შეიყვანე პირველი რიცხვი: "))
s = int(input("შეიყვანე მეორე რიცხვი: "))

print(d > s)


person_input = input("enter your word here: ")
word = "python"

print(person_input == word)



user = int(input("enter your number: "))
number = 100

print(user > number)


user_password = input("enter your password: ")
password = "Python123"

print(user_password == password)


user_person1 = int(input("enter your number here: "))
user_person2 = int(input("enter your number here: "))

print(user_person1 > user_person2)
print(user_person1 < user_person2)
print(user_person1 == user_person2)



user1 = input("enter your first word here: ")
user2 = input("enter your second word here: ")
user3 = input("enter your third word here: ")
user4 = input("enter your fourth word here: ")
user5 = input("enter your fifth word here: ")


print(user1 + user2 + user3 + user4 + user5)



num1 = int(input("enter your num: ")) #1
num2 = int(input("enter your num: ")) #2
num3 = int(input("enter your num: ")) #3
num4 = int(input("enter your num: ")) #4


print((num1 + num2 + num3 + num4) / 4) #5



element = "hello world"
element1 = 10
element2 = 10.5
element3 = True


print(type(element))
print(type(element1))
print(type(element2))
print(type(element3))


element_str = "hello"
element_str1 = "hello"

print(element_str == element_str1)


variable_str1 = "1"
variable_str2 = "2"
variable_str3 = "3"
variable_str4 = "4"

variable_int1 = int(variable_str1)
variable_int2 = int(variable_str2)
variable_int3 = int(variable_str3)
variable_int4 = int(variable_str4)


print(variable_int1 + variable_int2 + variable_int3 + variable_int4)



hitler1 = 1
hitler2 = 2
hitler3 = 3

stalini1 = str(hitler1)
stalini2 = str(hitler2)
stalini3 = str(hitler3)

print(stalini1 + stalini2 + stalini3)
