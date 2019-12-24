#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This is the MAIN of Aequus training app.

The script includes: interactive application suitable for
rehabilitation of people with multiple sclerosis, setup and calibration of
MPU6050 sensors, reading and processing data from sensors.

All credits go to the people who collaborated on the project
of the DiSfida non profit competition organized by the Politecnico di Milano in
collaboration with NEARlab.
"""

__author__ = "Manuel Carzaniga, Lorenzo Gualniera."
__credits__ = ["Manuel Carzaniga", "Lorenzo Gualniera"]
__version__ = "1.0.1"

import os
import pygame
import time

# Import classes from MPU6050
from MPU6050 import *

# Import classes from MPU_processing
from MPU_processing import mpu_sensor
from MPU_processing import multiplex

# Import classes from disfida_menu
from disfida_menu import Init_menu
from disfida_menu import Main_menu
from disfida_menu import Pref_menu
from disfida_menu import Setup_menu
from disfida_menu import Train_menu

# File path for sensors calibration
mpu0_path = "../Calibration/mpu0_cal.txt"
mpu1_path = "../Calibration/mpu1_cal.txt"
mpu2_path = "../Calibration/mpu2_cal.txt"
mpu3_path = "../Calibration/mpu3_cal.txt"
mpu4_path = "../Calibration/mpu4_cal.txt"
mpu5_path = "../Calibration/mpu5_cal.txt"

# Pygame constants
W_SIZE = 480            # Width in pixel
H_SIZE = 320            # Height in pixel
FPS = 60                # Frame per second

# Mux costants
i2c_bus = 1
mux_address = 0x70


def select_menu(posx, posy):
    """Select the screen requested by the user."""
    global Menu_APP, Duration, Difficulty
    MENU_STATE = Menu_APP.controls(posx, posy)
    if Menu_APP.__class__.__name__ == "Main_menu":
        if MENU_STATE == "Training":
            Menu_APP = Train_menu(Surface)
        # TODO: implement the others button on the main menu
        '''
        elif MENU_STATE == "Progress":
            Menu_APP = Prog_menu(Surface)
        elif MENU_STATE == "Options":
            Menu_APP = Option_menu(Surface)
        '''
    elif Menu_APP.__class__.__name__ == "Train_menu":
        if MENU_STATE == "Home":
            Menu_APP = Main_menu(Surface)
        elif MENU_STATE == "Start":
            Menu_APP = Setup_menu(Surface)
        elif MENU_STATE == "Preference":
            Menu_APP = Pref_menu(Surface, Duration, Difficulty)
    elif Menu_APP.__class__.__name__ == "Pref_menu":
        if MENU_STATE == "Back":
            Menu_APP = Train_menu(Surface)
        elif MENU_STATE == "Preference":
            Menu_APP = Pref_menu(Surface)
        else:
            Duration = Menu_APP.duration
            Difficulty = Menu_APP.difficulty
    elif Menu_APP.__class__.__name__ == "Init_menu":
        if MENU_STATE == "Back":
            Menu_APP = Train_menu(Surface)
        '''
        elif MENU_STATE == "Start":
            Menu_APP = Init_menu(Surface, Difficulty, Duration)
        '''


if __name__ == "__main__":
    # Pygame initialization
    pygame.init()
    pygame.font.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption('AEQUUS TRAINING APP')

    # Screen resolution calculation
    infoObject = pygame.display.Info()
    Screen_scale = (infoObject.current_h / H_SIZE)
    Surface = pygame.display.set_mode((int(W_SIZE * Screen_scale), int(H_SIZE * Screen_scale)))

    # Init training values prefereces
    Difficulty = "Low"
    Duration = 5

    # Init main menu
    Menu_APP = Main_menu(Surface)

    # Timer and clock
    Clock = pygame.time.Clock()
    timer = 0.0
    dt = 1.0 / FPS

    # Init mux i2c
    mux = multiplex(i2c_bus)

    while(True):

        # Tick clock
        Clock.tick(FPS)
        timer += dt

        # Menu events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                select_menu(Mouse_x, Mouse_y)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

        # Init sensors and i2c errors handling
        if Menu_APP.__class__.__name__ == "Setup_menu":
            try:
                mux.channel(mux_address, 0)
                mpu0 = mpu_sensor("mpu0", mpu0_path)
                Menu_APP.conn_sensor(mpu0.name, "Connected")
            except IOError:
                Menu_APP.conn_sensor(mpu0.name, "Error")
            for load in range(0, 18):
                Menu_APP.draw_loading(load)
                time.sleep(0.05)
            try:
                mux.channel(mux_address, 1)
                mpu1 = mpu_sensor("mpu1", mpu1_path)
                Menu_APP.conn_sensor(mpu1.name, "Connected")
            except IOError:
                Menu_APP.conn_sensor(mpu1.name, "Error")
            for load in range(18, 35):
                Menu_APP.draw_loading(load)
                time.sleep(0.05)
            try:
                mux.channel(mux_address, 2)
                mpu2 = mpu_sensor("mpu2", mpu2_path)
                Menu_APP.conn_sensor(mpu2.name, "Connected")
            except IOError:
                Menu_APP.conn_sensor(mpu2.name, "Error")
            for load in range(18, 52):
                time.sleep(0.05)
                Menu_APP.draw_loading(load)
            try:
                mux.channel(mux_address, 3)
                mpu3 = mpu_sensor("mpu3", mpu3_path)
                Menu_APP.conn_sensor(mpu3.name, "Connected")
            except IOError:
                Menu_APP.conn_sensor(mpu3.name, "Error")
            for load in range(52, 69):
                time.sleep(0.05)
                Menu_APP.draw_loading(load)
            try:
                mux.channel(mux_address, 4)
                mpu4 = mpu_sensor("mpu4", mpu4_path)
                Menu_APP.conn_sensor(mpu4.name, "Connected")
            except IOError:
                Menu_APP.conn_sensor(mpu4.name, "Error")
            for load in range(69, 86):
                time.sleep(0.05)
                Menu_APP.draw_loading(load)
            try:
                mux.channel(mux_address, 5)
                mpu5 = mpu_sensor("mpu5", mpu5_path)
                Menu_APP.conn_sensor(mpu5.name, "Connected")
            except IOError:
                Menu_APP.conn_sensor(mpu5.name, "Error")
            for load in range(86, 101):
                time.sleep(0.05)
                Menu_APP.draw_loading(load)
            # If all the sensors are connected go on, otherwise come back
            time.sleep(1)
            if Menu_APP.check_sensors():
                Menu_APP = Init_menu(Surface, Duration, Difficulty)
            else:
                Menu_APP = Train_menu(Surface)
