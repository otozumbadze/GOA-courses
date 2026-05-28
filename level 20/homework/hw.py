# 2) შექმენით ცვლადი სადაც შეინახავთ ინტეჯერ ტიპის მონაცემს, შემდეგ შეამოწმეთ თუ ეს რიცხვი რომელიც ცვლადში გაქვთ შენახული მეტია 10 ზე დაპრინტეთ "more than 10" სხვა შემთხვებაში დაპრინტეთ "less than 10"


variable = 15

if variable >= 10:
    print("more than 10")
else:
    print("less than 10")


# 3) მომხმარებელს შემოაყვანინეთ რიცხვი, შემდეგ შეამოწმეთ თუ ეს რიცხვი უდრის 15 ს დაუპრინტეთ "equal to 15" სხვა შემთხვევაში დაუპრინტეთ "not equal to 15"


user_input = int(input("enter your number: "))
if user_input == 15:
    print("equal to 15")
else:
    print("not equal to 15")


# 4) მომხმარებელს შემოატანეთ სტრინგი. შენი დავალებაა შეამოწმო, თუ მომხამრებლის მიერ შემოყვანილი სტრინგი არის group84 დაუპრინტეთ 'you are correct" სხვა შემთხვევაში დაუპრინტეთ "you are wrong"


user_input1 = input("enter your string: ")
if user_input1 == "group84":
    print("you are correct")
else:
    print("you are wrong")


# 5) დაატრიალეთ for ციკლი 50 დან 100 მდე 5 ის გამოტოვებით


for i in range(50,100,5):
    print(i)


# 6) for ციკლის დახმარებით გამოიტანეთ ტერმინალში თქვენი სახელი და გვარი


for i1 in range(2):
    print("oto zumbadze")


# 7) while loop ის დახმარებით ტერმინალში გამოიტანეთ რიცხვები 20 დან 50 მდე


var = 20

while var <= 50:
    print(var)
    var += 1


# 8) დაბეჭდეთ 0-დან 100-მდე ყველა რიცხვი. (for-თაც და while-თაც)


for i2 in range(100):
    print(i2)

var1 = 0

while var1 <= 100:
    print(var1)
    var1 += 1


# 9) დაბეჭდეთ 0-დან 100-ის ჩათვლით ყველა რიცხვი. (for-თაც და while-თაც)


#igive davalebaa aritvlebaa


# 10) დაბეჭდეთ 10-დან 20-მდე ყველე რიცხვი (for-თაც და while-თაც)


for i4 in range(10,20):
    print(i4)


var2 = 10

while var2 <= 20:
    print(var2)
    var2 += 1


# 11) დაბეჭდეთ 100-დან 200-ის ჩათვლით ყოველი მე-5 რიცხვი (for-თაც და while-თაც)


for i5 in range(100,200,5):
    print(i5)

var3 = 100

while var3 <= 200:
    print(var3)
    var3 += 5


# 12) დაბეჭდეთ 10-დან 0-ის ჩათვლით ყველა რიცხვი (for-თაც და while-თაც)


for i6 in range(10, -1 ,-1):
    print(i6)

var4 = 10

while var4 > 0:
    print(var4)
    var4 -= 1


# 13) მომხმარებელს შემოაყვანიეთ რაიმე რიცხვი(მთელი/ათწილადი); შეამოწმეთ ეს რიცხვი - 
# --> თუ დადებითია დაპრინტეთ 'ეს რიცხვი დადებითი რიცხვია'
# --> თუ უარყოფითია დაპრინტეთ 'ეს რიცხვი უარყოფითი რიცხვია'
# --> თუ ნულია დაპრინტეთ 'ეს რიცხვი ნულია'


user_int = int(input("enter your integer: "))
if user_int > 0:
    print('ეს რიცხვი დადებითი რიცხვია')
elif user_int < 0:
    print('ეს რიცხვი უარყოფითი რიცხვია')
else:
    print('ეს რიცხვი ნულია')


# 14) მომხმარებელს შემოაყვანიეთ თავისი ასაკი:
# 0–12 წლის ასაკი --> დაპრინტეთ 'ბავშვი ხარ'
# 13-19 წლის ასაკი --> დაპრინტეთ 'მოზარდი/თინეიჯერი ხარ'
# 20-64 წლის ასაკი --> დაპრინტეთ 'ზრდასრული ხართ'
# 65-120 წლის ასაკი --> დაპრინტეთ 'ხანში შესული ხართ'
# 120 და ზემოთ --> დაპრინტეთ 'გურუ ან ჯადოქარი'
# თუ შემოყვანილი ასაკი უარყოფითია --> დაპრინტეთ 'არასწორი ინფო'


user_age = int(input("enter your age: "))
if user_age < 12:
    print('ბავშვი ხარ')
elif user_age < 19:
    print('მოზარდი/თინეიჯერი ხარ')
elif user_age < 64:
    print('ზრდასრული ხართ')
elif user_age < 120:
    print('ხანში შესული ხართ')
elif user_age > 120:
    print('გურუ ან ჯადოქარი')
else:
    print('არასწორი ინფო')


# 15) მომხმარებელს შემოატანიეთ სამი რიცხვი(მთელი/ათწილადი) და ამ სამი რიცხვთაგან დაბეჭდეთ უდიდესი


varr1 = int(input("enter your integer: "))
varr2 = int(input("enter your integer: "))
varr3 = int(input("enter your integer: "))

if varr1 >= varr2 and varr1 >= varr3:
    print("varr1 is biggest number")
elif varr2 >= varr1 and varr2 >= varr3:
    print("varr2 is biggest number")
else:
    print("varr3 is biggest number")


# 16) შემოატანიეთ მომხმარებელს რიცხვი 1-დან 7-ჩათვლით
# თუ 1 --> დაპრინტეთ 'ორშაბათი'
# თუ 2 --> დაპრინტეთ 'სამშაბათი'
# თუ 3 --> დაპრინტეთ 'ოთხშაბათი'
# თუ 4 --> დაპრინტეთ 'ხუთშაბათი'
# თუ 5 --> დაპრინტეთ 'პარასკევი' 
# თუ 6 --> დაპრინტეთ 'შაბათი'
# თუ 7 --> დაპრინტეთ 'კვირა' 
# სხვა დანარჩენი --> 'არ ვიცი ეგ რა დღეა'


user_int = int(input("enter bitween 1-7: "))
if user_int == 1:
    print('ორშაბათი')
elif user_int == 2:
    print('სამშაბათი')
elif user_int == 3:
    print('ოთხშაბათი')
elif user_int == 4:
    print('ხუთშაბათი')
elif user_int == 5:
    print('პარასკევი')
elif user_int == 6:
    print('შაბათი')
elif user_int == 7:
    print('კვირა')
else:
    print('არ ვიცი ეგ რა დღეა')


# 17) მომხმარებელს შემოატანინეთ რიცხვი, თუ ის მეტია 50-ზე დაბეჭდეთ ეს რიცხვი გამრავლებული 5-ზე, სხვა შემთხვევაში დაბეჭდეთ ეს რიცხვი კვადრატში


user_int1 = int(input("enter your number: "))
if user_int1 > 50:
    print(user_int1 * 5)
else:
    print(user_int1 ** 2)


# 18) მომხმარებელს შემოატანინეთ პაროლი თუ ის უდრის მაგალითად "goa123"-ს დაბეჭდეთ "Password is correct!", სხვა შემთხვევაში დაბეჭდეთ "Incorrect password!"


password = input("emter your password: ")
if password == "goa123":
    print("Password is correct!")
else:
    print("Incorrect password!")


# 19) მომხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ 1-დან შემოტანილის ჩათვლით ყველა რიცხვის ჯამი.


integer = int(input("enter your number: "))
res = 0
for i7 in range(1, integer):
    res += i7
print(res)