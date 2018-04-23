inFile = open('../data/data.csv', 'rU')
dataStr = inFile.read()
statesStr = dataStr.split('\n\n')
data = dict()

for state in statesStr:
    stateData = dict()
    stateData['top'] = []

    lines = state.split('\n')
    causes = lines[1:11]
    population = int(lines[-1].replace(',', ''))
    
    for cause in causes:
        entries = cause.split(';')

        #name
        entries[0] = entries[0][entries[0].find(' ')+1:]

        #deaths
        entries[1] = int(entries[1].replace(',', ''))

        #rate
        entries[2] = float(entries[2])

        #rank
        entries[3] = int(entries[3].replace(' (tie)', '')[:-2])

        #us rate
        entries[4] = float(entries[4])

        #deaths per 100k
        entries.append(100000*entries[1]/float(population))
        
        stateData["top"].append(entries)
    
    abbrev = state[0:2]
    data[abbrev] = stateData
