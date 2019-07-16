import csv

# Avataan csv tiedosto ja koitetaan saada se käyttöön radan valinnassa
# Vielä tulostellaan testin vuoksi lista mitä tiedosto pitää sisällään
with open('cfg/radat.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    trackids = []
    tracknames = []
    for row in readCSV:
        trackid = row[0]
        trackname = row[1]

        trackids.append(trackid)
        tracknames.append(trackname)
        print(row)