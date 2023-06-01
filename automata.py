import re
import pygame


class State:
    """Defines a state that the automata can be in.
    """

    def __init__(self, position, name="", transitions=[]):
        """State constructor.

        Args:
            position    (tuple):            The x and y position tuple of the state.   
            name        (str, optional):    The name of the state. Defaults to "".
            transitions (list, optional):   The list of transitions to give to the state. Defaults to [].
        """
        self.name = name
        self.transitions = transitions
        self.position = position
        self.font = pygame.font.Font('freesansbold.ttf', 14)
        self.text = self.create_label()

    def add_transition(self, transition):
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


class Transition:
    """Defines a transition from the state that it is added to, and the state specified in the constructor.
    It follows rules that are given by a string.
    """
    def __init__(self, in_state, rules):
        """Transition constructor.

        Args:
            in_state    (State):    The state that transition will go to.
            rules       (dict):     The dict of rules that the transition has.
        """
        self.in_state = in_state
        self.rules = rules

    @staticmethod
    def create_transition(in_state, rule, alphabet):
        """Creates a new transition.

        Args:
            in_state    (State):    The state that transition will go to.
            rule        (str):      The string rule to be followed containing each transition under some symbol of the alphabet.
            alphabet    (str):      The string containng all characters of the alphabet.

        Returns:
            Transition: The new transition.
        """
        # Check that the rule follows the correct format
        match = re.match(f"([{alphabet}]/[{alphabet}],[LRN] \| )*[{alphabet}]/[{alphabet}],[LRN]", rule)

        if match is not None:
            ruledict = dict()
            rules = rule.split("|")
            for r in rules: # Creates the dict of symbols to be read and what to do under those symbols.
                r = r.strip()
                read, write, direction = r[0], r[2], r[4]
                ruledict[read] = (write, direction)

            return Transition(in_state, ruledict)
    


class Automata:
    """Defines the automata that has states and transitions.
    """

    S_RADIUS = 25
    S_WIDTH = 2

    def __init__(self, alphabet):
        """Automata constructor.

        Args:
            alphabet (str): The string containng all characters of the alphabet.
        """
        self.states = []
        self.current_state = None
        self.alphabet = alphabet


    def add_state(self):
        """Adds a state to the automata at the position of the mouse with name being its position
        in the state list.
        """
        pos = pygame.mouse.get_pos()
        self.states.append(State(pos, str(len(self.states))))


    def on_draw(self, surface):
        """Draws all of the states and transitions.

        Args:
            surface (Surface): The pygame surface that is being drawn onto.
        """
        for state in self.states:
            pygame.draw.circle(surface, color="black", center=state.position,
                               radius=self.S_RADIUS, width=self.S_WIDTH)
            surface.blit(state.text[0], state.text[1])
