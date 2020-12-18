#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import json
import yaml
import random
from yaml import Loader, SafeLoader, FullLoader

def construct_yaml_str(self, node):
    # Override the default string handling function 
    # to always return unicode objects
    return self.construct_scalar(node)

if __name__ == '__main__':

    Loader.add_constructor(u'tag:yaml.org,2002:str', construct_yaml_str)
    SafeLoader.add_constructor(u'tag:yaml.org,2002:str', construct_yaml_str)

    config = yaml.load(open(r"C:\software_projects\python\civ6_leader_picker\civ6_leader_picker\data\config.yaml", "r"), Loader=FullLoader)
    all_leaders = yaml.load(open(config["leaders"], "r"), Loader=SafeLoader)
    all_maps = yaml.load(open(config["maps"], "r"), Loader=FullLoader)
    # picker = LiliPicker(people=names)
    print(all_leaders)

    sg.theme('DarkAmber')	# Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text(text='Leaders:', size=(10,1)), sg.Listbox(values=all_leaders, default_values=all_leaders, size=(30, 10), key='-LEADERS-', enable_events=False, select_mode="multiple")],
                [sg.Text(text='Maps:', size=(10,1)), sg.Listbox(values=all_maps, default_values=all_maps, size=(30, 10), key='-MAPS-', enable_events=False, select_mode="multiple")],
                [sg.Text(text='Opponents:', size=(10,1)), sg.Listbox(values=all_leaders, default_values=all_leaders, size=(30, 10), key='-OPPONENTS-', enable_events=False, select_mode="multiple"), sg.Listbox(values=range(20), size=(2, 1), key='-N_OPPONENTS-', enable_events=False, select_mode="single")],
                [sg.Button('Choose')],
                [sg.Text(text='Leader:', size=(10,1)), sg.Text(size=(30,1), key='-SELECTED_LEADER-')],
                [sg.Text(text='Map:', size=(10,1)), sg.Text(size=(30,1), key='-SELECTED_MAP-')],
                [sg.Text(text='Opponents:', size=(10,1)), sg.Text(size=(30,10), key='-OPPONENT_CHOICES-')],
            ]

    # Create the Window
    window = sg.Window('CIV 6 Game Picker', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    picked = list()
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):	# if user closes window or clicks cancel
            break

        leaders = values["-LEADERS-"]
        maps = values["-MAPS-"]
        opponents = values['-OPPONENTS-']
        n_opponents = values['-N_OPPONENTS-']
        _leader = "NA"
        _map = "NA"
        _opponents = None

        if leaders:
            _leader = random.choice(leaders)
        if maps:
            _map = random.choice(maps)
        if n_opponents:
            if opponents:
                _opponents = opponents
            else:
                _opponents = leaders
            _opponents = random.sample(_opponents, n_opponents[0])
        else:
            _opponents = "NA"
            


        print(_opponents)
        # Update the "output" text element to be the value of "input" element
        window['-SELECTED_LEADER-'].update(_leader)
        window['-SELECTED_MAP-'].update(_map)
        window['-OPPONENT_CHOICES-'].update('\n'.join(_opponents))

    window.close()
