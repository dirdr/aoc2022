def solve() -> int:
    with open('input.txt', 'r') as file:
        lines: list = [line.strip() for line in file.readlines()]
        result: int = 0
        for line in lines:
            left, right = [get_value(letter) for letter in line[:len(
                line)//2]], [get_value(letter) for letter in line[len(line)//2:]]
            result += sum(list(set(left) & set(right)))
        return result


def get_value(letter: str) -> int:
    off: int = 96 if letter.islower() else 38
    return ord(letter) - off


def main() -> None:
    print(solve())


if __name__ == '__main__':
    main()
