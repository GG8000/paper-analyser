from flask import Flask, request, render_template
from helper import cutting_dois_into_array, generate_keywords_for_selection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def get_methods_of_paper():
    doi = request.form["doi-input"];
    selection = request.form["selection"];
    doi_res=cutting_dois_into_array(doi);
    print(generate_keywords_for_selection(selection))
    return doi_res