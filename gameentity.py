"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame
from random import randint
from cat import Cat

from globalvars import *
from spritesheet import SpriteSheet, key_image

class GameEntity(pygame.sprite.Sprite,Cat):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0
    
    playerWidth = 40
    playerHeight = 32
    
    updatetime = 0 #used for updating ai control

    # This holds all the images for the animated walk left/right
    # of our player
    

    # What direction is the player facing?
    direction = "R"
    
    
    

    # List of sprites we can bump against
    level = None
    
    baseSpeed = 3 #cat speed constants
    runningSpeed = 6
    jumpBoost = 3 #x axis boost while jumping
    jumpPower = 5 #y axis boost while jumping
    
    

    # -- Methods
    def __init__(self,age,rank,pelt,isAI = True,AIGroup = None, PlayerGroup = None):
        """ Constructor function """
        pygame.sprite.Sprite.__init__(self)
        Cat.__init__(self,age,rank)
        self.isAI = isAI
        self.fur = pelt
        self.walking_frames_l = []
        self.walking_frames_r = []
        self.running_frames_l = []
        self.running_frames_r = []
        self.idle_frames_l = []
        self.idle_frames_r = []
        self.sit_frames_l = []
        self.sit_frames_r = []
        self.Display = None
        self.nameFont = pygame.font.SysFont('Comic Sans MS',12)
        self.running = False
        self.jumping = False
        self.isAI = True
        
       
    def PlayerSetup(self):
        key_image("Images/cat.png",(70,220,70,255),filename = self.SayName() + '.png') #change fur color to any color(please don't make it white)
    def AISetup(self):
        key_image("Images/cat.png",self.fur,filename = self.SayName() + '.png') #change fur color to any color(please don't make it white)
    def CreateSprite(self):
         #call player or AI specific setup functions
        
        if self.isAI == True:
            self.AISetup()
        else:
            self.PlayerSetup()
        
        #create spritesheet
        sprite_sheet = SpriteSheet("Images/Cats/" + self.SayName() + ".png",True,WHITE)
        
        # Load all the left facing walk cycle images, them flip them.
        image = sprite_sheet.get_image(2, 33, self.playerWidth, self.playerHeight)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(48, 33, self.playerWidth, self.playerHeight)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(90, 33, self.playerWidth, self.playerHeight)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(135, 33, self.playerWidth, self.playerHeight)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(175, 33, self.playerWidth, self.playerHeight)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(220, 33, self.playerWidth, self.playerHeight)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_r.append(image)

        # Load all the left facing images for walk cycle.
        image = sprite_sheet.get_image(2, 33, self.playerWidth, self.playerHeight)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(48, 33, self.playerWidth, self.playerHeight)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(90, 33, self.playerWidth, self.playerHeight)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(135, 33, self.playerWidth, self.playerHeight)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(175, 33, self.playerWidth, self.playerHeight)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(220, 33, self.playerWidth, self.playerHeight)
        self.walking_frames_l.append(image)
        
        #load left facing running cycle images (looks better in reverse order)
        image = sprite_sheet.get_image(233,68, self.playerWidth, self.playerHeight)
        self.running_frames_l.append(image)
        image = sprite_sheet.get_image(185,68, self.playerWidth, self.playerHeight)
        self.running_frames_l.append(image)
        image = sprite_sheet.get_image(139,68, self.playerWidth, self.playerHeight)
        self.running_frames_l.append(image)
        image = sprite_sheet.get_image(96,68, self.playerWidth, self.playerHeight)
        self.running_frames_l.append(image)
        image = sprite_sheet.get_image(48,68, self.playerWidth, self.playerHeight)
        self.running_frames_l.append(image)
        image = sprite_sheet.get_image(3,68, self.playerWidth, self.playerHeight)
        self.running_frames_l.append(image)
        
        #load right facing running cycle by flipping left facing ones(don't load in reverse order)
        image = sprite_sheet.get_image(3,68, self.playerWidth, self.playerHeight)
        image = pygame.transform.flip(image, True, False)
        self.running_frames_r.append(image)
        image = sprite_sheet.get_image(48,68, self.playerWidth, self.playerHeight)
        image = pygame.transform.flip(image, True, False)
        self.running_frames_r.append(image)
        image = sprite_sheet.get_image(96,68, self.playerWidth, self.playerHeight)
        image = pygame.transform.flip(image, True, False)
        self.running_frames_r.append(image)
        image = sprite_sheet.get_image(139,68, self.playerWidth, self.playerHeight)
        image = pygame.transform.flip(image, True, False)
        self.running_frames_r.append(image)
        image = sprite_sheet.get_image(185,68, self.playerWidth, self.playerHeight)
        image = pygame.transform.flip(image, True, False)
        self.running_frames_r.append(image)
        image = sprite_sheet.get_image(233,68, self.playerWidth, self.playerHeight)
        image = pygame.transform.flip(image, True, False)
        self.running_frames_r.append(image)
        
        #load left facing idle frames
        image = sprite_sheet.get_image(0,0,self.playerWidth, self.playerHeight)
        self.idle_frames_l.append(image)
        image = sprite_sheet.get_image(41,0,self.playerWidth, self.playerHeight)
        self.idle_frames_l.append(image)
        
        #load right facing idle frames
        image = sprite_sheet.get_image(0,0,self.playerWidth, self.playerHeight)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_r.append(image)
        image = sprite_sheet.get_image(41,0,self.playerWidth, self.playerHeight)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_r.append(image)
        
        #load left facing sit frames
        image = sprite_sheet.get_image(84,0,self.playerWidth, self.playerHeight)
        self.sit_frames_l.append(image)
        image = sprite_sheet.get_image(125,0,self.playerWidth, self.playerHeight)
        self.sit_frames_l.append(image)
        
        #load right facing sit frames
        image = sprite_sheet.get_image(84,0,self.playerWidth, self.playerHeight)
        image = pygame.transform.flip(image, True, False)
        self.sit_frames_r.append(image)
        image = sprite_sheet.get_image(125,0,self.playerWidth, self.playerHeight)
        image = pygame.transform.flip(image, True, False)
        self.sit_frames_r.append(image)
        
        # Set the image the player starts with
        self.image = self.sit_frames_r[1]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = 340 #this is where the cat is created
        self.rect.y = (SCREEN_HEIGHT - self.rect.height) - 200
        
        self.Display = self.nameFont.render(str(self.name),False,(0,0,0))
    def PutSprite(self,spriteList,entityList):#add sprite to list of sprites to render
        spriteList.add(self)
        entityList.append(self)

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x 
        if self.running == True:
            if self.direction == "L":
                frame = (pos // 30) % len(self.running_frames_r)
                self.image = self.running_frames_r[frame]
            elif self.direction == "R":
                frame = (pos // 30) % len(self.running_frames_l)
                self.image = self.running_frames_l[frame]
            else:
                self.image = self.image
        else:
            if self.direction == "L":
                frame = (pos // 30) % len(self.walking_frames_r)
                self.image = self.walking_frames_r[frame]
            elif self.direction == "R":
                frame = (pos // 30) % len(self.walking_frames_l)
                self.image = self.walking_frames_l[frame]
            else:
                self.image = self.image

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -self.jumpPower
#            if self.direction == "L":
#                if self.running == True:
#                    self.change_x = -(JumpBoost + RunSpeed)
#                else:
#                    self.change_x = -(JumpBoost + BaseSpeed)
#            elif self.direction == "R":
#                if self.running == True:
#                    self.change_x = self.runningSpeed + self.jumpBoost
#                else:
#                    self.change_x = self.baseSpeed + self.jumpBoost
#            else:
#                self.change_x = 0

    # Player-controlled movement:
    def go_right(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -BaseSpeed
        self.direction = "R"
        self.running = False

    def go_left(self):
        """ Called when the user hits the right arrow. """
        self.change_x = BaseSpeed
        self.direction = "L"
        self.running = False
    
    def run_right(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -RunSpeed
        self.direction = "R"
        self.running = True

    def run_left(self):
        """ Called when the user hits the right arrow. """
        self.change_x = RunSpeed
        self.direction = "L"
        self.running = True

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.direction = "S"
        self.running = False
        
    def AIupdate(self):#update an AI entity
        if self.updatetime == 25:
            choice = randint(0,5)
            if choice == 0:
                self.go_right()
                self.running = False
            elif choice == 1:
                self.go_left()
                self.running = False
            elif choice == 2:
                self.jump()
            elif choice == 3:
                self.stop()
                self.running = False
            elif choice == 4:
                self.go_right()
                self.running = True
            elif choice == 5:
                self.go_left()
                self.running = True
            self.updatetime = 0
        else:
            self.updatetime = self.updatetime + 1
    
