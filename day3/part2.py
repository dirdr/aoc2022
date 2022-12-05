
def solve() -> int:
    with open('input.txt', 'r') as file:
        _lines: list = [line.strip() for line in file.readlines()]
        lines: list = list(_lines[i: i+3] for i in range(0, len(_lines), 3)) 
        result: int = 0
        for first, second, third in lines:
            badge = (set(first) & set(second) & set(third)).pop()
            result += get_value(badge)
    return result

def get_value(letter: str) -> int:
    off: int = 96 if letter.islower() else 38
    return ord(letter) - off
    
def main() -> None:
    print(solve())

if __name__ == '__main__':
    main()
