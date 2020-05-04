"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Social Distancing the Game"

# Choose the staring population size
POPULATION = 20
POPULATION_SPEED = 10

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
        
        self.player=[SCREEN_WIDTH,SCREEN_HEIGHT]
        self.people=[]
        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        
        # Setting the spawn coordinates for the population and their initial velocities
        for x in range(0,POPULATION):     
            # Setting the initial velocity of the population
            delta_x = random.randint(-POPULATION_SPEED,POPULATION_SPEED)
            if delta_x >= 0:
                delta_y = random.randrange(-1,2,2)*( POPULATION_SPEED - delta_x)
            else:
                delta_y = random.randrange(-1,2,2)*( POPULATION_SPEED + delta_x)
            
            spawn_coord_x = random.randint(10, SCREEN_WIDTH - 10)
            spawn_coord_y = random.randint(10, SCREEN_HEIGHT - 10)
            # Making sure the population doesnt spawn within the players circle
            while ((SCREEN_WIDTH/2) -5<spawn_coord_x< (SCREEN_WIDTH/2) +5) and ((SCREEN_HEIGHT/2) -5<spawn_coord_y< (SCREEN_HEIGHT/2) +5):
                spawn_coord_x = random.randint(10, SCREEN_WIDTH - 10)
                spawn_coord_y = random.randint(10, SCREEN_HEIGHT - 10)

            self.people.append([spawn_coord_x, spawn_coord_y, delta_x, delta_y])
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        arcade.draw_circle_filled(self.player[0]/2, self.player[1]/2, 8, arcade.color.GREEN)
        arcade.draw_circle_outline(self.player[0]/2, self.player[1]/2, 30, arcade.color.GREEN, 2)
        
        for person in self.people:
            arcade.draw_circle_filled(person[0], person[1], 8, arcade.color.BLACK)

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """

        for person in self.people:
            coord_x = person[0]
            coord_y = person[1]
            delta_x = person[2]
            delta_y = person[3] 

            # Update the x and y coordinates based on the velocity
            coord_x += delta_x 
            coord_y += delta_y

            person[0] = coord_x
            person[1] = coord_y
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
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        # Randomly generate the x,y,and z velocities
       

        # Adding the point to the point list
        
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