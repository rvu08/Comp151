list = []
names = input("What is your name? ")
tickets = int(input("How many tickets are you buying?"))
total = float(tickets * 11.5)
list.append(total)
list.append(tickets)
num = int(input("Pick a number"))
for i in range(1,11):
    print(num * i)


print(f"The total amount for {tickets} tickets is ${total}")