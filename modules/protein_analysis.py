from Bio.Seq import Seq


def find_orfs(dna_sequence):
    """Find complete ORFs in all three forward reading frames."""

    dna_sequence = dna_sequence.upper()
    stop_codons = {"TAA", "TAG", "TGA"}
    orfs = []

    for frame in range(3):
        sequence = dna_sequence[frame:]

        for start in range(0, len(sequence) - 2, 3):

            if sequence[start:start + 3] == "ATG":

                for end in range(start + 3, len(sequence) - 2, 3):

                    codon = sequence[end:end + 3]

                    if codon in stop_codons:
                        orf = sequence[start:end + 3]

                        orfs.append({
                            "Frame": frame + 1,
                            "Start": frame + start + 1,
                            "End": frame + end + 3,
                            "Length": len(orf),
                            "DNA": orf
                        })

                        break

    return orfs


def translate_dna(dna_sequence):
    """Translate DNA coding sequence into protein."""

    sequence = dna_sequence.upper()

    return str(Seq(sequence).translate())


def analyze_protein(dna_sequence):
    """Generate protein analysis report."""

    dna_sequence = dna_sequence.upper()

    if not dna_sequence or any(
        base not in "ATGCN" for base in dna_sequence
    ):
        raise ValueError("Invalid DNA sequence!")

    protein = translate_dna(dna_sequence)

    orfs = find_orfs(dna_sequence)

    return {
        "DNA Sequence": dna_sequence,
        "Protein Sequence": protein,
        "Protein Length": len(protein),
        "Identified ORFs": len(orfs),
        "ORF Details": orfs
    }


# Testing the module

if __name__ == "__main__":

    dna = "ATGAAATAG"

    result = analyze_protein(dna)

    print("\n===== GENESCOPE PROTEIN ANALYSIS =====")

    for key, value in result.items():
        print(f"{key}: {value}")

    print("======================================")