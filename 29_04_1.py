from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def carusel():
    return render_template('car.html')

@app.route('/second')
def car_2():
    return render_template('car_2.html')

@app.route('/third')
def car_3():
    return render_template('car_3.html')


if __name__ == "__main__":
    app.run()
