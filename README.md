🧬 GeneScope – DNA & Protein Sequence Analysis Platform

GeneScope is a Python-based bioinformatics application designed to analyze DNA sequences and perform basic protein sequence analysis through an interactive Streamlit dashboard.

Features

- DNA sequence validation
- Nucleotide frequency analysis (A, T, G, C)
- GC and AT content calculation
- DNA transcription into RNA
- Reverse complement generation
- DNA translation into protein sequence
- Open Reading Frame (ORF) identification
- Mutation detection between DNA sequences
- Pairwise sequence alignment
- Interactive data visualization
  
 Technologies Used

- Python
- Biopython
- Streamlit
- Pandas
- NumPy
- Matplotlib

📁 Project Structure

GeneScope/
│
├── modules/
│   ├── sequence_analysis.py
│   ├── protein_analysis.py
│   ├── mutation_analysis.py
│   └── alignment_analysis.py
│
├── data/
├── results/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

Installation and Setup

1. Clone the repository:

git clone https://github.com/swatipravsahoo15/GeneScope-Bioinformatics.git

2. Open the project folder:

cd GeneScope-Bioinformatics

3. Install dependencies:

pip install -r requirements.txt

4. Run the application:

python -m streamlit run app.py

Project Objective

The objective of GeneScope is to demonstrate fundamental bioinformatics concepts using Python programming, biological sequence processing, and interactive visualization.

 Author

Swatiprav Sahoo

Project: GeneScope – Bioinformatics Platform
