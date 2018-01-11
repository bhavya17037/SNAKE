import pygame
from pygame.locals import *
import sys
from time import *
import random
from math import *

class snake_head(pygame.sprite.Sprite):
	def __init__(self,image_file,location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location

class Background(pygame.sprite.Sprite):
	def __init__(self,image_file,location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left,self.rect.top = location

class Food(pygame.sprite.Sprite):
	def __init__(self,image_file,location):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left,self.rect.top = location


def update_snake_head(x,y,snake_directions):
	isOut = False
	if snake_directions[0][0]:
		y -= 20
	elif snake_directions[0][1]:
		x += 20
	elif snake_directions[0][2]:
		y += 20
	elif snake_directions[0][3]:
		x -= 20

	if x <= 10 or x >= 990 or y <= 10 or y >= 790:
		isOut = True

	sleep(0.01)
	return x,y,isOut

def check_if_snake_eats(x,y,a,b):
	if sqrt((x-a)**2 + (y-b)**2) <= 20:
		return True
	return False 




pygame.init()
pygame.mixer.init()


game_start = pygame.mixer.Sound('Pacman Song.wav')
eaten = pygame.mixer.Sound('shoot.wav')

game_end = pygame.mixer.Sound('end.wav')


screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width,screen_height))



food_available = True
fx = random.randint(40,960)
fy = random.randint(40,760)

food = Food('food.png',[fx,fy])

score = 0

snake = [snake_head('snake.png',[screen_width//2,screen_height//2])]
snake_pos = [[snake[0].rect.left,snake[0].rect.top]]
snake_directions = [[True,False,False,False]]


background = Background('background.png',[0,0])

game_over = pygame.font.SysFont('Comic Sans MS',100)
Score = pygame.font.SysFont('Comic Sans MS',30)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

gameOver = False
isIn = False


c = 0


start = time()

game_start.play()

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if len(snake) > 1:
					
					if snake_directions[1][2] == False:

						snake_directions[0][0] = True
						snake_directions[0][1] = False
						snake_directions[0][2] = False
						snake_directions[0][3] = False
				else:
					snake_directions[0][0] = True
					snake_directions[0][1] = False
					snake_directions[0][2] = False
					snake_directions[0][3] = False

			if event.key == pygame.K_RIGHT:
				if len(snake) > 1:

					if snake_directions[1][3] == False:
						
						snake_directions[0][0] = False
						snake_directions[0][1] = True
						snake_directions[0][2] = False
						snake_directions[0][3] = False
				else:
					snake_directions[0][0] = False
					snake_directions[0][1] = True
					snake_directions[0][2] = False
					snake_directions[0][3] = False
			if event.key == pygame.K_DOWN:
				if len(snake) > 1:
					
					if snake_directions[1][0] == False:
						
						snake_directions[0][0] = False
						snake_directions[0][1] = False
						snake_directions[0][2] = True
						snake_directions[0][3] = False
				else:
					snake_directions[0][0] = False
					snake_directions[0][1] = False
					snake_directions[0][2] = True
					snake_directions[0][3] = False
			if event.key == pygame.K_LEFT:
				if len(snake) > 1:
				
					if snake_directions[1][1] == False:
						
						snake_directions[0][0] = False
						snake_directions[0][1] = False
						snake_directions[0][2] = False
						snake_directions[0][3] = True
				else:
					snake_directions[0][0] = False
					snake_directions[0][1] = False
					snake_directions[0][2] = False
					snake_directions[0][3] = True

	if gameOver or isIn:
		text_surface = game_over.render("GAME OVER",False,RED)
		screen.blit(text_surface,(300,400))
		if c == 0:
			
			game_end.play()
		c = 1
	

	else:



		if food_available == False:
			food_available = True
			food.rect.left = random.randint(40,960)
			food.rect.top = random.randint(40,760)

		## Check collision between snake head and food

		hasEaten = check_if_snake_eats(snake[0].rect.left,snake[0].rect.top,food.rect.left,food.rect.top)
		if hasEaten:
			eaten.play()
			food_available = False

			score += 1

			n = len(snake) - 1

			if snake_directions[n][0]:
				x = snake[n].rect.left
				y = snake[n].rect.top + 50
			elif snake_directions[n][1]:
				y = snake[n].rect.top
				x = snake[n].rect.left - 50
			elif snake_directions[n][2]:
				x = snake[n].rect.left
				y = snake[n].rect.top - 50
			elif snake_directions[n][3]:
				y = snake[n].rect.left
				x = snake[n].rect.top + 50

			snake.append(snake_head('snake.png',[x,y]))
			snake_directions.append([snake_directions[n][0],snake_directions[n][1],snake_directions[n][2],snake_directions[n][3]])


		temp_x,temp_y = snake[0].rect.left,snake[0].rect.top
		snake[0].rect.left,snake[0].rect.top,isOut = update_snake_head(snake[0].rect.left,snake[0].rect.top,snake_directions)
		dir_1,dir_2,dir_3,dir_4 = snake_directions[0][0],snake_directions[0][1],snake_directions[0][2],snake_directions[0][3]
		if isOut:
			gameOver = True

		## Now set direction and position for other parts of body

		if len(snake) > 1:
			for i in range(1,len(snake)):
				temp1_x,temp1_y = snake[i].rect.left,snake[i].rect.top
				snake[i].rect.left,snake[i].rect.top = temp_x,temp_y
				temp_x,temp_y = temp1_x,temp1_y

				tdir_1,tdir_2,tdir_3,tdir_4 = snake_directions[i][0],snake_directions[i][1],snake_directions[i][2],snake_directions[i][3]
				snake_directions[i][0],snake_directions[i][1],snake_directions[i][2],snake_directions[i][3] = dir_1,dir_2,dir_3,dir_4
				dir_1,dir_2,dir_3,dir_4 = tdir_1,tdir_2,tdir_3,tdir_4

		isIn = False
		for i in range(1,len(snake)):
			if snake[0].rect.left == snake[i].rect.left and snake[0].rect.top == snake[i].rect.top:
				isIn = True




		screen.fill((255,255,255))
		screen.blit(background.image,background.rect)

		for i in range(len(snake)):
			screen.blit(snake[i].image,snake[i].rect)

		screen.blit(food.image,food.rect)
		points = Score.render("SCORE: " + str(score) + "  TIME: " + str(int((time() - start)/60)) + " minutes " + str(time() - start) + " seconds",False,WHITE)
		screen.blit(points,(50,50))

	pygame.display.update()

