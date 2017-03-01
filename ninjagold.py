from flask import Flask, render_template, redirect, session, request
import random, datetime

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'


@app.route('/')
def index():
    if 'balance' not in session:
        session['balance'] = 0
    if 'messages' not in session:
        session['messages'] = []
    return render_template('index.html', balance=session['balance'], messages=session['messages'] )

@app.route('/process_money', methods=['POST'])
def process():
    if request.form['building'] == "farm":
        print 'farm'
        new_gold = random.randrange(10,21)
        session['balance'] += new_gold
        session['messages'].append("Earned " + str(new_gold) + " golds from the farm! " + str(datetime.datetime.now()))
    elif request.form['building'] == "cave":
        print "cave"
        new_gold = random.randrange(5,11)
        session['balance'] += new_gold
        session['messages'].append("Earned " + str(new_gold) + " golds from the cave! " + str(datetime.datetime.now()))
    elif request.form['building'] == "house":
        print "house"
        new_gold = random.randrange(2,6)
        session['balance'] += new_gold
        session['messages'].append("Earned " + str(new_gold) + " golds from the house! " + str(datetime.datetime.now()))
    elif request.form['building'] == "casino":
        print "casino"
        new_gold = random.randrange(-50,51)
        session['balance'] += new_gold
        if new_gold < 0:
            new_gold = new_gold * -1
            session['messages'].append('Entered a casino and lost ' + str(new_gold)  + " golds from the casino! " + str(datetime.datetime.now()))
        else:
            session['messages'].append('Entered a casino and gained ' + str(new_gold) + " golds from the casino! " + str(datetime.datetime.now()))
    return redirect('/')

app.run(debug=True)
