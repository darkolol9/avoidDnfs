import pygame

class Ship():
	'''a ship'''
	def __init__(self,screen,settings):
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.moving_right = False
		self.moving_left = False

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def update(self,settings):
		if self.moving_right:
			self.rect.centerx += settings.ship_speed

		elif self.moving_left:
			self.rect.centerx -= settings.ship_speed	

	def blitme(self):
		self.screen.blit(self.image,self.rect)	
