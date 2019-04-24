from classes.Game import Game


class Snake:
    def __init__(self,
                 game: Game,
                 start_head_position: tuple,
                 length: int
                 ):
        self.body_segments = []
        self.length = length
        self.head = Head(start_head_position)

    def update(self):
        pass

    def destroy(self):
        for body in self.body_segments:
            body.destroy()
        self.head.destroy()


class Head:
    def __init__(self, start_position: tuple):
        pass

    def collide(self):
        pass

    def render(self):
        pass

    def destroy(self):
        pass


class Body:
    pass

    def collide(self):
        pass

    def render(self):
        pass
