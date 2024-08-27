"""
Oppgave 5
"""
from math import floor


def int_input():

    i = input("\nSkriv inn ett årstall (feks 1987): ")
    
    try:
        i = int(i)
        return i
    except:
        print("\nSvar ikke godkjent")

        not_int = True
        while not_int:
            i = input("\nPrøv på nytt, Skriv inn ett årstall (feks 1984):")

            try:
                i = int(i)
                return i
            except:
                pass


    return i

def number_to_month(n):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Des']

    return months[n-1]

def modulus(a, b):
    
    return a % b, floor(a/b)

def calculate_easter(year):

    a, _ = modulus( year, 19 )

    c, b = modulus( year,  100 )

    e, d = modulus( b,  4 )

    _, f = modulus( (b+8),  25 )

    _, g = modulus((b - f + 1),  3)

    h, _ = modulus((19 * a + b -d -g + 15), 30)

    k , i = modulus(c, 4)
    l, _ = modulus( (32 + 2 * e + 2* i - h- k), 7)
    _, m = modulus( a + 11 * h + 22* l, 451)
    p, n = modulus( h + l - 7*m + 114, 31)

    print(f"\nPåsken faller på den {p+1}. i måneden {number_to_month(n)}")

def main():
    year = int_input()

    calculate_easter(year)






if __name__ == "__main__":
    main()