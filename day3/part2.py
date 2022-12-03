
def solve() -> int:
    with open('input.txt', 'r') as file:
        lines: list = [line for line in file][:3]
        print(lines)
        result: int = 0

    return -1
def get_value(letter: str) -> int:
    off: int = 96 if letter.islower() else 38
    return ord(letter) - off
    
def main() -> None:
    print(solve())

if __name__ == '__main__':
    main()
