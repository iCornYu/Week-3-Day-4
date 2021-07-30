import re
file2 = open('Regex.txt')
data2 = [file2.readlines()]
print(data2)
file2.close
homeworkpattern = re.compile('(?P<first_name>[A-Z][a-z]+) (?P<last_name>[\w]+) ?(?P<last_name2>[\w]*)')
for line in data2:
    if homeworkpattern.match(line):
        print(line.strip("\n"))
    else:
        print(None)



