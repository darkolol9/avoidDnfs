import pygame


class Settings():
	"""settings of the game!"""
	def __init__(self):
		self.bg_color = (230,230,230)
		self.screen_w = 1200
		self.screen_h = 800
		self.bg = pygame.image.load("images/bg.bmp")
		self.dnf_speed = 6
		self.ship_speed = 9

