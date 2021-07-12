class Space():

    def __init__(self):
        self._value = 0

    def __repr__(self):
        return str(self._value)

    def __str__(self):
        return str(self._value)

    def set(self):
        self._value = 1

    def reset(self):
        self._value = 0

    def get(self):
        return self._value
