from Drawable import Drawable
import pygame
class Rectangle(Drawable):
    def __init__(self, xy, w, h, color):
        super().__init__(x=xy[0], y=xy[1])
        self.__x = xy[0]
        self.__y = xy[1]
        self.__width = w
        self.__height = h
        self.__color = color
    def updatePos(self):
        loc = super().getLoc()
        self.__x = loc[0]
        self.__y = loc[1]
    def draw(self, surface):
        self.updatePos()
        pygame.draw.rect(surface, self.__color, pygame.Rect(self.__x, self.__y, self.__width, self.__height))
class Snowflake(Drawable):
    def __init__(self, xy, color):
        super().__init__(x=xy[0], y=0)
        self.__x = xy[0]
        self.__y = 0
        self.__maxY = xy[1]
        self.__color = (255,255,255)
    def updatePos(self):
        loc = super().getLoc()
        self.__x = loc[0]
        self.__y = loc[1]
    def getMax(self):
        return self.__maxY
    def draw(self, surface):
        self.updatePos()
        pygame.draw.line(surface, self.__color, [self.__x-5, self.__y],[self.__x+5,self.__y], 1)
        pygame.draw.line(surface, self.__color, [self.__x, self.__y-5],[self.__x,self.__y+5], 1)
        pygame.draw.line(surface, self.__color, [self.__x-5, self.__y-5],[self.__x+5,self.__y+5], 1)
        pygame.draw.line(surface, self.__color, [self.__x-5, self.__y+5],[self.__x+5,self.__y-5], 1)