from flask import Flask, request, render_template
from helper import scrape_packages
from pdf_miner_main import search_pdfs_for_keywords

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def results():
    return search_pdfs_for_keywords()