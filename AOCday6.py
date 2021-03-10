def readInput(input):
    data = []
    person = []
    line = ""
    for i in input.readlines():
        i = i.strip()
        if i == "":
            data.append(person)
            person = []
        else:
            person.append(i)
    data.append(person)
    return data


def countAnswers1(input: list[str]) -> int:
    data = readInput(input)
    answers = []
    stripped = ""
    count = 0
    for i in data:
        print(i)
        for s in "".join(i):
            if s not in stripped:
                stripped += s
        count += len(stripped)
        stripped = ""
    return count

def countAnswers2(data: list[str]) -> int:
    data = readInput(data)
    count = 0
    result = 0
    for i in data:
        for j in range(len(i)):
            if j == 0:
                answer = set(i[j])
            else:
                answer = answer.intersection(i[j])
        count += len(answer)
    return count



if __name__ == '__main__':
    input4 = open('inputday6.txt')
    print(countAnswers2(input4))
