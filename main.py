import pygame, sys
from clan import Clan
from Namegen import *
from cat import Cat
from pygame.locals import *
from globalvars import *
from gameentity import GameEntity
import os, shutil


import levels

level_list = []
EveryCat = []
AIcats = []

pygame.init()
pygame.font.init()
nameFont = pygame.font.SysFont('Comic Sans MS',30)

# Set the height and width of the screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Cats are evil")

warriors = 0
WindClan = Clan("WindClan",warriors,EveryCat)
#WindClan.AddCat(kitty,"Apprentice",EveryCat)
#WindClan.SayCats()
#WindClan.ChooseMentor(kitty)
#ThunderClan = Clan("ThunderClan",warriors,EveryCat)
#ThunderClan.SayCats()
#ShadowClan = Clan("ShadowClan",warriors,EveryCat)
#ShadowClan.SayCats()
#RiverClan = Clan("RiverClan",warriors,EveryCat)
#RiverClan.SayCats()
#SkyClan isn't a real clan

# Create the player
player = GameEntity(6,'kit',RandomFur(),isAI = False)
player.Setup()
player.CreateSprite()

#player.Setup()
#print(player.SayName())


#level_list.append(levels.ForestCamp(player))
level_list.append(levels.Level_01(player))
level_list.append(levels.Level_02(player))



active_sprite_list = pygame.sprite.Group()

AI_sprite_list = pygame.sprite.Group()


active_sprite_list.add(player)
I=0
while I < len(EveryCat):
    #print (EveryCat[I].SayRank() + ": " + EveryCat[I].SayName())
    EveryCat[I].PutSprite(AI_sprite_list,AIcats)
    I=I + 1

EveryCat.append(player)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
  
cats = nameFont.render(str(len(EveryCat)),False,(0,0,0))

def getKey(key):
    return pygame.key.get_pressed()[eval("pygame.K_"+key)]

def main():
    """ Main Program """
    # Set the current level(this is in main because python is annoying)
    current_level_no = 1
    current_level = level_list[current_level_no]
    player.level = current_level
    I = 0
    while I < len(AIcats):
            AIcats[I].level = current_level
            I=I + 1
            
    test = pygame.draw.rect(screen,BLACK,pygame.Rect(0,0,10,10)) 

    #Loop until the user clicks the close button.
    done = False
    
    #player control variables
    isRight = False
    isLeft = False
    isUp = False
    isDown = False
    isCtrl = False
    isShift = False

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
            
            #get key values
            if event.type == pygame.KEYDOWN:
                if event.key == KeyRight:
                    isRight = True
                if event.key == KeyLeft:
                    isLeft = True
                if event.key == KeyUp:
                    isUp = True
                if event.key == KeyDown:
                    isDown = True
                if event.key == KeyCtrl:
                    isCtrl = True  
                if event.key == KeyShift:
                    isShift = True
            if event.type == pygame.KEYUP:
                if event.key == KeyRight:
                    isRight = False
                if event.key == KeyLeft:
                    isLeft = False
                if event.key == KeyUp:
                    isUp = False
                if event.key == KeyDown:
                    isDown = False
                if event.key == KeyCtrl:
                    isCtrl = False
                if event.key == KeyShift:
                    isShift = False
        
        #control player
        if not isShift:
            if isRight:
                player.go_right()
            if isLeft:
                player.go_left()
            if isUp:
                player.jump()
        else:
            if isRight:
                player.run_right()
            if isLeft:
                player.run_left()
            if isUp:
                player.jump()

        if (not isRight) and (not isLeft):
            player.stop()

        # Update the player.
        active_sprite_list.update()
        
        # update AI entitys
        AI_sprite_list.update()
        I=0
        while I < len(AIcats):
            AIcats[I].AIupdate()
            I=I + 1

        # Update items in the level
        current_level.update()
        
        


        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        AI_sprite_list.draw(screen)
        
        #display cat names
        I=0
        while I < len(EveryCat):
            screen.blit(EveryCat[I].Display,(EveryCat[I].rect.x,EveryCat[I].rect.y - 10))
            I = I + 1
        screen.blit(cats,(400,0))
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()

#delete all generated cat images
folder = 'Images/Cats'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)


