from flask import Flask, render_template, request, jsonify
from day10.dao_emp import DaoEmp

app = Flask(__name__, static_url_path='')
de = DaoEmp()
@app.route('/emp')
def emp():
    return render_template("emp.html")

@app.route('/ajax')
def ajax():
    emps = de.myselects()
    return jsonify({'msg': '저장 완료!'}) 

@app.route('/ajax_list')
def ajax_list():
    list = de.myselects()
    return jsonify(list) 

@app.route('/ajax_one')
def ajax_one():
    e_id = request.args.get('e_id')
    one = de.myselect(e_id);
    return jsonify(one)

@app.route('/ajax_del')
def ajax_del():
    e_id = request.args.get('e_id')
    cnt = de.mydelete(e_id);
    msg = "ng"
    if cnt==1:
        msg = "ok"
        
    return jsonify(msg)

@app.route('/ajax_ins',methods=['POST'])
def ajax_add():
    data = request.get_json();
    e_id = data['e_id']
    e_name = data['e_name']
    sex = data['sex']
    addr = data['addr']
    cnt = de.myinsert(e_id, e_name, sex, addr)
    msg = "ng"
    if cnt==1:
        msg = "ok"
        
    return jsonify(msg)

@app.route('/ajax_upd',methods=['POST'])
def ajax_upd():
    data = request.get_json();
    e_id = data['e_id']
    e_name = data['e_name']
    sex = data['sex']
    addr = data['addr']
    cnt = de.myupdate(e_id, e_name, sex, addr)
    msg = "ng"
    if cnt==1:
        msg = "ok"
        
    return jsonify(msg)

if __name__== "__main__":
    app.run(debug=True)