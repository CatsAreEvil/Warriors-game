import pygame, sys
from clan import Clan
from Namegen import *
from cat import Cat
from pygame.locals import *
from globalvars import *
from gameentity import GameEntity


import levels

level_list = []
EveryCat = []
AIcats = []
pygame.init()



# Set the height and width of the screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Cats are evil")



warriors = 10
WindClan = Clan("WindClan",warriors,EveryCat)
#WindClan.AddCat(kitty,"Apprentice",EveryCat)
#WindClan.SayCats()
#WindClan.ChooseMentor(kitty)
ThunderClan = Clan("ThunderClan",warriors * 10,EveryCat)
#ThunderClan.SayCats()
ShadowClan = Clan("ShadowClan",0,EveryCat)#ShadowClan is dead
#ShadowClan.SayCats()
RiverClan = Clan("RiverClan",warriors,EveryCat)
#RiverClan.SayCats()
#SkyClan isn't a real clan

I=0
while I < len(EveryCat):
    #print (EveryCat[I].SayRank() + ": " + EveryCat[I].SayName())
    I=I + 1

# Create the player
player = GameEntity(6,'kit')
#player.Setup()
#print(player.SayName())

bluestar = GameEntity(45,'Leader')
bluestar.NPCSetup("Bluestar",ThunderClan)

tigerclaw = GameEntity(24,'Deputy')
tigerclaw.NPCSetup("Bluestar",ThunderClan)



#level_list.append(levels.ForestCamp(player))
level_list.append(levels.Level_01(player))
level_list.append(levels.Level_02(player))



active_sprite_list = pygame.sprite.Group()
AI_sprite_list = pygame.sprite.Group()


active_sprite_list.add(player)
bluestar.PutSprite(AI_sprite_list,AIcats)
AI_sprite_list.add(tigerclaw)
AIcats.append(tigerclaw)



# Used to manage how fast the screen updates
clock = pygame.time.Clock()
  


def getKey(key):
    return pygame.key.get_pressed()[eval("pygame.K_"+key)]

def main():
    """ Main Program """
    # Set the current level(this is in main because python is annoying)
    current_level_no = 0
    current_level = level_list[current_level_no]
    player.level = current_level
    I = 0
    while I < len(AIcats):
            AIcats[I].level = current_level
            I=I + 1

    #Loop until the user clicks the close button.
    done = False

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    player.running = True
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_LSHIFT:
                    player.running = False

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



