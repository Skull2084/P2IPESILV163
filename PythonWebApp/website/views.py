from flask import Blueprint, render_template
from flask_login import login_required, current_user
from website import create_app
from backend import find_path, verifier_affluence
from flask import Blueprint, render_template, request, flash, redirect, url_for,jsonify,session
from datetime import datetime



views = Blueprint('views', __name__)

@views.route('/',methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        location = request.form.get('location')
        destination = request.form.get('destination')
        result = find_path(location, destination) 
        affluence = verifier_affluence()
        return render_template('home.html', user=current_user, result=result, affluence=affluence)
    affluence = verifier_affluence()
    return render_template('home.html', user=current_user,result=None,affluence=affluence)


@views.route('/report_issue', methods=['POST'])
def report_issue():
    data = request.get_json()
    issue_type = data.get('issue')
    description = data.get('description')
    
    if issue_type == 'affluence':
        with open('issues.txt', 'a') as f:
            f.write(f"{datetime.now()} - {description}\n")
        return jsonify(message="Affluence issue reported successfully"), 200

    return jsonify(message="Invalid issue type"), 400