# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:56:42 2023

@author: be
"""

import math

def calculate_max_height(velocity):
    # Calculate the time taken to reach maximum height
    time = velocity / 32  # Assuming gravitational acceleration of 32 ft/s^2

    # Calculate the maximum height using the kinematic equation
    height = (velocity ** 2) / (2 * 32)

    return height

# Prompt the user for the initial velocity
velocity = float(input("Enter the initial velocity (in ft/s): "))

# Call the function to calculate the maximum height
max_height = calculate_max_height(velocity)

# Print the result
print(f"The maximum height reached by the ball is {max_height:.2f} feet.")
