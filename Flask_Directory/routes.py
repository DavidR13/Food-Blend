from flask import render_template, request, redirect, url_for, flash, abort
from Flask_Directory import app
import os
from datetime import date


@app.route('/')
@app.route('/home')
def index():
    return render_template("home.html")
