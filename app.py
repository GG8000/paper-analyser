from flask import Flask, request, render_template
import os
from pdf_miner_v2 import find_r_packages_in_pdf
import glob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
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
        for file in pdf_files:
            filename = os.path.basename(file)
            result = find_r_packages_in_pdf(file, filename,r_packages)
            used_packages.append(result)
    
        # Delete all files in the "uploads" folder after processing
        for file in pdf_files:
            os.remove(file)

        return '\n'.join(used_packages)

    return 'No valid PDF files selected for upload.'

if __name__ == '__main__':
    app.run(debug=True)

