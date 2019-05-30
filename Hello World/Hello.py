#print("Hello")
#print("0----")
#print("  |||")
#print("*"*10)

#price = 10
#print(price)

#print("Patient information")
#name = "John Smith"
#age = 20
#is_new = True

#name = input("What is your name? ")
#print('Hi' + name)

#name = input("what is you name? ")
#color = input("What is your favorite color? ")
#print(name+' like '+color)
#Birth_year = input(" Birth year: ")
#print(type(Birth_year))
#age = 2019 - int(Birth_year)
#print(type(age))
#print(age)

#weight_lbs = input("Please kindly type your real weight :")
#weight_kg = float(weight_lbs) * 0.45
#print(weight_kg)

#str = 'Hello World'
#print(str[-1])
#print(str[0:3])
#str1 = str[0:4]
#print(str1)

#first = 'Kim'
#last = 'Theara'
#msg = f'{first} [{last}] is a code'
#print(msg)
##message = first +' ['+ last+'] is a code'
#print(message)
#print(len(message))
#print(message.upper())
#print(message.lower())
#print(message.find('i'))
#print(message.replace('Theara', 'Chhayly'))
#print('Kim' in message)

#x = 2.9
#print(round(x))

#is_hot = False #True
#if is_hot:
#   print("It's a hot day")
#  print("drink water")
#else:
#    print("It's a cold day")
#    print("Be careful")
#print("What a lovely day")

#str = 1000000
#is_buyer_credit = True
#if is_buyer_credit:
#    Down_payment = 0.1 * str
#else:
#    Down_payment = 0.2 * str
#print(f"Down payment: ${Down_payment}")

#has_high_income = True
#has_good_credit = True
#has_high_credit = False
#if has_high_income and has_good_credit:
#    print("Eligible for loan")
#if has_high_income and not has_high_credit:
#    print("Hello")

#temperature = 30
#if temperature > 30:
#    print("It is a hot day")
#else:
#    print("It is a cold day")

#name = input("Enter your name: ")
#if len(name)<3:
#    print("the character of name must have at least 3.")
#elif len(name)>50:
#    print("the character of name maximum is 50.")
#else:
#    print("Good name.")

weight = input("weight :")
print("(L)bs or (k)g :")
weight1 = int(weight) * 0.45
value = input("")
if value == 'K' or 'k':
    print("your weight is :", weight1)
elif value == 'L' or 'l':
    print("your weight is : ", weight)
else:
    print("error")