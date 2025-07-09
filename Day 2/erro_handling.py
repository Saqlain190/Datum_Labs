# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         print("You enter a valid Number")
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

num = input("Enter A Number :")
try:
    for i in range(1,11):
        print(f"{num} X {i}= {int(num)*i}")

except:
    print("You have entered an invalid number")

