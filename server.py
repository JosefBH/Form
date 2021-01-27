#app.py

from flask import Flask, request, render_template #import main Flask class and request object

app = Flask(__name__, template_folder="templates") #create the Flask app

@app.route('/result', methods=['POST', 'GET'])
def home():
    res = request.form
    result = request.args.get
    if request.method == "POST" and res is not None:
        print(res)
        return render_template('success.html')
    elif request.method == "POST" and result != None :
        print(result)
    else:
        print("None")
        return "erreur : echec"
@app.route('/', methods=['POST', 'GET']) 
def thing():
    res = request.form
    result = request.args.get
    if request.method == "POST" and res is not None:
        print(res)
        return 'you cant imagine how happy i am ! '
    elif request.method == "POST" and result != None :
        print(result)
    else:
        print("None")
        return "erreur : echec"









if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')