#მონაცემების მოთხოვნა, გასუფთავება ზედმეტი სფეისებისგან და დაიწერება ლამაზად.
first_name = input("გთხოვთ შეიყვანეთ თქვენი სახელი: \n").replace(" ", "").strip().title()
last_name = input("გთხოვთ შეიყვანეთ თქვენი გვარი: \n").replace(" ", "").strip().title()
mail_type = input("გთხოვთ აირჩიეთ ელ. ფოსტა: gmail.com, itstep.ge, yahoo.com \n")
# პირველი 2 ასოს ამოღება სახელიდან
name_first_2 = first_name[:2]
# მეილის აწყობა F სტრინგით
email = f"{name_first_2}{last_name}@{mail_type}"
# საბოლოო შედეგის გამოტანა
print("ელფოსტის გენერატირი")
print(email)
# აქ სრულდება პირველი ნაწილი.
#print(name_first_2)g
#print(first_name,last_name,mail_type)