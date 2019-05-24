from Room import Room
from Maze import Maze

rooms = []
for i in range(0,12):
    rooms.append(Room(''))

rooms[0].setDescription('This is the entrance')
rooms[1].setDescription('This room has a table. Maybe a dining room?')
rooms[2].setDescription('Smash Mouth\'s "All Star" is playing faintly.')
rooms[3].setDescription('This one has a floor rug.')
rooms[4].setDescription('Oh god there\'s blood everywhere.')
rooms[5].setDescription('Is that a body?')
rooms[6].setDescription('There is a Mariachi Band. Their instruments are out of tune.')
rooms[7].setDescription('Oooh! Free food on the table!')
rooms[8].setDescription('The walls here are painted orange.')
rooms[9].setDescription('This is the exit.')
rooms[10].setDescription('It smells like apple pie in here.')
rooms[11].setDescription('This room is a dead end.')

rooms[0].setSouth(rooms[1])

rooms[1].setNorth(rooms[0])
rooms[1].setEast(rooms[2])

rooms[2].setNorth(rooms[3])
rooms[2].setSouth(rooms[6])
rooms[2].setWest(rooms[1])

rooms[3].setSouth(rooms[2])
rooms[3].setEast(rooms[4])

rooms[4].setNorth(rooms[5])
rooms[4].setWest(rooms[3])

rooms[5].setSouth(rooms[4])

rooms[6].setNorth(rooms[2])
rooms[6].setEast(rooms[7])

rooms[7].setSouth(rooms[8])
rooms[7].setWest(rooms[6])

rooms[8].setNorth(rooms[7])
rooms[8].setSouth(rooms[10])
rooms[8].setEast(rooms[9])

rooms[9].setWest(rooms[8])

rooms[10].setNorth(rooms[8])
rooms[10].setWest(rooms[11])

rooms[10].setEast(rooms[10])

maze = Maze(st = rooms[0], ex = rooms[9])

print(maze.getCurrent())
inp = input('Move S, or restart\n')
while True:
    n = 'N, '
    s = 'S, '
    w = 'W, '
    e = 'E, '
    if inp.lower() == 's':
        if not maze.moveSouth():
            print('Invalid move.')
    if inp.lower() == 'n':
        if not maze.moveNorth():
            print('Invalid move.')
    if inp.lower() == 'e':
        if not maze.moveEast():
            print('Invalid move.')
    if inp.lower() == 'w':
        if not maze.moveWest():
            print('Invalid move.')
    if inp.lower() == 'restart':
        maze.reset()
    print(maze.getCurrent())
    if maze.atExit():
        break
    if maze.getCurrent().getNorth() is None:
        n = ''
    if maze.getCurrent().getSouth() is None:
        s = ''
    if maze.getCurrent().getEast() is None:
        e = ''
    if maze.getCurrent().getWest() is None:
        w = ''
    inp = input('Move '+n + s + e + w + 'or restart\n')
print('Congratulations!')
    