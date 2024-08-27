"""
Oppgave 3
"""

def main():
    mountains = [
        ["Galdhøpiggen", 2469],
        ["Glittertind", 2452],
        ["Store Skagastøltind", 2405],
        ["Store Styggedalstind", 2387],
        ["Skardstinden", 2373]
    ]

    shortest_name_length = min( [ len(mountain[0]) for mountain in mountains] ) # Vi må passe på at vi ikke forkorter den til noe lengere enn den korteste

    print("\n Dette er fjellene:")

    for mountain in mountains:
        mountain[0] = mountain[0][:shortest_name_length]

        print(f"\n {mountain[0]} | {mountain[1]}moh")


    


if __name__ == "__main__":
    main()