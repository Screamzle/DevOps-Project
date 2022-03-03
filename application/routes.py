from application import app, db
from application.models import ToDo
from flask import Flask, render_template, request
from application.html_forms import AddForm, UpdateForm, DeleteForm, CompleteForm

@app.route('/')