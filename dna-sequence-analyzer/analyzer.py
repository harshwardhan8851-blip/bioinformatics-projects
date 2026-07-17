"""
DNA Sequence Analyzer
----------------------
Validates a DNA sequence, then reports nucleotide composition,
GC/AT content with classification, the complementary strand,
and the reverse complement.
"""

DNA_sequence = input("Enter a DNA sequence: ").upper()
right_bases = {"A", "T", "G", "C"}
complementary_bases = {"A": "T", "T": "A", "G": "C", "C": "G"}
len1 = len(DNA_sequence)

if len1 == 0:
    print("The DNA sequence is empty. Please enter a valid DNA sequence.")
else:
    try:
        for base in DNA_sequence:
            if base not in right_bases:
                raise ValueError(f"Invalid base '{base}' found in the DNA sequence.")

        count_A = DNA_sequence.count("A")
        print(f"Count of Adenine (A): {count_A}")
        count_T = DNA_sequence.count("T")
        print(f"Count of Thymine (T): {count_T}")
        count_C = DNA_sequence.count("C")
        print(f"Count of Cytosine (C): {count_C}")
        count_G = DNA_sequence.count("G")
        print(f"Count of Guanine (G): {count_G}")

        gc_content = ((count_G + count_C) / len(DNA_sequence)) * 100
        at_content = (100 - gc_content)
        print(f"AT content: {at_content:.2f}%")

        if gc_content > 60:
            print(f"High GC content: {gc_content:.2f}%")
        elif 40 <= gc_content <= 60:
            print(f"Moderate GC content: {gc_content:.2f}%")
        else:
            print(f"Low GC content: {gc_content:.2f}%")

        complementary_sequence = "".join(complementary_bases[base] for base in DNA_sequence)
        reverse_sequence = complementary_sequence[::-1]
        print(f"Complementary DNA sequence: {complementary_sequence}")
        print(f"Reverse complementary DNA sequence: {reverse_sequence}")

    except ValueError as e:
        print(f"Error: {e} Please enter a valid DNA sequence containing only A, T, G, and C.")
