from random import randint
def switch(runs: int, switch: bool) -> tuple:
    lost: int = 0
    won: int = 0
    for i in range(1, runs+1):
        pick: int = randint(0, 2)
        correct: int = randint(0, 2)
        if switch:
            if pick != correct:
                won += 1
            if pick == correct:
                lost += 1
        else:
            if pick == correct:
                won += 1
            if pick != correct:
                lost += 1
        print(i)
    return lost, won

def main():
    lost, won = switch(int(input("How many time do you want to open a door? ")), bool(input("Do you want to switch every time (True, False)? ")))
    print(f"You lost {lost} times.")
    print(f"You won {won} times.")
if __name__ == '__main__':
    main()