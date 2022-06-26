# -*- coding: utf-8 -*-
"""
Created on Thu May 19 22:36:01 2022
@author: hafolahbi
 
"""
import pathlib
import platform
from IPython.display import display

import os
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import segysak
from segysak.segy import segy_header_scrape
os.chdir('/users/hafolahbi/Desktop/SEG_Y_only/')
def extract(file):
    """
    Parameters
    ----------
    file : TYPE
            SEG_Y
        DESCRIPTION.
            Function to extract longitude, latitude and depth of a SEG-Y file obtained from StrataBox
            
            Args:
                Input the SEG_Y file
            
            Returns:
                lon, lat, depth (float array)
            

    Returns
    -------
    lon : TYPE
        DESCRIPTION.
            Longitude of the file
    lat : TYPE
        DESCRIPTION.
            Latitude of the file
    depth : TYPE
        DESCRIPTION.
            Depth of the file

    """
        
    
    #file = input ("Please enter file name:\n")
    file_content = segy_header_scrape(file)
    SourceX = file_content[['SourceX']]
    long = SourceX.size
    lon = np.zeros([long])
    lon = np.squeeze(SourceX, axis = 1)
    lon [:] = lon[:]
    lon = lon/1000 # divide coordinates by 1000 to become actual measured coordinate (see Stratabox manual)
    lon = lon/3600 # Changing arc seconds to degree (3600 arc seconds equals 1 degree)
    
    SourceY = file_content[['SourceY']]
    latt = SourceY.size
    lat = np.zeros([latt])
    lat = np.squeeze(SourceY, axis=1)
    lat [:] = lat[:]
    lat = lat/1000
    lat = lat/3600 # Changing arc seconds to degree (3600 arc seconds equals 1 degree)

    SourceWaterDepth = file_content[['SourceWaterDepth']]
    dep = SourceWaterDepth.size
    depth = np.zeros([dep])
    depth = np.squeeze(SourceWaterDepth, axis=1)
    depth [:] = depth[:]
    depth = depth/10 # divide depth/elevation by 10 to give actual depth reading by Stratabox (See Stratabox manual)
    return lon,lat,depth
