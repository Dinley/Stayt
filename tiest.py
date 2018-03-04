"""What are you doing here? You will see all of my code and spoil all the easter eggs!"""

"""Boo!"""

import pygame
 
# Global constants
done = False

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

bg = pygame.image.load('poiwo_land.jpg')
 
class Player(pygame.sprite.Sprite):
    """
    This class represents the bar at the bottom that the player controls.
    """
    
    # -- Methods
    def __init__(self):
        """ Constructor function """
    
        # Call the parent's constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        #width = 70
        #height = 59
        self.image = pygame.image.load('icecream_player_stand.png')
        #self.image.fill(RED)
 
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None
 
    def update(self):
        """ Move the player. """
        global done
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if block.typeof == 'Kill':
                print('You ded')
                done = True
                
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
            if block.typeof == 'Kill':
                print('You ded')
                done = True
            
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
 
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
            
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .40
 
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
 
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -8
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 8
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
 
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
 
class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.image.load('grass_platform_small.png')
        #self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
        
        self.typeof = 'platform'

class RedPlatform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.image.load('red_platform_small.png')
        #self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
        
        self.typeof = 'redplatform'

class BluePlatform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.image.load('blue_platform_small.png')
        #self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
        
        self.typeof = 'blueplatform'

class YellowPlatform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.image.load('yellow_platform_small.png')
        #self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
        
        self.typeof = 'yellowplatform'

class Wall(pygame.sprite.Sprite):
    """ A wall """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.image.load('grass_wall_small.png')
        #self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
        
        self.typeof = 'wall'

class WallLarge(pygame.sprite.Sprite):
    """ A large wall """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.image.load('grass_wall_large.png')
        #self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
        
        self.typeof = 'walllarge'

class WallLargeKill(pygame.sprite.Sprite):
    """ Large Wall the user can't touch """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.image.load('grass_wall_large.png')
        #self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
        
        self.typeof = 'Kill'

class WallKill(pygame.sprite.Sprite):
    """ Wall the user can't touch """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.image.load('grass_wall_small.png')
        #self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
        
        self.typeof = 'Kill'

class PlatformLarge(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.image.load('grass_platform_large.png')
        #self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
        
        self.typeof = 'Large'

class BlueLarge(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.image.load('blue_platform_large.png')
        #self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
        
        self.typeof = 'BlueLarge'

class RedLarge(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.image.load('red_platform_large.png')
        #self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
        
        self.typeof = 'RedLarge'

class Title(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.image.load('title.png')
        #self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
        
        self.typeof = 'TITLE'

class SexyGorilla(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.image.load('gorrila_pawnch.png')
        #self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
        
        self.typeof = 'easter_egg'
 
class SexyGorillaEasterEgg(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
 
        self.image = pygame.image.load('gorilla_punch_easter_egg.png')
        #self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
        
        self.typeof = 'easter_egg_text'

class Kill(pygame.sprite.Sprite):   
    """ Platform the user CANT jump on """
    
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        
        self.image = pygame.image.load('grass_platform_small.png')
        #self.image.fill(GREEN)
        
        self.rect = self.image.get_rect()
        
        self.typeof = 'Kill'

class BigRedKill(pygame.sprite.Sprite):   
    """ Platform the user CANT jump on """
    
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        
        self.image = pygame.image.load('red_platform_2big5me.png')
        #self.image.fill(GREEN)
        
        self.rect = self.image.get_rect()
        
        self.typeof = 'Kill'

class BigKill(pygame.sprite.Sprite):   
    """ Platform the user CANT jump on """
    
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        
        self.image = pygame.image.load('grass_platform_2big5me.png')
        #self.image.fill(GREEN)
        
        self.rect = self.image.get_rect()
        
        self.typeof = 'Kill'

class BigBlueKill(pygame.sprite.Sprite):   
    """ Platform the user CANT jump on """
    
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        
        self.image = pygame.image.load('blue_platform_2big5me.png')
        #self.image.fill(GREEN)
        
        self.rect = self.image.get_rect()
        
        self.typeof = 'Kill'

class BigYellowKill(pygame.sprite.Sprite):   
    """ Platform the user CANT jump on """
    
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        
        self.image = pygame.image.load('yellow_platform_2big5me.png')
        #self.image.fill(GREEN)
        
        self.rect = self.image.get_rect()
        
        self.typeof = 'Kill'

class RedKill(pygame.sprite.Sprite):   
    """ Platform the user CANT jump on """
    
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        
        self.image = pygame.image.load('red_platform_small.png')
        #self.image.fill(GREEN)
        
        self.rect = self.image.get_rect()
        
        self.typeof = 'Kill'

class BlueKill(pygame.sprite.Sprite):   
    """ Platform the user CANT jump on """
    
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        
        self.image = pygame.image.load('blue_platform_small.png')
        #self.image.fill(GREEN)
        
        self.rect = self.image.get_rect()
        
        self.typeof = 'Kill'

class YellowKill(pygame.sprite.Sprite):   
    """ Platform the user CANT jump on """
    
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this code.
            """
        super().__init__()
        
        self.image = pygame.image.load('yellow_platform_small.png')
        #self.image.fill(GREEN)
        
        self.rect = self.image.get_rect()
        
        self.typeof = 'Kill'
 
class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """
    change_x = 0
    change_y = 0
 
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0
 
    player = None
 
    level = None
    
    typof = 'moving'
 
    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
 
            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
 
        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
 
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
 
 
class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
        self.evil_list = pygame.sprite.Group()
         
        # Background image
        self.background = None
     
        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        #screen.fill(BLUE)
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
 
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything:
        """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
 
# Create platforms for the level
class Level_01(Level):
    """ Definition for Title Level. """
 
    def __init__(self, player):
        """ Create Title Level. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.level_limit = -50
 
        # Title coordinates
        level = [[210, 70, 400, 200],
                 #[210, 70, 800, 400],
                 #[210, 70, 1000, 500],
                 #[210, 70, 1120, 280],
                 ]
 
        # Title
        for platform in level:
            block = Title(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

 
# Create platforms for the level
class Level_02(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.level_limit = -1720

        # Harambe coordinates
        level = [[210, 70, -1000, 200],
                 #[210, 70, 800, 400],
                 #[210, 70, 1000, 500],
                 #[210, 70, 1120, 280],
                 ]
 
        # Harambe
        for platform in level:
            block = SexyGorilla(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Harambe text coordinates
        level = [[210, 70, -1000, 0],
                 #[210, 70, 800, 400],
                 #[210, 70, 1000, 500],
                 #[210, 70, 1120, 280],
                 ]
 
        # Harambe text
        for platform in level:
            block = SexyGorillaEasterEgg(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
 
        # Platform coordinates (first two numbers not necessary)
        level = [[210, 70, 700, 450],
                 #[210, 70, 900, 400],
                 #[210, 70, 1100, 350],
                 #[210, 70, 900, 100],
                 ]
 
        # Platform
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Red Platform coordinates (first two numbers not necessary)
        level = [[210, 70, 900, 400],
                 #[210, 70, 900, 400],
                 #[210, 70, 1100, 350],
                 #[210, 70, 900, 100],
                 ]
 
        # Red Platform
        for platform in level:
            block = RedPlatform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Blue Platform coordinates (first two numbers not necessary)
        level = [[210, 70, 1100, 350],
                 #[210, 70, 900, 400],
                 #[210, 70, 1100, 350],
                 #[210, 70, 900, 100],
                 ]
 
        # Blue Platform
        for platform in level:
            block = BluePlatform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Yellow Platform coordinates (first two numbers not necessary)
        level = [[210, 70, 2180, 120],
                 [210, 70, 2360, 120],
                 [210, 70, 2530, 120],
                 #[210, 70, 900, 100],
                 ]
 
        # Yellow Platform
        for platform in level:
            block = YellowPlatform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Wall coordinates (first two numbers not necessary)
        level = [[210, 70, 1310, 400],
                 [210, 70, 2150, 120],
                 #[210, 70, 1000, 500],
                 #[210, 70, 1120, 280],
                 ]
 
        # Wall
        for platform in level:
            block = Wall(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Large Wall coordinates (first two numbers not necessary)
        level = [[210, 70, 2150, 320],
                 #[210, 70, 800, 400],
                 #[210, 70, 1000, 500],
                 #[210, 70, 1120, 280],
                 ]
 
        # Wall Large
        for platform in level:
            block = WallLarge(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
 
        # Add a custom moving platform
        block = MovingPlatform(70, 40)
        block.rect.x = 1350
        block.rect.y = 350
        block.boundary_left = 1330
        block.boundary_right = 1730
        block.change_x = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        # Add another custom moving platform
        block = MovingPlatform(70, 40)
        block.rect.x = 1930
        block.rect.y = 200
        block.boundary_top = 120
        block.boundary_bottom = 320
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        #Large platform coordinates (first two numbers not necessary)
        level = [[210, 70, 400, 500],
                #[210, 70, 400, 400],
                #[210, 70, 500, 500],
                #[210, 70, 600, 600],
                ]
        
        #Large Platform
        for platform in level:
            block = PlatformLarge(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
        
        #Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 1330, 585],
                #[210, 70, 1530, 585],
                #[210, 70, 1730, 585],
                [210, 70, 1930, 585],
                ]
        
        #Kill 
        for platform in level:
            block = Kill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
            
        #Red Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 1530, 585],
                #[210, 70, 1530, 585],
                #[210, 70, 1730, 585],
                #[210, 70, 1930, 585],
                ]
        
        #Red Kill 
        for platform in level:
            block = RedKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        #Blue Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 1730, 585],
                #[210, 70, 1530, 585],
                #[210, 70, 1730, 585],
                #[210, 70, 1930, 585],
                ]
        
        #Blue Kill 
        for platform in level:
            block = BlueKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)   
 
 
# Create platforms for the level
class Level_03(Level):
    """ Definition for level 2. """
 
    def __init__(self, player):
        """ Create level 2. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.level_limit = -3800
 
        # Large Platform coordinates (first two numbers not nessecary)
        level = [[210, 70, 500, 550],
                 #[210, 70, 800, 400],
                 #[210, 70, 1000, 500],
                 #[210, 70, 1120, 280],
                 ]
 
        # Platform Large
        for platform in level:
            block = PlatformLarge(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Large red coordinates (first two numbers not nessecary)
        level = [[210, 70, 1850, 350],
                 #[210, 70, 800, 400],
                 #[210, 70, 1000, 500],
                 #[210, 70, 1120, 280],
                 ]
 
        # Red Large
        for platform in level:
            block = RedLarge(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Large blue coordinates (first two numbers not nessecary)
        level = [[210, 70, 3080, 50],
                 #[210, 70, 800, 400],
                 #[210, 70, 1000, 500],
                 #[210, 70, 1120, 280],
                 ]
 
        # Blue Large
        for platform in level:
            block = BlueLarge(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        #Blue Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 2500, 585],
                [210, 70, 2900, 585],
                [210, 70, 2100, 585],
                [210, 70, 3300, 585],
                ]
        
        #Blue Kill 
        for platform in level:
            block = BlueKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        #Red Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 2700, 585],
                [210, 70, 2300, 585],
                [210, 70, 3100, 585],
                [210, 70, 3500, 585],
                ]
        
        #Red Kill 
        for platform in level:
            block = RedKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        #Blue Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 3700, 585],
                [210, 70, 4100, 585],
                [210, 70, 4500, 585],
                [210, 70, 4900, 585],
                ]
        
        #Blue Kill 
        for platform in level:
            block = BlueKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        #Red Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 3900, 585],
                [210, 70, 4300, 585],
                [210, 70, 4700, 585],
                [210, 70, 5100, 585],
                ]
        
        #Red Kill 
        for platform in level:
            block = RedKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 1250
        block.rect.y = 410
        block.boundary_left = 1020
        block.boundary_right = 1400
        block.change_x = -4
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add another custom moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 2150
        block.rect.y = 200
        block.boundary_top = 100
        block.boundary_bottom = 300
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Yellow Platform coordinates (first two numbers not nessecary)
        level = [[210, 70, 2500, 0],
                 [210, 70, 3600, 150],
                 #[210, 70, 1000, 500],
                 #[210, 70, 1120, 280],
                 ]
 
        # Platform Yellow
        for platform in level:
            block = YellowPlatform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Add another one
        block = MovingPlatform(70, 70)
        block.rect.x = 4200
        block.rect.y = 100
        block.boundary_left = 4000
        block.boundary_right = 4800
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

# Create platforms for the level
class Level_04(Level):
    """ Definition for Level 3. """
 
    def __init__(self, player):
        """ Create Level 3. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.level_limit = -4900

        # Main moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 0
        block.rect.y = 500
        block.boundary_left = 0
        block.boundary_right = 8000
        block.change_x = 6
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #Red Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 800, 430],
                [210, 70, 2800, 450],
                [210, 70, 3000, 450],
                [210, 70, 3600, 450],
                ]
        
        #Red Kill 
        for platform in level:
            block = RedKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        #Blue Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 1900, 400],
                [210, 70, 2400, 450],
                [210, 70, 2600, 450],
                [210, 70, 3200, 450],
                ]
        
        #Blue Kill 
        for platform in level:
            block = BlueKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        #Red Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 3800, 450],
                #[210, 70, 2800, 450],
                #[210, 70, 3000, 450],
                #[210, 70, 3600, 585],
                ]
        
        #Red Kill 
        for platform in level:
            block = RedKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        #Blue Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 3400, 450],
                #[210, 70, 2400, 450],
                #[210, 70, 2600, 450],
                #[210, 70, 3200, 585],
                ]
        
        #Blue Kill 
        for platform in level:
            block = BlueKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Yellow Platform coordinates (first two numbers not nessecary)
        level = [[210, 70, 1600, 430],
                 [210, 70, 2150, 390],
                 [210, 70, 3300, 130],
                 [210, 70, 4050, 380],
                 ]
 
        # Platform Yellow
        for platform in level:
            block = YellowPlatform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 2350
        block.rect.y = 300
        block.boundary_top = 150
        block.boundary_bottom = 360
        block.change_y = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Another Moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 3000
        block.rect.y = 140
        block.boundary_left = 2800
        block.boundary_right = 3100
        block.change_x = -3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Yellow Platform coordinates (first two numbers not nessecary)
        level = [[210, 70, 4350, 300],
                 [210, 70, 4700, 220],
                 #[210, 70, 3300, 130],
                 #[210, 70, 4100, 380],
                 ]
 
        # Platform Yellow
        for platform in level:
            block = YellowPlatform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        #Red Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 2550, 190],
                #[210, 70, 1530, 585],
                #[210, 70, 1730, 585],
                #[210, 70, 1930, 585],
                ]
        
        #Red Kill 
        for platform in level:
            block = RedKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Large Kill Wall coordinates (first two numbers not necessary)
        level = [[210, 70, 5000, 180],
                 #[210, 70, 800, 400],
                 #[210, 70, 1000, 500],
                 #[210, 70, 1120, 280],
                 ]
 
        # Wall Large Kill
        for platform in level:
            block = WallLargeKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        #Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 0, 585],
                [210, 70, 200, 585],
                [210, 70, 400, 585],
                [210, 70, 600, 585],
                ]
        
        #Kill 
        for platform in level:
            block = Kill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        #Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 800, 585],
                [210, 70, 1000, 585],
                [210, 70, 1200, 585],
                [210, 70, 1400, 585],
                ]
        
        #Kill 
        for platform in level:
            block = Kill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        #Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 1600, 585],
                [210, 70, 1800, 585],
                [210, 70, 2000, 585],
                [210, 70, 2200, 585],
                ]
        
        #Kill 
        for platform in level:
            block = Kill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        #Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 2400, 585],
                [210, 70, 2600, 585],
                [210, 70, 2800, 585],
                [210, 70, 3000, 585],
                ]
        
        #Kill 
        for platform in level:
            block = Kill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        #Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 3200, 585],
                [210, 70, 3400, 585],
                [210, 70, 3600, 585],
                [210, 70, 3800, 585],
                ]
        
        #Kill 
        for platform in level:
            block = Kill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        #Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 4000, 585],
                [210, 70, 4200, 585],
                [210, 70, 4400, 585],
                [210, 70, 4600, 585],
                ]
        
        #Kill 
        for platform in level:
            block = Kill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        #Kill platform coordinates (first two numbers not necessary)
        level = [[210, 70, 4800, 585],
                [210, 70, 5000, 585],
                #[210, 70, 400, 585],
                #[210, 70, 600, 585],
                ]
        
        #Kill 
        for platform in level:
            block = Kill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

# Create platforms for the level
class Level_05(Level):
    """ Definition for Level 4. """
 
    def __init__(self, player):
        """ Create Level 4. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.level_limit = -3500
 
        # Moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 100
        block.rect.y = 500
        block.boundary_left = 10
        block.boundary_right = 2000
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 200
        block.rect.y = 450
        block.boundary_left = 200
        block.boundary_right = 1900
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 300
        block.rect.y = 400
        block.boundary_left = 300
        block.boundary_right = 1800
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 400
        block.rect.y = 350
        block.boundary_left = 400
        block.boundary_right = 1700
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 500
        block.rect.y = 300
        block.boundary_left = 500
        block.boundary_right = 1600
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 600
        block.rect.y = 250
        block.boundary_left = 600
        block.boundary_right = 1500
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 700
        block.rect.y = 200
        block.boundary_left = 700
        block.boundary_right = 1400
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 800
        block.rect.y = 150
        block.boundary_left = 800
        block.boundary_right = 1300
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 900
        block.rect.y = 100
        block.boundary_left = 900
        block.boundary_right = 1200
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 1000
        block.rect.y = 50
        block.boundary_left = 1000
        block.boundary_right = 1100
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Blue Kill Platform coordinates (first two numbers not necessary)
        level = [[210, 70, 2050, 150],
                 [210, 70, 2250, 150],
                 #[210, 70, 1100, 350],
                 #[210, 70, 900, 100],
                 ]
 
        # Blue Kill Platform
        for platform in level:
            block = BlueKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Red Platform coordinates (first two numbers not necessary)
        level = [[210, 70, 2000, 400],
                 [210, 70, 2200, 400],
                 #[210, 70, 1100, 350],
                 #[210, 70, 900, 100],
                 ]
 
        # Red Platform
        for platform in level:
            block = RedPlatform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Kill Wall coordinates (first two numbers not necessary)
        level = [[210, 70, 2450, 0],
                 #[210, 70, 800, 400],
                 #[210, 70, 1000, 500],
                 #[210, 70, 1120, 280],
                 ]
 
        # Kill Wall
        for platform in level:
            block = WallKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Platform coordinates (first two numbers not necessary)
        level = [[210, 70, 2600, 300],
                 [210, 70, 3000, 200],
                 #[210, 70, 1100, 350],
                 #[210, 70, 900, 100],
                 ]
 
        # Platform
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 3400
        block.rect.y = 100
        block.boundary_top = 100
        block.boundary_bottom = 400
        block.change_y = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 3800
        block.rect.y = 50
        block.boundary_left = 3800
        block.boundary_right = 5000
        block.change_x = 3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Big Platform coordinates (first two numbers not necessary)
        level = [[210, 70, 0, 585],
                 #[210, 70, 3000, 200],
                 #[210, 70, 1100, 350],
                 #[210, 70, 900, 100],
                 ]
 
        # Big Platform
        for platform in level:
            block = BigKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Big Red Platform coordinates (first two numbers not necessary)
        level = [[210, 70, 6000, 585],
                 #[210, 70, 3000, 200],
                 #[210, 70, 1100, 350],
                 #[210, 70, 900, 100],
                 ]
 
        # Big Red Platform
        for platform in level:
            block = BigRedKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Big Blue Platform coordinates (first two numbers not necessary)
        level = [[210, 70, 2000, 585],
                 #[210, 70, 3000, 200],
                 #[210, 70, 1100, 350],
                 #[210, 70, 900, 100],
                 ]
 
        # Big Blue Platform
        for platform in level:
            block = BigBlueKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Big Yellow Platform coordinates (first two numbers not necessary)
        level = [[210, 70, 4000, 585],
                 #[210, 70, 3000, 200],
                 #[210, 70, 1100, 350],
                 #[210, 70, 900, 100],
                 ]
 
        # Big Yellow Platform
        for platform in level:
            block = BigYellowKill(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)



def main():
    """ Main Program """
    global done
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("TIEST")
 
    # Create the player
    player = Player()
 
    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    level_list.append(Level_03(player))
    level_list.append(Level_04(player))
    level_list.append(Level_05(player))
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
 
    # Loop until the user clicks the close button.
    #done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_ESCAPE:
                    print('You hit escape idiot!')
                    done = True
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                    
 
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()
        
        # Kill platforms
        
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)
 
        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            if current_level_no < len(level_list)-1:
                player.rect.x = 120
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
            else:
                # Out of levels. This just exits the program.
                # You'll want to do something better.
                #pygame.image.load('game_over.png')
                done = True
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
 
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