from flask import Blueprint, render_template

sub1_2_blueprint = Blueprint('sub1_2', __name__)

@sub1_2_blueprint.route('/sub1/sub1_2')
def sub1_2():
    return render_template('/sub1/sub1_2.html')