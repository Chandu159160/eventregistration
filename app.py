from flask import Flask,render_template,request
from pymongo import MongoClient

client = MongoClient('mongodb+srv://chanduwarriors973:Batch17@cluster0.y0m04xo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['eventApp']
abc = db['tech']
quiz= db['quiz']
other= db['other']


app = Flask(__name__)

@app.route('/')
def lan():
    return render_template('land.html')

@app.route('/quiz')
def qyuiz():
    return render_template('quiz.html')

@app.route('/techevent')
def tech():
    return render_template('tech.html')

@app.route('/otherevent')
def ot():
    return render_template('other.html')

@app.route('/all')
def all():
    teche = abc.find()
    quize = quiz.find()
    othere = other.find()
    return render_template('all.html',a=teche,b=quize,c=othere)

@app.route('/register/<evename>',methods=['POST'])
def reg(evename):
    if evename=="tech":
        name = request.form['name']
        dept = request.form['department']
        org = request.form['organizer']
        frm = request.form['from']
        to = request.form['to']
        hall = request.form['hall']
        abc.insert_one({"name":name,"dept":dept,"org":org,"from":frm,"to":to,"hall":hall})
        return render_template('tech.html',status="Event confirmed")
    if evename=="quiz":
        name = request.form['name']
        dept = request.form['department']
        org = request.form['organizer']
        topic = request.form['topic']
        frm = request.form['from']
        to = request.form['to']
        hall = request.form['hall']
        quiz.insert_one({"name":name,"dept":dept,"org":org,"from":frm,"to":to,"hall":hall,"topic":topic})
        return render_template('quiz.html',status="Event confirmed")
    if evename=="other":
        name = request.form['name']
        dept = request.form['department']
        org = request.form['organizer']
        frm = request.form['from']
        to = request.form['to']
        hall = request.form['hall']
        other.insert_one({"name":name,"dept":dept,"org":org,"from":frm,"to":to,"hall":hall})
        return render_template('other.html',status="Event confirmed")
        
if __name__=="__main__":
    app.run()