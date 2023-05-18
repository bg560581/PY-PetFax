from flask import ( Blueprint, render_template, request ) 
import json 
pets = json.load(open('pets.json'))
bp = Blueprint('facts', __name__, url_prefix="/facts")

@bp.route('/', methods=['POST'])
def index():
    print(request.form)
    return 'Thanks for submitting a fun fact!'

@bp.route('/new')
def fact():
    return render_template('facts/new.html', pets=pets)