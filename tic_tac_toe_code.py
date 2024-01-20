import random



def sum(a,b,c):
    return a+b+c
def printboard(xstate,ystate):
    
 one="X" if xstate[1] else ("O" if ystate[1] else 1)
 two="X" if xstate[2] else ("O" if ystate[2] else 2)
 three="X" if xstate[3] else ("O" if ystate[3] else 3)
 four="X" if xstate[4] else ("O" if ystate[4] else 4)
 five="X" if xstate[5] else ("O" if ystate[5] else 5)
 six="X" if xstate[6] else ("O" if ystate[6] else 6)
 seven="X" if xstate[7] else ("O" if ystate[7] else 7)
 eight="X" if xstate[8] else ("O" if ystate[8] else 8)
 nine="X" if xstate[9] else ("O" if ystate[9] else 9)
 
 print(f'{one} | {two} | {three}')
 print("---------")
 print(f'{four} | {five} | {six}')
 print("---------")
 print(f'{seven} | {eight} | {nine}')
 
def checkwinner(xstate,ystate):
    
    wins=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
    for win in wins:
     if sum  ( xstate[win[0]] , xstate[win[1]] , xstate[win[2]]) ==3:
        print("x wins")
        return 1
    
     if sum(ystate[win[0]] , ystate[win[1]] , ystate[win[2]]) ==3:
        print("o wins")
        return 0
     
    return -1
  
xstate=[0,0,0,0,0,0,0,0,0,0]
ystate=[0,0,0,0,0,0,0,0,0,0]
turn=1
value=0
while True:
    printboard(xstate,ystate) 
    
    if(turn==1): 
        
        print("X Enter the no: ")
        
        
        value=int(input())
        xstate[value]=1
        
    else:
        value=value-1
        print("O Enter the no: ")
        value=random.randint(1,9)
        ystate[value]=1
        cwin=checkwinner(xstate,ystate)
        if (cwin != -1):
         break
        
    turn=1-turn
   
    
    
   
    
    
    
        
   