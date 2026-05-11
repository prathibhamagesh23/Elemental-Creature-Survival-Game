# Elemental Creature Survival Game

A Python-based object-oriented adventure and survival game developed for the RMIT COSC2531 Programming Fundamentals Final Coding Challenge.

The game combines exploration, creature battles, inventory management, survival mechanics, and dynamic world interactions in a text-based RPG environment.

---

# Project Overview

In this game, players control a creature called a Pymon and explore a world of interconnected locations filled with creatures, items, and challenges.

The main objective is to:
- Explore the map
- Battle and capture creatures
- Manage energy and inventory
- Survive encounters
- Collect items and resources
- Discover and interact with dynamic locations

The game is fully developed using Object-Oriented Programming (OOP) principles in Python.

---

# Core Features

## Exploration System
- Interconnected map-based locations
- Directional movement system
- Dynamic room navigation
- Randomized starting locations

## Creature Battle System
- Rock-paper-scissors battle mechanics
- Turn-based encounters
- Energy-based survival system
- Creature adoption after victories
- Battle statistics and logs

## Inventory System
- Pick up and use items
- Consumable and non-consumable items
- Inventory management
- Item effects and abilities

## Survival Mechanics
- Energy depletion and restoration
- Movement penalties
- Immunity system using magic potions
- Game over conditions

## Advanced Gameplay Features
- Save and load game progress
- Randomized map connections
- Dynamic creature spawning
- Custom location creation
- Custom creature creation
- Battle history tracking

---

# Technologies Used

- Python
- Object-Oriented Programming (OOP)
- CSV File Handling
- Randomization Algorithms
- Exception Handling
- File Management
- Menu-Driven Console Application

---

# Object-Oriented Design

The game was designed using multiple interacting classes:

- Location
- Creature
- Pymon
- Item
- Record
- Operation

The class structure includes:
- Inheritance
- Encapsulation
- Modular design
- Dynamic object interactions

The implemented class relationships and methods are shown in the project class diagram. :contentReference[oaicite:0]{index=0}

---

# Game Features

## Locations
Players can travel between interconnected locations:
- School
- Playground
- Beach
- Additional dynamically loaded locations

Each location may contain:
- Creatures
- Items
- Connected doors
- Environmental descriptions

---

# Items

The game includes interactive items such as:
- Apple
- Magic Potion
- Binocular
- Tree

Items provide gameplay advantages including:
- Energy restoration
- Temporary immunity
- Location foresight
- Exploration support

---

# Battle System

Battles are based on:
- Rock
- Paper
- Scissors

Features include:
- Best-of-three encounters
- Energy deductions
- Creature capture system
- Battle logs with timestamps
- Win/loss statistics

---

# File Structure

```bash
elemental-creature-survival-game/
│
├── pymon_game.py
├── locations.csv
├── creatures.csv
├── items.csv
├── class_diagram.pdf
├── README.md
```

---

# Exception Handling

Custom exceptions implemented:
- InvalidDirectionException
- InvalidInputFileFormat

These improve:
- Input validation
- File validation
- Gameplay reliability
- Error management

---

# Learning Outcomes

This project demonstrates:
- Object-oriented programming
- Software design principles
- Python application development
- Game logic implementation
- File processing
- Exception handling
- Modular architecture
- Interactive console application design

---

# Academic Context

Developed for:
- RMIT University
- COSC2531 Programming Fundamentals

The project required students to design and implement a fully object-oriented game system with dynamic gameplay mechanics, CSV-based data loading, inventory systems, creature battles, and advanced game interactions. :contentReference[oaicite:1]{index=1}

The implementation includes HD-level gameplay features such as save/load systems, randomized connections, battle statistics, inventory mechanics, and custom game content management. :contentReference[oaicite:2]{index=2}

---

# Author

Prathibha Magesh  
Master of Data Science  
RMIT University
