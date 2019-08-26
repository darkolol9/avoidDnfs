import pygame
import sys
import settings
from button import Button

blank = True



gs = settings.Settings()

def menu(blank):
	pygame.init()
	game_settings = settings.Settings()
	screen = pygame.display.set_mode((800,800))
	play_button = Button(screen,'play')
	pygame.display.set_caption("menu")


	screen.fill(gs.bg_color)	
	screen.blit(gs.bg,(0,0))
	play_button.draw_button()
	pygame.mixer.music.load('sound/intro.mp3')
	pygame.mixer.music.play(-1)
	#background needs to be behind any element
	


	#last to be done, print the screen frame
	pygame.display.flip()		

	while blank:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x,mouse_y = pygame.mouse.get_pos()
				if play_button.rect.collidepoint(mouse_x,mouse_y):
					blank = False
					print('clicked play')




#menu(blank)
