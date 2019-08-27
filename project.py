import random
mp=0
choice=1
while(choice!=0):
    print("\n")
    ch=int(input(('''*********************\n* 1)Start Game      *\n* 2)View all scores *\n* 3)Instructions    *\n* 4)Exit            *\n*********************\n''')))
    fp=open("score.txt","a+")
    score=0
    if ch==1:
        name=input("Enter your name:")
        print('''enter level\n1.Easy\n2.Medium\n3.Hard\n''')
        n1=int(input())
        c=[]
        if(n1==1):
            while(True):
                t1=random.randint(10,99)
                c=list(map(int,list(str(t1))))
                if(len(c)!=len(list(set(c)))):
                    continue
                else:
                    break
        elif(n1==2):
            while(True):
                t1=random.randint(100,999)
                c=list(map(int,list(str(t1))))
                if(len(c)!=len(list(set(c)))):
                    continue
                else:
                    break
        elif(n1==3):
            while(True):
                t1=random.randint(1000,9999)
                c=list(map(int,list(str(t1))))
                if(len(c)!=len(list(set(c)))):
                    continue
                else:
                    break
        bulls=0
        cows=0
        if(n1==1):
            score=100
            while(bulls<2):
                num=input("enter 2 digit number: ")
                if num=="-1":
                    st=''
                    for lm in c:
                        st+=str(lm)
                    print("Random number generated by the system is : ",st)
                    mp=1
                    break
                else:
                    bulls=0
                    cows=0
                    dummy=0
                    num=list(num)
                    for i in range(len(num)):
                        if int(num[i])==c[i]:
                            bulls=bulls+1
                        if int(num[i]) in c:
                            dummy=dummy+1
                    cows=dummy-bulls
                    print("BUlls:",bulls,"COWS:",cows)
                    score=score-1
        elif(n1==2):
            score=1000
            while(bulls<3):
                num=input("enter 3 digit number: ")
                if num=="-1":
                    st=''
                    for lm in c:
                        st+=str(lm)
                    print("Random number generated by the system is : ",st)
                    mp=1
                    break
                else:
                    bulls=0
                    cows=0
                    dummy=0
                    num=list(num)
                    for i in range(len(num)):
                        if int(num[i])==c[i]:
                            bulls=bulls+1
                        if int(num[i]) in c:
                            dummy=dummy+1
                    cows=dummy-bulls
                    print("BUlls:",bulls,"COWS:",cows)
                    score=score-1
        elif(n1==3):
            score=10000
            while(bulls<4):
                num=input("enter 4 digit number: ")
                if num=="-1":
                    st=''
                    for lm in c:
                        st+=str(lm)
                    print("Random number generated by the system is : ",st)
                    mp=1
                    break
                else:
                    bulls=0
                    cows=0
                    dummy=0
                    num=list(num)
                    for i in range(len(num)):
                        if int(num[i])==c[i]:
                            bulls=bulls+1
                        if int(num[i]) in c:
                            dummy=dummy+1
                    cows=dummy-bulls
                    print("BUlls:",bulls,"COWS:",cows)
                    score=score-1
    elif ch==2:
        fp=open("score.txt","r")
        content=fp.read()
        print(content)
        if(content==""):
            print("No records to display")
    elif ch==3:
        print("\t\t\t******INSTRUCTIONS******\n\n")
        print('''\t\tThis is a simple number guessing game

               User has to guess the 2(Easy)/3(Medium)/4(Hard) digit number that is generated
               
               by the system in lowest possible attempts
               
               after every attempt user will be given a clue
               
               by printing no.of cows and no.of bulls
               
               cows indicate that digit is present in the
               
               two/three/four digit number but not in correct position
               
               where as bulls indicate that digit is present in
               
               two/three/four digit number in correct position

               Enter -1 instead of number to exit at any point of game.\n\n''')
        
    elif(ch==4):
        print("Thank You, Come again")
        break
    if(ch!=2 and ch!=3):
        if(mp!=1):
            print("You Won")
            print("Name : ",name)
            print("level : ",n1)
            print("Score: ",score)
            print("\n")
        else:
            print("You lose")
            print("Name : ",name)
            print("level : ",n1)
            print("Score: 0")
            print("\n")
        fp.write("Name : %s" % name)
        fp.write("\n")
        fp.write("level: %d"%n1)
        fp.write("\n")
        fp.write("Score : %d" % score)
        fp.write("\n")
        fp.close()
    restart=input("Do you want to play again(Y/N)")
    if restart=='y' or restart=='Y':
        choice=choice+1
    else:
        print('Thank You, Come Again\n')
        choice=0
