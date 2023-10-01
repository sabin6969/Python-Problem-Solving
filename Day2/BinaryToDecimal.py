binary = input("Enter a binary number: ")
binary = binary[-1::-1]
decimal_number=0;
for i in range(len(binary)):
    decimal_number = decimal_number+ int(binary[i])*pow(2,i)
print(decimal_number)