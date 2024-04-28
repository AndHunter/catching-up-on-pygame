from pygame import *
# создание окна игры
window = display.set_mode((700, 500)) # размеры окна
display.set_caption('Догонялки') # заголовок
background = transform.scale(image.load('background.png'),(700, 500)) # загрузка картинки на фон
# создание персонажей и их параметров
sprite1 = transform.scale(image.load('sprite1.png'),(100, 100)) # первое название картинки второе размер
sprite2 = transform.scale(image.load('sprite2.png'),(100, 100))
# кординаты персонажей
sprite1_rect = sprite1.get_rect()
sprite2_rect = sprite2.get_rect()
# начальные позиции персонажей
x1 = 100
y1 = 300
x2 = 300
y2 = 300
# переменные
game = True
font.init()
while game:
    for e in event.get():
        if e.type == QUIT: # нажатие на крестик
            game = False
    #отрисовка персонажей
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))
    # перемещение
    key_pressed = key.get_pressed()
#Устанавливаем границы за которые персонаж выйти не может
    # перемещение первого персонажа
    if key_pressed[K_UP] and y1 >= 0:    #  кнопки и границы
        y1 -= 1
    if key_pressed[K_DOWN] and y1 <= 380:
        y1 += 1
    if key_pressed[K_RIGHT] and x1 <= 600:
        x1 += 1
    if key_pressed[K_LEFT] and x1 >= 0:
        x1 -= 1
    # перемещение второго персонажа
    key_pressed = key.get_pressed()
    if key_pressed[K_w] and y2 >= 0:
        y2 -= 1
    if key_pressed[K_s] and y2 <= 380:
        y2 += 1
    if key_pressed[K_d] and x2 <= 600:
        x2 += 1
    if key_pressed[K_a] and x2 >= 0:
        x2 -= 1
    #Обрабатываем если персонажи столкнуться
    sprite1_rect.x = x1
    sprite1_rect.y = y1
    if sprite1_rect.colliderect(sprite2_rect):
        font1 = font.SysFont('verdana', 50) # название шрифта, размера
        text = font1.render('Джо забыл как играть', True, (0,0,0)) # текст и цвет, сглаживание
        window.blit(text,(100,100)) # отрисовка
    sprite2_rect.x = x2
    sprite2_rect.y = y2
    if sprite2_rect.colliderect(sprite1_rect):
        font1 = font.SysFont('verdana', 50)
        text = font1.render('Джо забыл как играть', True, (0,0,0))
        window.blit(text,(100,100))
    display.update() # обновление экрана