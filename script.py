rent=0
n=0
print("\t\t\t\t\tWelcome to the RENT calculator.")
print("\t\t\t\t\t\tDeveloped by Shuvam Koirala.")
print(" ")
print("What is the total rent of your rooms?:-")
rent=int(input())
print("")
print("Total number of people living in those rooms?:-")
n=int(input())
print("Enter name of people living in those rooms?:-")
print("")
name=[]
for i in range (0,n):
    print("Enter name:- ")
    name.append(input())
expense={}
for person in name[:]:
    print("Enter expenses of {}".format(person))
    choice="y"
    expense[person] = []
    while (choice!="n" and choice!="N"):
        print("Expense:")
        expense[person].append(int(input()))
        print("Want to add more expenses?")
        choice=input()
    print(" ")
partial=0
print("Rent of you rooms:- {}".format(rent))
for pe in name[:]:
    tot=0
    for e in expense[pe]:
        tot=tot+e
        rent=rent+e
    print("Total expense of {} :- {}".format(pe,tot))
print("Rent with expenses :- {}".format(rent))
partial=rent/n
print("Total divided by {} : {}".format(n,partial))
for per in name[:]:
    total=0
    for ex in expense[per]:
        total=total+ex
    print("{} has to pay:{}".format(per, (partial - total)))





