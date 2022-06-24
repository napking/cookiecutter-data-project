# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:08:26 2022

@author: Dave

#util/get_data.py

Utility functions to retrieve and store interim data elsewhere in the project.
run: from src.util.get_data import {function name}
"""
import shelve
from config.definitions import ROOT_DIR, DATA_DIR, DATA_INTERIM_DIR, SHELF_NAME

#%% Shelving

def get_interim_data(interim_directory=DATA_INTERIM_DIR, key='default',
                     shelf_name=SHELF_NAME ):
    with shelve.open(str(interim_directory / shelf_name)) as shelf:
        return shelf[key]

def store_interim_data(interim_data, key, interim_directory=DATA_INTERIM_DIR,
                    shelf_name=SHELF_NAME ):
    with shelve.open(str(interim_directory / shelf_name)) as shelf:
        shelf[key] = interim_data
        return None

def get_interim_keys(interim_directory=DATA_INTERIM_DIR,
                     shelf_name=SHELF_NAME):
    with shelve.open(str(interim_directory / shelf_name)) as shelf:
        return list(shelf.keys())
