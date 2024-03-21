from os import getenv

from dotenv import load_dotenv
from flask import Flask, render_template, request

from backend import clear

from backend.artificial_intelligence.gemini.gemini_api import get_ideas
from backend.artificial_intelligence.gemini.write_outline import get_book_outline

from backend.artificial_intelligence.claude.new_convo import claude_outline

load_dotenv('/.env')
app = Flask(__name__)

app.config['SECRET_KEY'] = getenv('SECRET_KEY')


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/generate-ideas')
def generate_ideas():
    return render_template("generateIdeas.html")


@app.route('/load-ideas')
def load_ideas():
    if request.args:
        audience = request.args.get('a')

        if audience == '':
            return ['ERROR: Please enter the audience.']

        return get_ideas(audience)


@app.route('/load-overview')
def load_overview():
    if request.args:
        title = clear.spaces(request.args.get('t'))
        description = clear.spaces(request.args.get('d'))
        audience = clear.spaces(request.args.get('a'))

        book = claude_outline(title, audience, description)

        return book


@app.route('/custom-ideas')
def custom_ideas():
    return render_template("customIdeas.html")


@app.route('/custom-ideas/<title>/<audience>/<description>')
def custom_ideas_filled(title, audience, description):
    title = clear.spaces(title)
    description = clear.spaces(description)
    audience = clear.spaces(audience)

    return render_template("customIdeas.html", title=title, description=description, audience=audience)


if __name__ == '__main__':
    app.run(debug=True)
