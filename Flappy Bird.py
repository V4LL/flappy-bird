# Import and Initialize
import pygame, mySprites
pygame.init()
screen = pygame.display.set_mode((288, 512))
 
def main():
    '''This function defines the 'mainline logic' for the Flappy Bird pygame.'''
      
    # Display
    pygame.display.set_caption("Flappy Bird")
     
    # Entities
    background = pygame.image.load("background.png")
    background = background.convert()
    screen.blit(background, (0, 0))
    
    # Sprites for: Pipe, ScoreKeeper, Coin, Bird, Ground, and PointZone
    pipe = mySprites.Pipe(screen)
    scoreKeeper = mySprites.ScoreKeeper()
    coin = mySprites.Coin(screen)
    bird = mySprites.Bird(screen)
    ground = mySprites.Ground(screen)
    pointZone = mySprites.PointZone(screen)
    allSprites = pygame.sprite.OrderedUpdates(pointZone, pipe, ground, coin, bird, scoreKeeper)    
    
    # Load "GameOver" Image to Display After Game Loop Terminates
    gameover = pygame.image.load ("Game Over.png")
    
    # Background Music and Sound Effects
    pygame.mixer.music.load("background music.wav")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    bing = pygame.mixer.Sound ("bing.ogg")
    bing.set_volume(0.6)
    
    died = pygame.mixer.Sound("died.ogg")
    died.set_volume(0.6)
    
    # ACTION
     
    # Assign 
    clock = pygame.time.Clock()
    keepGoing = True
 
    # Loop
    while keepGoing:
     
        # Time
        clock.tick(30)
     
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                # When the space key is pressed, the go_up() method from the bird class is called
                if event.key == pygame.K_SPACE:
                    bird.go_up()
            elif event.type != pygame.KEYDOWN:
                # If no key is pressed, the go_down() method from the bird class is called
                bird.go_down()
                    
        # Check if the coin was hit, if so, 2 points will be added to the score as bonus        
        if bird.rect.colliderect(coin):
            scoreKeeper.player_scored (2)
            coin.died()
        
        # Check if the bird had collided with the pipe
        if bird.rect.colliderect(pipe.rect):
            #Check if the bird has collided with a certain point on the pipe
            for y in range (0, pipe.rect.bottom):
                if bird.rect.collidepoint (pipe.rect.left, y):
                    #If the bird did not collide with any points, continue the game
                    if y in range (pipe.rect.centery - 30, pipe.rect.centery + 50):                 
                        keepGoing = True
                    # If the bird had collided with any of the points, terminate game
                    else:
                        keepGoing = False
        
        # Check if the bird had collided with pointzone
        if bird.rect.colliderect (pointZone.rect):
            #Add one point and plays sound effect
            scoreKeeper.player_scored (1)
            bing.play()
        
        # End game loop when the player hits the ground
        if bird.lost():
            pygame.mixer.music.fadeout(2000)
            keepGoing = False
            
        # Check to see if the player has beat the game, if so end the game loop
        if scoreKeeper.winner():
            pygame.mixer.music.fadeout(2000)
            keepGoing = False
        
        # Check to see if the player is at the half way point of the game, if so, change the background
        if scoreKeeper.half_way():
            background = pygame.image.load("night background.png")
            background = background.convert()
            screen.blit(background, (0, 0))            
        
        # Refresh screen
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
         
        pygame.display.flip()
     
    #Play ending sound effect    
    died.play()
    # Blit gameover message
    screen.blit(gameover, (50, 150))
    pygame.display.flip()
    # Delay to close the game window
    pygame.time.delay(3000)        
    
    # Close the game window
    pygame.quit()    
     
# Call the main function
main()