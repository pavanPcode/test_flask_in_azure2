from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello first word in az"

if __name__ == '__main__':
   app.run()

