#!/usr/bin/python
##########################################################
# Piano.py, when run, creates a window that simulates a  #
# two-octave piano. This program was originally created  #
# for the final project of CS 214 at Calvin College.     #
#                                                        #
# Created by: Jesse Kuntz                                #
# Date of Presentation: 05/12/16                         #
##########################################################

# Import the package that allows me to manipulate windows and
# graphics. 'Tkinter' is for Python 2, while 'tkinter' is for
# Python 3. This allows for it to be run on either version.
black_key = ['61', '63', '66', '68', '70', '73', '75', '78', '80', '82']

try:
    from Tkinter import Tk, Frame, BOTH, Label, PhotoImage
except ImportError:
    from tkinter import Tk, Frame, BOTH, Label, PhotoImage
# Import the package that allows me to play sounds.
import simpleaudio as sa
# Import the package that allows me to keep track of time.
import time as t
# Import the package that allows me to concurrently run operations.
from _thread import start_new_thread
from magenta.models.performance_rnn import performance_rnn_generate
import tensorflow as tf
from config import PATH
import pygame.mixer


FLAGS = tf.app.flags.FLAGS
primer_melody = []
pygame.mixer.init()

tf.app.flags.DEFINE_string('f', '', 'kernel')
FLAGS.bundle_file = PATH.bundle_file
FLAGS.output_dir = PATH.gen_dir
FLAGS.num_outputs = 1
FLAGS.num_steps = 3000

start = t.time()

# These two lines wipe the file.
file = open('songs/song.txt', 'w')
file.close()

recording = False


##########################################################
# Description: label_pressed is a method that will       #
# change the image of the Label passed in through the    #
# click of the mouse to a 'pressed' or darkened version  #
# of that image.                                         #
#                                                        #
# Accepts: event, the mouse event that is tied to the    #
# Label that is clicked.                                 #
##########################################################
def label_pressed(event):
    print(event.widget.name)
    if event.widget.name == 'red_button':
        img = 'pictures/red_button_pressed.gif'
    elif event.widget.name == 'green_button':
        img = 'pictures/green_button_pressed.gif'
        FLAGS.primer_melody = str(primer_melody)
        print(FLAGS.output_dir)
        performance_rnn_generate.main(FLAGS)
    elif event.widget.name in black_key:
        img = 'pictures/black_key_pressed.gif'
    else:
        img = 'pictures/white_key_pressed.gif'

    key_img = PhotoImage(file=img)
    event.widget.configure(image=key_img)
    event.widget.image = key_img


##########################################################
# Description: label_released is a method that will      #
# change the image of the Label passed in through the    #
# click of the mouse to the original version of that     #
# image.                                                 #
#                                                        #
# Accepts: event, the mouse event that is tied to the    #
# Label that is clicked.                                 #
##########################################################
def label_released(event):
    if not event.widget.name in black_key:
        img = 'pictures/white_key.gif'
    elif event.widget.name in black_key:
        img = 'pictures/black_key.gif'
    elif event.widget.name == 'red_button':
        img = 'pictures/red_button.gif'
    else:
        img = 'pictures/green_button.gif'
    key_img = PhotoImage(file=img)
    event.widget.configure(image=key_img)
    event.widget.image = key_img


##########################################################
# Description: play is a method used in the method       #
# playback that contains the code for opening a file,    #
# reading it and playing each note that the file         #
# contains in time.                                      #
#                                                        #
# Accepts: file_name, which contains a string with the   #
# name of the file that holds to song that is to be      #
# played.                                                #
##########################################################
def play(file_name):
    song_file = open(file_name, 'r')
    print("Playback Started")
    first_line = song_file.readline().split()
    note = first_line[0]
    time_scale = float(first_line[1])
    for line in song_file:
        wave_obj = sa.WaveObject.from_wave_file('sounds/' + note + '.wav')
        wave_obj.play()
        line_elements = line.split()
        note = line_elements[0]
        time = float(line_elements[1])
        t.sleep(time - time_scale)
        time_scale = time
    wave_obj = sa.WaveObject.from_wave_file('sounds/' + note + '.wav')
    wave_obj.play()
    print("Playback Stopped")


##########################################################
# Description: playback is a driver method for the       #
# method play and checks what is clicked to tell what    #
# song to play back.                                     #
#                                                        #
# Accepts: event, the mouse event that is tied to the    #
# Label that is clicked.                                 #
##########################################################
def play_back(event):
    if event.char == '1':
        start_new_thread(play, ('songs/1.txt',))
    elif event.char == '2':
        start_new_thread(play, ('songs/2.txt',))
    else:
        label_pressed(event)
        # This line starts a new thread and runs the method
        # play on that new thread. Go concurrency!
        start_new_thread(play, ('songs/song.txt',))
        return primer_melody


##########################################################
# Description: record_on_off is a method that changes    #
# the global variable recording to its opposite and      #
# presses down the record_button Label if the program    #
# is currently recording, and releases it if it is not.  #
#                                                        #
# Accepts: event, the mouse event that is tied to the    #
# Label that is clicked.                                 #
##########################################################
def record_on_off(event):
    global recording
    recording = not recording
    print('Recording: ', recording)
    if recording:
        label_pressed(event)
    else:
        label_released(event)


##########################################################
# Description: record is a method used in key_pressed    #
# and button_pressed that opens a file and writes note   #
# to that file, as well as the current time elapsed.     #
#                                                        #
# Accepts: file_name, the name of the file that is to be #
# written to; note, the note that is to be written to    #
# the file.                                              #
##########################################################
def record(file_name, note):
    song_file = open(file_name, 'a')
    end = t.time()
    time = end - start
    song_file.write(note + ' ' + str(time))
    song_file.write('\n')
    primer_melody.append(int(note))
    primer_melody.append(-2)

##########################################################
# Description: find_label is a method used in            #
# key_pressed and key_released that searches the array   #
# passed in for name, and returns the Label associated   #
# with that element.                                     #
#                                                        #
# Accepts: name, the name of the note that is to be      #
# checked for; array, the array that is to be searched.  #
##########################################################
def find_label(name, array):
    for x in range(len(array)):
        # checks against the name component in keys
        if name == array[x][1]:
            # returns the Label component in keys
            return array[x][2]


##########################################################
# Description: key_pressed is a method bound to each of  #
# the keyboard keys in the dictionary KEYS_TO_NOTES that #
# plays the note associated with the key pressed,        #
# records that note and changes the image to the         #
# 'pressed' or darkened version of that image.           #
#                                                        #
# Accepts: event, the keyboard event that is tied to the #
# key that is pressed.                                   #
##########################################################
def key_pressed(event):
    # This is so that if a key that is not in KEYS_TO_NOTES
    # is pressed, it will not return an error.
    note = KEYS_TO_NOTES.get(event.char, None)
    if note:
        wave_obj = sa.WaveObject.from_wave_file('sounds/' + note + '.wav')
        wave_obj.play()

        if recording:
            record('songs/song.txt', note)
        if not note in black_key:
            img = 'pictures/white_key_pressed.gif'
        else:
            img = 'pictures/black_key_pressed.gif'
        key_img = PhotoImage(file=img)
        find_label(note, event.widget.keys).configure(image=key_img)
        find_label(note, event.widget.keys).image = key_img


##########################################################
# Description: key_pressed is a method bound to each of  #
# the keyboard keys in the dictionary KEYS_TO_NOTES that #
# changes the image back to the original version of that #
# image.                                                 #
#                                                        #
# Accepts: event, the keyboard event that is tied to the #
# key that is pressed.                                   #
##########################################################
def key_released(event):
    note = KEYS_TO_NOTES.get(event.char, None)
    if note:
        if not note in black_key:
            img = 'pictures/white_key.gif'
        else:
            img = 'pictures/black_key.gif'
        key_img = PhotoImage(file=img)
        find_label(note, event.widget.keys).configure(image=key_img)
        find_label(note, event.widget.keys).image = key_img


##########################################################
# Description: button_pressed is a method bound to each  #
# of the keys, or Labels, on the piano that plays the    #
# sound tied to the Label passed in through event,       #
# records that note to the file 'song.txt' and calls     #
# label_pressed for that Label.                          #
#                                                        #
# Accepts: event, the mouse event that is tied to the    #
# Label that is clicked.                                 #
##########################################################
def button_pressed(event):
    wave_obj = sa.WaveObject.from_wave_file('sounds/' + event.widget.name + '.wav')
    wave_obj.play()
    if recording:
        record('songs/song.txt', event.widget.name)
    label_pressed(event)

# KEYS_TO_NOTES is a dictionary that ties note
# names to certain keys on the keyboard.
KEYS_TO_NOTES = {
    'z': '60',
    'x': '62',
    'c': '64',
    'v': '65',
    'b': '67',
    'n': '69',
    'm': '71',
    's': '61',
    'd': '63',
    'g': '66',
    'h': '68',
    'j': '70',
    'Z': '72',
    'X': '74',
    'C': '76',
    'V': '77',
    'B': '79',
    'N': '81',
    'M': '83',
    'S': '73',
    'D': '75',
    'G': '78',
    'H': '80',
    'J': '82',
}


##########################################################
# Description: Piano is a class that initializes the     #
# window and populates it with all of the necessary      #
# Labels needed to play the piano.                       #
#                                                        #
# Accepts: Frame, which contains the Tkinter window      #
# object.                                                #
##########################################################
class Piano(Frame):

    ##########################################################
    # Description: __init__ is a method that creates         #
    # the window, colors it and calls init_user_interface.   #
    #                                                        #
    # Accepts: self, which contains the window; parent,      #
    # which is a reference to the window.                    #
    ##########################################################
    def __init__(self, parent):

        # This is the initialization of the window along with the
        # coloring of the background.
        Frame.__init__(self, parent, background='SkyBlue3')

        # So that the parent reference does not go out of scope.
        self.parent = parent

        # A call to the init_user_interface method.
        self.init_user_interface()

    ##########################################################
    # Description: init_user_interface is a method that      #
    # populates the window passed in all of the Labels,      #
    # sizes the window, titles it, centers it on the screen  #
    # and binds various methods to it.                       #
    #                                                        #
    # Accepts: self, which contains the window.              #
    ##########################################################
    def init_user_interface(self):

        # The 2-dimensional array keys holds the locations, names and after the
        # for loops are executed below, the Labels that are needed
        # to create each key, both white and black.
        keys = [
            [0, '60'],
            [35, '61'],
            [50, '62'],
            [85, '63'],
            [100, '64'],
            [150, '65'],
            [185, '66'],
            [200, '67'],
            [235, '68'],
            [250, '69'],
            [285, '70'],
            [300, '71'],
            [350, '72'],
            [385, '73'],
            [400, '74'],
            [435, '75'],
            [450, '76'],
            [500, '77'],
            [535, '78'],
            [550, '79'],
            [585, '80'],
            [600, '81'],
            [635, '82'],
            [650, '83']
        ]

        # This for loop populates the window with the white key Labels
        # and appends a Label to each slot in keys.
        for key in keys:
            if not key[1] in black_key:
                img = 'pictures/white_key.gif'
                key.append(self.create_key(img, key))

        # This for loop populates the window with the black key Labels
        # and appends a Label to each slot in keys.

        for key in keys:
            if key[1] in black_key:
                img = 'pictures/black_key.gif'
                key.append(self.create_key(img, key))

        # This group of lines creates the record Label.
        img = PhotoImage(file='pictures/red_button.gif')
        record_button = Label(self, image=img, bd=0)
        record_button.image = img
        record_button.place(x=700, y=0)
        record_button.name = 'red_button'
        record_button.bind('<Button-1>', record_on_off)

        # This group of lines creates the play Label.
        img = PhotoImage(file='pictures/green_button.gif')
        play_button = Label(self, image=img, bd=0)
        play_button.image = img
        play_button.place(x=700, y=50)
        play_button.name = 'green_button'
        play_button.bind('<Button-1>', play_back)
        play_button.bind('<ButtonRelease-1>', label_released)

        # This titles the window.
        self.parent.title('The Piano')

        # This group of lines centers the window on the screen
        # and specifies the size of the window.
        w = 750
        h = 200
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # This group of lines saves a reference to keys so that
        # it does not go out of scope and binds the presses and
        # releases of keys to their respective methods
        self.parent.keys = keys
        self.parent.bind('<KeyPress>', key_pressed)
        self.parent.bind('<KeyRelease>', key_released)

        # These 2 lines bind the '1' and '2' keys on the keyboard
        # to the playback method, which then hooks them up to their
        # respective files. This is mostly for demonstration and
        # experimentation purposes.
        self.parent.bind('1', play_back)
        self.parent.bind('2', play_back)

        # This line packs all elements bound to the window.
        self.pack(fill=BOTH, expand=1)

    ##########################################################
    # Description: create_key is a method that creates and   #
    # returns a Label with an image, a location, a name and  #
    # multiple bindings.                                     #
    #                                                        #
    # Accepts: self, the Piano class; img, the image that    #
    # the Label will be displayed as; key, the element of    #
    # the 2-dimensional array passed in.                     #
    ##########################################################
    def create_key(self, img, key):
        key_image = PhotoImage(file=img)
        label = Label(self, image=key_image, bd=0)
        label.image = key_image
        label.place(x=key[0], y=0)
        label.name = key[1]
        label.bind('<Button-1>', button_pressed)
        label.bind('<ButtonRelease-1>', label_released)
        return label


# The main method creates an instance of the Piano class
# and keeps it running until termination.
def main():
    root = Tk()
    app = Piano(root)
    app.mainloop()

if __name__ == '__main__':
    main()