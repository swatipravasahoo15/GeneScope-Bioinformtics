from Bio.Align import PairwiseAligner


def align_sequences(reference, sample):

    # Remove spaces and convert to uppercase
    reference = "".join(reference.split()).upper()
    sample = "".join(sample.split()).upper()

    # Validate DNA sequences
    valid_bases = set("ATGC")

    if not reference or not sample:
        raise ValueError("Both DNA sequences are required.")

    if not set(reference).issubset(valid_bases):
        raise ValueError("Invalid bases in reference sequence.")

    if not set(sample).issubset(valid_bases):
        raise ValueError("Invalid bases in sample sequence.")

    # Create Pairwise Aligner
    aligner = PairwiseAligner()

    aligner.mode = "global"
    aligner.match_score = 2
    aligner.mismatch_score = -1
    aligner.open_gap_score = -2
    aligner.extend_gap_score = -0.5

    # Perform alignment
    alignments = aligner.align(reference, sample)

    best_alignment = alignments[0]

    # Get aligned sequences
    aligned_reference = str(best_alignment[0])
    aligned_sample = str(best_alignment[1])

    # Identify differences
    differences = []

    ref_position = 0
    sample_position = 0

    for i, (ref_base, sample_base) in enumerate(
        zip(aligned_reference, aligned_sample)
    ):

        if ref_base != "-":
            ref_position += 1

        if sample_base != "-":
            sample_position += 1

        if ref_base == sample_base:
            continue

        if ref_base == "-":
            mutation_type = "Insertion"

        elif sample_base == "-":
            mutation_type = "Deletion"

        else:
            mutation_type = "Substitution"

        differences.append({
            "Alignment Position": i + 1,
            "Reference Position": ref_position if ref_base != "-" else "-",
            "Sample Position": sample_position if sample_base != "-" else "-",
            "Reference Base": ref_base,
            "Sample Base": sample_base,
            "Type": mutation_type
        })

    return {
        "Alignment Score": best_alignment.score,
        "Aligned Reference": aligned_reference,
        "Aligned Sample": aligned_sample,
        "Total Differences": len(differences),
        "Differences": differences
    }