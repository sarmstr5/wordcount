import os

dir = '../sotu/'
files = os.listdir(dir)
target_files = []
count = 0
for f in files:
    if '.txt' in f:
        datelist = f.split('.')
        year = datelist[0][:4]
        if int(year) > 1984:
            target_files.append(f)
target_files = sorted(target_files)
print(target_files)

with open('1985andlater2.txt', 'w') as output:
    for f in target_files:
        with open(dir+f) as newfile:
            print(f)
            for line in newfile:
                output.write(line)
        output.write('\n')
