from flask import Flask, render_template, redirect

import pymongo

import scrape_mars

app = Flask(__name__)

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.facts.df
collection = db.mars 

@app.route('/scrape')
def scrape():
        
