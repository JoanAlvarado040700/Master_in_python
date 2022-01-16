#Ejemplo 2 : IF nested 

print("")
print("************ Example 2: if nested    ***********")

name = "Joan larios"
city = "Bilwi"
continent = "nort america"
age = int(input(f"please mr {name} , enter your age: "))
legal_age = 18


if age >= legal_age:
    print(f" {name} is of legal age ")
    if continent != "Central america":
        print(f" {name}  does not belong to central america  ")

else: 
    print(f" {name} is not of legal age ")