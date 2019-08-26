import pygame
import sys
import game_functions as gf
import settings
from button import Button
from menu import menu
from ship import Ship
import dnf
import scoreboard 

blank = True
game_running = True

highscore = open('highscore.txt','r')
hs = int(highscore.read())
highscore.close()

def rungame():
	pygame.init()
	score = 0
	game_settings = settings.Settings()
	
	screen = pygame.display.set_mode((game_settings.screen_w,game_settings.screen_h))
	sb = scoreboard.Scoreboard(screen,score)
	ship = Ship(screen,game_settings)
	d_n_f = dnf.Dnf(screen,game_settings)
	play_button = Button(screen,'PLAY')
	exit_button = Button(screen,'exit')
	pygame.display.set_caption("avoid the dnfs!")


	while game_running:
		gf.check_events(ship)
		d_n_f.update(game_settings,score,sb,ship,game_running,hs,exit_button)
		sb.update(score,hs)
		ship.update(game_settings)
		gf.update_screen(screen,game_settings,ship,d_n_f,sb)


		

menu(blank)
rungame()	
