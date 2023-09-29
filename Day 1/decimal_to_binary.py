# Program to convert decimal number into binary
decimal_number = int(input("Enter a decimal number: "))
remainder = ""
int_number = decimal_number
while(int_number):
    if(int_number%2==0):
        remainder+="0"
        int_number=int_number//2
    else:
        remainder+="1"
        int_number=int_number//2
print(f"Binary equivalent of {decimal_number} is {remainder[-1::-1]}")