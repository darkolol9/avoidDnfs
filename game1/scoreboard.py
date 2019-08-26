import pygame
class Scoreboard():
	def __init__(self,screen,score):
		'''scoreboard to present score'''
		self.score = score
		self.screen = screen
		self.screen_rect = screen.get_rect()

		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,48)
		init_score_str = str(self.score)
		self.score_img = self.font.render(init_score_str,True,self.text_color,
			(230,230,230))

		self.score_rect = self.score_img.get_rect()
		self.score_rect.right = self.screen_rect.right - 800
		self.screen_rect.top = 20

	def draw(self):
		self.screen.blit(self.score_img,self.score_rect)	

	def update(self,score,hs):
		score_str = 'number of DNFs avoided: ' + str(self.score) + ' current highscore: ' + str(hs)

		self.score_img = self.font.render(score_str,True,self.text_color,
			(230,230,230))


	

