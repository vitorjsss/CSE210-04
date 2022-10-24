from email.errors import MessageError
from game.casting.actor import Actor


class Artifact(Actor):
    """Generates the Artifacts getting properties from the Actor Class

    The responsibility of Artifact is to generate the artifacts and calcuate the score.

    Attributes:
        _points (integer): Adds or subtracts points from the score.
    """

    def __init__(self):
        super().__init__()
        self._points = 0

    def get_points(self):
        if (self.get_text() == '*'):
            self._points = 1
        else:
            self._points = -1
        
        return self._points