import random

uppercase_letters = "ABCDEFGHIJKMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "123456789"
symbols = "()!@#$%^&*:?><+__[]*,,."
print(" ========== Strong password Generator===========")
inputt = str(input("Do you wish to generate a strong password: "))
amountno = int(input("How many passwords do you wish to generate?:  "))
lengthno = int(input("what should be the length of your password?: "))
if inputt  =="yes":
    upper, lower, nums, syms = True, True, True, True
    all = ""
    if upper:
        all += uppercase_letters
        if lower:
            all += lowercase_letters
            if nums:
                all += digits
                if syms:
                    all += symbols
                    length = lengthno
                    amount = amountno
    for x in range(amount):
        password = "".join(random.sample(all, length))
        print("your password is ",password)

else:
    print(" Good bye!")
    quit
