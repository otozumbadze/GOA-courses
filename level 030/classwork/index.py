# 1) მომხმარებელს შემოატანინეთ სახელი და დაბეჭდეთ ის uppercase-ში.

name = input("enter your name:")

print(name.upper())

# 2) მომხმარებელს შემოატანინეთ სახელი დაბეჭდეთ lowercase-ში.

name1 = input("enter your name:")

print(name1.lower())

#3) მომხმარებელს შემოატანინეთ სახელი და დაბეჭდეთ ისე, რომ მისი პირველი ასო იყოს uppercase-ში დაწერილი, ხოლო დანარჩენი lowercase-ში.

name2 = input("enter your name:")

print(name2.capitalize())

# 4) შექმენით ცვლადი, სადაც შეინახავთ ნებისმიერ სიტყვას. მომხმარებელს შემოატანინეთ სიმბოლო, რომლის ინდექსიც უნდა იპოვოთ სთრინგში და დუბეჭდოთ შემდეგი ფორმატით "a - 0". არ მაქვს გაკეთებული ვერ გავიგე
 
 
# 5) შექმენით ცვლადი და შიგნით შეინახეთ თქვენი სახელი, გაიგეთ თქვენი სახლის სიგრძე შესაბამისი ფუნქციის მეშვეობით.

my_name = "Otiko"

print(len(my_name))

# 6) მომხმარებელს შემოატანინეთ სახელი და შეამოწმეთ იწყება თუ რა იგი ასო-ბგერა "g"-თი.

name3 = input("enter your name:")

if name3.startswith("g"):
    
    print("start with g")
else:
    print("does not start with g")

# 7) მომხმარებელს შემოატანინეთ სახელი და შეამოწმეთ მთავრდება თუ რა იგი ასო-ბგერა "l"-თი

name4 = input("enter your name:")

if name4.endswith("l"):
    
    print("ends with l")
else:
    print("does not ends with l")




