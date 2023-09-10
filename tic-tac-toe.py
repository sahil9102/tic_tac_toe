a={'A':'   |   |   ','B':'   |   |   ','C':'   |   |   '}
b=[['A1','A2','A3'],['B1','B2','B3'],['C1','C2','C3'],['A1','B1','C1'],['A2','B2','C2'],['A3','B3','C3'],['A1','B2','C3'],['A3','B2','C1']]
pla1=[]
pla2=[]
no=0
l2=0
print("------------------ Tic-Tac-Toe ------------------")
print()
print("                   1   2   3 ")
print("                  "+a['A']+"- A")
print("                 "+"-------------")
print("                  "+a['B']+"- B")
print("                 "+"-------------")
print("                  "+a['C']+"- C")
cvg=1
hu=0
while 1!=0:
    for ju in range(hu):
        a={'A':'   |   |   ','B':'   |   |   ','C':'   |   |   '}
        print("                   1   2   3 ")
        print("                  "+a['A']+"- A")
        print("                 "+"-------------")
        print("                  "+a['B']+"- B")
        print("                 "+"-------------")
        print("                  "+a['C']+"- C")
    for ij in range(cvg):
        jkl=1
        while 1!=0:
            player1=input("Enter the position of your move(PLAYER 1) or 'q' to just quit: ")
            if len(player1)==2 and (player1[0]=='A' or player1[0]=='B' or player1[0]=='C') and (player1[1]=='1' or player1[1]=='2' or player1[1]=='3'):
                break
            elif player1=='q':
                print("Player 2 has won the game")
                break
            else:
                print("Inputed value is wrong")
                continue
        if player1=='q':
            break
        if (player1 in pla1) or (player1 in pla2):
            print('Sorry this place is occupied by a player')
            jkl=0
            continue
        rw=player1[0]
        col=player1[1]
        if col=="1":
            fg=1
        if col=="2":
            fg=5
        if col=="3":
            fg=9
        for rt in list(a.keys()):
            if rw==rt:
                a[rw]=a[rw][0:fg]+"$"+a[rw][(fg+1):]
        print("                   1   2   3 ")
        print("                  "+a['A']+"- A")
        print("                 "+"-------------")
        print("                  "+a['B']+"- B")
        print("                 "+"-------------")
        print("                  "+a['C']+"- C")
        no+=1
        pla1.append(player1)
        for i in b:
            l1=0
            for j in i:
                if j in pla1:
                    l1+=1
                if l1==3:
                    print('player 1 has won the game1')
                    break
            if l1==3:
                break
        if l1==3 or no==9:
            break
    if player1=='q':
                break
    if l1==3 or no==9:
        bd=input("Enter 'Y' to restart the match and 'N' to end it here: ")
        jkl=0
        if bd=='Y':
            hu=1
            continue
        elif bd=='N':
            break
    for kl in range(jkl):
        cvg=1
        while 1!=0:
            player2=input("Enter the position of your move(PLAYER 2) or 'q' to just quit: ")
            if len(player2)==2 and (player2[0]=='A' or player2[0]=='B' or player2[0]=='C') and (player2[1]=='1' or player2[1]=='2' or player2[1]=='3'):
                break
            elif player2=='q':
                break
            else:
                print("Inputed value is wrong")
                continue
        if player2=='q':
            print("Player 1 has won the game")
            break
        if (player2 in pla1) or (player2 in pla2):
            print('Sorry this place is occupied by a player')
            cvg=0
            continue
        rw=player2[0]
        col=player2[1]
        if col=="1":
            fg=1
        if col=="2":
            fg=5
        if col=="3":
            fg=9
        for rt in list(a.keys()):
            if rw==rt:
                a[rw]=a[rw][0:fg]+"#"+a[rw][(fg+1):]
        print("                   1   2   3 ")
        print("                  "+a['A']+"- A")
        print("                 "+"-------------")
        print("                  "+a['B']+"- B")
        print("                 "+"-------------")
        print("                  "+a['C']+"- C")
        no+=1
        pla2.append(player2)
        if len(pla2)>2:
            for K in b:
                l2=0
                for L in K:
                    if L in pla2:
                        l2+=1
                    if l2==3:
                        print('player 2 has won the game1')
                        break
                if l2==3:
                    break
            if l2==3:
                break
        if l2==3 or no==9:
            break
    if player2=='q':
        break
    if l1==3 or no==9:
        bd=input("Enter 'Y' to restart the match and 'N' to end it here: ")
        if bd=='Y':
            hu=1
            continue
        elif bd=='N':
            break
