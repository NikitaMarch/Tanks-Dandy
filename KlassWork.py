from pygame import *


class Tank:
    """Наивысший класс, создаёт переменные для любого танка"""

    def __init__(self, noise: str, tank_x: int, tank_y, skin, speed, armor=100, health_point=100, bullets=60, width=12,
                 height=10, target=""):
        self.noise = noise  # выводит слово сохраненное в нем
        self.skin = skin  # цвет танка
        self.armor = armor  # броня
        self.health_point = health_point  # ХП
        self.bullets = bullets  # ПАТРОНЫ
        self.speed = speed  # Скорость
        self.tank_x = tank_x  # КООРДИНАТЫ ПО ИКСУ
        self.tank_y = tank_y  # КООРДИНАТЫ ПО ИГРИКУ
        self.width = width  # ширина
        self.height = height  # высота
        self.target = target

    def draw_tank(self):
        draw.rect(screen, self.skin, Rect(self.tank_x, self.tank_y, self.width, self.height))

    def move(self):  # меняем координаты для танка (двигаем танк)
        pass

    def check_coordinates(self):
        """Ограничивает поле, где могут ездить танки"""
        if self.tank_y <= 0:
            self.tank_y += self.speed
        if self.tank_x <= 0:
            self.tank_x += self.speed
        if self.tank_x >= 800 - self.width:
            self.tank_x -= self.speed
        if self.tank_y >= 600 - self.height:
            self.tank_y -= self.speed


class Buldog(Tank):
    """Наш танк"""
    def move(self):
        if key.get_pressed()[key.key_code("w")]:
            self.tank_y -= self.speed
            self.target = 'u'
        if key.get_pressed()[key.key_code("s")]:
            self.tank_y += self.speed
        if key.get_pressed()[key.key_code("a")]:
            self.tank_x -= self.speed
        if key.get_pressed()[key.key_code("d")]:
            self.tank_x += self.speed


class Enemy(Tank):  # вражеский танк
    pass


class Bullet:
    """старший класс пули, общие настройки"""
    def __init__(self, damage: int, speed: int, width: int, height: int):
        self.damage = damage
        self.speed = speed
        self.width = width
        self.height = height

    def draw_bullet(self):
        draw.rect(screen, self.width, self.height)  # Rect(1, 1, 2, 2) - пример

    def move(self):
        """Пуля двигается (летит)"""
        # 1) сохранять направление для танка
        # 2) проверять направление танка (конкретно пушки)
        # 3) передать последнее направление танка (в момент выстрела) для пули
        # 4) меняем координаты пули (двигаем) согласно этому направляю
        # 5) если пуля вышла за пределы или пуля попала в чужой танк - пуля уничтожается
        pass

    def make_damage(self):
        pass


screen = display.set_mode([800, 600])


def check_tanks_coordinates(buldog: Buldog, enemy: Enemy) -> None:
    """не разрешает танкам заезжать друг на друга"""
    if (buldog.tank_y + buldog.height > enemy.tank_y) and (buldog.tank_y < enemy.tank_y + enemy.height) \
            and (buldog.tank_x + buldog.width >= enemy.tank_x) and (buldog.tank_x <= enemy.tank_x):  # слева направо
        buldog.tank_x -= buldog.speed
    if (buldog.tank_y + buldog.height > enemy.tank_y) and (buldog.tank_y < enemy.tank_y + enemy.height) \
            and (buldog.tank_x <= enemy.tank_x + enemy.width) and (buldog.tank_x >= enemy.tank_x):  # справа налево
        buldog.tank_x += buldog.speed

    if (buldog.tank_y + buldog.height + 1 > enemy.tank_y) and (buldog.tank_y < enemy.tank_y + enemy.height) \
            and (buldog.tank_x + buldog.width > enemy.tank_x) and (buldog.tank_x < enemy.tank_x + enemy.width):
        # сверху вниз
        buldog.tank_y -= buldog.speed

    if (buldog.tank_y < enemy.tank_y + enemy.height + 1) and (buldog.tank_y > enemy.tank_y) \
            and (buldog.tank_x + buldog.width > enemy.tank_x) and (buldog.tank_x < enemy.tank_x + enemy.width):
        # снизу вверх
        buldog.tank_y += buldog.speed


def game(play, tanks, own_tank):
    """Следит, что происходит в игре"""

    while play:  # бесконечный цикл, который перезапускает проверку игры
        for e in event.get():
            if e.type == QUIT:
                play = False
        draw.rect(screen, "white", Rect(0, 0, 800, 600))
        own_tank.check_coordinates()

        for tank in tanks:
            check_tanks_coordinates(own_tank, tank)
            tank.draw_tank()

        own_tank.move()
        own_tank.draw_tank()
        display.update()


def start():  # игра запускается
    init()
    play = True
    enemies = [Enemy('wrrrwrrrwrrw', 377, 300, 'gray', 23), Enemy('wrrrwrrrwrrw', 377, 400, 'gray', 23),
               Enemy('wrrrwrrrwrrw', 377, 444, 'gray', 23)]
    own_tank = Buldog("efdssvbfdb", 280, 172, 'brown', 0.1)  # можно изменить цвет через rgb код (гуглить)
    game(play, enemies, own_tank)


start()
