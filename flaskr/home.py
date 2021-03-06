from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db


bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/')
def index():
    db = get_db()
    skills = db["skills"]
    projects = db["projects"]
    return render_template('home/index.html', skills=skills, projects=projects)

