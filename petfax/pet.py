from flask import ( Blueprint, render_template ) 
import json 
pets = json.load(open('pets.json'))

bp = Blueprint('pet', __name__, url_prefix="/pets")


@bp.route('/')
def index(): 
    return render_template('/pets/index.html', pets=pets)

@bp.route('/<int:pet_id>')
def show():
    # pet = pets[pet_id - 1]
    # for pet_id in pets:
        # print(pet_id)
        print(pets[0], '*****')
        return render_template('/pets/show.html', pets=pets)
    
# @bp.route('/new')
# def fact():
#     return render_template('facts/new.html')

# print(pets)



