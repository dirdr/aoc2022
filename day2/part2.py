def solve() -> int:
    values: dict = {'A': 1, 'B': 2, 'C': 3}
    outcome_values: dict = {'X': 0, 'Y': 3, 'Z': 6}
    with open('input.txt', 'r') as file:
        lines: list = file.readlines()
        total_score: int = 0
        for line in lines:
            line = line.strip()
            splited: list = line.split(' ')
            other_play: str = splited[0]
            needed_outcome: str = splited[1]
            move: str = get_move(other_play, needed_outcome)
            score = values[move] + outcome_values[needed_outcome]
            total_score += score
        return total_score


def get_move(other_play: str, needed_outcome: str) -> str:
    if needed_outcome == 'X':  # need to loose
        if other_play == 'A':
            return 'C'
        if other_play == 'B':
            return 'A'
        if other_play == 'C':
            return 'B'
    if needed_outcome == 'Y':
        return other_play  # need to draw
    if needed_outcome == 'Z':  # need to win
        if other_play == 'A':
            return 'B'
        if other_play == 'B':
            return 'C'
        if other_play == 'C':
            return 'A'
    return 'error'


def main() -> None:
    print(solve())


if __name__ == '__main__':
    main()
