#აქ ვარკვევ დაბლოკილია თუ არა ანგარიში, რომ შემდეგი ოპერაციები გავაგრძელო
account_active = input("შეიყვანეთ ანგარიშის სტატუსი: 'active','blocked': ")
is_account_active = account_active == "active"
if is_account_active == False:
    print("ანგარიში დაბლოკილია. შეკვეთა ვერ დამუშავდება. ")
#აქ ვადგენ ანგარიშ ხომ არ მინუსდება, რომ შემდეგი ოპერაციები გავაგრძელო
else:
 cart_total = float(input("შეიყვანეთ კალათის ღირებულება (ლარებში): "))
if cart_total <=0:
    print("შეცდომა: კალათა ცარიელია ან მინუსებშია. შეკვეთა ვერ გატარდება.")
    #აქედან უკვე ვიწყებ  პირობების განსაზღვრას.
else:
  loyalty_points = int(input("დაგროვილი ქულები: "))
  promo_code = input("გაქვთ პრომო კოდი? ('yes, 'no'): ")
  has_promo_code = promo_code == "yes"
  discount = 0
  user_status = input("შეიყვანეთ სტატუსი ('regular', 'vip', 'admin'): ")
  #აქედან ვიწყებ პირობების დაკმაყოფილებას - ყველაზე რთული ნაწილი
  if user_status == "admin":
    discount = 50   
  elif  user_status == "vip":
    discount = 20
    if loyalty_points >= 500:
        discount = 25
  elif user_status == "regular":
      if has_promo_code or cart_total >= 150:
        discount = 10
  else: 
      discount = 0
      # საბოლოო ფასდაკლების შემდეგ უნდა დადგინდეს მარკეტის პროდუქციის ფასი
market_cost = float(cart_total - (cart_total * discount / 100))
# უნდა განისაზღვროს ქალაქების მიხედვით მიტანის ფასი
delivery_city = input("მიუთითეთ მიტანის ადგილი: 'თბილისი', 'ქუთაისი', 'ბათუმი', 'რეგიონები' ")
delivery_cost = 15
# აქედან ვიწყებ მიტანის პირობების დაკმაყოფილებას
if delivery_city in ['თბილისი', 'ქუთაის', 'ბათუმი' ]:
  if market_cost >= 100:
    delivery_cost = 0
  else:
    delivery_cost =5
else:
  delivery_cost = 15 
  # აქ გამომყავს საბოლოო ღირებულება, რომელსაც მომხმარებელი გადაიხდის პროდუქციაში და მიტანის სერვისში.
total_cost = market_cost + delivery_cost
#აქ ხდება საბოლოო ინვოისის განსაზღვრა და ვასრულებ ოპერაციას.
print("საწყისი ღირებულება - ", cart_total, "GEL | ", "ფასდაკლება - ", discount,"% | ", "მიტანის საფასური - ", delivery_cost,"GEL | ", "ჯამური ღირებულება - ", total_cost, " GEL |")

  

# if delivery_city in ["თბილისი, ბათუმი, რეგიონები: " ]



# print("Discount: ", discount)


# # if user_status == "regular":
     
     
# # loyalty_points = int(input("დაგროვილი ქულები: "))
# #  promo_code = input("გაქვთ პრომო კოდი? ('yes, 'no'): ")
# # has_promo_code = promo_code == "yes"
# #  promo_code == "yes"
# # if user_status == "vip": 
# #          discount = "20%"
# # if loyalty_points >= 500:
# #       discount = "25%"
# # elif user_status == "regular" and has_promo_code == "yes" or cart_total >= 150:
# #        discount = "10%"
# # else:
# #         delivery_city = input("თბილისი, ბათუმი, რეგიონები: " )