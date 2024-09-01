import pygame
from State import State
from typing import Optional

class Automata:
    """Defines the automata that has states and transitions.
    """

    S_RADIUS = 25
    S_WIDTH = 2

    def __init__(self, alphabet: str):
        """Automata constructor.

        Args:
            alphabet (str): The string containng all characters of the alphabet.
        """
        self.states: list = []
        self.current_state: Optional[State] = None
        self.selected_state: Optional[State] = None
        self.adding_transition = False
        self.alphabet = alphabet


    def add_state(self):
        """Adds a state to the automata at the position of the mouse with name being its position
        in the state list.
        """
        pos = pygame.mouse.get_pos()
        self.states.append(State(pos, str(len(self.states))))


    def on_draw(self, surface: pygame.Surface):
        """Draws all of the states and transitions.

        Args:
            surface (Surface): The pygame surface that is being drawn onto.
        """
        if self.selected_state:
            selected_pos = self.selected_state.position
            mouse_pos = pygame.mouse.get_pos()
            if self.adding_transition:
                pygame.draw.aaline(surface, "black", selected_pos, mouse_pos)


        for state in self.states:
            if state == self.selected_state:
                state.set_visually_selected(True)
            else:
                state.set_visually_selected(False)

            # Inside colour.
            pygame.draw.circle(surface, color=state.fill_colour, center=state.position,
                               radius=self.S_RADIUS, width=0)
            # Border.
            pygame.draw.circle(surface, color=state.border_colour, center=state.position,
                               radius=self.S_RADIUS, width=self.S_WIDTH)
            surface.blit(state.text[0], state.text[1])
    

    def handle_click(self, mouse_pos):
        """Handles a users click."""
        state_clicked = False
        for state in self.states:
            dist = ((state.position[0] - mouse_pos[0])**2 + (state.position[1] - mouse_pos[1])**2)**0.5
            if (dist <= Automata.S_RADIUS):
                self.selected_state = state
                state_clicked = True
        if not state_clicked:
            self.selected_state = None


    def toggle_adding_transition(self):
        """Toggles whether the user is adding a transition or not."""
        if self.selected_state is not None:
            self.adding_transition = not self.adding_transition
        else:
            self.adding_transition = False
            
