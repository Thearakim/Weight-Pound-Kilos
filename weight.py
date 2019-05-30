weight = int(input("Please enter your weight :"))
type = input("Choose (L)bs or (K)g :")
if type.upper() == 'K':
    weight1 = weight * 0.45
    print(f"You are {weight1} kilos .")
elif type.upper() == 'L':
    weight2 = weight/0.45
    print(f"You are {weight2} pounds ." )
else:
    print("error")