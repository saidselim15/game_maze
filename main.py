from pygame import *
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  #конструктор класса
  def __init__(self, player_image, player_x, player_y, player_speed):
      # Вызываем конструктор класса (Sprite):
      sprite.Sprite.__init__(self)

      # каждый спрайт должен хранить свойство image - изображение
      self.image = transform.scale(image.load(player_image), (80, 80))
      self.speed = player_speed

      # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
   #метод, отрисовывающий героя на окне
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
    
  side = "down"
  def update(self):
      if self.rect.y <= 0:
          self.side = "up"
      if self.rect.y >= win_width - 720:
          self.side = "down"
      if self.side == "down":
          self.rect.y -= self.speed
      else:
          self.rect.y += self.speed
        
  


#класс главного игрока
class Player(GameSprite):
  #метод, в котором реализовано управление спрайтом по кнопкам стрелочкам клавиатуры
  def update(self):
      keys = key.get_pressed()
      if keys[K_LEFT] and self.rect.x > 5  or sprite.collide_rect(packman, w1) or sprite.collide_rect(packman, w2) or sprite.collide_rect(packman, w3):
          self.rect.x -= self.speed
      if keys[K_RIGHT] and self.rect.x < win_width - 80 or sprite.collide_rect(packman, w1) or sprite.collide_rect(packman, w2) or sprite.collide_rect(packman, w3) :
          self.rect.x += self.speed
      if keys[K_UP] and self.rect.y > 5  or sprite.collide_rect(packman, w1) or sprite.collide_rect(packman, w2) or sprite.collide_rect(packman, w3):
          self.rect.y -= self.speed
      if keys[K_DOWN] and self.rect.y < win_height - 80 or sprite.collide_rect(packman, w1) or sprite.collide_rect(packman, w2) or sprite.collide_rect(packman, w3):
          self.rect.y += self.speed

      


#класс спрайта-врага    
class Enemy(GameSprite):
  side = "left"
   #движение врага
  def update(self, run = False):
      if run:
          if self.rect.x <= run:
              self.side = 'right'

      if self.rect.x <= 0:
          self.side = "right"
      if self.rect.x >= win_width - 85:
          self.side = "left"
      if self.side == "left":
          self.rect.x -= self.speed
      else:
          self.rect.x += self.speed
        
  side = "left"
   #движение врага
  def update1(self):
      if self.rect.y <= 0:
          self.side = "right"
      if self.rect.y >= win_width - 720:
          self.side = "left"
      if self.side == "left":
          self.rect.y -= self.speed
      else:
          self.rect.y += self.speed
#класс элемента стены
class Wall(sprite.Sprite):
  def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
       sprite.Sprite.__init__(self)
       self.color_1 = color_1
       self.color_2 = color_2
       self.color_3 = color_3
       self.width = wall_width
       self.height = wall_height

       # картинка стены - прямоугольник нужных размеров и цвета
       self.image = Surface([self.width, self.height])
       self.image.fill((color_1, color_2, color_3))

       # каждый спрайт должен хранить свойство rect - прямоугольник
       self.rect = self.image.get_rect()
       self.rect.x = wall_x
       self.rect.y = wall_y

  def draw_wall(self):
      draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))
#Создаем окошко
win_width = 1350
win_height = 800

display.set_caption("Лабиринт")
window = display.set_mode((win_width, win_height))
#создаем стены
w1 = Wall(0, 255, 0, win_width / 2 - win_width / 3, win_height / 2, 300, 10)
w2 = Wall(0, 255, 0, 410, win_height / 2 - win_height / 4, 10, 350)
w3 = Wall(0, 255, 0, 100, 600, 1280, 10)
#создаем спрайты
packman = Player('hero.png', 5, win_height - 80, 5)
monster = Enemy('cyborg.png', win_width - 80, 200, 2)
monster1 = Enemy('cyborg.png', win_width - 80, 650, 4)
monster2 = Enemy('cyborg.png', win_width - 80, 0, 4)
final_sprite = GameSprite('pac-1.png', win_width - 85, win_height - 100, 6)

#переменная, отвечающая за то, как кончилась игра
finish = False
#игровой цикл
run = True
while run:
  #цикл срабатывает каждую 0.05 секунд
  time.delay(15)
   #перебираем все события, которые могли произойти
  for e in event.get():
      #событие нажатия на кнопку “закрыть”
      if e.type == QUIT:
          run = False

#проверка, что игра еще не завершена
  if not finish:
      #обновляем фон каждую итерацию
      window.fill((255, 100, 0))
       #рисуем стены
      w1.draw_wall()
      w2.draw_wall()
      w3.draw_wall()
       #запускаем движения спрайтов
      packman.update()
      monster.update(420)
      monster1.update()
      monster2. update1()
      final_sprite.update()
       #обновляем их в новом местоположении при каждой итерации цикла
      packman.reset()
      monster.reset()
      monster1.reset()
      monster2.reset()
      final_sprite.reset()


      #Проверка столкновения героя с врагом и стенами
      if sprite.collide_rect(packman, monster) or sprite.collide_rect(packman, monster1) or sprite.collide_rect(packman, monster2) :
          finish = True
          #вычисляем отношение
          img = image.load('game-over_1.png')
          d = img.get_width() // img.get_height()
          window.fill((255, 255, 255))
          window.blit(transform.scale(img, (win_height * d, win_height)), (90, 0))

      if sprite.collide_rect(packman, final_sprite):
          finish = True
          img = image.load('thumb.jpg')
          window.fill((255, 255, 255))
          window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
 
  display.update()