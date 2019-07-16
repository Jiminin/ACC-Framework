from bottle import route, run, template, view, post, request
import bottle
import csv

# Avataan csv tiedosto ja koitetaan saada se käyttöön radan valinnassa
# Vielä tulostellaan testin vuoksi lista mitä tiedosto pitää sisällään
with open('cfg/radat.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    trackid = []
    trackname = []
    for row in readCSV:
        trackid.append(row[0])
        trackname.append(row[1])
        print(row)
        

bottle.TEMPLATE_PATH.insert(0, "C:/Users/Jimi/Documents/Koodaus/ACC Framework/views")

# Mitä arvoja lähetetään selaimeen ja mitä sieltä pyydetään täyttämään/valitsemaan
@route('/')
@view('race_template.tpl')
def index():
    options = {
        "race_name": "Jimba race",
        "track_list": [
            {
                "id": trackid,
                "name": trackname
            },
            {
                "id": "ID2",
                "name": "ID2 Nimi"
            },
            {
                "id": "ID3",
                "name": "ID3 Nimi"
            }
        ]
    }
    return options


# Pyydetään tietoja mitä selaimessa on annettu ja lähetetään ne seuraavaan kaavakkeeseen/conffi tiedostoon
@post("/race")
def lets_race():
    track = request.forms["track"]
    weather = request.forms["weather"]
    
    return template("<h1>Starting race on track: {{track}} Ja sää on arvoltaan: {{weather}}</H1>", dict(track=track, weather=weather))

run(host='localhost', port=8080, debug=True,reloader=True)