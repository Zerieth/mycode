#!/usr/bin/python3

item = ''

def showInstructions():
    print('''
    RPG   Game
    ==========
    Commands
        go [direction]
        get [item]
    ''')

def showStatus():
    print('--------------------')
    print(f'You are in the {currentRoom}')
    print(f'Inventory: {inventory}')
    if "item" in rooms[currentRoom]:
        print(f'You see a {rooms[currentRoom]} {item}')
    
    print("-------------------------")


inventory = []

## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall'
                },
            'Dining Room' : {
                  'west' : 'Hall'
             }
          }


currentRoom = 'Hall'

showInstructions()

while True:
    showStatus()

    move = ''
    while move == '':
        move = input('>')

    move == move.lower().split(" ", 1)

    if move[0] == 'go':
        if move[1] in rooms[currentRoom][move[1]]:
            currentRoom = rooms[currentRoom][move[1]]
    else:
        print('you can\'t go that way!')

    if move[0] == 'get' :
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory.append(move[1])
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']
        else:
            print('Can\'t get ' + move[1] + '!')


