print("hello welcome to coffe shop")
name = input("what your name?\n")
print ("hello " + name + ",thanks for coming today happy nice day\n\n")

menu = "kopi hitam,kopi susu, teh manis"

print(name + ",what your like for coffe today ? here is ehat we are serving.\n\n" + menu)

order = input()
price = 3000
quantity = input("how many coffe would you like?\n")

total = price * int(quantity)

print("thank you, your total is : Rp" + str(total))


print("Sound good " + name + ",wil have that " + order + " ready for you in a moment")
