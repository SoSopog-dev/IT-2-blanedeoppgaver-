"""
Oppgave 3
"""


def int_input():

    i = input("\nSkriv inn en månede (der Jan = 1 Feb = 2 osv): ")
    
    try:
        i = int(i)
        return i
    except:
        print("\nSvar ikke godkjent")

        not_int = True
        while not_int:
            i = input("\nPrøv på nytt, skriv inn en månede (der Jan = 1 Feb = 2 osv):")

            try:
                i = int(i)
                return i
            except:
                pass


    return i

def main():
    maaneder = "JanFebMarAprMaiJunJulAugSepOktNovDes" #Dette er både en rotete å stygg måte å lagre dataene på, noe bedre hadde vært ["Jan", "Feb", ...]
    m = list(maaneder)

    months = []

    for i in range(0,len(maaneder), 3):
        months.append(m[i] + m[i+1]+ m[i+2])
    
    print(months)
    index = int_input()

    print(months[index-1])
    




if __name__ == "__main__":
    main()
