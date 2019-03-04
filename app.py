import os
import requests
import operator
import re
import nltk

from flask import Flask, render_template, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import pandas as pd 

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from rq import Queue
from rq.job import Job
from worker import conn

############GENERAL NOTES############
##
##Ensure that postgresql is setup first (see config file)
##Ensure that config file 'export...' command run to to ensure proper calls // export APP_SETTINGS="config.DevelopmentConfig"
##Ensure that migrations are then run via the migrations file (e.g., db init, db migrate, db upgrade)
##Ensure that 'redis server' is running in one terminal, and then in another, 'python worker' is running
##For general questions, this is based roughly on https://realpython.com/flask-by-example-part-1-project-setup/
##
############GENERAL NOTES############

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)
q = Queue(connection=conn)


##note - import to have thie import of the models further down here to avoid bringing in multiple calls of the same
##stuff / same functions 
from models import *

@app.route('/', methods=['GET', 'POST'])

def index():


    results = {}

    if request.method == "POST":
        url = request.form['url']
        job = q.enqueue_call(func=boomer, args=(url,), result_ttl=5000)
        # results = job.get_id()
        return job.get_id()
        print(job.get_id())

    return render_template('index.html', results=results)




@app.route("/results/<job_key>", methods=['GET'])
def get_results(job_key):

    job = Job.fetch(job_key, connection=conn)

    if job.is_finished:
        return str(job.result), 200
    else:
        return "Nay!", 202


if __name__ == '__main__':
    app.run()
