# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 08:57:32 2019

@author: barto
"""

num_pins = 256
drill_up_pos = 10.0
drill_down_pos = -9.0
spindle_speed = 1000
drill_feed = 1600
output_filename = "drill.nc"

f_gcode = open(output_filename, "w")


f_gcode.write("G21\n") # metric mode
f_gcode.write("G90\n") # absolute mode
f_gcode.write("G55\n") # drill fixture is zero'd in G55
f_gcode.write(f'G0 Z{drill_up_pos:.2f}\n')
f_gcode.write("G0 X0\n")
f_gcode.write(f'S{spindle_speed:.2f}\n') # set RPM
f_gcode.write("M3\n") # spindle on
f_gcode.write("G4 P5.0\n") # wait a while for spinup


for pin_number in range(num_pins):
    f_gcode.write(f'G0 X{pin_number:.2f}\n') # go to the pin to drill
    f_gcode.write(f'G1 Z{drill_down_pos:.2f} F{drill_feed:.2f}\n') # drill
    f_gcode.write(f'G0 Z{drill_up_pos:.2f}\n') # move up
    

f_gcode.write("M5\n") # spindle off
f_gcode.write("G54\n") # back to G54
    
f_gcode.close

