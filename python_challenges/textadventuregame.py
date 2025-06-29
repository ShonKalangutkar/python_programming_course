
rooms = {
    "clearing": {
        "name": "Forest Clearing",
        "description": "You are in a peaceful forest clearing. Sunlight filters through the canopy above. A dense forest lies to the north, and a small, inviting cave entrance is to the east.",
        "exits": {"north": "forestpath", "east": "caveEntrance"},
        "items": ["flower", "smooth stone"]
    },
    "forestpath": {
        "name": "Narrow Forest Path",
        "description": "The path is overgrown with thick bushes and ancient trees. You can hear birds chirping. The clearing is to the south.",
        "exits": {"south": "clearing", "west": "spidercave"},
        "items": []
    },
    "caveEntrance": {
        "name": "Dark Cave Entrance",
        "description": "The air grows cooler and damp here. A faint smell of mildew hangs in the air. You can see deeper into the cave to the east, and the forest clearing is to the west.",
        "exits": {"west": "clearing", "east": "darkcave"},
        "items": ["rusty key"]
    },
    "darkcave": {
        "name": "Deep Dark Cave",
        "description": "It's pitch black in here, and you can barely see your hand in front of your face. You might need a light source to proceed deeper. The cave entrance is to the west.",
        "exits": {"west": "caveEntrance", "north": "treasureroom"}, 
        "items": []
    },
    "treasureroom": {
        "name": "Hidden Treasure Room",
        "description": "You've stumbled into a hidden chamber filled with glistening gold coins, ancient artifacts, and a large, ornate chest. A cool breeze comes from the south, leading back into the dark cave.",
        "exits": {"south": "darkcave"},
        "items": ["golden idol", "ancient scroll"]
    },
    "spidercave": {
        "name": "Spider's Lair",
        "description": "The air is thick with cobwebs, and you can hear the skittering of many legs. Giant spiders lurk in the shadows. This is a very dangerous place. The forest path is to the east.",
        "exits": {"east": "forestpath"},
        "items": ["shiny orb"]
    }
}

curRoom = "clearing" 
inventory = []            
gameover = False         



def displayroom():
    global curRoom 
    rminfo = rooms[curRoom]
    print(f"\n--- {rminfo['name']} ---")
    print(rminfo['description'])

    if rminfo['exits']:
        print("Exits:", ", ".join(rminfo['exits'].keys()))
    else:
        print("There are no visible exits from here.")

    if rminfo['items']:
        print("Items here:", ", ".join(rminfo['items']))
    else:
        print("There are no visible items here.")

def godirection(direction):
    global curRoom 
    rminfo = rooms[curRoom]

    if direction in rminfo['exits']:
        nxtRoom = rminfo['exits'][direction]

        if nxtRoom == "treasureroom" and "rusty key" not in inventory:
            print("The path ahead is blocked by a heavy, ornate door. It seems to require a key.")
            return 
        elif nxtRoom == "darkcave" and "lantern" not in inventory: 
            print("It's too dark to enter this part of the cave without a light source.")
            return 

        curRoom = nxtRoom 
        displayroom() 
    else:
        print(f"You can't go {direction} from here.")

def takeitem(item_name):
    """Attempts to take an item from the current room."""
    global inventory 
    rminfo = rooms[curRoom]

    if item_name in rminfo['items']:
        inventory.append(item_name) 
        rminfo['items'].remove(item_name) 
        print(f"You took the {item_name}.")
    else:
        print(f"I don't see a '{item_name}' here.")

def dropitem(item_name):
    """Attempts to drop an item into the current room."""
    global inventory 
    rminfo = rooms[curRoom]

    if item_name in inventory:
        inventory.remove(item_name) 
        rminfo['items'].append(item_name) 
        print(f"You dropped the {item_name}.")
    else:
        print(f"You don't have a '{item_name}' to drop.")

def showinventory():
    """Displays the player's current inventory."""
    if inventory:
        print("Your inventory:", ", ".join(inventory))
    else:
        print("Your inventory is empty.")


print("Welcome to the Python Text Adventure!")
print("Type 'help' for a list of commands.")
displayroom() 

while not gameover:
    command = input("\nWhat do you do? ").lower().strip()
    commandparts = command.split(" ", 1) 
    action = commandparts[0] 
    target = commandparts[1] if len(commandparts) > 1 else None

    if action == "help":
        print("\n--- Available Commands ---")
        print("go [direction] (e.g., 'go north', 'go east')")
        print("look (or 'look around')")
        print("take [item] (e.g., 'take key')")
        print("drop [item] (e.g., 'drop stone')")
        print("inventory (or 'inv')")
        print("quit (or 'exit')")
        print("--------------------------")
    elif action == "go":
        if target:
            godirection(target)
        else:
            print("Go where? Please specify a direction (e.g., 'go north').")
    elif action == "look" or action == "look around":
        displayroom()
    elif action == "take":
        if target:
            takeitem(target)
        else:
            print("Take what? Please specify an item (e.g., 'take key').")
    elif action == "drop":
        if target:
            dropitem(target)
        else:
            print("Drop what? Please specify an item (e.g., 'drop stone').")
    elif action == "inventory" or action == "inv":
        showinventory()
    elif action == "quit" or action == "exit":
        gameover = True 
        print("Thanks for playing! Goodbye.")
    else:
        print("I don't understand that command. Type 'help' for a list of commands.")

    if curRoom == "treasureroom" and "golden idol" in inventory and not gameover:
        print("\n--- CONGRATULATIONS! ---")
        print("You found the legendary Golden Idol and escaped the dangers of the cave!")
        print("You win!")
        gameover = True 
