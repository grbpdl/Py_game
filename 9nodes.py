from classapp7 import *


class Demo(App):
    def __init__(self):
        super().__init__()
        Scene(caption='Nodes - vertical placement')
        Node()
        Node()
        Node()
        Node(pos=(200, 20), size=(200, 50))
        Node()
        Node()
        Scene(caption='Nodes - horizontal placement')
