
print("===============================================================")

print("                    FARMER RIVER CROSSING")

print("===============================================================")

print("In this game you will be required to take 3 objects across a river safely. A lion, goat and grass")

print("============================================================")

print("HERE ARE THE RULES TO THE GAME;- ")

print("1. The farmer must always be in the boat when crossing the river.")

print("2. The boat can carry the farmer and at most one item at a time.")

print("3. The farmer may also cross the river without taking an item.")

print("4. The farmer may take an item with him in either direction.")

print("=============================================================")



print("ON THE LEFT SIDE:-")

print("1. Lion")

print("2. Grass")

print("3. Goat")



opt1 = int(input("WHO WOULD YOU LIKE TO TAKE TO THE RIGHT SIDE OF THE RIVER? "))

while opt1 != 0:

    if opt1 == 1:

        print("")

        print("taking the lion to the other side...")

        print("")

        print("OH NO! YOU LEFT THE GOAT WITH THE GRASS")

        print("--------------")

        print("YOU LOSE!")

        print("--------------")

        print("TRY AGAIN?")

        print("")

        print("ON THE LEFT SIDE:-")

        print("1. Lion")

        print("2. Grass")

        print("3. Goat")

        print("")

        opt1 = int(input("WHO WOULD YOU LIKE TO TAKE TO THE RIGHT HAND SIDE OF THE RIVER? "))

    elif opt1 == 2:

        print("")

        print("taking the Grass to the other side...")

        print("")

        print("OH NO! YOU LEFT THE GOAT WITH THE LION")

        print("--------------")

        print("YOU LOSE!")

        print("--------------")

        print("TRY AGAIN?")

        print("")

        print("ON THE LEFT SIDE:-")

        print("1. Lion")

        print("2. Grass")

        print("3. Goat")

        print("")

        opt1 = int(input("WHO WOULD YOU LIKE TO TAKE TO THE RIGHT HAND SIDE OF THE RIVER?: "))



    else:

        print("")

        print("taking the Goat to the other side...")

        print("")

        print("NICE WORK")

        print("==================")

        break

print("ON THE LEFT SIDE;-")

print("")

print(". Lion")

print(". Grass")

print("")

print("ON THE RIGHT SIDE:-")

print("")

print("1. Farmer")

print("2. Goat")

print("")



opt2 = int(input("WHO WOULD YOU LIKE TO TAKE TO THE LEFT SIDE? "))



while opt2 != 0:

    if opt2 == 2:

        print("")

        print("TAKING ONLY THE GOAT TO THE LEFT SIDE...")

        print("")

        print("BAD MOVE!")

        print("==========================")

        print("THIS MOVE WILL START THE GAME FROM ALL OVER AGAIN")

        print("==========================")

        print("")

        print("TRY AGAIN?")

        print("")

        print("ON THE LEFT SIDE;-")

        print("")

        print(". Lion")

        print(". Grass")

        print("")

        print("ON THE RIGHT SIDE:-")

        print("")

        print("1. Farmer")

        print("2. Goat")

        print("")

        opt2 = int(input("WHO WOULD YOU LIKE TO TAKE TO THE LEFT SIDE? "))



    elif opt2 == 1:

        print("")

        print("TAKING ONLY THE FARMER TO THE LEFT SIDE...")

        print("")

        print("GOOD WORK, ALMOST THERE!")

        print("==========================")

        print("ON THE LEFT SIDE;-")

        print("")

        print("1. Lion")

        print("2. Grass")

        print("")

        print("ON THE RIGHT SIDE:-")

        print("")

        print(". Goat")

        print("")

        break



opt3 = int(input("WHO WOULD YOU LIKE TO TAKE TO THE RIGHT SIDE? "))



while opt3 != 0:

    if opt3 == 1:

        print("")

        print("THATS NOT A VERY GOOD MOVE!!")

        print("")

        print("===========================================")

        print("1. BY TAKING THE LION TO THE RIGHT SIDE IT WILL EAT THE GRASS")

        print("2. BY TAKING THE GRASS TO THE LEFT SIDE, THE GOAT WILL EAT IT")

        print("       ITS A LOSE LOSE       ")

        opt3 = int(input("WHO WOULD YOU LIKE TO TAKE TO THE RIGHT SIDE? "))



    elif opt3 == 2:

        print("")

        print("TAKING ONLY THE Grass TO THE LEFT SIDE...")

        print("")

        print("NICE!!!!")

        print("ON THE LEFT SIDE:-")

        print(". Goat")

        print(". Grass")

        print("")

        print("ON THE RIGHT SIDE:-")

        print("1. Lion")

        print("2. Farmer")

        print("")

        break



opt4 = int(input("WHO WOULD YOU LIKE TO TAKE TO THE LEFT SIDE? "))

while opt4 != 0:

    if opt4 == 1:

        print("")

        print("TAKING LION TO THE LEFT SIDE")

        print("SOOO CLOSE! YET STILL WRONG")

        print("==========================")

        print("1. BY TAKING THE LION BACK THE GAME WOULD START FROM THE BEGINNING AGAIN")

        print("==========================")

        print("")

        print("TRY AGAIN?")

        print("")

        print("ON THE LEFT SIDE:-")

        print(". Goat")

        print(". Grass")

        print("")

        print("ON THE RIGHT SIDE:-")

        print("1. Lion")

        print("2. Farmer")

        print("")

        opt4 = int(input("WHO WOULD YOU LIKE TO TAKE TO THE LEFT SIDE? "))

    elif opt4 == 2:

        print("")

        print("TAKING ONLY THE FARMER TO THE LEFT SIDE")

        print("")

        print("WOW YOU ARE ON A ROLL!! GREAT")

        print("==========================")

        print("ON THE LEFT SIDE:-")

        print("")

        print("1. Grass")

        print("2. Goat")

        print("ON THE RIGHT SIDE:-")

        print("")

        print(". Lion")

        print("")

        break

print("==========================================")

print("YOU ARE ABOUT TO WIN, JUST FOCUS!! =)")

print("")

print("ON THE LEFT SIDE:-")

print("")

print("1. Grass")

print("2. Goat")

print("ON THE RIGHT SIDE:-")

print("")

print(". Lion")

opt5 = int(input("WHO WOULD YOU LIKE TO TAKE TO THE RIGHT SIDE? "))



while opt5 != 0:

    if opt5 == 2:

        print("")

        print("OOOOH THAT WAS SO CLOSE")

        print("==========================")

        print("1. BY TAKING THE GOAT, THE LION WOULD EAT THE GOAT")

        print("2. BY TAKING THE LION BACK YOUD START FROM YOUR 2ND MATCH ONCE AGAIN")

        print("==========================")

        print("")

        print("TRY AGAIN?")

        print("")

        print("ON THE LEFT SIDE:-")

        print("")

        print("1. Grass")

        print("2. Goat")

        print("ON THE RIGHT SIDE:-")

        print("")

        print(". Lion")

        opt5 = int(input("WHO WOULD YOU LIKE TO TAKE TO THE RIGHT SIDE? "))

    elif opt5 == 1:

        print("")

        print("TAKING ONLY THE GRASS TO THE LEFT SIDE")

        print("")

        print("AMAZING WORK!!")

        print("==========================")

        print("ON THE LEFT SIDE:-")

        print("Goat")

        print("")

        print("ON THE RIGHT SIDE:-")

        print("")

        print("1. Lion")

        print("2. Grass")

        break

print("========================================")

print("WELL I'M PRETTY SURE THE CHOICE HERE IS QUITE OBVIOUS LOL, SO I'M GONNA TAKE YOU BACK TO THE LEFT SIDE =)")

print("ON THE LEFT SIDE:-")

print("1. Goat")

print("")

print("ON THE RIGHT SIDE:-")

print("")

print(". Lion")

print(". Grass")



opt6 = int(input("LAST BUT NOT LEAST, WHO WOULD YOU LIKE TO TAKE TO THE RIGHT SIDE? "))

if opt6 == 1:

    print("")

print("\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~")

print("CONGRATULATIONS YOU HAVE WON THE PUZZLE, YOU ARE VERY SMART")

print("\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~")




 

passtud = 0

Fstud = 0

mxminmrk = []

tstudents = 0

tmarks = 0

avg = 0

clasgrad = avg

 

marks = int(input("plese entr the number of marks achieved by student, Enter -1 to enter the summary database? "))

 

while marks >= 0 and marks <= 100:

    tmarks = tmarks + marks

    tstudents += 1

    avg = tmarks / tstudents

    mxminmrk.append(marks)

 

    print("sucessfully added to database ")

 

    if marks > 0 and marks < 30:

        Fstud += 1

        print(" the student achieved a C grade ")

 

    elif marks > 30 and marks < 50:

        Fstud += 1

        print("student achived a B grade ")

 

    else:

        passtud += 1

        print("student achieved an A grade ")

 

    marks = int(input("Enter the marks of other students "))

 

    if marks < 0 and marks != -1:

        print("invalid number of marks entered, try again ")

        marks = int(input("Enter marks again "))

 

    if marks == -1:

        csuc = str(input("Are you sure yud like to enter the summary database? Y/N "))

 

        if csuc == "Y":

            clasgrad = avg

            perc = passtud / tstudents * 100

            perc2 = Fstud / tstudents * 100

 

            print("calculating...")

            print("the total number of student who passed the class = ", passtud, "which is", perc, "%", "of the total students")

            print("total number of students who failed  = ", Fstud, "which is", perc2, "%", "of total students")

            print("total number of student in class = ", tstudents)

            print("total cumalative marks acheieved = ", tmarks)

            print("the average marks of the class is = ", avg)

            print("highest marks achived are = ", max(mxminmrk))

            print("lowest marks achieved are =", min(mxminmrk))

 

        else:

            print("data has been stored succefully")

 

        if clasgrad < 50:

            print("class is underperforming, try harder lol")




 

sbal = 1000

interest = 0.05

subsbal = 0

 

Q = str(input("would you like to pay the regular amount of $ 100 towards your debt? "))

 

while Q == "Yes" and sbal != 100:

    print("$100 will be subtracted from your debt")

    sbal = sbal - 100

    print("your reamining debt is", sbal)

 

    Q = str(input("would you like to make another payment? "))

 

    if Q == "No":

        print("okay your gonna have to pay more, because of interest =)")

        sbal = (sbal * interest) + sbal

        print("your new remaining loan is ", sbal)

 

    while sbal == 100 and sbal != 0:

        print("only $100 reaming in loan, lower payments can now be made")

        lmin = int(input("how much do you want to pay? "))

        sbal = sbal - lmin

        print("debt reamining is", sbal)

 

        if sbal == 0:

            print("no more loan reaming")




 

texp = 0

tbudg = 3

Ans = 0

 

exp = int(input("How much did you spend today?, press 1. Start calculating , 0. end of day summary "))

 

while tbudg != 0:

    exp = int(input("How much did you spend today? "))

 

    if exp < 50:

        tbudg = tbudg - 1

        texp = texp + exp

        print("great work budgeting")

 

    elif exp > 50:

        tbudg = tbudg - 1

        texp = texp + exp

        print("going out of budget")

 

while tbudg == 0:

    Ans = int(input("would you like to know how much you spent today 1. Yes 2. No "))

    if Ans == 1:

        print("your total expense is ", texp)

        break

    else:

        print("Great work, tracking your budget")

        break




 

ttrans = 0

tsal = 0

 

s = int(input("Enter the vlaue of your purchased product "))

 

while s != 0:

    s = int(input("Enter the vlaue of your purchased product, press 0 once final transaction is done "))

 

    if s > 0:

        tsal = tsal + s

        ttrans += 1

        print("value", s, "has been added to database")

 

    else:

        print("taking you to summary page")

 

if s == 0:

    Ans = int(input("would you like the end of day summary?, 1. yes , 2. No "))

 

    if Ans == 1:

        print("your total number of trnsactions today are", ttrans)

        print("the total number sale made tday are", tsal)

 

    else:

        print("nice =)")


 

balance = 100

depo = 0

whithdraw = 100

print("1. checking balance")

print("2. depositing money")

print("3. withdrawing money")

print("4. Exit")

 

opt = int(input("please choose one option from 1 - 4 "))

 

while opt > 0:

    if opt == 2:

        depoam = int(input("how much money do you want to deposit into account "))

        depo = depoam

        print("$", depoam, "has been transffered into your account successfully")

        newbal = depoam + balance

        print("your new balance is ", newbal)

        break

    elif opt == 1:

        balance = balance

        print("your current balace is", "$", balance)

        break

 

    elif opt == 3:

        num = int(input("how much would you like to withdraw?"))

        whithdraw = 100 - num

        print("money has been withdrawn your new balace is", "$", whithdraw)

 

    else:

        print("Goodbye")

        break

#  STOP&#x20;

 

Answer = str("Python")

Attempts = 0

 

while Attempts != 3:

    Question = str(input("what coding language is this?"))

 

    if Question != Answer:

        print("incorrect answer please try again")

        Attempts += 1

    else:

        print("answer is correct")

    if Attempts == 3:

        print("answered wrong 3 times")



# STOP&#x20;

 

num = int(input("write a set of numbers"))

ascending = True

while num > 0:

    num1 = num % 10  # last value

    nvar = num // 10  # reduced value

    num2 = nvar % 10  # second last value

 

    if num1 < num2:

        ascending = False

 

    num = num // 10

 

if ascending:

    print("the sequence is ascending")

else:

    print("the sequence is not ascending")


num = int(input("please enter a nmber"))

div3 = 0

for i in range(0, num):

    if i % 3 == 0:

        div3 += 1

print(div3)


num = int(input("please enter a nmber"))

num2 = 0

while num != 0:

    num3 = num % 10

    num = num // 10

    num2 += 1

print("there are num2 integrs in the number")



for i in range(0, 5):

    for j in range(0, 5):

        print("*", end=" ")

    print()

for i in range(0, 5):

    for j in range(i):

        print("*", end=" ")

    print()

for i in range(5, 0, -1):

    for j in range(i):

        print("*", end="")

    print()

r = int(input("hw many rows of strs do you want? "))

c = int(input("how many coloumns of stars do you want? "))

for i in range(r):

    for j in range(c):

        print("*", end="")

    print()

for i in range(0, 6):

    for j in range(1, i):

        print(j, end="")

    print()

for i in range(0, 6):

    for j in range(1, i):

        print(i, end="")

    print()

for i in range(0, 3):

    for j in range(5):

        print(i, end="")

    print()

for i in range(0, 3):

    for j in range(1, 4):

        print(j, end="")

    print()

for i in range(0, 5):

    for j in range(5 - i):

        print("", end="")

    for j in range(3 * i - 1):

        print("", end="")

    print()


temperature_by_day = (10, 15, 20, 21, 24)

inc = 0

for i in range(1, 5):

    if temperature_by_day[i] > temperature_by_day[i - 1]:

        inc += 1

print("The temperature was higher than the day before", inc, "number of times")


number = [10, 15, 20, 25, 10, 11, 5]

seq = 0

longest = 0

for i in range(1, len(number)):

    if number[i] > number[i - 1]:

        seq += 1

    else:

        print("calculating result")

        seq = 0

    if seq > longest:

        longest = seq

print("The longest sequence is of", longest + 1, "numbers")

# STOP&#x20;

number = (10, 15, 20, 25, 10, 11, 5)

for i in range(1, len(number)):

    avg = sum(number[:i]) / i

    if number[i] > avg:

        print(number[i])

# STOP&#x20;

number = (10, 15, 20, 25, 10, 11, 5)

for n in number:

    if number.count(n) == 2:

        print(n)

# STOP&#x20;

number = [5, 10, 15, 20, 30, 10, 6, 7]

 

unique_numbers = sorted(set(number))

if len(unique_numbers) >= 3:

    no3 = unique_numbers[2]

    print(no3)

# STOP&#x20;

 

chair = (

    (0, 0, 0),

    (0, 1, 0),

    (1, 1, 0),

    (0, 0, 0)

)

length = 0

row = 0

for i in range(4):

    rw = 0

    for k in range(3):

        if chair[i][k] == 0:

            rw += 1

            if rw > length:

                length = rw

                row = i

        else:

            rw = 0

print(row)

# STOP&#x20;

 

num = (

    (10, 5, 15),

    (3, 2, 7),

    (1, 1, 5)

)

 

inc = 0

for k in range(3):

    for i in range(2):

        if num[i][k] >= num[i + 1][k]:

            break

    else:

        inc += 1

print(inc)

# STOP&#x20;

number = (1, 5, 7, 9, 10, 100)

number2 = []

for i in range(4):

    diff = number[i + 2] - number[i]

    number2.append(diff)

print(number2)

# STOP&#x20;

matrix = []

for i in range(len(grid) - 1):

    row = []

    print(grid[i])

    for j in range(len(grid[i])):

        value = grid[i][j] - grid[i + 1][j]

        row.append(value)

    matrix.append(row)

print(matrix)

# STOP&#x20;

num = int(input("please enter a number"))

hw = int(input("how mny numbers do you want?"))

num1 = num + 1

print(num)

print(num1)

for i in range(11):

    num2 = num + num1

    print(num2)

    num = num1

    num1 = num2

# STOP&#x20;

num = int(input("write a set of numbers"))

 

while num > 0:

    num1 = num % 10

    nvar = num // 10

    num2 = nvar % 10

    if num1 > num2:

        print("the sequence is ascending")

    elif num2 > num1:

        print("the sequence is not ascending")

    else:

        print("sequence is invalid")

    num = num // 10


