import os, re, csv, sys

regex = re.compile(r"\@([a-z0-9][a-z0-9._-]*)")
contributers = {}
fileCount = 0
fileLocations = []
executives = ['sirhype', 'angus', 'sjames5', 'rshanule', 'liam', 'arthur', 'brijesh', 'daniel_connolly', 'daviddob', 'liesel', 'mklein5', 'wguo24']

try:
    if len(sys.argv) == 1:
        fileLocations.append("checkins/")
        fileLocations.append("hackathons/")
    elif len(sys.argv) > 1:
        fileLocations = sys.argv[1:]
    
    for index, path in enumerate(fileLocations):
        if "hack" in path:
            # Adds modifier to 1 when adding values
            modifier = 1
        else:
            modifier = 0
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
                            contributers[name][index]+=(1 + modifier)
                        else:
                            contributers[name]=[0] * (len(fileLocations))
                            contributers[name][index]+=(1 + modifier)

    with open('scores.csv', 'w+') as csvfile:
        sortedList = sorted(contributers.items(), key=lambda tup: tup[1], reverse=True)
        wr = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        titleArray = ["rating", "name", "score", "hackscore", "total"]
        wr.writerow(titleArray)
        ratingIndex = 1
        for person, counts in sortedList:
            if person not in executives:
                total = 0
                rowArray = [ratingIndex, person]
                for count in counts:
                    total += count
                    rowArray.append(count)
                rowArray.append(total)
                wr.writerow(rowArray)
                ratingIndex+=1
    print("Scores from " + str(len(contributers)) + " different members addeds")
except Exception as e:
    print(e.message)