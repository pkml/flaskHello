# ----fLASK hELLO wORLD ----#

#Import the flask class 
from flask import Flask

# create the application obj
app = Flask(__name__)

#use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

#define the view using a function, which returns a string
def hello_world():
    return "Hello, World!"

#start the development server using hte run() method
if __name__ == "__main__":
    app.run()
