from flask import Blueprint, render_template

sub2_2_blueprint = Blueprint('sub2_2', __name__)

@sub2_2_blueprint.route('/sub2/sub2_2')
def sub2_2():
    return render_template('/sub2/sub2_2.html')