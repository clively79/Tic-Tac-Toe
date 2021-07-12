class Space():
    """
        A Python class representing a single space of a game board.  
        _value = 0 unocupied
        _value_ = 1 occupied
    """

    def __init__(self):
        """Constructor method
        """
        self._value = 0

    def __repr__(self):
        return str(self._value)

    def __str__(self):
        return str(self._value)

    def set(self):
        """set _value to 1 (occupied)
        """
        self._value = 1

    def reset(self):
        """Set's _value to 0 (unoccupied)
        """
        self._value = 0

    def get(self):
        """getter method

        Returns:
            Integer: returns  _value
        """
        return self._value
