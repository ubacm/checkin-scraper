import os, re, csv, sys

regex = re.compile(r"\@([a-z0-9][a-z0-9._-]*)")
contributers = {}
fileCount = 0

try:
    directory_name=sys.argv[1]
    for subdir, dirs, files in os.walk(os.path.abspath(directory_name)):
        for noAbsFile in files:
            file = os.path.join(subdir, noAbsFile)
            if file.lower().endswith(".txt"):
                fileCount+=1
                file = open(file, 'r')
                text = file.read()
                file.close()
                # name = regex.search(text)
                for (name) in re.findall(regex, text):
                    if name in contributers:
                        contributers[name]+=1
                    else:
                        contributers[name]=1

    with open('people.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for person, count in contributers.items():
            wr.writerow([person, count])
    print(len(contributers))
    print(directory_name)
except Exception as e:
    logger.error('Exception occured: ' + str(e))