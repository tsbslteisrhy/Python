from flask import Blueprint, render_template

sub2_1_blueprint = Blueprint('sub2_1', __name__)

@sub2_1_blueprint.route('/sub2/sub2_1')
def sub2_1():
    return render_template('/sub2/sub2_1.html')