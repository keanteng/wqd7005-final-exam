# WQD7007 Final Exam

![Static Badge](https://img.shields.io/badge/python-3.12-blue)
[![made-with-latex](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/)
[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/keanteng/wqd7005-final-exam)


This repository contains the code for the final exam of WQD7007. The exam consists of two parts with both a written part and a coding part.

## Title

Retail Insights from Time Series Data: A Multi-Method Approach to Store Performance and Customer Behavior

## Repository Structure

```plaintext
+---bin
+---data
|   +---exam
|   |   +---processed
|   |   \---raw_2
|   +---gemini
|   +---sample-2
|   |   \---processed
|   \---samples
+---images
+---notebooks
|   \---models
+---paper
+---prompts
+---public
+---sample
\---sample-2
```

## Using This Repository

1. Clone the repository to your local machine:

```bash
git clone https://github.com/keanteng/wqd7005-final-exam
```

## Report Production & Documentation

Install pandoc from this distribution:

```bash
https://github.com/jgm/pandoc/releases/download/3.7.0.2/pandoc-3.7.0.2-linux-amd64.tar.gz
```

You will write the report in `report.md`. The report will be compiled to PDF using the following command:

```bash
# Note: Need to update the file name in the script to match your report file name
# this will generate the report in DOCX format
bin/to-doc.sh

# this will generate the report in PDF format
bin/to-pdf.sh
```

To merge all the jupyter notebooks into a single PDF, you can use the following command:

```bash
# this will merge all jupyter notebooks into a single jupyter notebook
# remember to update the path of the jupyter notebooks in the merge.py file
py -3.12 bin/merge.py

# Note: Need to update the file name in the script to match your notebook file name
# this will convert the merged jupyter notebook to PDF
bin/py-to-pdf.sh
```