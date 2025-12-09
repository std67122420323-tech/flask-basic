from flask import Flask 
import uuid
app = Flask(__name__) 
@app.route('/') 
def index(): 
    return f"""<!DOCTYPE html> 
<html lang="en"> 
 <head> 
  <meta charset="UTF-8"> 
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
  <title>Flask Basic</title> 
 </head>
 <body> 
  <h1>Home page</h1>
  <hr>
  </body>
</html>
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    
@app.route('/name') 
def name(): 
      return "<h1>surachai</h1>"

@app.route('/user/<username>')
def user(username): 
    return f"<h1>my name is {username}</h1>"

@app.route('/calculate/addition/<int:a>/<int:b>')
def addition(a, b): 
    return f"<{a}+{b}: {a + b}</h1>"

@app.route('/calculate/subtraction/<int:a>/<int:b>')
def subtraction(a, b): 
    return f"<{a}-{b}: {a - b}</h1>"

@app.route('/calculate/multiplication/<int:a>/<int:b>')
def multiplication(a, b): 
    return f"<{a}*{b}: {a * b}</h1>"

@app.route('/calculate/division/<int:a>/<int:b>')
def division(a, b): 
    return f"<{a}/{b}: {a / b}</h1>"

@app.route('/secretkey/<uuid:sk>')
def my_secretkey(sk):
    return f"<h1>my secret key is {sk}</h1>"
##if __name__ == '__main__': ##app.run(debug=True)
