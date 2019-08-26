import pygame
import random
import sys
import time
from game_functions import exitgame

class Dnf():
	def __init__(self,screen,settings):
		'''a dnf pic falling down'''
		self.image = pygame.image.load('images/dnf.bmp')
		self.rect = self.image.get_rect()
		self.screen = screen
		self.screen_rect = self.screen.get_rect()

		self.rect.centerx = random.randint(1,settings.screen_w)
		self.rect.top = self.screen_rect.top
		self.score = 0
		self.speed = settings.dnf_speed

	def update(self,settings,score,sb,ship,game_running,hs,exit_button):

		if self.rect.colliderect(ship.rect):
			print("hit!")
			if sb.score > hs:
				print('new highscore!')
				file = open('highscore.txt','w')
				string = str(sb.score)
				file.write(string)

			pygame.mixer.music.load("sound/go.mp3")
			pygame.mixer.music.play()
			exit_button.draw_button()
			time.sleep(6)
			sys.exit()
			
								

		if self.rect.top < settings.screen_h:
			self.rect.centery += self.speed
		else:
			sb.score += 1
			effect = pygame.mixer.Sound('sound/coin.wav')
			effect.play()
			print(sb.score)
			self.rect.centerx = random.randint(1,settings.screen_w)	
			self.rect.centery = 0
			self.score += 1
			self.speed  += 1

	def blitme(self):
		self.screen.blit(self.image,self.rect)				


