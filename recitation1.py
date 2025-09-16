print("Welcome! You are in room 1.")
print("You can use keys: W, A, S, & D to move.")

currRoom = 1

while currRoom != 5:
    if currRoom == 1:
        location = input("Enter the direction you would like to go: ")
        if location == "D":
            print("Yay! You made it to room 2!")
            currRoom = 2
    elif currRoom == 2:
        location = input("Enter the direction you would like to go: ")
        if location == "A":
            print("You are back in room 1.")
            currRoom = 1
        elif location == "S":
            print("Treasue NOT in room 3. Click W to return to room 2")
            currRoom = 3
        else:
            location == "D"
            print("You are in room 4. Keep going to find the treasure!")
            currRoom = 4
    elif currRoom == 3:
            location = input("Enter the direction you would like to go: ")
            if location == "W":
                print("You are back in room 2.")
                currRoom = 2
            location = input("Enter the direction you would like to go: ")
            if location == "D":
                print("You are in room 4. Keep going to find the treasure!")
                currRoom = 4
    elif currRoom == 4:
        location = input("Enter the direction you would like to go: ")
        if location == "D":
            print("You are back in room 2.")
            currRoom = 2
        else:
            location == "S"
            print("Congrats! You found the treasure. Hooray!!")
            currRoom = 5

    elif currRoom == 5:
        break


        
            
        

