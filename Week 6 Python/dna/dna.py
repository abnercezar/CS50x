import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Erro: número incorreto de argumentos!")
        sys.exit()

    # TODO: Read database file into a variable
    csv_filename = sys.argv[1]
    with open(csv_filename, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        individuals = list(csv_reader)

    # TODO: Read DNA sequence file into a variable
    dna_filename = sys.argv[2]
    with open(dna_filename, "r") as dna_file:
        dna_seq = dna_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    str_counts = {}
    for str_seq in list(individuals[0])[1:]:
        str_counts[str_seq] = longest_match(dna_seq, str_seq)

    # TODO: Check database for matching profiles
    for individual in individuals:
        match = True
        for str_seq in list(individual)[1:]:
            if str_counts[str_seq] != int(individual[str_seq]):
                match = False
                break
        if match:
            print(individual["name"])
            return
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
