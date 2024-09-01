import pygame
from State import State
from Transition import Transition
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
        new_state = State(pos, [], str(len(self.states)))
        self.states.append(new_state)


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
            for transition, to_state in state.transitions:
                pygame.draw.aaline(surface, "black", state.position, to_state.position)

        # Draw states
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
        state_clicked = None
        for state in self.states:
            dist = ((state.position[0] - mouse_pos[0])**2 + (state.position[1] - mouse_pos[1])**2)**0.5
            if (dist <= Automata.S_RADIUS):
                state_clicked = state

        if self.adding_transition and self.selected_state is not None and state_clicked is not None:
            self.selected_state.add_transition(Transition.create_transition("", self.alphabet), state_clicked)
            self.toggle_adding_transition()

        if not state_clicked:
            self.selected_state = None
        else:
            self.selected_state = state_clicked
        for state in self.states:
            print(state)
        


    def toggle_adding_transition(self):
        """Toggles whether the user is adding a transition or not."""
        if self.selected_state is not None:
            self.adding_transition = not self.adding_transition
        else:
            self.adding_transition = False
            
