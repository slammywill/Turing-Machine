import re


class State:
    """Defines a state that the automata can be in.
    """
    def __init__(self, name="", transitions=[]):
        """State constructor.

        Args:
            name (str, optional): The name of the state. Defaults to "".
            transitions (list, optional): The list of transitions to give to the state. Defaults to [].
        """
        self.name = name
        self.transitions = transitions

    def add_transition(self, transition):
        """Adds a transition to the state.

        Args:
            transition (Transition): The transition to be added.
        """
        self.transitions.append(transition)


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
    def __init__(self, alphabet):
        """Automata constructor.

        Args:
            alphabet (str): The string containng all characters of the alphabet.
        """
        self.states = []
        self.current_state = None
        self.alphabet = alphabet

