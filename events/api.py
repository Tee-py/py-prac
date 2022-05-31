from events import event_manager
from listeners.register import post_register_event

event_manager.subscribe('register', post_register_event)


def register_company(name: str):

    print(f'I have registered Company---> {name}')
    event_manager.publish('register', 'name')

register_company('Teepy Ventures')