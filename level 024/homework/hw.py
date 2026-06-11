# 2) შექმენით პროგრამა რომელიც მომხმარებლისგან მიიღებს რიცხვს, შემდეგ დაადგენს დადებითია, უარყოფითი თუ ნული if-elif-else ის საშვალებით, თუ რიცხვი დადებითია შეამოწმეთ არის თუ არა ლუწი თუ არის დაბეჭდეთ "The number is positive and even." ხოლო სხვა შემთხვევაში დაბეჭდეთ "The number is positive and odd."

list = [-1,-2,-3,-4,5]
for i in list:
    if i > 0:
        if i % 2 == 0:
            print("The number is positive and even.")
        else:
            print("The number is positive and odd.")

# 3) მომხმარებელს იქამდე შეეკითხეთ რიცხვები სანამ უარყოფით რიცხვს არ შემოიყვანს, while ციკლისა და input ინსტრუქციის საშვალებით, ასევე პირობითი განცხადებების დადებითობა/უარყოფითობის შესამოწმებლად.

number = 0
while number >= 0:
    number = int(input("enter your number: "))

    if number >= 0:
        print("Even")
    else:
        print("Odd")


# 4) მომხმარებელს 3 მცდელობა აქვს სწორი PIN კოდის შეყვანისთვის. თუ შეიყვანს სწორად, დაიბეჭდება "Access Granted", სხვა შემთხვევაში "Access Denied" გამოიყენეთ პირობითი განცხადებები

pin_code = "6767"
for i in range(3):
    user_pin = input("enter your guess pin: ")

    if user_pin == pin_code:
        print("acces granted")
        break
    else:
        print("Acces denied")

# 5) შექმენი სია fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ალუბალი"] და დაბეჭდე მესამე ელემენტი

fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ალუბალი"]
print(fruits[2])

# 6) შექმენი სია numbers = [10, 20, 30, 40, 50], შეცვალე მეორე ელემენტი 25-ით და დაბეჭდე განახლებული სია
 
numbers = [10, 20, 30, 40, 50]
number[1] = 25
print(numbers)

# 7) მომხმარებელს შეაყვანინე ინდექსი (`0`-დან `4`-მდე) და დაბეჭდე შესაბამისი ელემენტი სიიდან colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]

colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]
index = int(input("enter between 0-4: "))
print(colors[index])


# 8) შექმენი სია animals = ["ძაღლი", "კატა", "სპილო", "ვეფხვი", "ლომი"], შეცვალე ბოლო ელემენტი "გემი"-თ და დაბეჭდე სია

animals = ["ძაღლი", "კატა", "სპილო", "ვეფხვი", "ლომი"]
animals[-1] = "გემი"
print(animals)

# 9) მომხმარებელს შეაყვანინე ინდექსი და ახალი ფერი, შეცვალე ამ ინდექსზე არსებული ფერი სიაში colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]` და დაბეჭდე განახლებული სია

colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]
index2 = int(input("enter your index: "))
new_color = input("enter your color: ")
colors[index] = new_color
print(colors)

