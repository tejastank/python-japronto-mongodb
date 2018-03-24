import os.path
from mongoengine import *
from japronto import Application


app = Application()
r = app.router

def index(request):
    return request.Response(json={'company': 'snippetbucket'})

r.add_route('/', index, method='GET')

app.run(debug=True)

