"""
Oppgave 2
"""


from math import pi
import matplotlib.pyplot as plt
from numpy import linspace
import csv


def cone(r, h):
    return h/3 * r**2 * pi

def cyllinder(r, h):
    return h * r**2 * pi

def sphere(r):
    return (4/3) * r**3 * pi

def h_given(r, V):
    return (V*3) / (4 * pi * r**2) - r

def save_to_file(R, H):

    filename = "data.csv"

    with open(filename, mode='w', newline='') as file:

        writer = csv.writer(file)

        for r,h in zip(R,H):
            writer.writerow([r,h])

def main():
    TOTAL_VOLUME = 0.5

    # Her må det kommenteres at det finnes mange løsninger så programmet returnerer alle sett med løsninger med verdier fra 0


    R = linspace(0.01, 10, 1000)
    H = [h_given(r, TOTAL_VOLUME) for r in R]

    save_to_file(R,H)

    plt.autoscale(False)

    plt.plot(R,H)
    plt.xlabel('radius')
    plt.ylabel('høyde')
    plt.show()




if __name__ == "__main__":
    main()