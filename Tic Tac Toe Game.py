import sys           # For stoping the executions of a function

B = [0,1,2,3,4,5,6,7,8]          


def p():
    
    print(B[0],B[1],B[2])     # These will prints Board on Screen
    print(B[3],B[4],B[5])
    print(B[6],B[7],B[8])
    print()
    
        
    A1=eval(input("choose an option for player 1: "))   
    B[A1] = "X"
    
    if B[A1] == "X":
         
        
        if B[0] == B[1] == B[2]== "X":  # Winning Condtions for 1st Player
            
            print(B[0],B[1],B[2])  
            print(B[3],B[4],B[5])
            print(B[6],B[7],B[8])          
           
            print("Player 1 is winner")  
            sys.exit()                    #sys.exit will stop the execution       
            
        elif B[3] == B[4] == B[5]== "X":
                      
            print(B[0],B[1],B[2])
            print(B[3],B[4],B[5])
            print(B[6],B[7],B[8])
            print("Player 1 is Winner")
            sys.exit()
            
        elif B[6] == B[7] == B[8]== "X":
                      
            print(B[0],B[1],B[2])
            print(B[3],B[4],B[5])
            print(B[6],B[7],B[8])
            print("Player 1 is Winner")
            sys.exit()
            
        elif B[0] == B[3] == B[6]== "X":
                      
            print(B[0],B[1],B[2])
            print(B[3],B[4],B[5])
            print(B[6],B[7],B[8])
            print("Player 1 is Winner")
            sys.exit()
            
        elif B[1] == B[4] == B[7]== "X":
                      
            print(B[0],B[1],B[2])
            print(B[3],B[4],B[5])
            print(B[6],B[7],B[8])
            print("Player 1 is Winner")
            sys.exit()
            
        elif B[2] == B[5] == B[8]== "X":
                      
            print(B[0],B[1],B[2])
            print(B[3],B[4],B[5])
            print(B[6],B[7],B[8])
            print("Player 1 is Winner")
            sys.exit()
            
        elif B[0] == B[4] == B[8]== "X":
                  
            print(B[0],B[1],B[2])
            print(B[3],B[4],B[5])
            print(B[6],B[7],B[8])
            print("Player 1 is Winner")
            sys.exit()
            
        elif B[2] == B[4] == B[6]== "X":
                  
            print(B[0],B[1],B[2])
            print(B[3],B[4],B[5])
            print(B[6],B[7],B[8])
            print("Player 1 is Winner")
            sys.exit()
    
    
    print(B[0],B[1],B[2])          # These will prints Board on the screen
    print(B[3],B[4],B[5])
    print(B[6],B[7],B[8])    
       
    def p2():
        A2 = eval(input("choose an option for player 2: "))  # Input for 2nd Player
        
        
        if A2==A1 or A1==A2:
            print("Wrong option! Restart Your Game")
            sys.exit()
     
        else:
            B[A2] = "Y"
        
   
        if B[0] == B[1] == B[2]== "Y":    # Winning Conditions for 2nd Player
                      
            print(B[0],B[1],B[2])           
            print(B[3],B[4],B[5])          
            print(B[6],B[7],B[8])
            print("Player 2 is winner")
            sys.exit()
            
        elif B[3] == B[4] == B[5]== "Y":
                      
            print(B[0],B[1],B[2])
            print(B[3],B[4],B[5])
            print(B[6],B[7],B[8])
            print("Player 2 is Winner")
            sys.exit()
            
        elif B[6] == B[7] == B[8]== "Y":
                      
            print(B[0],B[1],B[2])
            print(B[3],B[4],B[5])
            print(B[6],B[7],B[8])
            print("Player 2 is Winner")
            sys.exit()
            
        elif B[0] == B[3] == B[6]== "Y":
                      
            print(B[0],B[1],B[2])
            print(B[3],B[4],B[5])
            print(B[6],B[7],B[8])
            print("Player 2 is Winner")
            sys.exit()
            
        elif B[1] == B[4] == B[7]== "Y":
                      
            print(B[0],B[1],B[2])
            print(B[3],B[4],B[5])
            print(B[6],B[7],B[8])
            print("Player 2 is Winner")
            sys.exit()
            
        elif B[2] == B[5] == B[8]== "Y":
                      
            print(B[0],B[1],B[2])
            print(B[3],B[4],B[5])
            print(B[6],B[7],B[8])
            print("Player 2 is Winner")
            sys.exit()
            
        elif B[0] == B[4] == B[8]== "Y":
                      
            print(B[0],B[1],B[2])
            print(B[3],B[4],B[5])
            print(B[6],B[7],B[8])
            print("Player 2 is Winner")
            sys.exit()
            
        elif B[2] == B[4] == B[6]== "Y":
                      
            print(B[0],B[1],B[2])
            print(B[3],B[4],B[5])
            print(B[6],B[7],B[8])
            print("Player 2 is Winner")
            sys.exit()
      
    p2()
    p()
    

p()    

    

    
    
    
