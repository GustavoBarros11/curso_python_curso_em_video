# Tocando musica (mp3) no python
import pygame

pygame.init()
pygame.mixer.music.load('some.mp3')
pygame.mixer.music.play()
pygame.event.wait()