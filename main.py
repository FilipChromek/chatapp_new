

import flask
import flask_socketio


app = flask.Flask(__name__, template_folder='templates', static_folder='static')
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'klucpresifrovaniekomunikacie_12345_hmm'

socketio = flask_socketio.SocketIO(app)

@app.route("/",methods=["POST", "GET"])
def home():
    if flask.request.method == "POST":

        zoznam=(flask.session)["text"]
        
        text=flask.request.form.get("text")
        zoznam.append(text)
        (flask.session)["text"]=zoznam

        #print((flask.session)["text"])
        #((flask.session)["text"]).append(text)
        #print((flask.session)["text"])
        #zoznam.append(text)
        #(flask.session)["text"]=zoznam

        return flask.render_template(f"home.html",premenna=zoznam)
            
            
        
    if flask.request.method == "GET":
        
        (flask.session)["text"]=[]

        #print((flask.session)["text"])
        return flask.render_template(f"home.html",premenna=())
if __name__ == "__main__":
    #socketio.run(app, debug=True,port=1000)
    app.run("0.0.0.0",threaded=True,port=10000,debug=True)
    #serve(app, host='0.0.0.0', port=10000)