import os, re, csv, sys

regex = re.compile(r"\@([a-z0-9][a-z0-9._-]*)")
contributers = {}
fileCount = 0
fileLocations = []
try:
    if len(sys.argv) == 1:
        fileLocations.append("checkins/")
        fileLocations.append("hackathons/")
    elif len(sys.argv) > 1:
        fileLocations = sys.argv[1:]
    
    for index, path in enumerate(fileLocations):
        for subdir, dirs, files in os.walk(os.path.abspath(path)):
            for noAbsFile in files:
                file = os.path.join(subdir, noAbsFile)
                if file.lower().endswith(".txt"):
                    fileCount+=1
                    file = open(file, 'r')
                    text = file.read()
                    file.close()

                    for (name) in re.findall(regex, text):
                        if name in contributers:
                            contributers[name][index]+=1
                        else:
                            contributers[name]=[0] * (len(fileLocations))
                            contributers[name][index]+=1

    with open('scores.csv', 'w+') as csvfile:
        sortedList = sorted(contributers.items(), key=lambda tup: tup[1], reverse=True)
        wr = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        titleArray = ["name", "score", "hackscore", "total"]
        wr.writerow(titleArray)
        for person, counts in sortedList:
            total = 0
            rowArray = [person]
            for count in counts:
                total += count
                rowArray.append(count)
            rowArray.append(total)
            wr.writerow(rowArray)
    print("Scores from " + str(len(contributers)) + " different members addeds")
except Exception as e:
    print(e.message)