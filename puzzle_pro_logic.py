import random
#used random module to initialize a random list (not sorted)


def win_or_not(puz):
    count_move=0
    #created variable with starting value 0, for count the moves of player
   
    new_puz=[1,2,3,4,5,6,7,8,'-']
    #created new_puz list for compairing the new_puz and puz 
    #if the puz list will similar to new_puz then player win
    while True:
        #used the while loop because dont knwo how many moves it takes player to win the game
        
        move=input('left right up down choose-l,f,r,t- ')
        #create move variable for user input or action
        
        ind=puz.index('-')
        #before doing any move firstly store the index of '-' in ind variable
        
        if(move=='l'):       
        #if move is l i.e. left then check below condition
            if(ind==0):
                print('cant go left')
            elif(ind==3):
                print('cant goto left')
            elif(ind==6):
                print('cant goto left')
            #if ind(index of '-' is 0,3,6 then print message that cant goto the leftside)
            else:
                b=puz.index('-')-1
                #store the previous index of '-' in b
                dsh=puz[ind]
                #store the index of '-' in dsh variable
                puz[ind]=puz[b]
                #put previous indexof '-' value to on the '-'
                puz[b]=dsh
                #and vice a verca (interchange the values)
            count_move=count_move+1
            #in every move add-1 to count_move variable
            if(new_puz==puz):
            #if this condition true then print winning message and break the loop for stop the program
                print(f"You win the Puzzle in {count_move} moves")
                break
                
        elif(move=='r'):
            if(ind==2):
                print('cant go right')
            elif(ind==5):
                print('cant goto right')
            elif(ind==8):
                print('cant goto right')
            else:
                b=puz.index('-')+1
                #store the index of next value of '-'
                #same procedure below like above
                dsh=puz[ind]
                puz[ind]=puz[b]
                puz[b]=dsh
                
            count_move=count_move+1
            if(new_puz==puz):
                print(f"You win the Puzzle in {count_move} moves")
                break
        
        elif(move=='u'):
            if(ind==0):
                print('cant go up')
            elif(ind==1):
                print('cant goto up')
            elif(ind==2):
                print('cant goto up')
            else:
                if(ind==3):
                    b=puz[ind]
                    puz[ind]=puz[0]
                    puz[0]=b
                if(ind==4):
                    b=puz[ind]
                    puz[ind]=puz[1]
                    puz[1]=b
                if(ind==5):
                    b=puz[ind]
                    puz[ind]=puz[2]
                    puz[2]=b
                    
                if(ind==6):
                    b=puz[ind]
                    puz[ind]=puz[3]
                    puz[3]=b
                if(ind==7):
                    b=puz[ind]
                    puz[ind]=puz[4]
                    puz[4]=b
                if(ind==8):
                    b=puz[ind]
                    puz[ind]=puz[5]
                    puz[5]=b
            count_move=count_move+1
            if(new_puz==puz):
                print(f"You win the Puzzle in {count_move} moves")
                break
                    
        elif(move=='d'):
            if(ind==6):
                print('cant go down')
            elif(ind==7):
                print('cant goto down')
            elif(ind==8):
                print('cant goto down')
            else:
                if(ind==0):
                    b=puz[ind]
                    puz[ind]=puz[3]
                    puz[3]=b
                if(ind==1):
                    b=puz[ind]
                    puz[ind]=puz[4]
                    puz[4]=b
                if(ind==2):
                    b=puz[ind]
                    puz[ind]=puz[5]
                    puz[5]=b
                    
                if(ind==3):
                    b=puz[ind]
                    puz[ind]=puz[6]
                    puz[6]=b
                if(ind==4):
                    b=puz[ind]
                    puz[ind]=puz[7]
                    puz[7]=b
                if(ind==5):
                    b=puz[ind]
                    puz[ind]=puz[8]
                    puz[8]=b
            count_move=count_move+1
            if(new_puz==puz):
                print(f"You win the Puzzle in {count_move} moves")
                break         


        print(puz[0],puz[1],puz[2])
        print(puz[3],puz[4],puz[5])
        print(puz[6],puz[7],puz[8])
        if(move=='e'):
            break



def game(puz):
    
    while True:
    #used while loop for generate the random until the condition satisfied
        ele=random.randint(0,8)
        #ele(elements) get one random no at time(0 to 8)
        if(ele not in puz):
        #now if ele(number) not in list then add the no else go to loop and generate another
            puz.append(ele)
        
        if(len(puz)==9):
        #if the generated no are 9 means total are 9 then we have to stop the loop
            break
        
    ind=puz.index(0)
    #get the index of 0 from puz list
    
    puz[ind]='-'
    #now we got the index of 0 so change the no 0 to '-' for better understanding while playing game

    print(puz[0],puz[1],puz[2])
    print(puz[3],puz[4],puz[5])
    print(puz[6],puz[7],puz[8])
    #diplay the puzzle list firstly(that has 0-8 no with random index)

    win_or_not(puz)  
    #send the generated list to win_or_not function for checking the winning requirements

puz=[]
#create blank list name puz
game(puz)
#now send blank list to game fuction
