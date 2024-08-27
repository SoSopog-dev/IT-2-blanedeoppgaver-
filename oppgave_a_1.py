"""
Oppgave 1
"""
from math import pi



def main():
    average_speed = 50 #kph

    #a 

    avstand = 0
    r = 31.83

    avstand += 200 + pi*r*2
    print(f"\nAvstanden rundt banen er {avstand} meter")

    #b

    average_speed_m_s = 50 / 3.6
    print(f"\nGjennomsnittsfarten i m/s er {average_speed_m_s}")

    #c

    time = avstand/average_speed_m_s

    print(f"\nTiden syklisten bruker er {time} sekunder")

if __name__ == "__main__":
    main()