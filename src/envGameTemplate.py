import time
import pygame
from config import Config
from entity import Entity
from environment import Environment
from graphik import Graphik


# @author Daniel McCoy Stephenson
# @since August 25th, 2022
class EnvGameTemplate:
    def __init__(self):
        pygame.init()
        self.config = Config()
        self.initializeGameDisplay()
        self.graphik = Graphik(self.gameDisplay)
        self.running = True
        self.initialize()
        self.tick = 0

    def initializeGameDisplay(self):
        if self.config.fullscreen:
            self.gameDisplay = pygame.display.set_mode((self.config.displayWidth, self.config.displayHeight), pygame.FULLSCREEN)
        else:
            self.gameDisplay = pygame.display.set_mode((self.config.displayWidth, self.config.displayHeight), pygame.RESIZABLE)

    def initializeLocationWidthAndHeight(self):
        x, y = self.gameDisplay.get_size()
        self.locationWidth = x/self.environment.getGrid().getRows()
        self.locationHeight = y/self.environment.getGrid().getColumns()

    # Draws the environment in its entirety.
    def drawEnvironment(self):
        for location in self.environment.getGrid().getLocations():
            self.drawLocation(location, location.getX() * self.locationWidth, location.getY() * self.locationHeight, self.locationWidth, self.locationHeight)

    # Returns the color that a location should be displayed as.
    def getColorOfLocation(self, location):
        if location == -1:
            color = self.config.white
        else:
            color = self.config.white
            if location.getNumEntities() > 0:
                topEntity = location.getEntities()[-1]
                return topEntity.getColor()
        return color

    # Draws a location at a specified position.
    def drawLocation(self, location, xPos, yPos, width, height):
        color = self.getColorOfLocation(location)
        self.graphik.drawRectangle(xPos, yPos, width, height, color)
    
    def restartApplication(self):
        self.initialize()

    def quitApplication(self):
        pygame.quit()
        quit()
    
    def getLocation(self, entity: Entity):
        locationID = entity.getLocationID()
        grid = self.environment.getGrid()
        return grid.getLocation(locationID)

    def getLocationAndGrid(self, entity: Entity):
        locationID = entity.getLocationID()
        grid = self.environment.getGrid()
        return grid, grid.getLocation(locationID)
    
    def removeEntityFromLocation(self, entity: Entity):
        location = self.getLocation(entity)
        if location.isEntityPresent(entity):
            location.removeEntity(entity)

    def removeEntity(self, entity: Entity):
        self.removeEntityFromLocation(entity)
    
    def handleKeyDownEvent(self, key):
        if key == pygame.K_q:
            self.running = False
        elif key == pygame.K_F11:
            if self.config.fullscreen:
                self.config.fullscreen = False
            else:
                self.config.fullscreen = True
            self.initializeGameDisplay()
        elif key == pygame.K_l:
            if self.config.limitTickSpeed:
                self.config.limitTickSpeed = False
            else:
                self.config.limitTickSpeed = True
        elif key == pygame.K_r:
            self.restartApplication()
            return "restart"
    
    def initialize(self):
        self.tick = 0
        self.environment = Environment("environment", self.config.gridSize)
        self.initializeLocationWidthAndHeight()
        pygame.display.set_caption("EnvGameTemplate - " + str(self.config.gridSize) + "x" + str(self.config.gridSize))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitApplication()
                elif event.type == pygame.KEYDOWN:
                    result = self.handleKeyDownEvent(event.key)
                    if result == "restart":
                        continue
                elif event.type == pygame.WINDOWRESIZED:
                    self.initializeLocationWidthAndHeight()

            self.gameDisplay.fill(self.config.white)
            self.drawEnvironment()
            pygame.display.update()

            if self.config.limitTickSpeed:
                time.sleep(self.config.tickSpeed)
                self.tick += 1
        
        self.quitApplication()

envgametemplate = EnvGameTemplate()
envgametemplate.run()