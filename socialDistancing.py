"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import random
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Social Distancing the Game"

# Choose the staring population size
POPULATION = 20
POPULATION_SPEED = 7
BOUNCINESS = 1
CIRCLE_RADIUS = 8
PEOPLE_RADIUS = 30
SPRITE_SCALING_PLAYER = 0.7
SPRITE_SCALING_POWERUP = 0.5
POWERUP_DROP_RATE = 0.5

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
        
        self.player=[SCREEN_WIDTH/2,SCREEN_HEIGHT/2]
        self.people=[]
        self.people_speed = POPULATION_SPEED
        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        self.player_list = arcade.SpriteList()
        self.powerup_list = arcade.SpriteList()
        self.powerup_draw = arcade.SpriteList()
        self.slowdownL = arcade.SpriteList()

        self.slowdown_sprite = arcade.Sprite(os.getcwd()+"/cold-sprite.png", SPRITE_SCALING_POWERUP)
        self.powerup_list.append(self.slowdown_sprite)
        self.slowdownL.append(self.slowdown_sprite)
        

        self.player_sprite = arcade.Sprite(os.getcwd()+"/corona-sprite.png", SPRITE_SCALING_PLAYER)
        self.player_list.append(self.player_sprite)

        # Setting the spawn coordinates for the population and their initial velocities
        for x in range(0,POPULATION):    
            change_x =  1
            change_y = -1 

            # Setting the initial velocity of the population
            delta_x = random.randint(-self.people_speed,self.people_speed)
            if delta_x >= 0:
                delta_y = random.randrange(-1,2,2)*( self.people_speed - delta_x)
            else:
                delta_y = random.randrange(-1,2,2)*( self.people_speed + delta_x)
            
            spawn_coord_x = random.randint(10, SCREEN_WIDTH - 10)
            spawn_coord_y = random.randint(10, SCREEN_HEIGHT - 10)

            # Making sure the population doesnt spawn within the players circle
            while ((SCREEN_WIDTH/2) -5 < spawn_coord_x < (SCREEN_WIDTH/2) +5) and ((SCREEN_HEIGHT/2) -5<spawn_coord_y< (SCREEN_HEIGHT/2) +5):
                spawn_coord_x = random.randint(10, SCREEN_WIDTH - 10)
                spawn_coord_y = random.randint(10, SCREEN_HEIGHT - 10)

            self.people.append([spawn_coord_x, spawn_coord_y, delta_x, delta_y, change_x, change_y, 0])
        pass
    
    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        arcade.draw_circle_outline(self.player[0], self.player[1], PEOPLE_RADIUS, arcade.color.GREEN, 2)
        self.player_sprite.center_x = self.player[0]
        self.player_sprite.center_y = self.player[1]
        self.player_list.draw()
        self.powerup_draw.draw()
        
        for person in self.people:
            if person[6]==1:
                arcade.draw_circle_filled(person[0], person[1], CIRCLE_RADIUS, arcade.color.GREEN)
            else:
                arcade.draw_circle_filled(person[0], person[1], CIRCLE_RADIUS, arcade.color.BLACK)


    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

        for person in self.people:
            # Update the x and y coordinates based on the velocity
            person[0] += person[2]
            person[1] += person[3]

            # If the population hits either of the side edges it bounces back
            if person[0] < CIRCLE_RADIUS and person[2] < 0:
                person[2] *= -BOUNCINESS

            elif person[0] > SCREEN_WIDTH - CIRCLE_RADIUS and person[2] > 0:
                person[2] *= -BOUNCINESS

            # If it hit the edges at the bottom or top
            if person[1] < CIRCLE_RADIUS and person[3] < 0:
                person[3] *= -BOUNCINESS

            elif person[1] > SCREEN_HEIGHT - CIRCLE_RADIUS and person[3] > 0:
                person[3] *= -BOUNCINESS

            # Change Velocity of person by chance
            chance = random.randint(0,100)
            if chance <= 10:
                if person[2] ==  self.people_speed and person[4] == 1:
                    person[4] = person[4] * (-1)

                if person[2] == -self.people_speed and person[4] == -1:
                    person[4] = person[4] * (-1)

                if person[3] ==  self.people_speed and person[5] == 1:
                    person[5] = person[5] * (-1)

                if person[3] == -self.people_speed and person[5] == -1:
                    person[5] = person[5] * (-1)

                person[2] += person[4]
                person[3] += person[5]

            # If a person is within radius of the player the person gets infected
            if (self.player[0] - PEOPLE_RADIUS < person[0] < self.player[0] + PEOPLE_RADIUS) and (self.player[1] - PEOPLE_RADIUS < person[1] < self.player[1] + PEOPLE_RADIUS):
                person[6] = 1
        
        # if there are power ups available spawn them by chance
        if len(self.powerup_list) != 0 :
            drop = random.randint(0,100)
            if drop <= POWERUP_DROP_RATE:
                # choose a random powerup from the list
                powerup = random.randint(0,len(self.powerup_list) - 1)
                self.powerup_list[powerup].center_x = random.randint(10,SCREEN_WIDTH  -10)
                self.powerup_list[powerup].center_y = random.randint(10,SCREEN_HEIGHT -10)
                # remove it from the power up list and add it to the powerup draw list
                self.powerup_draw.append(self.powerup_list.pop(powerup))
        
        if arcade.check_for_collision(self.player_sprite, self.slowdown_sprite):            
            if self.people_speed > 2:
                self.people_speed -= 2

                for person in self.people:
                    
                    # Decrease the x and y velocities
                    person[2] = person[2]/2
                    person[3] = person[3]/2
                    
                    # Decrease the change in x and y velocities
                    person[4] = person[4]/2
                    person[5] = person[5]/2
            
            
               
        pass
        

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """

        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        self.player[0] = x
        self.player[1] = y  

        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()