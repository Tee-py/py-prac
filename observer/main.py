

class Subject:

    def __init__(self):
        self.observers = set()
        self._state = None 
    
    def add(self, obs):
        self.observers.add(obs)

    def remove(self, obs):
        self.observers.remove(obs)

    def notify(self):
        for obs in self.observers:
            obs.update()
        
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, new_state):
        self._state = new_state
        self.notify()

class Observer:

    def __init__(self, subject):
        self.subject = subject
    
    def update(self):
        print(f"{self.subject.__class__.__name__} was changed to {self.subject.state}!!!")


sub = Subject()
obj = Observer(sub)
sub.add(obj)
sub.state = "Hello"
sub.remove(obj)
sub.state = "Hiii"
