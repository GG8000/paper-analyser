# PDF Processing Web App

This web application allows you to upload PDF files and perform various tasks on them, including finding R packages mentioned in the papers and extracting publication years. It provides a user-friendly interface for uploading PDF files and downloading processed data.

## Getting Started

These instructions will help you set up and run the application on your local machine. It is recommended to use a virtual environment for managing project dependencies.

### Prerequisites

You'll need to have the following software and libraries installed:

- Python 3.x
- Flask
- pdfminer.six
- PyMuPDF (fitz)
- pandas

### Using a Virtual Environment

It's recommended to create a virtual environment to manage project dependencies. Here's how to do it on different operating systems:

#### macOS and Linux

1. Open your terminal.

2. Navigate to the project directory:

```bash
cd /path/to/paper-analyser
```
    Create a virtual environment (replace "venv" with your preferred environment name):

```bash

python -m venv venv
```
    Activate the virtual environment:

```bash
source venv/bin/activate
```

    Install the required packages from the requirements.txt file:
```bash
pip install -r requirements.txt
```
    You can now run the application within the virtual environment:

```bash
python3 app.py
```

    To deactivate the virtual environment when you're done:

```bash
deactivate
```
Windows

    Open your Command Prompt.

    Navigate to the project directory:

```bash
cd C:\path\to\pdf-processing-app
```
    Create a virtual environment (replace "venv" with your preferred environment name):

```bash
python -m venv venv
```
    Activate the virtual environment:

```bash
venv\Scripts\activate
```
    Install the required packages from the requirements.txt file:

```bash
pip install -r requirements.txt
```
    You can now run the application within the virtual environment.

```bash
python3 app.py
```

    To deactivate the virtual environment when you're done:
```bash
deactivate
```


### Usage

    Access the web app by opening your web browser and navigating to http://localhost:5000/.

    Click the "Upload PDF Files" button and select one or more PDF files to upload. Supported files should have the .pdf extension.

    Click the "Process PDFs" button to start processing the uploaded PDF files. The application will find R packages mentioned in the papers and extract publication years.

    After processing, you can click the "Download CSV" button to download the processed data in CSV format.