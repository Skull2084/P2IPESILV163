from flask import Blueprint, render_template
from flask_login import login_required, current_user
from website import create_app
from backend import find_path
from flask import Blueprint, render_template, request, flash, redirect, url_for



views = Blueprint('views', __name__)

@views.route('/',methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        location = request.form.get('location')
        destination = request.form.get('destination')
        result = find_path(location, destination) 
        return render_template('home.html', user=current_user, result=result)
    return render_template('home.html', user=current_user,result=None)
