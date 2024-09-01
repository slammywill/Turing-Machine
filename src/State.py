import pygame
from Transition import Transition

class State:
    """Defines a state that the automata can be in.
    """

    def __init__(self, position: tuple, name="", transitions=[]):
        """State constructor.

        Args:
            position    (tuple):            The x and y position tuple of the state.   
            name        (str, optional):    The name of the state. Defaults to "".
            transitions (list, optional):   The list of transitions to give to the state. Defaults to [].
        """
        self.name = name
        self.fill_colour = "grey"
        self.border_colour = "black"
        self.transitions = transitions
        self.position = position
        self.font = pygame.font.Font('freesansbold.ttf', 14)
        self.text = self.create_label()

    def add_transition(self, transition: Transition):
        """Adds a transition to the state.

        Args:
            transition (Transition): The transition to be added.
        """
        self.transitions.append(transition)
    

    def create_label(self):
        """Creates the name label of the state.

        Returns:
            tuple: The text and its bounding rectangle.
        """
        text = self.font.render(self.name, True, "black")
        textRect = text.get_rect()
        textRect.center = self.position
        return (text, textRect)


    def set_visually_selected(self, is_selected: bool):
        """Used to change the visual style of the state if it is currently selected or not.

        Args:
            is_selected     (bool): Whether the state is selected or not.
        """
        if is_selected:
            self.fill_colour = "grey"
            self.border_colour = "blue"
        else:
            self.fill_colour = "grey"
            self.border_colour = "black"

