from flask import Flask, request, render_template, make_response
import os
from pdf_miner_v2 import find_r_packages_in_pdf, visualization_used_packages, extract_publication_year, get_metadata
from helper import create_uploads_folder
import glob
from io import StringIO
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_csv():
    uploaded_files = request.files.getlist('pdf_files[]')

    if not uploaded_files:
        return 'No files selected for upload.'

    uploaded_pdf_files = []

    for uploaded_file in uploaded_files:
        if uploaded_file.filename != '':
            # Check if the file has a .pdf extension
            if uploaded_file.filename.endswith('.pdf'):
                # Save the uploaded file to a specific directory
                uploaded_file.save(os.path.join('uploads', uploaded_file.filename))
                uploaded_pdf_files.append(uploaded_file.filename)

    if uploaded_pdf_files:
        # Perform your PDF processing here using the algorithm you mentioned
        with open('bioc_cran_packages.txt', 'r') as file:
            # Read the lines and remove leading/trailing whitespace
            package_names = [line.strip() for line in file.readlines()]

        # Convert the list to a comma-separated string
        package_string = ", ".join(package_names)

        r_packages = package_names

        folder_path = "./uploads/"
        pdf_files = glob.glob(os.path.join(folder_path, '*.pdf'))

        used_packages = []
        pub_years = []
        titles = []
        issns = []
        journals = []
        for file in pdf_files:
            filename = os.path.basename(file)
            #pub_year = extract_publication_year(file)
            #pub_year = get_publication_year_from_doi(doi)
            result = find_r_packages_in_pdf(file, filename,r_packages)
            used_packages.append([filename,result])
            title, pub_year, issn, journal = get_metadata(file)
            pub_years.append([filename, pub_year])
            titles.append([filename, title])
            issns.append([filename, issn])
            journals.append([filename, journal])
        # Delete all files in the "uploads" folder after processing
        for file in pdf_files:
            os.remove(file)
        #print(pub_years)
        #print(used_packages)
        df = visualization_used_packages(used_packages, pub_years, titles, issns, journals, False)
        # Downloading df as csv
        csv_data = df.to_csv(index=True, sep=";")
    
        # Set the appropriate content type and headers for CSV download
        response = make_response(csv_data)
        response.headers['Content-Type'] = 'text/csv'
        response.headers['Content-Disposition'] = 'attachment; filename=paper_packages.csv'
    
        return response

    return 'No valid PDF files selected for upload.'


@app.route('/upload', methods=['POST'])
def upload():
    create_uploads_folder()
    uploaded_files = request.files.getlist('pdf_files[]')

    if not uploaded_files:
        return 'No files selected for upload.'

    uploaded_pdf_files = []

    for uploaded_file in uploaded_files:
        if uploaded_file.filename != '':
            # Check if the file has a .pdf extension
            if uploaded_file.filename.endswith('.pdf'):
                # Save the uploaded file to a specific directory
                uploaded_file.save(os.path.join('uploads', uploaded_file.filename))
                uploaded_pdf_files.append(uploaded_file.filename)

    if uploaded_pdf_files:
        # Perform your PDF processing here using the algorithm you mentioned
        with open('bioc_cran_packages.txt', 'r') as file:
            # Read the lines and remove leading/trailing whitespace
            package_names = [line.strip() for line in file.readlines()]

        # Convert the list to a comma-separated string
        package_string = ", ".join(package_names)

        r_packages = package_names

        folder_path = "./uploads/"
        pdf_files = glob.glob(os.path.join(folder_path, '*.pdf'))

        used_packages = []
        pub_years = []
        titles = []
        issns = []
        journals = []
        for file in pdf_files:
            filename = os.path.basename(file)
            #pub_year = extract_publication_year(file)
            #pub_year = get_publication_year_from_doi(doi)
            result = find_r_packages_in_pdf(file, filename,r_packages)
            used_packages.append([filename,result])
            title, pub_year, issn, journal = get_metadata(file)
            pub_years.append([filename, pub_year])
            titles.append([filename, title])
            issns.append([filename, issn])
            journals.append([filename, journal])
        # Delete all files in the "uploads" folder after processing
        for file in pdf_files:
            os.remove(file)
        #print(pub_years)
        #print(used_packages)
        df = visualization_used_packages(used_packages, pub_years, titles, issns, journals, True)
        # Downloading df as csv
        # csv_data = df.to_csv(index=True, sep=";")
    
        # # Set the appropriate content type and headers for CSV download
        # response = make_response(csv_data)
        # response.headers['Content-Type'] = 'text/csv'
        # response.headers['Content-Disposition'] = 'attachment; filename=paper_packages.csv'
    
        # return response

        return render_template('results.html', dataframe=df.to_html(classes='table table-striped'))

        # template = """
        # <!DOCTYPE html>
        # <html>
        # <head>
        #     <title>DataFrame Visualization</title>
        # </head>
        # <body>
        #     <h1>DataFrame Visualization</h1>
        #     {{ dataframe | safe }}
        # </body>
        # </html>
        # """

        # return render_template_string(template, dataframe=df.to_html(classes='table table-striped'))

    return 'No valid PDF files selected for upload.'


if __name__ == '__main__':
    app.run(debug=True)

