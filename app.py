from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/beta')
def beta():
    return 'Halo Beta Sign-Up Coming Soon!'

if __name__ == '__main__':
    app.run(debug=True)