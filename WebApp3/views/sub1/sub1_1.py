from flask import Blueprint, render_template

sub1_1_blueprint = Blueprint('sub1_1', __name__)

@sub1_1_blueprint.route('/sub1/sub1_1')
def sub1_1():
    return render_template('/sub1/sub1_1.html')