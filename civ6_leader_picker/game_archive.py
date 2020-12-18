import datetime as dt
import json

class game():
    def __init__(self):
        self._leader = None
        self._map = None
        self._won = False
        self._last_round = None
        self._victory_type = None
        self._game_modes = None
        self._date = None
    
    def serialize_json(self):
        return json.dump(self.__dict__)

class game_archive():
    def __init__(self, **kwargs):
        self._games = kwargs.get('games', None)

    def serialize_json(self):
        for g in self._games:
            