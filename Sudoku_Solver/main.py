from flask import Flask, render_template, redirect, url_for, request,session
import solver
from datetime import timedelta

app = Flask(__name__,static_url_path='')

app.secret_key="madafaka" #secretkey for session to keep cyroted in server

app.permanent_session_lifetime = timedelta(days= 1) # we define permanent session life time duration


class Htmls():
    def __init__(self, *args, **kwargs):
        self.HOME = "home.html"
        self.SOLVED = "solved.html"

htmls = Htmls()

def create9x9List():
        line = []
        table = []
        for i in range(9):
            line.append([])
        for j in range(9):
            table.append(line.copy())
        return table

@app.route("/",methods=["POST","GET"])
def home():
    if "solvedlist" in session:
        session.pop("solvedlist",None)
    if request.method == "POST":
        session.permanent = True
        takenlist = create9x9List()
        for i,line in enumerate(takenlist):
            for j,grid in enumerate(line):
                formkey = str(i)+","+str(j)
                value = request.form[formkey]
                if value == "":
                    value=0
                else:
                    value = int(value)
                line[j]=value
        game = solver.Game(table=takenlist)
        game.solve()
        game.show()
        session["solvedlist"] = takenlist
        return redirect(url_for("solved"))
    return render_template(htmls.HOME)

@app.route("/solved", methods=["POST","GET"])
def solved():
    if request.method == "POST":
        return redirect(url_for("home"))
    if "solvedlist" in session:
        solvedlist= session["solvedlist"]
    return render_template(htmls.SOLVED,solvedlist=solvedlist)



if __name__ == "__main__":
    app.run(debug=True)