import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.wav')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue