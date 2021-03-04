import re

def passport(data):
    input = data.read().split("\n\n")
    count = 0
    myList = ["byr", "eyr", "iyr", "hgt", "hcl", "ecl", "pid"]
    eclList = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    for i in input:
        if all(x in i for x in myList):
            j = re.split("[ \n]", i)
            j.sort()
            if j[1][:3] == "cid":
                j.remove(j[1])

            if re.findall("^[0-9]*$", j[0].split(":")[1]) and len(j[0].split(":")[1]) == 4:
                byr = int(j[0].split(":")[1])
            else:
                continue

            if re.findall("[A-Za-z]", j[1].split(":")[1]) and len(j[1].split(":")[1]) == 3:
                ecl = j[1].split(":")[1]
            else:
                continue

            if re.findall("^[0-9]*$", j[2].split(":")[1]) and len(j[2].split(":")[1]) == 4:
                eyr = int(j[2].split(":")[1])
            else:
                continue

            if re.findall("[A-Za-z0-9]", j[4].split(":")[1]) and 6 > len(j[4].split(":")[1]) > 3:
                hgt = j[4].split(":")[1]
            else:
                continue

            if j[3].split(":")[1][0] == "#" and re.findall("^[0-9a-f]*$", j[3].split(":")[1][1:]):
                hcl = j[3].split(":")[1]
            else:
                continue

            if re.findall("^[0-9]*$", j[5].split(":")[1]):
                iyr = int(j[5].split(":")[1])
            else:
                continue

            if re.findall("^[0-9]*$", j[6].split(":")[1]):
                pid = j[6].split(":")[1]
            else:
                continue

            # print(byr, ecl, eyr, hcl, hgt, iyr, pid)
            if 2002 >= byr >= 1920:
                if 2020 >= iyr >= 2010:
                    if 2030 >= eyr >= 2020:
                        if ecl in eclList:
                            if len(pid) == 9:
                                if len(hgt) == 5:
                                    if hgt[-2:] == "cm" and 193 >= int(hgt[:3]) >= 150:
                                        count += 1
                                elif len(hgt) == 4:
                                    if hgt[-2:] == "in" and 76 >= int(hgt[:2]) >= 59:
                                        count += 1
        # else:
        #     print(i)

    return count
