def solve() -> int:
    values: dict = {'X': 1, 'Y': 2, 'Z': 3}
    with open('input.txt', 'r') as file:
        lines: list = file.readlines()
        total_score: int = 0
        for line in lines: 
            line = line.strip()
            splited: list = line.split(' ')
            other_play: str = splited[0]
            our_play: str = splited[1]
            outcome: int = get_outcome(other_play, our_play)
            score: int = outcome + values[our_play]
            total_score += score
        return total_score

def get_outcome(a: str, b: str) -> int:
    if a == 'A':
        if b == 'X': return 3
        if b == 'Y': return 6
        if b == 'Z': return 0
    if a == 'B':
        if b == 'X': return 0
        if b == 'Y': return 3
        if b == 'Z': return 6
    if a == 'C':
        if b == 'X': return 6
        if b == 'Y': return 0
        if b == 'Z': return 3
    return -1

def main():
    print(solve())

if __name__ == '__main__':
    main()
