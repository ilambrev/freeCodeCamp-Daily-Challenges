def detect_mutations(strand1, strand2):
    mutations = []

    for i in range(len(strand1)):
        if not strand1[i] == strand2[i]:
            mutations.append(i)

    return sorted(mutations)

# print(detect_mutations("ATCG", "ATGG"))
# print(detect_mutations("ATGCGTACGTTAGC", "ATGCATACGATTGC"))
# print(detect_mutations("GATCTAGCTAGGCTAGCTAG", "GATCTAGCTAGGCTAGCTAG"))
# print(detect_mutations("TCAGATCATGGCTAGCTACGATCAGCTAGCATGCATATCGACTG", "TCAGATCATGGCTAGAGCTGATCAGCTAGCATGCATATCGACTG"))
# print(detect_mutations("ACGTCAGTACGCACATGACCATTGACATA", "AACGTCAGTACGCACATGACCATTGACAT"))