
class EventManager:

    def __init__(self):
        self.subscribers = dict()
    
    def subscribe(self, event: str, func):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(func)

    def publish(self, event: str, arg):
        if not event in self.subscribers:
            return
        for sub in self.subscribers[event]:
            sub(arg)

event_manager = EventManager()
