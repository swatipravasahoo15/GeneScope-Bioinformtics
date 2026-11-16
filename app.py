import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from modules.sequence_analysis import analyze_sequence
from modules.protein_analysis import analyze_protein
from modules.mutation_analysis import detect_mutations
from modules.alignment_analysis import align_sequences

# Page Configuration
st.set_page_config(
    page_title="GeneScope | Bioinformatics",
    page_icon="🧬",
    layout="wide"
)

# Header
st.title("🧬 GeneScope")
st.subheader("DNA & Protein Sequence Analysis Platform")

st.write(
    "A Python-based bioinformatics platform "
    "for biological sequence analysis and visualization."
)

dna = st.text_area(
    "Enter your DNA sequence",
    value="ATGCGTACGTAGCTAGCTAG",
    height=120
)

if st.button(" Analyze DNA", type="primary"):

    sequence = "".join(dna.split()).upper()

    try:
        if not sequence:
            st.warning("Please enter a DNA sequence.")

        else:
            # DNA Analysis
            result = analyze_sequence(sequence)

            # Protein Analysis
            protein = analyze_protein(sequence)

            st.success("Analysis completed successfully!")

            st.divider()
            st.header(" DNA Analysis Results")

            counts = result["Nucleotide Count"]

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Sequence Length",
                result["Sequence Length"]
            )

            col2.metric(
                "GC Content",
                f'{result["GC Content (%)"]}%'
            )

            col3.metric(
                "AT Content",
                f'{result["AT Content (%)"]}%'
            )

            # Nucleotide chart
            st.subheader("Nucleotide Distribution")

            chart_data = pd.DataFrame({
                "Nucleotide": ["A", "T", "G", "C", "N"],
                "Count": [
                    counts["A"],
                    counts["T"],
                    counts["G"],
                    counts["C"],
                    counts["N"]
                ]
            })

            st.bar_chart(
                chart_data.set_index("Nucleotide")
            )

            # Sequence details
            st.subheader("Sequence Information")

            st.write("**DNA:**", sequence)
            st.write("**RNA:**", result["RNA Sequence"])
            st.write(
                "**Reverse Complement:**",
                result["Reverse Complement"]
            )

            st.divider()

            # Protein Analysis
            st.header(" Protein Analysis")

            st.write(
                "**Protein Sequence:**",
                protein["Protein Sequence"]
            )

            st.metric(
                "Protein Length",
                protein["Protein Length"]
            )

            st.metric(
                "Identified ORFs",
                protein["Identified ORFs"]
            )

            st.divider()

            # Download Report
            st.header(" Download Analysis Report")

            report = {
                "Parameter": [
                    "Sequence Length",
                    "A Count",
                    "T Count",
                    "G Count",
                    "C Count",
                    "N Count",
                    "GC Content",
                    "AT Content",
                    "RNA Sequence",
                    "Reverse Complement",
                    "Protein Sequence",
                    "Protein Length",
                    "Identified ORFs"
                ],
                "Result": [
                    result["Sequence Length"],
                    counts["A"],
                    counts["T"],
                    counts["G"],
                    counts["C"],
                    counts["N"],
                    result["GC Content (%)"],
                    result["AT Content (%)"],
                    result["RNA Sequence"],
                    result["Reverse Complement"],
                    protein["Protein Sequence"],
                    protein["Protein Length"],
                    protein["Identified ORFs"]
                ]
            }

            df = pd.DataFrame(report)

            st.download_button(
                label="Download CSV Report",
                data=df.to_csv(index=False),
                file_name="genescope_report.csv",
                mime="text/csv"
            )

    except ValueError as error:
        st.error(str(error))

    except Exception as error:
        st.error(f"Analysis error: {error}")
        # ==========================================
# MUTATION DETECTION
# ==========================================

st.divider()

st.header(" Mutation Detection")

st.write(
    "Compare two DNA sequences to identify "
    "nucleotide substitutions."
)

col1, col2 = st.columns(2)

with col1:
    reference_dna = st.text_area(
        "Reference DNA Sequence",
        value="ATGCGTAC",
        height=100,
        key="reference_dna"
    )

with col2:
    sample_dna = st.text_area(
        "Sample DNA Sequence",
        value="ATGAGTTC",
        height=100,
        key="sample_dna"
    )

if st.button(" Compare DNA Sequences"):

    try:
        mutations = detect_mutations(
            reference_dna,
            sample_dna
        )

        st.subheader("Comparison Results")

        if mutations:
            st.success(
                f"Total Differences Found: {len(mutations)}"
            )

            mutation_df = pd.DataFrame(mutations)

            st.dataframe(
                mutation_df,
                use_container_width=True
            )
            st.download_button(
                label="📥 Download Mutation Report",
                data=mutation_df.to_csv(index=False).encode("utf-8"),
                file_name="genescope_mutation_report.csv",
                mime="text/csv"
            )

        else:
            st.info("No differences found.")
            
    except ValueError as error:
        st.error(str(error))
        # ==========================================
# PAIRWISE SEQUENCE ALIGNMENT
# ==========================================

st.divider()

st.header("🧬 Pairwise Sequence Alignment")

st.write(
    "Compare DNA sequences of different lengths "
    "using Biopython Pairwise Alignment."
)

reference_alignment = st.text_area(
    "Reference DNA for Alignment",
    value="ATGCGTAC",
    height=100,
    key="alignment_reference"
)

sample_alignment = st.text_area(
    "Sample DNA for Alignment",
    value="ATGCTAC",
    height=100,
    key="alignment_sample"
)

if st.button("🔬 Perform Pairwise Alignment"):

    try:
        alignment_result = align_sequences(
            reference_alignment,
            sample_alignment
        )

        st.success("Sequence alignment completed!")

        st.subheader("Alignment Results")

        col1, col2 = st.columns(2)

        col1.metric(
            "Alignment Score",
            alignment_result["Alignment Score"]
        )

        col2.metric(
            "Total Differences",
            alignment_result["Total Differences"]
        )

        st.write("**Aligned Reference:**")
        st.code(alignment_result["Aligned Reference"])

        st.write("**Aligned Sample:**")
        st.code(alignment_result["Aligned Sample"])

        st.subheader("Difference Analysis")

        differences = alignment_result["Differences"]

        if differences:

            difference_df = pd.DataFrame(differences)

            st.dataframe(
                difference_df,
                use_container_width=True
            )

        else:
            st.info("No differences found.")

    except ValueError as error:
        st.error(str(error))

st.divider()

st.divider()

st.caption("GeneScope | Python-Based Bioinformatics Project")
import streamlit as stM
