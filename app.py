from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def home():
    # Home page with just basic instructions and a link to the recommendations page
    return render_template('index.html')

@app.route('/enter_weather')



if __name__ == '__main__':
    app.run(debug=True)
