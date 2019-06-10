from magenta.models.performance_rnn import performance_rnn_generate
import tensorflow as tf
from config import PATH
import piano
import pygame.mixer

# The main method creates an instance of the Piano class
# and keeps it running until termination.
def main():
    try:
        pygame.mixer.music.load(
            '/home/pirl/Documents/aimusic/output/generated/2019-06-10_170321_1.mid')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception:
        pygame.mixer.music.load('welcome.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


if __name__ == '__main__':
    main()