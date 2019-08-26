import pygame
import sys

def check_events(ship):   #checks for inputs
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					ship.moving_right = True
				if	event.key == pygame.K_LEFT:
					ship.moving_left = True

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					ship.moving_right = False
				if	event.key == pygame.K_LEFT:
					ship.moving_left = False		

def update_screen(screen,settings,ship,dnf,sb):   #updates the objects on the screen and prints a frame
	screen.fill(settings.bg_color)	
	screen.blit(settings.bg,(0,0))
	sb.draw()
	#background needs to be behind any element

	dnf.blitme()
	ship.blitme()

	#last to be done, print the screen frame
	pygame.display.flip()	

def exitgame(exit_button):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x,mouse_y = pygame.mouse.get_pos()
				if exit_button.rect.collidepoint(mouse_x,mouse_y):
					sys.exit()
