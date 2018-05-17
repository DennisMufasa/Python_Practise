from math import pi
def volume(r,h):

    vol=pi*r*r*h
    return vol

r=input("enter cylinder's radius")
r=float(r)
h=input("enter cylinder height")
h=float(h)
vol=volume(r,h)

print("Volume of your cylinder is ",vol)
