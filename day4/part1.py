def solve():
    with open('input.txt', 'r') as file:
        lines: list = [line.strip() for line in file.readlines()]
        result: int = 0
        for line in lines:
            splited: list = line.split(',')
            left_splited: list = splited[0].split('-')
            right_splited: list = splited[1].split('-')
            left_range: range = range(
                int(left_splited[0]), int(left_splited[1]) + 1)
            right_range: range = range(
                int(right_splited[0]), int(right_splited[1]) + 1)
            if (left_range.start >= right_range.start and left_range.stop <= right_range.stop) or (right_range.start >= left_range.start and right_range.stop <= left_range.stop):
                result += 1
        return result


def main() -> None:
    print(solve())


if __name__ == '__main__':
    main()
