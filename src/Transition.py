import re


class Transition:
    """Defines a transition from the state that it is added to, and the state specified in the constructor.
    It follows rules that are given by a string.
    """
    def __init__(self, rules: dict):
        """Transition constructor.

        Args:
            rules       (dict):     The dict of rules that the transition has.
        """
        self.rules = rules

    @staticmethod
    def create_transition(rule: str, alphabet: str):
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

            return Transition(ruledict)
