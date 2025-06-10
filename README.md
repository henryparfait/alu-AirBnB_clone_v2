# Airbnb Clone - Command Interpreter

This repository contains the first part of the Airbnb Clone project - a command interpreter (console) that will be the foundation for all future Airbnb projects.

## Command Interpreter

The command interpreter is a custom shell that allows management of AirBnB objects:
- Create new objects (Users, Places, etc.)
- Retrieve objects
- Update object attributes
- Destroy objects

### How to Start
```bash
./console.py


Usage Examples

Interactive mode:

bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$

Non-interactive mode:

bash
$ echo "help" | ./console.py
(hbnb)
Documented commands...
(hbnb) 
$

Authors

See AUTHORS file for project contributors. 
