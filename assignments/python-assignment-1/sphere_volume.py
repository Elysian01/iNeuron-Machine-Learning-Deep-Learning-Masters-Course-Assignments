"""
    Write a Python program to find the volume of a sphere with diameter 12 cm
"""
import math

if __name__ == '__main__':
    diameter = 12
    radius = diameter/2
    volume = 4/3 * math.pi * (radius)**3
    print(f"Volume of sphere with diameter {diameter} is {volume}")
