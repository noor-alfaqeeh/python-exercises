from flask import Flask, render_template
app = Flask(__name__)

#...............exercise1..........

#@app.route('/')  
#def index():
#    return 'This is the Index page'
#
#@app.route('/hello')  
#def hello():
#    return 'Hello World!'
#
#@app.route('/members')  
#def members():
#    return 'Members Page'
#
#if __name__ == '__main__':
#    app.run()


#...............exercise2..........
#@app.route('/marks/<int:score>')  
#def hello_name(score):
#    return render_template('index.html', marks = score)



#...............exercise3..........
@app.route('/css')
def css():
  return render_template('index2.html')

if __name__ == '__main__':
    app.run()