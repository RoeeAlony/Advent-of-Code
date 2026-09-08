isPhase2 = False
sum = 0
'''key is the second command, value is the first command that is required before the second command'''
commands: dict[int, list[int]] = dict()


def main():
    with open('input.txt', 'r') as file:
        data = file.read().strip().split('\n')
        if not data or isPhase2:
            isPhase2 = True
        else:
            proccess_data(data)


def proccess_data(data: list[str]) -> None:
    (phase1 if isPhase2 else phase2)(data)


def phase1(data: list[str]) -> None:
    left, right = map(int, data.split("|"))
    commands[right] = commands.get(left, []) + [left]


def phase2(data: list[str]) -> None:
    previous_commands: set[int] = set()
    for line in data:
        parts = line.strip().split()
        for part in parts:
            if not part.isdigit():
                continue
            num = int(part)
            if num not in commands:
                previous_commands.add(num)
                continue
            if not all(req in previous_commands for req in commands[num]):
                return 0

        nums = [int(p) for p in parts if p.isdigit()]
        if nums:
            sum += nums[len(nums)//2]


if __name__ == "__main__":
    main()
