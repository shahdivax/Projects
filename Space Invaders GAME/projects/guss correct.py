import random

while True:
    flag = True
    num = input(" Input the upper limit : ")
    while flag:
        if num.isdigit():
            print(" Lets play!")
            num = int(num)
            flag = False
        else:
            print(" invalid input , Try again!")

    sceret = random.randint(1,num)

    guess = None

    count = 1

    while guess != sceret:
        guess = input(" please input a number between 1 and "+str(num) +" : ")
        if guess.isdigit():
            guess = int(guess)
        
        if guess == sceret:
            print(" you got it !")
        else:
            print(" please try again !")
            count+=1
    print("It took you " +str(count)+" gusses !")



