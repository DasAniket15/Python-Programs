"""
Receives a list containing an existing list of frequencies, as well as a string representing
a new DNA sequence, and update the previous numbers to reflect their added frequencies.
The program also prints the nucleotides being added to each frequency.
"""

def merge(list1, list2):
    """
    Merging two lists back into one list of tuples (REQUIRES LIST COMPREHENSION)
    """
    
    merged_list = [(list1[i], list2[i]) for i in range (0, len(list1))]
    
    return merged_list


def update_frequencies(old_frequencies, new_sequence):
    """
    Updating frequencies of nucleotides
    """
    
    freqA = freqC = freqT = freqG = 0

    #Unzipping list
    nucleotides = [i[0] for i in old_frequencies]
    frequencies = [i[1] for i in old_frequencies]
    
    #Updating values of frequencies of nucleotides
    for i in new_sequence:
        if i == "A":
            frequencies[0] += 1
            freqA += 1
        
        elif i == "C":
            frequencies[1] += 1
            freqC += 1

        elif i == "T":
            frequencies[2] += 1
            freqT += 1

        elif i == "G":
            frequencies[3] += 1
            freqG += 1

    #Printing number of nucleotides added to each frequency
    print (f"Number of nucleotides added: A -> {freqA} | C -> {freqC} | T -> {freqT} | G -> {freqG}")

    updated_frequencies = merge(nucleotides, frequencies)

    return updated_frequencies


def main():
    old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
    new_sequence = "ACCCGTTA"
    
    new_frequencies = update_frequencies(old_frequencies, new_sequence)

    print (new_frequencies)


main()