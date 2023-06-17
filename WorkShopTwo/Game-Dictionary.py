print("Welcome to the Text Adventure Game!")

# Define the rooms in the building using dictionaries
rooms = {
    "kitchen": {
        "description": "You are in the kitchen. It smells like freshly baked cookies.",
        "exits": {
            "living room": "You go to the living room.",
            "dining room": "You go to the dining room."
        }
    },
    "living room": {
        "description": "You are in the living room. It's cozy with a fireplace.",
        "exits": {
            "kitchen": "You go to the kitchen.",
            "bedroom": "You go to the bedroom."
        }
    },
    "dining room": {
        "description": "You are in the dining room. There's a large table set for dinner.",
        "exits": {
            "kitchen": "You go to the kitchen.",
            "garden": "You go to the garden."
        }
    },
    "bedroom": {
        "description": "You are in the bedroom. The bed looks comfortable.",
        "exits": {
            "living room": "You go to the living room.",
            "bathroom": "You go to the bathroom."
        }
    },
    "bathroom": {
        "description": "You are in the bathroom. There's a mirror and a bathtub.",
        "exits": {
            "bedroom": "You go to the bedroom."
        }
    },
    "garden": {
        "description": "You are in the garden. It's filled with colorful flowers.",
        "exits": {
            "dining room": "You go to the dining room."
        }
    }
}

current_room = "kitchen"
game_over = False
    
while not game_over:
    print("\n" + rooms[current_room]["description"])
    print("Exits:", ', '.join(rooms[current_room]["exits"].keys()))
    print("Where do you want to go?")
    next_room = input("> ")
    
    if next_room in rooms[current_room]["exits"]:
        current_room = next_room
    elif next_room =='exit' or next_room=='Exit':
        game_over = True
    else:
        print("Invalid choice. Try again!")
    
    if current_room == "garden":
        print("\nCongratulations! You found the garden. You win!")
        game_over = True


print("\nThank you for playing!")

