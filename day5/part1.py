def solve() -> str:
    with open('input.txt', 'r') as file:
        lines: list = [line.strip() for line in file.readlines()]
        splited: list = []
        index: int = 0

        for line in lines:
            if line and line[0] == '[':
                index += 1
                _splited = [line[i] for i in range(1, len(line), 4)]
                splited.append(_splited)
            else:
                break

        index += 2
        _max = max([len(stack) for stack in splited])
        stack_list: list = [[] for _ in range(_max)]
        for arr in splited:
            if len(arr) < _max:
                arr.append(' ')

        for col in range(_max):
            for row in range(len(splited) - 1, -1, -1):
                token: str = splited[row][col]
                if token != ' ':
                    stack_list[col].append(token)

        for line in lines[index:]:
            splited = line.split(' ')
            to_move, from_stack, to_stack = int(splited[1]), int(
                splited[3]) - 1, int(splited[5]) - 1
            for _ in range(to_move):
                temp: int = stack_list[from_stack].pop()
                stack_list[to_stack].append(temp)

        return ''.join(stack.pop() for stack in stack_list if stack)


def main() -> None:
    print(solve())


if __name__ == '__main__':
    main()
