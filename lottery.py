import logging
from datetime import datetime


class Lottery(object):
    """
    This is Lottery object. Pick your fruit
    """
    _start: int
    _state: dict
    _votes: dict

    def __init__(self):
        logging.debug("Lottery object created")
        self._start = datetime.now().timestamp()
        self._state = {
            'strawberry': 0,
            'apple': 0,
            'pear': 0,
            'banana': 0,
        }
        self._votes = {}

    def get_start(self) -> int:
        """
        Returns the moment in time when Lottery has started
        """
        return self._start

    def increment(self, action, user):
        if action in self._state.keys():
            self._state[action] += 1
        else:
            logging.error(f"access to non-existent key {action}")

    def get_scores(self):
        return self._state

    def finish(self):
        pass


if __name__ == "__main__":
    l = Lottery()
    print(l.get_start())
    l.increment('banana', 'foo')
    l.increment('foo', 'foo')
    print(l.get_scores())
