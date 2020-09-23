# Bowling Application for 2-4 players


def display_frames(f):
    """Converts list of frames (stored as lists) into printable format"""
    # Print | character for start of line
    print(" |", end = '')

    # Iterate through frames
    for frame in f:
        # Find number of rolls in frame
        rolls = len(frame)

        # If first roll is not a strike
        if frame[0] != 10:
            print(str(frame[0]), end = ' ') # first roll

            # If second roll is a spare
            if (frame[0] + frame[1]) == 10:
                print("\\", end = '') # Possibly last score, no space, space added for start of 3rd roll

                # If spare is in 10th frame
                if rolls == 3:
                    print(" " + str(frame[2]), end = '') # Last score, no space

            # If second roll is not a spare
            else:
                print(str(frame[1]), end = '') # Last score, no space

        # If first roll is a strike
        elif frame[0] == 10:
            print("X", end = ' ') # first roll

            # If strike in 10th frame
            if rolls == 3:

                # If second roll is a strike
                if frame[1] == 10:
                    print("X", end = ' ') # second roll

                    # If third roll is a strike
                    if frame[2] == 10:
                        print("X", end = '') # Last score, no space

                    # If third roll is not a strike
                    else:
                        print(str(frame[2]), end = '') # Last score, no space

                # If second roll is not a strike
                else:
                    print(" " + str(frame[1]), end = ' ') # Second roll

                    # If third roll creates a spare
                    if (frame[1] + frame[2]) == 10:
                        print("\\", end = '') # Last score, no space

                    # If third roll does not create a spare
                    else:
                        print(str(frame[2]), end = '') # Last score, no space
            else:
                print(" ", end = '') # Space added if only strike to keep frames even
        print("|", end = '') # | Character added for end of frame
    print("") # newline for end of frames


if __name__ == '__main__':
    players = [] # List of players
    num_players = 0 # Null value to enter while loop
    while num_players < 2 or num_players > 4:
        temp_players = input("How many players are there? (only 2-4 allowed): ") # Set a temp variable for testing valid input
        if not temp_players.isdigit(): # Determine if value entered is a number
            print("Please enter an integer value.") # Return message stating error to user
        else:
            num_players = int(temp_players) # Set num_players to temp value
            if num_players < 2 or num_players > 4: # Input is not valid number
                print("Number of players must be 2-4") # Return message stating error to user

    # Collect Player Names
    temp_name = input("\nWhat is the first player's name?: ")
    players.append({"name": temp_name, "score": 0, "frames": [], "strike": 0, "strike_list": [], "spare": 0})
    temp_name = input("What is the second player's name?: ")
    players.append({"name": temp_name, "score": 0, "frames": [], "strike": 0, "strike_list": [], "spare": 0})
    if num_players >= 3:
        temp_name = input("What is the third player's name?: ")
        players.append({"name": temp_name, "score": 0, "frames": [], "strike": 0, "strike_list": [], "spare": 0})
        if num_players == 4:
            temp_name = input("What is the fourth player's name?: ")
            players.append({"name": temp_name, "score": 0, "frames": [], "strike": 0, "strike_list": [], "spare": 0})

    # Instructions
    print("\nFor each roll enter number of pins hit down.")
    
    # Gameplay
    for frame in range(1, 11): # 10 frames
        for p in players:
            score_list = [] # Collect frame scores to append to frame
            for roll in range(1, 4): # 3 rolls
                if roll==3 and frame != 10: # Can only have 3 rolls if it is the 10th frame
                    continue
                else:
                    # Display current Frame
                    print("\nPlayer " + p["name"] + " (Frame " + str(frame) + ", Roll", str(roll) + ")")

                    # Collect Number of Pins
                    num_pins = -1 # Invalid input to enter while loop
                    while num_pins < 0 or num_pins > 10:
                        temp_pins = input("How many pins were knocked down?: ") # Collect number of pins and store as temp variable
            
                        if not temp_pins.isdigit(): # Determine if value entered is a number
                            print("Please enter an integer value between 0 and 10.") # Return message stating error to user
                            
                        else:
                            num_pins = int(temp_pins) # Set num_pins to temp value
                            
                            # Number is too big or small
                            if num_pins < 0 or num_pins > 10:
                                print("Number of pins must be 0-10") # Return message stating error to user

                            # Number exceeds 10 pins possible
                            elif frame != 10 and roll == 2 and num_pins > (10 - score_list[0]):
                                print("Combined number of pins for roll 1 and 2 exceeds 10. Please reenter value: ")
                                num_pins = -1

                            # Frame 10 Conditions
                            elif frame == 10 and roll == 2:
                                
                                # Number exceeds 10 pins possible
                                if score_list[0] != 10 and num_pins > (10 - score_list[0]):
                                    print("Combined number of pins for roll 1 and 2 exceeds 10. Please reenter value: ")
                                    num_pins = -1
                                    
                            elif frame == 10 and roll == 3:

                                # Number exceeds 10 pins possible for rolls 2 and 3
                                if score_list[0] == 10 and score_list[1] != 10 and num_pins > (10 - score_list[1]): # Input is not a valid number
                                    print("Combined number of pins for roll 2 and 3 exceeds 10. Please reenter value: ")
                                    num_pins = -1
                                    
            
                    # Valid Score Entered
                    score_list.append(num_pins)
                    
                    if frame != 10: # Add pins to score
                        p["score"] += num_pins
                        
                    if frame == 10: # Add pins to score except for strikes and spares
                        if roll == 1:
                            p["score"] += num_pins
                        elif roll == 2:
                            if score_list[0] != 10:
                                p["score"] += num_pins

                    # Check if Old Spare
                    if roll == 1 and p["spare"] == 1: # Can only have 1 spare at a time
                        p["score"] += num_pins # Add bonus roll to score
                        p["spare"] = 0 # Reset spare value
                        print(str(num_pins) + " added to score for spare")

                    # Check if Old Strike still needs rolls
                    if p["strike"] > 0:
                        strike_num = 1
                        for s in p["strike_list"]:
                            if len(s) == 2:
                                continue
                            else:
                                s.append(num_pins)
                                p["score"] += num_pins
                                print(str(num_pins) + " added to score for strike number " + str(strike_num))
                                strike_num +=1
                    
                    # Check for New Strike
                    if roll == 1 and num_pins == 10:
                        p["strike"] += 1
                        p["strike_list"].append([])
                        print("You got a strike!")
                        if frame != 10:
                            break;
                    
                    # Check for New Spare
                    elif roll == 2 and score_list[0] != 10 and (num_pins + score_list[0]) == 10:
                        p["spare"] = 1
                        print("You got a spare!")
                        if frame != 10:
                            break;

                    # If Frame 10 without Spare or Strike, skip 3rd roll
                    if frame == 10 and roll == 2 and (score_list[0] + score_list[1]) < 10:
                        break;
                    
            p["frames"].append(score_list)
            print("\n" + p["name"] + "'s total score is: " + str(p["score"]))

    print("\nFinal Scores:")
    for p in players:
        print("\n" + p["name"] + ": " + str(p["score"]))
        display_frames(p["frames"])
            
