import pygame
from pygame.locals import *
from automata import *


class TuringMachine:

    def __init__(self):
        """The main class constructor that starts the application.
        """
        self._running = False
        self.size = self.width, self.height = 1280, 720


    def on_init(self):
        """Runs the pygame initialization after the application is created.
        """
        pygame.init()
        pygame.display.set_caption('Turing Machine')
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.automata = Automata("01")
        self._running = True


    def on_event(self, event):
        """Runs when an event happens in the application.

        Args:
            event (Event): The event that has happened.
        """
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.automata.add_state()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            left, middle, right = pygame.mouse.get_pressed()
            if left:
                pass



    def on_loop(self):
        """Runs as the main application loop.
        """
        pass


    def on_render(self):
        """Renders things to the screen.
        """
        self._display_surf.fill("white")
        self.automata.on_draw(self._display_surf)
        pygame.display.flip()


    def on_cleanup(self):
        """Runs when the application is closed.
        """
        pygame.quit()


    def on_execute(self):
        """Executes the start of the application.
        """
        if self.on_init() == False:
            self._running = False

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    """Main.
    """
    tm = TuringMachine()
    tm.on_execute()

