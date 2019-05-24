from Room import Room
class Maze:
    #Inputs: Pointer to start room and exit room
    #Sets current to be start room
    def __init__(self,st=None,ex=None):
        #Room the player starts in
        self.__start_room = st
        #If the player finds this room they win
        self.__exit_room = ex
        #What room is the player currently in
        self.__current = st
    #Return the room the player is in (current)
    def getCurrent(self):
        #Implement Me
        return self.__current
    #The next four all have the same idea
    #See if there is a room in the direction
    #If the direction is None, then it is impossible to go that way
    #in this case return false
    #If the direction is not None, then it is possible to go this way
    #Update current to the new move (move the player)
    #then return true so the main program knows it worked.
    def moveNorth(self):
        if not self.__current.getNorth() is None:
            self.__current = self.__current.getNorth()
            return True
        else:
            return False
        #Implement Me
    def moveSouth(self):
        #Implement Me
        if not self.__current.getSouth() is None:
            self.__current = self.__current.getSouth()
            return True
        else:
            return False
    def moveEast(self):
        if not self.__current.getEast() is None:
            self.__current = self.__current.getEast()
            return True
        else:
            return False
        #Implement Me
    def moveWest(self):
        #Implement Me
        if not self.__current.getWest() is None:
            self.__current = self.__current.getWest()
            return True
        else:
            return False
    #If the current room is the exit,
    #then the player won! return true
    #otherwise return false
    def atExit(self):
        #Implement Me
        if self.__current == self.__exit_room:
            return True
        return False
    #If you get stuck in the maze, you should be able to go
    #back to the start
    #This sets current to be the start_room
    def reset(self):
        self.__current = self.__start_room
        #Implement Me