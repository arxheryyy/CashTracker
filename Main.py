from time import localtime, strftime
print("This is a spending traker created by Arxheryyy")
print("----------------------------------------------")
bool = False
saved = []
spendings = []
comments = []
z = 0
fileObj = open(r"spendings.txt", "r")
fileObj.seek(0)
saved = fileObj.readlines()
length = len(saved)
dividedLen = int(round(length/3, 0))
for x in saved:
    if z == 0:
        for dividedLen:
            comments.append(saved[z][:-1])
            z = z+3
    elif z == 1:
        for divdedLen:
            spendings.append(saved[z][:-1])
            z = z+1
fileObj.close()
while bool == False:
    print("Enter 1 to Check total spendings")
    print("----------------------------------------------")
    print("Enter 2 to View Spendings")
    print("----------------------------------------------")
    print("Enter 3 to Add Spendings")
    print("----------------------------------------------")
    print("Enter 4 to Exit")
    print("----------------------------------------------")
    uInput = input()
    if uInput == '1':
        total = 0.00
        y = 0
        for x in spendings:
            total = total + float(spendings[y])
            y = y+1
        print(total)
    elif uInput == '2':
        y = 0
        for x in spendings:
            print("$" + str(spendings[y]) + " " + comments[y])
            y = y+1
    elif uInput == '3':
        print("Enter Amount")
        amountIn = input()
        amount = float(amountIn)
        amount = round(amount, 2)
        spendings.append(amount)
        print("Enter Comment")
        comment = input()
        comments.append(comment)
        entry = (comment + '\n' + str(amount) + '\n')
        fileObj = open(r"spendings.txt", "a")
        fileObj.writelines(entry)
        currentTime = strftime("%y-%m-%d", localtime())
        fileObj.writelines("Date" + currentTime)
        fileObj.close()
        print("Successfully added")
    elif uInput == '4':
        bool = True
