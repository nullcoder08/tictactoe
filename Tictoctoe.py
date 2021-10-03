import random
import time
def board(pName,pc,p,ps,cs):
    print("\t\t\t  : ",pName.upper()+"["+ps+"]", "   vs   ",pc+"["+cs+"]" )
    print("\t\t\t (++++++++++++++++++++++++++++++++++++++")
    print("\t\t\t |1          |2           |3           |")
    print("\t\t\t |     "+p[0]+ "     |      "+p[1]+"     |     "+p[2]+"      |")
    print("\t\t\t |           |            |            |")
    print("\t\t\t  _____________________________________")
    print("\t\t\t |4          |5           |6           |")
    print("\t\t\t |     "+p[3]+ "     |      "+p[4]+"     |     "+p[5]+"      |")
    print("\t\t\t |           |            |            |")
    print("\t\t\t  _____________________________________")
    print("\t\t\t |7          |8           |9           |")
    print("\t\t\t |     "+p[6]+ "     |      "+p[7]+"     |     "+p[8]+"      |")
    print("\t\t\t |           |            |            |")
    print("\t\t\t (++++++++++++++++++++++++++++++++++++++")
def winner(p,t):
    if((p[0] == t and p[1] ==t and p[2] == t) or
        (p[3] == t and p[4] == t and p[5] == t) or
        (p[6] == t and p[7] == t and p[8] == t) or
        (p[0] == t and p[3] == t and p[6] == t) or
        (p[1] == t and p[4] == t and p[7] == t) or
        (p[2] == t and p[5] == t and p[8] == t) or
        (p[0] == t and p[4] == t and p[8] == t) or
        (p[2] == t and p[4] == t and p[6] == t)):
        return True
    else:
        return False


if __name__ == '__main__':
    again=1
    print('\n\n\n!!-------------: PlAY  ("_") TIC TAC TOE ("_")  WITH COMPUTER / Friend :-----------!!')
    print("==================================================================================")
    print("---------: MODE :---------\n 1   -    COMPUTER :\n 2   -    FRIEND: ")
    ck = input("Enter Choice : ")
    while (ck != "1" and ck != "2"):
        print("------> Invalid Choice <-----")
        ck = input("Enter Choice : ")
    ck = ord(ck) - 48
    pName = input("Enter Your Name :\t").upper()
    if (ck == 1):
        pc = "COMPUTER"
    else:
        pc = input("Enter Friend's Name : ").upper()
    p = [" ", " ", " ", " ", " ", " ", " ", " ", " "] # [" "]*9
    cnt = 0
    ps = input("Choose Your Symbol  (O , X) : ").upper()
    while (ps != "O" and ps != "X"):
        ps = input("Please choose either 'o' or 'x' :").upper()
    if (ps == "X"):
        cs = "O"
    else:
        cs = "X"

    while(again):
        board(pName, pc, p,ps,cs)
        print("\n\t\t GAME IS LOADING PLEASE WAIT......!!!!!")
        time.sleep(3)
        while (cnt < 9):
            if (cnt % 2 == 0):
                if (ck == 1):
                    choice = random.randint(1, 9)
                else:
                    print(pc, "Turns ", end=" ")
                    choice = input(" Enter Choice :")
                    choice = ord(choice) - 48
                    if (choice > 0 and choice < 10):
                        if (p[choice - 1] == cs or p[choice - 1] == ps):
                            print("------>Invalid Choice<-----")
                            continue
                    else:
                        print("------>Invalid Choice<-----")
                        continue

                if (p[choice - 1] != cs and p[choice - 1] != ps):
                    p[choice - 1] = cs
                    cnt += 1
                    print("\t", pc, "turns processing....Wait please...??")
                    if (ck == 1):
                        time.sleep(1)
                    print("\t", pc, "TURNS :\t DONE: ")
                    board(pName, pc, p, ps, cs)
                    if (winner(p, cs)):
                        print("  !!!---->-->--->opps, Bad Luck -----Better Luck Next Time-------!!!")
                        cnt=0
                        break

            else:
                print(pName, "Turns ", end="")
                choice = input("Enter Choice :")
                choice = ord(choice) - 48
                if (choice > 0 and choice < 10):
                    if (p[choice - 1] == cs or p[choice - 1] == ps):
                        print("------>Invalid Position :<-----")
                    else:
                        p[choice - 1] = ps
                        cnt += 1
                        board(pName, pc, p, ps, cs)
                        if (winner(p, ps)):
                            print("    !!!->-->->-Congrats " + pName + ", YOU WON<--<-<-  !!!-------!!!")
                            break;
                else:
                    print("------>Invalid Choice<-----")
        if (cnt > 8):
            print("   ----->>-->  No-One Wons ,<--<<-------")
        print("Wanna play again: type 'yes': Otherwise click any key ::",end="")
        sk=input().upper()
        if(sk!="YES"):
            again=0
            "==================================================================================")

            print("\t\t\t\t\t---->>>-->>>>--THANKU YOU--<<<<<<<<----------------")
            "==================================================================================")
