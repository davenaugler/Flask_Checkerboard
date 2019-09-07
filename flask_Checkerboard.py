from flask import Flask, render_template

app = Flask(__name__)

# 1. http://localhost:5000 - should display 8 by 8 checkerboard
@app.route('/')
def checkerboard():
    num = int(8)
    return render_template("index.html", times=num, another=num, color1='black', color2='red')

# 2. http://localhost:5000/4 - should display 8 by 4 checkerboard
@app.route('/<num>')
def numCheckerboard(num):
    num=int(num)
    return render_template("index.html", times=num, another=8, color1='black', color2='red')

# 3. http://localhost:5000/(x)/(y) - should display x by y checkerboard.
@app.route('/<x>/<y>')
def choiceCheckerboard(x, y):
    num=int(x)
    rem=int(y)

    return render_template("index.html", times=rem, another=num, color1='black', color2='red')

@app.route('/<x>/<y>/<color1>/<color2>')
def colorCheckerboard(x, y, color1, color2):
    num=int(x)
    rem=int(y)

    return render_template("index.html", times=rem, another=num, color1=color1, color2=color2 )











if __name__=="__main__":
    app.run(debug=True)