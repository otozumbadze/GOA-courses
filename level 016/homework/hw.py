# 2) ლოგიკური ოპერატორებისა და შედარების ოპერატორებზე შეადგინეთ 10 მაგალითი,5 მაგალითმა უნდა დააბრუნოს False
# და 5 მაგალითმა უნდა დაააბრუნოს True
 

# 5 ცალი მაგალითი False - ზე. 

print(10 > 20 and 3 > 2) # False
print(80 > 100 or 25 > 40) # False
print(120 < 50 and 60 > 20) # False
print(70 < 30 or 65 < 35) # False
print(150 < 200 and 140 < 130) # False


# 5 ცალი მაგალითი True - ზე.

print(15 > 10 and 20 > 15) # True
print(55 < 60 or 35 > 40) # True
print(65 > 45 and 25 < 30) # True
print(70 < 85 or 20 > 10) # True
print(95 > 80 and 75 > 50) # True


# 3) კომენტარის სახით დაწერეთ თუ რა არის sequancing,iteration,selection აღწერე თითეული მათგანი თქვენი სიტყვებით


# Sequencing - არის რომ კოდი ზემოდან-ქვემოთ სრულდება ბოლომდე ნაბიჯ-ნაბიჯ.

# Iteration - არის კოდის მრავალჯერ ერთი და იგივეს გამეორება.

# Selection - არის გადაწყვეტილება თუ როდის რა უნდა გააკეთოს პროგრმამ სიტვაციების მიხედვით.


# 4) მოიყვანე sequencing ის მაგალითი,და კომენტარით მიუწერე რატომ არის შენს მიერ მოყვანილი მაგალითი sequence


print("Niako") # First Niako
print("Oto") # Second Oto
print("Nika") #Third Nika
print("Davit") # Fourth Davit

# ეს იმიტომ არის Sequencing რომ ამ კოდიდან ჯერ პირველი ნიაკო გამოვა და მერე სხვებიც ნაბიჯ-ნაბიჯ თანმიმდევრულად.


# 5) კომენტარის სახით ახსენით თუ რა არის for loop და რაში გვეხმარება ის


# For loop - მეშვეობით შეგვიძლია უფრო მარტივად დავწეროთ კოდი როგორიც არის მაგ. გვინდა რომ 100 რიცხვი გამოვიტანოთ და პრინტების წერას მაგის გარდა ჩვენ ვიყენებ For loop - ს რადგან რომ გადავცემთ For loop - ს 1,100 რომ გამოიტანოს რიცხვები სანამ არ შეასრულებს მოთხოვნას.


# 6) კომენტარის სახით ახსენით თუ რა გადაეცემა range() ფუნქციას და როგორ მუშაობს for loop


# For loop - მუშაობს ასე ჩვენ range() ფუნქციაში გადავცემთ თუ საიდან დაიწყოს ათვლა და სად დაამთავროს, და კიდევ თუ რამდენჯერ გამოტოვოს რიცხვები მაგ. range(0,100,2) პირველი 0 ეგ არის თუ საიდან უნდა დაიწყოს ათვლა, მეორე 100 არის თუ სად უნდა დამთავროს ათვლა, მესამე კი არის თუ რამდენით გადაახტეს რიცხვებს ანუ რამდენი ნაბიჯით.

# for i in range(0,50,2):
    # print(i)


# 7) შენი დავალებაა ტერმინალში გამოიყანო საყვარელი ავტომობილის სახელი ტერმინალში გამოიყენე for loop


car1 = "BMW M5 COMPETITIVE"

for i in range(1):
    print(car1)


# 8) შენი დავალებაა ტერმინალში გამოიტანო შენი გვარი 100 ჯერ


for i in range(0,100):
    print("Zumbadze")


# 9) შენი დავალებაა ტერმინალში გამოიტანო საყვარელი ფერი 46 ჯერ


for i in range(0,46):
    print("red")


# 10) შენი დავალებაა ტერმინალში გამოიტანო შენი სახელის პირველი ასო 32 ჯერ


for i in range(0,32):
    print("O")


# # გამეორება / Revise -->

# 11) მომხმარებელს შემოატანინე 3 სტრინგ ტიპის და ერთი ინტეჯერ ტიპის მნიშვნელობები და შენი დავალებაა მოახდინო ამ ოთხი მნიშვნელობის კონკატინაცია(გამოიყენე შესაბამისი ფუნქცია რომ მოახდინოთ მონაცემთა ტიპიების გარდაქმნა ერთ მონაცემთა ტიპში რომ შეძლოთ კონკატინაცია)


user_number1 = input("Enter your first number: ")
user_number2 = input("Enter your second number: ")
user_number3 = input("Enter your third number: ")
user_number4 = int(input("Enter your fourth number: "))

print(user_number1 + user_number2 + user_number3 + str(user_number4))


# 12) შექმენი 4 ცვლადი,თითოეულში შეინახე განსხვავებული მონაცემთა ტიპები,შენი დავალებაა გაიგო ამ ცვლადებში 
# შენახული მნიშვნელობის მონაცემთა ტიპი(გამოიყენე შესაბამისი ფუნქცია)


variable1 = "Niako"
variable2 = 100
variable3 = 10.5
variable4 = True 

print(type(variable1))
print(type(variable2))
print(type(variable3))
print(type(variable4))


# 13) მომხმარებელს შემოატანინე 4 რიცხვი და ტერმინალში დააბრუნე ამ 4 რიცხვის ჯამი


user_num1 = int(input("Enter your first number: "))
user_num2 = int(input("Enter your second number: "))
user_num3 = int(input("Enter your third number: "))
user_num4 = int(input("Enter your fourth number: "))

print(user_num1 + user_num2 + user_num3 + user_num4)






