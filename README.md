Resume Analyzer
This is a simple Python project that analyzes a resume by comparing it with a job description. It extracts text from a PDF resume, checks which required skills are present, identifies missing skills, and calculates a basic ATS score.

Features

* Extract text from PDF resumes
* Compare resume with a job description
* Find matching and missing skills
* Calculate an ATS score
* Easy command-line interface

 Tech Stack

* Python
* PyPDF2
* scikit-learn
* NLTK
* ReportLab

 Project Structure

```text
resume-analyzer/
│── main.py
│── pdf_reader.py
│── analyzer.py
│── requirements.txt
└── README.md
```

Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

 How to Run

Run the project using:

```bash
python main.py
```

Then enter:

* The path to your resume PDF
* The job description

The program will display:

*  Matching skills
*  Missing skills
*  ATS Score

 Supported Skills

* Python
* SQL
* Machine Learning
* Deep Learning
* TensorFlow
* PyTorch
* Pandas
* NumPy
* Excel
* Power BI
* Tableau
* Java
* C++
* Git
* Docker

Future Improvements

* Support DOCX resumes
* Better skill extraction using NLP
* Web interface with Flask or Streamlit
* AI-based resume suggestions
* Export results as a PDF

⭐ Feel free to improve the project or use it as a learning resource.
