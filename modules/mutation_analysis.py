def detect_mutations(reference, sample):
    """Identify substitutions between equal-length DNA sequences."""

    reference = "".join(reference.split()).upper()
    sample = "".join(sample.split()).upper()

    valid = set("ATGC")

    if not reference or not sample:
        raise ValueError("Both sequences are required.")

    if not set(reference).issubset(valid):
        raise ValueError("Reference contains invalid bases.")

    if not set(sample).issubset(valid):
        raise ValueError("Sample contains invalid bases.")

    if len(reference) != len(sample):
        raise ValueError(
            "Sequences must have equal lengths for this comparison."
        )

    mutations = []

    for i, (ref_base, sample_base) in enumerate(
        zip(reference, sample), start=1
    ):
        if ref_base != sample_base:
            mutations.append({
                "Position": i,
                "Reference": ref_base,
                "Sample": sample_base,
                "Change": f"{ref_base} → {sample_base}"
            })

    return mutations


if __name__ == "__main__":

    reference = "ATGCGTAC"
    sample = "ATGAGTTC"

    results = detect_mutations(reference, sample)

    print("===== GENESCOPE MUTATION ANALYSIS =====")

    print("Reference:", reference)
    print("Sample:", sample)
    print("Total Differences:", len(results))

    for mutation in results:
        print(mutation)

    print("======================================")