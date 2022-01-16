#Ejemplo 3 : elif

print("")
print("************ Example 2: elif    ***********")


nota = int(input("enter your grade: "))

if nota == 60 : 
    print("aprove")
elif nota >= 80:
    print("your grades are above average, execellent!!")
    
elif nota < 60:
        print("does not have an average to pass")