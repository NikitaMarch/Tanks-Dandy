from pygame import *


class Tank:
    """Наивысший класс, создаёт переменные для любого танка"""
    def __init__(self, noise: str, tank_x: int, tank_y, skin, speed, armor=100, health_point=100, bullets=60):
        self.noise = noise  # выводит слово сохраненное в нем
        self.skin = skin  # скин (надо изменить)
        self.armor = armor  # броня
        self.health_point = health_point #ХП
        self.bullets = bullets#ПАТРОНЫ
        self.speed = speed#Скорость
        self.tank_x = tank_x#КООРДИНАТЫ ПО ИКСУ
        self.tank_y = tank_y#КООРДИНАТЫ ПО ИГРИКУ

    def move(self):  # меняем координаты для танка (двигаем танк)
        pass

    def check_coordinates(self):
        """Ограничивает поле, где могут ездить танки"""
        if self.tank_y <= 0:
            self.tank_y += self.speed
        if self.tank_x <= 0:
            self.tank_x += self.speed
        if self.tank_x >= 788:
            self.tank_x -= self.speed
        if self.tank_y >= 590:
            self.tank_y -= self.speed


class Buldog(Tank):  # класс нашего танка (характеристики)
    def draw_tank(self):
        draw.rect(screen, self.skin, Rect(self.tank_x, self.tank_y, 12, 10))

    def move(self):
        if key.get_pressed()[key.key_code("w")]:
            self.tank_y -= self.speed
        if key.get_pressed()[key.key_code("s")]:
            self.tank_y += self.speed
        if key.get_pressed()[key.key_code("a")]:
            self.tank_x -= self.speed
        if key.get_pressed()[key.key_code("d")]:
            self.tank_x += self.speed


class Enemy(Tank):# вражеский танк
    def draw_tank(self):
        draw.rect(screen, self.skin, Rect(self.tank_x, self.tank_y, 12, 10))

# надо дописать комментарии


screen = display.set_mode([800, 600])


def game(play, tank, own_tank):
    """Следит, что происходит в игре"""

    while play:  # бесконечный цикл, который перезапускает проверку игры
        for e in event.get():
            if e.type == QUIT:
                play = False
        draw.rect(screen, "white", Rect(0, 0, 800, 600))
        own_tank.move()
        own_tank.check_coordinates()
        tank.draw_tank()
        own_tank.draw_tank()
        display.update()


def start(): #игра запускается
    init()
    play = True
    own_tank = Buldog("efdssvbfdb", 280, 172, 'brown', 0.1)  # можно изменить цвет через rgb код (гуглить)
    on_tank = Enemy('wrrrwrrrwrrw', 377, 300, 'gray', 23)  # можно изменить цвет через rgb код (гуглить)
    game(play, on_tank, own_tank)


start()
