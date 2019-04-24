from classes.Render import WindowRender, ConsoleRender
from classes.BattleState import BattleState


class Game:
    def __init__(self):
        self.updatable = []
        self.renderable = []
        self.collideable = []

        self.screen_width = 800
        self.screen_height = 600
        self.render_type = "Window"
        self.volume = 5

        if open("config") is not None:
            self.load_config()
        else:
            self.create_config()
            self.load_config()

        if self.render_type == "Window":
            self.renderer = WindowRender(self.screen_width, self.screen_height)
        else:
            self.renderer = ConsoleRender()

        self.game_state = BattleState()
        self.start()

    def load_config(self):
        """
        Загужает настройки игры из файла config.cfg
        в переменные
        self.screen_width
        self.screen_height
        self.render_type
        self.volume
        :return:
        """
        pass

    def create_config(self):
        """
        Создает файл config.cfg с базовыми настройками
        self.screen_width
        self.screen_height
        self.render_type
        self.volume
        :return:
        """
        pass

    def update(self):
        """
        Обновляет состояние текущих объектов
        :return:
        """
        for element in self.updatable:
            element.update()

    def render(self):
        """
        Отрисовыает элементы на экране
        :return:
        """
        for element in self.renderable:
            self.renderer.render(element)

    def start(self):
        """
        Основной цикл игры
        :return:
        """
        # pygame init
        while True:
            self.update()
            self.render()
