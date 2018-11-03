import pygame, random

class Ground(pygame.sprite.Sprite):
    '''This class defines the sprite forthe ground.'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes, the x direction and screen of the ground.'''
        # Call the parent __init__() method        
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image and rect attributes for the Ground
        self.image = pygame.image.load ("ground.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.bottom = screen.get_height()
        
        # Instance variables to keep track of the screen surface
        # Set the initial x vector for the Ground
        self.__screen = screen
        self.__dx = -2
    
    def update(self):
        '''This method will be called automatically to reposition the
        ground sprite on the screen.'''
        # Check if the ground have reached the left of the screen
        if self.rect.right < self.__screen.get_width():
            #If so, the ground will reappear at the other side of the screen 
            self.rect.left = 0

class Bird(pygame.sprite.Sprite):
    '''This class defines the sprite for our Bird.'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as a parameter, initializes the image and rect attributes, the y direction and screen of the bird.'''
        # Call the parent __init__() method        
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image and rect attributes for the Bird
        self.image = pygame.image.load("bird still.png")
        self.rect = self.image.get_rect()
        self.rect.left = (screen.get_width()/2) - 34
        self.rect.bottom = (screen.get_height()/2) - 24
        
        # Instance variables to keep track of the screen surface
        # Set the initial y vector for the Bird
        self.__screen = screen
        self.__dy = 0
        
    def go_up (self):
        '''This method increases the y direction of the bird so it moves up.'''
        #Sets y vector to -17
        self.__dy -= 17
        self.rect.top += self.__dy
        
    def go_down (self):
        '''This method decreases the y direction of the bird so it moves down.'''
        #Sets y vector to 5
        self.__dy = 5
        
    def lost (self):
        '''This method checks to see if the bird has hit the ground, if it does, True will be returned.'''
        if self.rect.bottom >= self.__screen.get_height()-112:
            return True
        
    def update (self):
        '''This method will be called automatically to reposition the
        bird sprite on the screen.'''        
        self.rect.top += self.__dy
        #Checks if the bird have reached the top of the screen, if so, the bird will continue traveling straight along the side of the screen
        if  self.rect.top <= 0:
            self.rect.top = 0

class Coin(pygame.sprite.Sprite):
    '''This class defines the sprite for the Coin.'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes, the x direction and the screen of the coin.'''        
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Set the image and rect attributes for the Coin
        self.image = pygame.image.load ("silver coin.png")
        self.rect = self.image.get_rect()
        self.rect.left = screen.get_width()-44
        self.rect.top = random.randrange(0,screen.get_height()-156)
        
        # Instance variables to keep track of the screen surface
        # Set the initial x vector for the Coin
        self.__dx = -3
        self.__screen = screen
        
    def died (self):
        '''This method checks to see if the bird has hit the coin, if it did, the coin will reappear at the right side of the screen.'''
        self.rect.left = self.__screen.get_width()
        self.rect.top = random.randrange(0,self.__screen.get_height()-156)  
        
    def update (self):
        '''This method will be called automatically to reposition the
        coin sprite on the screen.'''
        # Check if the coin have reached the left side of the screen
        # If not, the coin will keep moving
        if self.rect.left >= 0:
            self.rect.left += self.__dx
        # If yes, the coin will be reposition to the right side of the screen
        else:
            self.rect.left = self.__screen.get_width()
            self.rect.top = random.randrange(0,self.__screen.get_height()-156)
            self.rect.left += self.__dx

class ScoreKeeper(pygame.sprite.Sprite):
    '''This class defines the sprite for the Score keeper.'''
    def __init__(self):
        '''This initializer sets the font and player's score of the score keeper.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Load the custom font, and initialize the starting score.
        self.__font = pygame.font.Font("FlappyBird.ttf", 40)
        self.__playerScore = 0
         
    def player_scored(self, point):
        '''This method takes a point parameter and adds the point to the player's score.'''
        #Add the value of the point parameter to the total points
        self.__playerScore += point

     
    def half_way (self):
        '''This method checks to see if the player is halfway through the game.'''
        #Checks to see if the game is half way done
        #If yes, return True
        if self.__playerScore == 50 or self.__playerScore == 51:
            return True
        #If not, return False
        else:
            return False
        
    def winner(self):
        '''This method checks to see if the player have reached 100 points.'''
        #Checks to see if the game is finished
        #If yes, return True        
        if self.__playerScore == 100 or self.__playerScore == 101:
            return True
        #If not, return False
        else:
            return False
 
    def update(self):
        '''This method will be called automatically to refresh the points displayed on the screen.'''
        message = "%d" % (self.__playerScore)
        self.image = self.__font.render(message, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (144, 100)
        
class Pipe(pygame.sprite.Sprite):
    '''This class defines the sprite for the pipe.'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as a parameter, initializes
        the image and rect attributes, the x direction, screen and  the pipe height of the pipe.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        self.__pipe_height = random.randrange(40, screen.get_height()-136)
        
        # Set the image and rect attributes for the Pipe
        self.image = pygame.image.load ("pipe set.png")     
        self.rect = self.image.get_rect()
        self.rect.left = screen.get_width()-36
        self.rect.centery = self.__pipe_height
        
        # Instance variables to keep track of the screen surface    
        # Set the initial x vector for the Pipe
        self.__dx = -2
        self.__screen = screen
            
    def update (self):
        '''This method will be called automatically to reposition the
        pipe sprite on the screen.'''         
        #Check if the pipe have reached the left end of the screen
        # If not, it will keep moving in the same direction and pace
        if self.rect.left >= 0:
            self.rect.left += self.__dx
        #If yes, reposition the pipe to the right side of the screen
        else:
            self.rect.left = self.__screen.get_width()
            self.rect.centery = random.randrange(40, self.__screen.get_height()-136)
            self.rect.left += self.__dx
            
class PointZone(pygame.sprite.Sprite):
    '''This class defines the sprite for the point zone'''
    def __init__(self, screen):
        '''This initializer takes a screen surface as parameters. initializes
        the image and rect attributes, the x direction and screen of the pointzone.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
         
        # The pointzone sprite will be a 1 pixel wide turquoise line.
        self.image = pygame.Surface((1, screen.get_height()))
        self.image = self.image.convert()
        self.image.fill((72, 209, 204))
         
        # Set the rect attributes for the endzone
        self.rect = self.image.get_rect()
        self.rect.left = 270
        self.rect.bottom = screen.get_height()
        
        # Instance variables to keep track of the screen surface
        # Set the initial x vector for the PointZone
        self.__dx = -2
        self.__screen = screen
    
    def update (self):
        '''This method will be called automatically to reposition the pointzone sprite on the screen.'''
        # Check if the pointZone line have reached a certain point
        # If not, the line will keep moving in the same direction and pace
        if self.rect.left >= 143:
            self.rect.left += self.__dx
        #If yes, reposition the line to the right side of the screen and keep moving in the same direction and pace
        else:
            self.rect.left = self.__screen.get_width() + 144
            self.rect.centery = random.randrange(40, self.__screen.get_height()-136)
            self.rect.left += self.__dx