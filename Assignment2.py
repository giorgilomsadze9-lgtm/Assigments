name = input("name: ")
surname = input("surname: ")
birthyear = int(input("birthyear: "))
favoriteprogramminglanguage = input("favorite programming language: ")
now = 2026
age = int(now-birthyear)
score = int(input("score (max 20: )"))
grade = score // 2
print(name.upper(),surname.upper(),birthyear,favoriteprogramminglanguage,age,age > 18,sep=" | ")
print("Grade:",grade)
