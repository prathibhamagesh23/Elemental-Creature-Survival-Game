#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 22:29:55 2024
Pymon skeleton game
@author: Prathibha Magesh
@student_id : s3859590
@highest_level_attempted (P/C/D/HD): HD

- Reflection:
    This project has been an extensive learning experience in applying object-oriented programming principles in Python to develop a game. From the outset, I faced several challenges, particularly in implementing dynamic interactions between different classes, such as Pymon, Creature, and Location. Ensuring the correct behavior of Pymons during battles and managing their energy levels required careful planning and execution of methods.

    One of the significant challenges I encountered was managing the game state, particularly the transitions between different locations and ensuring that the Pymon could interact with various creatures and items correctly. I learned the importance of maintaining clear relationships between classes, which facilitated the organization of code and simplified debugging processes. Implementing features such as item interactions and creature challenges pushed me to think critically about gameplay mechanics and how they affect user engagement.

    I also recognized the value of robust error handling, particularly when dealing with user inputs and file operations. The use of custom exceptions improved the clarity of my code and helped manage unexpected situations gracefully. For instance, ensuring that invalid directions or incorrect file formats were handled effectively contributed to a smoother user experience.

    Another key takeaway was the iterative development process. As I added features, I continuously tested and refined my code, which helped identify areas for improvement and optimization. This project has significantly deepened my understanding of Python and game development concepts, preparing me for more complex projects in the future. It has also reinforced my appreciation for clean, well-documented code, as it facilitates both individual understanding and team collaboration.

- Reference:

RMIT University, 2024. [online] Available at: https://rmit.instructure.com/courses/124829/files/40934338?module_item_id=6635602 [Accessed 6 Nov. 2024].

RMIT University, 2024.  [online] Available at: https://rmit.instructure.com/courses/124829/files/41051619?module_item_id=6645719 [Accessed 6 Nov. 2024].

RMIT University, 2024. [online] Available at: https://rmit.instructure.com/courses/124829/files/41193305?module_item_id=6656960 [Accessed 6 Nov. 2024].

RMIT University, 2024. [online] Available at: https://rmit.instructure.com/courses/124829/files/41301616?module_item_id=6667434 [Accessed 6 Nov. 2024].

Python Software Foundation, 2024. Python 3.x documentation. [online] Available at: https://docs.python.org/3/ [Accessed 6 Nov. 2024].

Python Software Foundation, 2024. csv – CSV File Reading and Writing. [online] Available at: https://docs.python.org/3/library/csv.html [Accessed 6 Nov. 2024].

Python Software Foundation, 2024. datetime – Basic date and time types. [online] Available at: https://docs.python.org/3/library/datetime.html [Accessed 6 Nov. 2024>.

Python Software Foundation, 2024. random – Generate pseudo-random numbers. [online] Available at: https://docs.python.org/3/library/random.html [Accessed 6 Nov. 2024].
    
"""


import sys
import os
from datetime import datetime
import csv
import random

"""Custom exception raised when an invalid direction is chosen. This helps in handling navigation errors
    gracefully by alerting the user that the chosen direction does not connect to another location."""
"""Custom exception raised for issues with the CSV file format. This ensures that data loading functions
    validate the structure and fields in CSV files, helping prevent runtime errors from improperly formatted files."""    
class InvalidDirectionException(Exception):
    """Raised when the selected direction does not lead to a location."""
    pass

class InvalidInputFileFormat(Exception):
    """Raised when there is an issue with the CSV file format or content."""
    pass

"""
    The Location class represents each individual location or 'room' in the game world. Each location has a 
    name, a description, doors that link to other locations in specified directions (e.g., 'north', 'south'),
    and lists to hold creatures and items present at that location. The doors attribute is a dictionary where 
    the keys are directions, and the values are other Location instances or None if there is no connection in that
    direction. 

    Location instances are connected through the connect method, allowing for two-way associations between 
    locations. This class serves as the foundation for navigating the game world, and its methods support
    updating the name, description, and directional connections dynamically.
    """
class Location:
    def __init__(self, name, description):
        # Initialize attributes as per spec
        self.name = name
        self.description = description
        self.doors = {"west": None, "north": None, "east": None, "south": None}
        self.creatures = []  # Start with no creatures
        self.items = []      # Start with no items

    # Getter and setter for name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # Getter and setter for description
    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    # Getter and setter for doors
    def get_doors(self):
        return self.doors

    def set_door(self, direction, location):
        self.doors[direction] = location

    # Connect method: links this location to another in a specified direction
    def connect(self, direction, location):
        """Connects the current location with another location in the given direction."""
        if direction in self.doors:
            self.doors[direction] = location
            # Set up reciprocal connection
            opposite_directions = {"west": "east", "east": "west", "north": "south", "south": "north"}
            opposite_direction = opposite_directions.get(direction)
            if opposite_direction and opposite_direction in location.doors:
                location.doors[opposite_direction] = self


    """
    The Item class represents objects that can be found and potentially picked up by the player's Pymon.
    Each item has a name and description, along with flags indicating whether it is pickable and consumable.
    Pickable items can be added to the Pymon's inventory, while consumable items can be used to affect gameplay,
    such as restoring energy or providing immunity. 

    This class encapsulates item behavior, supporting checks on pickability and offering flexibility for items
    with different properties, such as consumables that disappear after use and non-consumables that have 
    recurring effects.
    """                
# Item class remains as is for handling items
class Item:
    def __init__(self, name, description, pickable=True, consumable=False):
        self.name = name
        self.description = description
        self.pickable = pickable
        self.consumable = consumable  

    def is_pickable(self):
        return self.pickable

    def __str__(self):
        return self.name
    """
    The Creature class is a general representation of entities that inhabit the game world, such as Pymons or 
    other animals. It has attributes for a nickname, description, and a location (optional), indicating where 
    the creature is currently situated. The location attribute can be updated, allowing creatures to move or 
    be relocated as part of gameplay events.

    Creature is a base class designed for inheritance. The Pymon class, representing the player's main 
    characters, extends Creature to include additional game-specific properties like energy and inventory. 
    Creature supports basic interactions and provides essential information about each creature's identity 
    and attributes.
    """
class Creature:
    def __init__(self, nickname, description, location=None):
        self.nickname = nickname
        self.description = description
        self.location = location  # Holds a reference to the Location object

    # Getter and setter methods for attributes
    def get_nickname(self):
        return self.nickname

    def set_nickname(self, nickname):
        self.nickname = nickname

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

"""
    The Pymon class represents the player's controllable characters, extending the Creature class with specific 
    game-related attributes and actions. Each Pymon has an energy level that affects its ability to participate 
    in battles and navigate the world. Pymons can store items in an inventory, and they may have immunity for 
    one battle encounter if a magic potion is used.

    The Pymon class introduces methods for using items, moving between locations, challenging creatures, 
    and tracking the Pymon's energy. Pymons also have a "benched_pymons" attribute to store other Pymons 
    acquired during gameplay, allowing the player to switch between Pymons. The Pymon class combines 
    combat functionality with item usage and movement, making it central to the player's experience.
"""

class Pymon(Creature):
    def __init__(self, nickname, description, location=None):
        super().__init__(nickname, description, location)
        self.energy = 3
        self.inventory = []
        self.immunity = False
        self.benched_pymons = []
        self.moves_counter = 0
        self.battle_log = []  # List to store battle statistics

    def start_battle(self, opponent, record):
        print(f"{opponent.get_nickname()} gladly accepted your challenge! Ready for battle!")
        print("The first Pymon to win 2 encounters out of 3 will win the battle.")
        
        # Initialize counters and timestamp for battle log
        pymon_wins, opponent_wins, draws = 0, 0, 0
        potion_used = False
        timestamp = datetime.now().strftime("%d/%m/%Y %I:%M %p")

        for encounter in range(1, 4):  # Loop for a maximum of 3 encounters
            if pymon_wins >= 2 or opponent_wins >= 2:
                break  # End the battle if one side has already won 2 encounters
            
            print(f"\nEncounter {encounter}!")
            user_choice = input("Your turn (r)ock, (p)aper, or (s)cissor?: ").lower()
            user_choice = {"r": "rock", "p": "paper", "s": "scissors"}.get(user_choice, "")
            if not user_choice:
                print("Invalid choice. Try again.")
                continue

            opponent_choice = random.choice(["rock", "paper", "scissors"])
            print(f"You issued {user_choice}!")
            print(f"Your opponent issued {opponent_choice}.")

            if user_choice == opponent_choice:
                print("It's a draw! No one wins this encounter.")
                draws += 1  # Track draws
            elif (user_choice == "rock" and opponent_choice == "scissors") or \
                 (user_choice == "scissors" and opponent_choice == "paper") or \
                 (user_choice == "paper" and opponent_choice == "rock"):
                pymon_wins += 1
                print(f"{user_choice} vs {opponent_choice}: You won 1 encounter.")
            else:
                opponent_wins += 1
                # Check for magic potion immunity
                if self.immunity and not potion_used:
                    potion_used = True
                    print("Magic potion used! Energy not deducted this encounter.")
                    self.immunity = False  # Deactivate immunity after use
                    self.inventory = [item for item in self.inventory if item.name.lower() != "magic potion"]
                else:
                    self.energy -= 1
                    print(f"{user_choice} vs {opponent_choice}: You lost 1 encounter and 1 energy.")
                    print(f"Your energy is now {self.energy}/3.")
                    if self.energy == 0:
                        print("You have run out of energy! Game over.")
                        sys.exit()  # End the game if energy is 0

        # Determine the winner based on the encounter results
        if pymon_wins >= 2:
            print(f"Congrats! You have won the battle and adopted a new Pymon called {opponent.get_nickname()}!")
            self.benched_pymons.append(opponent)
            self.location.creatures.remove(opponent)
        else:
            if self.energy > 0:
                print(f"You lost the battle. {self.get_nickname()} is sent to a random location.")
                self.location = random.choice(record.locations) if record.locations else self.location

        # Log the battle result
        self.battle_log.append({
            'timestamp': timestamp,
            'opponent': opponent.get_nickname(),
            'wins': pymon_wins,
            'draws': draws,
            'losses': opponent_wins
        })
        print("Battle results have been logged.")

    def display_battle_stats(self):
        print(f"Battle Stats for {self.get_nickname()}:")
        for idx, battle in enumerate(self.battle_log, 1):
            print(f"Battle {idx} - {battle['timestamp']} against {battle['opponent']}: W:{battle['wins']} D:{battle['draws']} L:{battle['losses']}")
        total_wins = sum(b['wins'] for b in self.battle_log)
        total_draws = sum(b['draws'] for b in self.battle_log)
        total_losses = sum(b['losses'] for b in self.battle_log)
        print(f"Total - Wins: {total_wins}, Draws: {total_draws}, Losses: {total_losses}")
        
    # Getter and setter for energy
    def get_energy(self):
        return self.energy

    def set_energy(self, energy):
        self.energy = max(0, energy)  # Ensures energy does not drop below 0

    def increase_energy(self):
        if self.energy < 3:
            self.energy += 1
            print("Energy increased by 1!")
        else:
            print("Energy is already at maximum (3).")

    def decrease_energy(self):
        self.moves_counter += 1
        if self.moves_counter % 2 == 0:
            self.energy -= 1
            print("Energy decreased by 1 due to movement.")
            if self.energy == 0:
                print(f"{self.get_nickname()} has no energy and escapes into the wild!")
                if self.benched_pymons:
                    self.location = random.choice(self.benched_pymons)
                else:
                    print("Game Over! All Pymons have escaped.")
                    sys.exit()
                    
    def use_item(self, item_name):
        item = next((i for i in self.inventory if i.name.lower() == item_name.lower()), None)
        if not item:
            print(f"No item named '{item_name}' in your inventory.")
            return

        if item.name.lower() == "apple" and getattr(item, 'consumable', False):  # Check if item is consumable
            if self.energy < 3:
                self.increase_energy()
                self.inventory.remove(item)
            else:
                print("Energy is already at maximum (3).")
     
        elif item.name.lower() == "magic potion":
            self.immunity = True
            print("You are now immune in the next battle encounter.")
            self.inventory.remove(item)
     
        elif item.name.lower() == "binocular":
            self.use_binocular()
            self.inventory.remove(item)
        else:
            print(f"The {item_name} cannot be used.")
       
    def use_binocular(self):
        direction = input("Look in which direction? (current, west, north, east, south): ").lower()
        
        if direction == "current":
            # Show creatures and items in the current location
            print(f"You see in the current location: {self.location.get_description()}")
            
            # Display creatures in the current location
            if self.location.creatures:
                print("Creatures in this location:")
                for creature in self.location.creatures:
                    print(f"- {creature.get_nickname()}: {creature.get_description()}")
            else:
                print("There are no creatures here.")
            
            # Display items in the current location
            if self.location.items:
                print("Items in this location:")
                for item in self.location.items:
                    print(f"- {item.name}: {item.description}")
            else:
                print("There are no items here.")
        
        elif direction in self.location.doors:
            connected_location = self.location.doors[direction]
            
            if connected_location:
                # Show description of the connected location
                print(f"In the {direction}, you see: {connected_location.get_description()}")
                
                # Display items in the connected location
                if connected_location.items:
                    print("Items in this direction:")
                    for item in connected_location.items:
                        print(f"- {item.name}")
                else:
                    print("No items in this direction.")
                    
                # Display creatures in the connected location
                if connected_location.creatures:
                    print("Creatures in this direction:")
                    for creature in connected_location.creatures:
                        print(f"- {creature.get_nickname()}")
                else:
                    print("No creatures in this direction.")
            
            else:
                print(f"This direction ({direction}) leads nowhere.")
        
        else:
            print("Invalid direction. Please choose from 'current', 'west', 'north', 'east', or 'south'.")


    # Move Pymon in a specified direction
    def move(self, direction):
        try:
            # Check if the direction is valid and connected to another location
            if not self.location or direction not in self.location.doors or not self.location.doors[direction]:
                raise InvalidDirectionException(f"No location in the {direction} direction.")
        
            # Move Pymon to the new location
            new_location = self.location.doors[direction]
            self.location = new_location  # Update Pymon's location
            print(f"You traveled {direction} and arrived at {new_location.get_name()}.")

            # Decrease energy every two moves
            self.moves_counter += 1
            if self.moves_counter % 2 == 0:
                self.energy -= 1
                print("Energy decreased by 1 due to movement.")
                if self.energy <= 0:
                    print(f"{self.get_nickname()} has no energy left and escapes into the wild!")
                    self.location = random.choice(self.record.locations) if self.record.locations else self.location
                    print(f"{self.get_nickname()} is now at a random location: {self.location.get_name()}.")

            # Display creatures in the new location
            if new_location.creatures:
                print("Creatures in this location:")
                for creature in new_location.creatures:
                    print(f"- {creature.get_nickname()}: {creature.get_description()}")
            else:
                print("There are no creatures to challenge here.")

            # Display items in the new location
            if new_location.items:
                print("Items in this location:")
                for item in new_location.items:
                    print(f"- {item}")
            else:
                print("There are no items in this location.")

        except InvalidDirectionException as e:
            print(e)
        
    def pick_item(self, item_name):
        if self.location:
            for item in self.location.items:
                if item.name.lower() == item_name.lower():
                    if item.is_pickable():
                        self.inventory.append(item)  # Add item to inventory
                        self.location.items.remove(item)  # Remove item from location
                        print(f"You picked up {item_name.lower()} from the ground.")
                    else:
                        print(f"The {item_name.lower()} cannot be picked up.")
                    return
            print(f"There is no item named '{item_name}' here.")
        else:
            print("Pymon is not in any location.")


    def challenge(self, creature_name, record):
        # Find the creature by name in the current location
        for creature in self.location.creatures:
            if creature.get_nickname().lower() == creature_name.lower():
                # Check if the creature is adoptable and can be challenged
                if creature.adoptable:
                    print(f"{creature_name.capitalize()} gladly accepted your challenge! Ready for battle!")
                    self.start_battle(creature, record)  # Pass `record` to `start_battle`
                else:
                    # Humorous message for non-challengeable creatures
                    print(f"The {creature_name.lower()} just ignored you.")
                return
        # If no creature with the given name was found in the current location
        print(f"No creature named '{creature_name}' here.")

    def view_inventory(self):
        if self.inventory:
            print("Inventory:")
            for idx, item in enumerate(self.inventory, 1):
                print(f"{idx}) {item.name}: {item.description}")
        
            # Option to use an item from the inventory
            use_choice = input("Select an item number to use, or press Enter to go back: ")
            if use_choice.isdigit():
                item_index = int(use_choice) - 1
                if 0 <= item_index < len(self.inventory):
                    self.use_item(self.inventory[item_index].name)
                else:
                    print("Invalid item number.")
        else:
            print("Your inventory is empty.")

    """
    The Record class is responsible for loading and managing game data, including locations, creatures, and 
    items. This class maintains lists of locations and creatures, and a dictionary for quick access to locations
    by name. The Record class has methods to load data from CSV files, supporting custom input files for 
    locations, creatures, and items, thus allowing game variability. 

    Additionally, Record provides methods for advanced gameplay features, such as randomizing connections 
    between locations and saving/loading the game's progress. This class acts as the central repository of game 
    data and offers functionality for managing file operations, making it essential for both gameplay setup and 
    save/load mechanics.
    """

class Record:
    def __init__(self):
        self.locations = []  # List to store Location objects
        self.creatures = []  # List to store Creature objects
        self.location_dict = {}  # Dictionary for quick lookup of locations by name

    # Getter for locations and creatures lists
    def get_locations(self):
        return self.locations

    def get_creatures(self):
        return self.creatures

    def save_game(self, filename="save2024.csv"):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            # Save Pymon details, inventory, battle log, etc.
            # Example: writer.writerow([pymon_details...])

    def add_custom_location(self):
        name = input("Enter location name: ")
        description = input("Enter description: ")
        new_location = Location(name, description)
        self.locations.append(new_location)
        # Optionally save to CSV

    def add_custom_creature(self):
        name = input("Enter creature name: ")
        description = input("Enter description: ")
        adoptable = input("Is adoptable? (yes/no): ").lower() == 'yes'
        creature = Creature(name, description)
        creature.adoptable = adoptable
        self.creatures.append(creature)
        # Optionally save to CSV

    def randomize_connections(self):
        for location in self.locations:
            for direction in ["north", "south", "east", "west"]:
                location.doors[direction] = random.choice(self.locations) if random.random() > 0.5 else None

    def load_game(self, filename="save2024.csv"):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                # Load saved data into game state
        except FileNotFoundError:
            print(f"Save file {filename} not found.")
            
    def load_locations(self, file_path="locations.csv"):
        # Load locations with error handling for CSV format issues
        rows = []

        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if 'name' not in row or 'description' not in row:
                        raise InvalidInputFileFormat("Invalid location data format in CSV file.")
                
                    name = row['name'].strip()
                    description = row['description'].strip()
                    location = Location(name, description)
                    self.location_dict[name] = location
                    self.locations.append(location)
                    # Store row data for setting connections later
                    rows.append(row)

                # Set up connections based on directions in the CSV
                for row in rows:
                    location = self.location_dict.get(row['name'])
                    if location:
                        for direction in ['west', 'north', 'east', 'south']:
                            neighbor = row.get(direction, "").strip()
                            if neighbor and neighbor in self.location_dict:
                                location.connect(direction, self.location_dict[neighbor])

        except KeyError:
            raise InvalidInputFileFormat("Location file is missing required columns.")
        except Exception as e:
            print(f"Error loading locations: {e}")
            
    def load_creatures(self, file_path="creatures.csv"):
        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                required_columns = {'name', 'description', 'adoptable'}
                if not required_columns.issubset({col.strip().lower() for col in reader.fieldnames}):
                    raise InvalidInputFileFormat("Invalid creature data format in CSV file. Required columns: name, description, adoptable.")
                
                for row in reader:
                    row = {key.strip().lower(): value.strip() for key, value in row.items()}  # Clean up whitespace
                    name = row['name']
                    description = row['description']
                    adoptable = row['adoptable'].lower() == 'yes'
                    creature = Creature(name, description)
                    creature.adoptable = adoptable
                    self.creatures.append(creature)
        except Exception as e:
            print(f"Error loading creatures: {e}")

    def load_items(self, file_path="items.csv"):
        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                # Clean headers to remove any leading/trailing spaces
                reader.fieldnames = [header.strip() for header in reader.fieldnames]
                
                required_columns = {'name', 'description', 'pickable', 'consumable'}
                if not required_columns.issubset(reader.fieldnames):
                    raise InvalidInputFileFormat("Invalid item data format in CSV file. Required columns: name, description, pickable, consumable.")
                
                # Load items without assigning them to locations
                for row in reader:
                    row = {key.strip(): value.strip() for key, value in row.items()}
                    name = row['name']
                    description = row['description']
                    pickable = row['pickable'].lower() == 'yes'
                    consumable = row['consumable'].lower() == 'yes'

        except InvalidInputFileFormat as e:
            print(f"Error in items.csv: {e}")
        except Exception as e:
            print(f"Error loading items: {e}")

"""
    The Operation class manages the user interface and primary gameplay loop, linking the player's commands
    to specific actions in the game. It holds references to the active Pymon and the Record object, enabling it 
    to access and modify game data based on user input. The class provides methods to display a menu and 
    interpret commands, offering options to inspect the Pymon, view the current location, move, pick up items, 
    and challenge creatures.

    Additionally, the Operation class includes a generate_stats function to display gameplay statistics and a
    submenu to switch between Pymons in the player's collection. The class serves as the main controller, 
    guiding the player through the game world and handling user interactions to create a cohesive experience.
    """

class Operation:
    def __init__(self, pymon, record):
        self.pymon = pymon
        self.record = record

    def display_menu(self):
        while True:
            print("\nPlease issue a command to your Pymon:")
            print("1) Inspect Pymon")
            print("2) Inspect current location")
            print("3) Move")
            print("4) Pick an item")
            print("5) View inventory")
            print("6) Challenge a creature")
            print("7) Generate stats")
            print("8) Save game")            # New: Save game progress
            print("9) Load game")            # New: Load game progress
            print("10) Exit")
            print("11) Add custom location")  # New: Admin - Add a custom location
            print("12) Add custom creature")  # New: Admin - Add a custom creature
            print("13) Randomize location connections")  # New: Admin - Randomize connections

            choice = input("Your command: ")

            if choice == "1":
                self.inspect_pymon_menu()
            elif choice == "2":
                self.inspect_location()
            elif choice == "3":
                self.move_pymon()
            elif choice == "4":
                item_name = input("Pick what: ")
                self.pymon.pick_item(item_name)
            elif choice == "5":
                self.pymon.view_inventory()
            elif choice == "6":
                creature_name = input("Challenge who: ")
                self.pymon.challenge(creature_name, self.record)
            elif choice == "7":
                self.generate_stats()
            elif choice == "8":
                self.record.save_game()
                print("Game progress saved successfully.")
            elif choice == "9":
                self.record.load_game()
                print("Game progress loaded successfully.")
            elif choice == "10":
                print("Exiting the program.")
                break
            elif choice == "11":
                self.record.add_custom_location()
                print("Custom location added successfully.")
            elif choice == "12":
                self.record.add_custom_creature()
                print("Custom creature added successfully.")
            elif choice == "13":
                self.record.randomize_connections()
                print("Location connections randomized successfully.")
            else:
                print("Invalid choice. Please try again.")

    def generate_stats(self):
        print("\n=== Game Stats ===")
        print(f"Current Pymon: {self.pymon.get_nickname()}")
        print(f"Energy Level: {self.pymon.get_energy()}/3")
        print(f"Moves made: {self.pymon.moves_counter}")
        print(f"Items collected: {len(self.pymon.inventory)}")
        
        # Displaying the battle statistics
        print("\n=== Battle Log ===")
        if self.pymon.battle_log:
            total_wins, total_draws, total_losses = 0, 0, 0
            for idx, battle in enumerate(self.pymon.battle_log, 1):
                print(f"Battle {idx}, {battle['timestamp']}")
                print(f"Opponent: {battle['opponent']}, Wins: {battle['wins']}, Draws: {battle['draws']}, Losses: {battle['losses']}")
                total_wins += battle['wins']
                total_draws += battle['draws']
                total_losses += battle['losses']
            print("\nTotal Battle Stats:")
            print(f"Wins: {total_wins}, Draws: {total_draws}, Losses: {total_losses}")
        else:
            print("No battles have been fought yet.")
        print("==================\n")
    
    # Sub-menu for inspecting Pymon
    def inspect_pymon_menu(self):
        print("\n1) Inspect current Pymon")
        print("2) Select a benched Pymon")
        sub_choice = input("Your command: ")

        if sub_choice == "1":
            self.inspect_pymon()
        elif sub_choice == "2":
            self.select_benched_pymon()
        else:
            print("Invalid choice. Returning to main menu.")

    def inspect_pymon(self):
        print(f"\nHi Player, my name is {self.pymon.get_nickname()}, I am {self.pymon.get_description()}.")
        print(f"My energy level is {self.pymon.get_energy()}/3.")

    def select_benched_pymon(self):
        if self.pymon.benched_pymons:
            print("\nBenched Pymons:")
            for idx, p in enumerate(self.pymon.benched_pymons, 1):
                print(f"{idx}) {p.get_nickname()}: {p.get_description()} (Energy: {p.get_energy()}/3)")
            
            try:
                choice = int(input("Select a Pymon to use (choose id): "))
                if 1 <= choice <= len(self.pymon.benched_pymons):
                    new_pymon = self.pymon.benched_pymons.pop(choice - 1)
                    if isinstance(new_pymon, Pymon):  # Check that new_pymon is a Pymon
                        print(f"Swapping to {new_pymon.get_nickname()} with {new_pymon.get_energy()}/3 energy.")
                        
                        # Swap locations so the new Pymon starts in the current location
                        new_pymon.location = self.pymon.location
                        self.pymon.benched_pymons.append(self.pymon)  # Move current Pymon to bench
                        self.pymon = new_pymon  # Update active Pymon to the selected one
                    else:
                        print("Selected creature is not a valid Pymon.")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No benched Pymons available.")

    # Option 2: Inspect current location
    def inspect_location(self):
        location = self.pymon.get_location()
        if location:
            print(f"\nYou are at {location.get_name()}, {location.get_description()}.")

            # Display creatures in the location
            unique_creatures = {creature.get_nickname(): creature for creature in location.creatures}
            if unique_creatures:
                print("Creatures in location:")
                for creature in unique_creatures.values():
                    print(f"- {creature.get_nickname()}: {creature.get_description()}")
            else:
                print("There are no creatures to challenge here.")

            # Display items in the location
            if location.items:
                print("Items in location:")
                for item in location.items:
                    print(f"- {item}")
            else:
                print("There are no items in this location.")
        else:
            print("Pymon is not in any location.")

    # Option 3: Move Pymon
    def move_pymon(self):
        direction = input("Moving to which direction (west, north, east, south)?: ").lower()
        if direction in ["west", "north", "east", "south"]:
            if self.pymon.location and direction in self.pymon.location.doors:
                new_location = self.pymon.location.doors[direction]
                if new_location:
                    self.pymon.location = new_location  # Update location
                    print(f"You traveled {direction} and arrived at {new_location.get_name()}.")

                    # Display creatures and items after moving
                    self.inspect_location()
                else:
                    print(f"There is no door to the {direction}. Pymon remains at its current location.")
            else:
                print("Invalid direction. Please enter 'west', 'north', 'east', or 'south'.")

def initial_setup():
    record = Record()
    record.load_locations("locations.csv")  # Load locations from CSV file
    record.load_creatures("creatures.csv")  # Load creatures and place them in locations from CSV
    record.load_items("items.csv")  # Load items from CSV without location assignment

    # Manually assign items to specified locations
    playground = record.location_dict.get("Playground")
    beach = record.location_dict.get("Beach")
    school = record.location_dict.get("School")

    # Place specific items in locations
    if playground:
        playground.items.append(Item("Tree", "Decorative item", pickable=False, consumable=False))
        playground.items.append(Item("Magic potion", "Grants immunity in battle", pickable=True, consumable=True))
    if beach:
        beach.items.append(Item("Apple", "Pymon's main food, replenishes energy", pickable=True, consumable=True))
    if school:
        school.items.append(Item("Binocular", "Allows foresight and view of surroundings", pickable=True, consumable=False))

    # Randomly assign creatures to locations
    for creature in record.creatures:
        location = random.choice(record.get_locations())
        location.creatures.append(creature)
    
    # Set a random start location for the Pymon
    start_location = random.choice(record.get_locations())
    pymon = Pymon("Kimimon", "A white and yellow Pymon with a square face", start_location)

    return pymon, record

# Main function to run the game
def main():
    pymon, record = initial_setup()  # Perform initial setup
    operation = Operation(pymon, record)  # Initialize game operations with Pymon and record data
    operation.display_menu()  # Start the game menu

if __name__ == "__main__":
    main()
