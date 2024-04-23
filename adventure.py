class Room:
    def __init__(self, name, desc, exits, items=None):
        self.name = name
        self.desc = desc
        self.exits = exits
        self.items = items if items else []

    def __str__(self):
        exits_str = ', '.join(self.exits.keys())
        items_str = ', '.join(self.items) if self.items else "None"
        return f"{self.name}\n\n{self.desc}\n\nItems: {items_str}\n\nExists: {exits_str}\n"
    

class Player:
    def __init__(self):
        self.current_room = None
        self.inventory = []

    def go(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print(f"You go {direction}.")
            print()
            return True
        else:
            print("There's no way in that direction.")
            return False

    def look(self):
        print(self.current_room)
        return str(self.current_room)

    def get(self, item):
        if item in self.current_room.items:
            self.current_room.items.remove(item)
            self.inventory.append(item)
            print(f"You pick up the {item}.")
        else:
            print(f"There's no {item} here.")

    def show_inventory(self):
        if not self.inventory:
            print("You're not carrying anything.")
        else:
            print("You're carrying:")
            for item in self.inventory:
                print(item)

# Define rooms
room1 = Room("A white room", "You are in a simple room with white walls.", {}, items = ["key"])
room2 = Room("A blue room", "This room is simple, too, but with blue walls.", {}, [])
room3 = Room("A green room", "You are in a simple room, with bright green walls.", {}, items = ["banana", "bandana", "bellows", "deck of cards"])
room4 = Room("A red room", "This room is fancy. It's red!", {}, items = ["rose"])

# Connect each room
room1.exits = {"north": room2, "east": room4}
room2.exits = {"east": room3, "south": room1}
room3.exits = {"south": room4, "west": room2}
room4.exits = {"west": room1, "north": room3}

# Initialize Player
player = Player()
player.current_room = room1
print(player.current_room)
while True:
    action = input("What would you like to do?").strip().lower().split()
    if not action:
        continue
    verb = action[0]
    if verb == "go":
        if len(action) < 2:
            print("Sorry, you need to go somewhere.")
            continue
        direction = action[1]
        if player.go(direction):
            player.look()
    elif verb == "look":
        player.look()
    elif verb == "get":
        item = action[1]
        player.get(item)
    elif verb == "inventory":
        player.show_inventory()
    elif verb == "quit":
        print("Goodbye!")
        break
    else:
        print("I don't understand that command.")

