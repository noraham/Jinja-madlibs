"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

TOPPINGS = ['Pepperoni', 'Mushroom', 'Olive', 'Onion', 'Truffle oil', 'Pineapple']


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """play madlibs"""

    resp = request.args.get("game")
    toppings = TOPPINGS

    if resp == "no":
        return render_template("goodbye.html")
    else:
        return render_template('game.html', toppings=toppings)


@app.route('/madlib')
def show_madlib():
    """Return completed madlib"""
    per = request.args.get("name")
    col = request.args.get("color")
    noun = request.args.get("noun")
    adj = request.args.get("adjective")
    bev = request.args.get("bev")
    pizza = request.args.getlist("pizza")
    # for i, each in enumerate(pizza):
    #     pizza[i] = each.lower()
    print pizza

    return render_template('madlib.html',
                           name=per,
                           color=col,
                           noun=noun,
                           adjective=adj,
                           bev=bev,
                           pizza=pizza)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
