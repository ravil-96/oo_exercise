'''Defining the Repo class'''
class Repo():
    all = []

    def __init__(self, data):
        self._name = data['name']
        self._description = data['description']
        self._save()

    def _save(self):
        self.all.append(self) 
    
    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description

    @classmethod
    def find_by_input(cls, user_input):
        return cls.all[int(user_input)-1] 