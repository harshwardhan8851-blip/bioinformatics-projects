"""
GC Content Analyzer
--------------------
Takes a DNA sequence as input, validates that it only contains real
DNA bases (A, T, G, C), then calculates and classifies its GC content.
"""

DNA_sequence = input("Enter a DNA sequence: ").upper()
right_bases = {"A", "T", "G", "C"}
len1 = len(DNA_sequence)

if len1 == 0:
    print("The DNA sequence is empty. Please enter a valid DNA sequence.")
else:
    try:
        for base in DNA_sequence:
            if base not in right_bases:
                raise ValueError(f"Invalid base '{base}' found in the DNA sequence.")

        count_C = DNA_sequence.count("C")
        count_G = DNA_sequence.count("G")
        gc_content = ((count_G + count_C) / len(DNA_sequence)) * 100

        if gc_content > 60:
            print(f"High GC content: {gc_content:.2f}%")
        elif 40 <= gc_content <= 60:
            print(f"Moderate GC content: {gc_content:.2f}%")
        else:
            print(f"Low GC content: {gc_content:.2f}%")
    except ValueError as e:
        print(f"Error: {e} Please enter a valid DNA sequence containing only A, T, G, and C.")
