from flask import Flask,jsonify

app = Flask(__name__)
@app.route('/details')
def get_details():
    Details={
        "FName": "Abbbo",
        "LName": "Florence",
        "Age": "22years",
        "Course": "ComputerScience",
        "Email": "flo@gmail.com"
    }


    return jsonify(Details)

if __name__=='main':
 app.run(debug = True)