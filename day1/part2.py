def solve() -> int:
    result: list = []
    with open('input.txt', 'r') as file:
        lines: list = file.readlines()
        total_kcal: int = 0
        for line in lines:
            if line.strip():
                total_kcal += int(line.strip())
            else:
                result.append(total_kcal)
                total_kcal = 0
        result.sort()
        result.reverse()
        return result[0] + result[1] + result[2]


def main() -> None:
    print(solve())


if __name__ == '__main__':
    main()
