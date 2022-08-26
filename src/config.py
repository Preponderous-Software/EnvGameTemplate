# @author Daniel McCoy Stephenson
# @since August 6th, 2022


# @author Daniel McCoy Stephenson
# @since August 6th, 2022
class Config:
    def __init__(self):
        # display
        self.displayWidth = 500
        self.displayHeight = 500
        self.fullscreen = False
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.textSize = 50

        # grid size
        self.gridSize = 5
        self.randomizeGridSizeUponRestart = True
        self.minGridSize = 5
        self.maxGridSize = 12
        self.increaseGridSizeUponRestart = False # this overrides randomizeGridSizeUponRestart
        self.gridSizeIncreaseAmount = 2

        # tick speed
        self.limitTickSpeed = True
        self.tickSpeed = 0.1

        # misc
        self.debug = False
        self.restartUponCollision = True
        