import sys
import pygame

class AlienInvasion:
    """ Overall class to manage game assets and behavior """
    
    def _init_(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.sreen_height))
        pygame.display.pygame.display.set_caption("Alien Invasion", icontitle=None)
        
        # Set the backgroun color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.git():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
        
if _name_ == '_main_':
    # Make a game instance, and run game.
    ai = AlienInvasion()
    ai.run_game()