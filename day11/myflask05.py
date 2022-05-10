from flask import Flask,render_template,jsonify
from day10.dao_emp import DaoEmp
app = Flask(__name__)
de = DaoEmp()
@app.route('/emp')
def emp():
    return render_template('emp.html')

@app.route('/ajax')
def ajax():
    mylist = de.myselects()
    return jsonify({'mylist': mylist})


if __name__ == '__main__':
    app.run(debug=True)