from bottle import route, run, template, view, post, request
import bottle

bottle.TEMPLATE_PATH.insert(0, "C:/Users/Jimi/Documents/Koodaus/ACC Framework/views")


@route('/')
@view('race_template.tpl')
def index():
    options = {
        "race_name": "Jimba race",
        "track_list": [
            {
                "id": "1",
                "name": "TRACK 1"
            },
            {
                "id": "2",
                "name": "TRACK 2"
            }
        ]
    }
    return options

@post("/race")
def lets_race():
    track = request.forms["track"]
    weather = request.forms["weather"]
    
    return template("<h1>Starting race on track: {{track}} Ja sää on arvoltaan: {{weather}}</H1>", dict(track=track, weather=weather))

run(host='localhost', port=8080, debug=True,reloader=True)