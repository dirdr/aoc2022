def solve() -> int:
    with open('input.txt', 'r') as file:
        result: int = 0
        root: list = []
        lines = [line.rstrip() for line in file.readlines()]
        for line in lines:
            print(line)
    return result


def main() -> None:
    print(solve())


if __name__ == '__main__':
    main()
