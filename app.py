from flask import Flask
from flask import render_template, jsonify
import random

app = Flask(__name__)


def quote():
    quotes = [
    "A bug in the code is worth two in the documentation.",
    "A computer's attention span is as long as its power cord.",
    "A computer scientist is someone who fixes things that aren't broken.",
    "Adding manpower to a late software project makes it later.",
    "All computers wait at the same speed.",
    "Any program that runs right is obsolete.",
    "A printer consists of three main parts: the case, the jammed paper tray and the blinking red light.",
    "A program is never finished until the programmer dies.",
    "ASCII stupid question, get a stupid ANSI!",
    "Be aware of Programmers who carry screwdrivers.",
    "Build a system that even a fool can use, and only a fool will use it.",
    "Computers are unreliable, but humans are even more unreliable.",
    "Computers can never replace human stupidity.",
    "Computer Science: solving today's problems tomorrow.",
    "Computers follow your orders, not your intentions.",
    "Computers make very fast, very accurate mistakes.",
    "Failure is not an option, it comes bundled with the software."
    ]
    q = random.choice(quotes)
    #print("returning: \"{}\"".format(q))
    return q


@app.route('/new_quote')
def new_quote():
    q = quote()
    return jsonify(q)


@app.route('/')
def get_quote():
    item = quote()
    return render_template('quote.html', item=item)
