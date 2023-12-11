from flask import Flask, request, render_template
import os
import nltk
from nltk.corpus import words, wordnet
from pdf_miner_v2 import (
    find_r_packages_in_pdf,
    visualization_used_packages,
    extract_publication_year,
    get_metadata,
)
from helper import create_uploads_folder
import glob
from io import StringIO
import pandas as pd

app = Flask(__name__)


# Check if english words are already downloaded
def download_nltk_corpus():
    try:
        if nltk.corpus.wordnet.fileids():
            print("WordNet is already downloaded.")
        else:
            print("WordNet is not downloaded.")
            nltk.download("wordnet")
        nltk.data.find("corpora/words.zip")
    except LookupError:
        print("Downloading NLTK words corpus...")
        nltk.download("words")

        # Check if WordNet is downloaded


@app.route("/")
def index():
    download_nltk_corpus()
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    create_uploads_folder()
    uploaded_files = request.files.getlist("pdf_files[]")

    if not uploaded_files:
        return "No files selected for upload."

    uploaded_pdf_files = []

    for uploaded_file in uploaded_files:
        if uploaded_file.filename != "":
            # Check if the file has a .pdf extension
            if uploaded_file.filename.endswith(".pdf"):
                # Save the uploaded file to a specific directory
                uploaded_file.save(os.path.join("uploads", uploaded_file.filename))
                uploaded_pdf_files.append(uploaded_file.filename)

    if uploaded_pdf_files:
        # Perform your PDF processing here using the algorithm you mentioned
        with open("bioc_cran_packages.txt", "r") as file:
            # Read the lines and remove leading/trailing whitespace
            package_names = [line.strip() for line in file.readlines()]

        # Convert the list to a comma-separated string
        package_string = ", ".join(package_names)

        r_packages = package_names

        folder_path = "./uploads/"
        pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))

        non_packages_all = []
        used_packages = []
        pub_years = []
        titles = []
        issns = []
        journals = []
        for file in pdf_files:
            filename = os.path.basename(file)
            # pub_year = extract_publication_year(file)
            # pub_year = get_publication_year_from_doi(doi)
            result, non_packages = find_r_packages_in_pdf(
                file, filename, r_packages, set(words.words("en"))
            )
            used_packages.append([filename, result])
            title, pub_year, issn, journal = get_metadata(file)
            pub_years.append([filename, pub_year])
            titles.append([filename, title])
            issns.append([filename, issn])
            journals.append([filename, journal])
            if non_packages:
                non_packages_all.append([filename, non_packages])
        # Delete all files in the "uploads" folder after processing
        for file in pdf_files:
            os.remove(file)
        # print(pub_years)
        # print(used_packages)
        df = visualization_used_packages(
            used_packages, pub_years, titles, issns, journals, False
        )

        print(f"possible non packages are: {non_packages_all} ")
        # # return response
        rendered_html = render_template(
            "results.html",
            dataframe=df.to_html(classes="table table-striped"),
            caution_packages=non_packages_all,
        )
        return rendered_html

    return "No valid PDF files selected for upload."


if __name__ == "__main__":
    app.run(debug=True)
