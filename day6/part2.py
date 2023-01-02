def solve() -> int:
    with open('input.txt', 'r') as file:
        line = file.readlines()[0].rstrip()
        print(line[1230:])
        cons: int = 0
        seen = set()
        count: int = 0
        for char in line:
            if char in seen:
                seen.clear()
                seen.add(char)
                cons = 1
            else:
                cons += 1
                if cons == 14:
                    return count
                seen.add(char)
            count += 1
    return -1


def main() -> None:
    print(solve())


if __name__ == '__main__':
    main()
