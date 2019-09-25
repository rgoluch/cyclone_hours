from back_end import back_end
from flask import render_template

@back_end.route('/')
@back_end.route('/index')
def index():
    return render_template('front_end/index.html', title='Home')