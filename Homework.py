import re
file2 = open('Regex.txt')
data2 = [file2.read()]
print(data2)
file2.close
homeworkpattern = re.compile('(?P<first_name>[A-Z][a-z]+) (?P<last_name>[\w]+) ?(?P<last_name2>[\w]*)')
matched = homeworkpattern.finditer(data2)
print(homeworkpattern.findall(data2))
for line in matched:
    if line.group('last_name'):
        print(f"{line.group('first_name')} {line.group('last_name')} {line.group('last_name2')}")
    else:
        print(None)


#could not get a for loop to work through the txt.file. It kept returning letters as the iterables instead of phrases.