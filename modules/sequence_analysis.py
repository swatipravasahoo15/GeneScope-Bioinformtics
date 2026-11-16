# ==========================================
# GeneScope - DNA Sequence Analysis Module
# ==========================================

from Bio.Seq import Seq


def validate_sequence(sequence):
    """Check whether the DNA sequence is valid."""

    sequence = sequence.upper().replace(" ", "").replace("\n", "")

    valid_bases = set("ATGCN")

    if not sequence:
        return False

    return all(base in valid_bases for base in sequence)


def nucleotide_count(sequence):
    """Count A, T, G and C nucleotides."""

    sequence = sequence.upper()

    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C"),
        "N": sequence.count("N")
    }


def calculate_gc_content(sequence):
    """Calculate GC percentage."""

    sequence = sequence.upper()

    if not sequence:
        return 0.0

    gc_count = sequence.count("G") + sequence.count("C")

    return round((gc_count / len(sequence)) * 100, 2)


def calculate_at_content(sequence):
    """Calculate AT percentage."""

    sequence = sequence.upper()

    if not sequence:
        return 0.0

    at_count = sequence.count("A") + sequence.count("T")

    return round((at_count / len(sequence)) * 100, 2)


def transcribe_dna(sequence):
    """Convert DNA into RNA."""

    return str(Seq(sequence.upper()).transcribe())


def reverse_complement(sequence):
    """Generate reverse complement of DNA."""

    return str(Seq(sequence.upper()).reverse_complement())


def analyze_sequence(sequence):
    """Generate complete DNA analysis report."""

    sequence = sequence.upper().replace(" ", "").replace("\n", "")

    if not validate_sequence(sequence):
        raise ValueError("Invalid DNA sequence! Use A, T, G, C or N.")

    report = {
        "Sequence Length": len(sequence),
        "Nucleotide Count": nucleotide_count(sequence),
        "GC Content (%)": calculate_gc_content(sequence),
        "AT Content (%)": calculate_at_content(sequence),
        "RNA Sequence": transcribe_dna(sequence),
        "Reverse Complement": reverse_complement(sequence)
    }

    return report


# ==========================================
# TESTING THE MODULE
# ==========================================

if __name__ == "__main__":

    dna = "ATGCGTACGTAGCTAGCTAG"

    print("\n========== GENESCOPE ==========")
    print("DNA SEQUENCE ANALYSIS")
    print("==============================")

    result = analyze_sequence(dna)

    for key, value in result.items():
        print(f"{key}: {value}")

    print("==============================")