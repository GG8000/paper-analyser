# PDF Processing Web App

This web application allows you to upload PDF files and perform various tasks on them, including finding R packages mentioned in the papers and extracting publication years. It provides a user-friendly interface for uploading PDF files and downloading processed data.

## Getting Started

These instructions will help you set up and run the application on your local machine. It is recommended to use a virtual environment for managing project dependencies.

### Prerequisites

You'll need to have the following software and libraries installed:

- Python 3.x

### Using a Virtual Environment

It's recommended to create a virtual environment to manage project dependencies. Here's how to do it on different operating systems:

#### macOS, Linux and Windows

1. Open your terminal.

2. Navigate to the project directory and initialize Virtual Environment:
For macOS and Linux:
```bash
cd /path/to/paper-analyser
python -m venv venv
```
For Windows User:
```bash
cd C:\path\to\pdf-processing-app
python -m venv venv

```
3. Activate the virtual environment:
For macOS and Linux:
```bash
source venv/bin/activate
```
For Windows User:
```bash
venv\Scripts\activate
```
4. Install the required packages from the requirements.txt file:
```bash
pip install -r requirements.txt
```
5. You can now run the application within the virtual environment:
```bash
python app.py
```
6. To deactivate the virtual environment when you're done:
```bash
deactivate
```

### Usage
    After running the web app at Step 5. access the web app by opening your web browser and navigating to the location which is presented in the terminal.

    Click the "Durchsuchen" button and select one or more PDF files to upload. Files must have the .pdf extension.

    Click the "Analyze" button to start processing the uploaded PDF files. The application will find R packages mentioned in the papers and print them. After processing, you can click the "Download CSV" button to download the processed data in CSV format.

    This is the format you are getting:
    | File Name | Published In | Package1 | Package2 | Package3 | Package4 | Package5 | Package6 | Package7 | Title | Journal | ISSN       |
    |-----------|--------------:|----------|----------|----------|----------|----------|----------|----------|------------|--------------|------------|
    | file1.pdf |          2022 |        1 |        1 |        0 |        0 |        0 |        0 |        0 | title1 | Journal1        | ISSN1      |
    | file2.pdf |          2021 |        0 |        0 |        1 |        1 |        0 |        0 |        0 | title2 | Journal2        | ISSN2      |
    | file3.pdf |          2023 |        0 |        0 |        0 |        0 |        1 |        1 |        1 | title3   | Journal3        | ISSN3      |


