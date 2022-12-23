from flask import Flask, request
from lights import cycleTo

app = Flask(__name__)

def switchLights(mode):
    cycleTo(mode)

@app.route("/")
def lights_change_status():
    api_key = "IR4OiaIvsh3iBh0"
    authheader = request.headers.get('api-key')

    if authheader != api_key:
        return "Key invalid, permission denied...", 403

    print("The key's valid!")
    switchLights(int(request.args.get("mode")))
    return "Light status changed", 200


app.run("0.0.0.0")
