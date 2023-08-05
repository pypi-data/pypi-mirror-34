from bases import Bases

def run_test():
    n_mer_length = 4

    #pattern_to_number('ACGTGCA')


    nda_seq = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'

    skew(14, nda_seq)
    #print(pattern_match(nda_seq, 'CGC'))

    #rev_comp = reverse_complement('GCTAGCT')

    #pattern_count(nda_seq, 'CGCG')

    #computing_frequencies(nda_seq, 2)



# print(kmers[-1])
# print(kmers)


# anon_ndex = nc.Ndex2("http://public.ndexbio.org")
# query_result_cx = anon_ndex.get_neighborhood('c9243cce-2d32-11e8-b939-0ac135e8bacf', 'XRN1')

def skew(k, dna_seq):
    skew_count = 0
    index = 0
    output_list = []
    output_list.append(str(skew_count))
    for char in dna_seq:
        if char == 'C':
            skew_count -= 1
        elif char == 'G':
            skew_count += 1

        if index == k:
            print('%d - %d' % (index, skew_count))
            break

        output_list.append(str(skew_count))
        index += 1

    return index
    #print(' '.join(output_list))


def computing_frequencies(text, k):
    freq_array = []
    for i in range(0, ((4**k) - 1)):
        freq_array.append(0)
    for i in range(0, (len(text) - k)):
        pattern = text[i:i + k]
        j = pattern_to_number(pattern)
        freq_array[j] += 1

def pattern_to_number(pattern):
    base_pair_to_number = {
        'A': '0',
        'C': '1',
        'G': '2',
        'T': '3'
    }
    converted = ''
    for c in pattern:
        converted = converted + base_pair_to_number.get(c)

    octal = "{0:o}".format(124)
    bases = Bases()

    quad = bases.toBase(123, 4)

    return converted


def find_clumps(text, k, L, t):
    kmer_dict = get_kmer_dict(text, k)
    kmer_dict_filtered = {k: v for k, v in kmer_dict.items() if v >= t}

    kmer_clumps_found = []
    print('%s total iterations' % str(len(text) - (L - 1)))
    for key, v1 in kmer_dict_filtered.items():
        for i in range(0, len(text) - (L - 1)):
            print(str(i))
            if len(pattern_match(text[i: i +L], key).split(' ')) >= t:
                kmer_clumps_found.append(key)
                break

    return kmer_clumps_found


def pattern_count(text, pattern):
    n_mer_length = len(pattern)
    nmer_count = 0
    for i in range(0, len(text) - (n_mer_length - 1)):
        if text[i: i +n_mer_length] == pattern:
            nmer_count += 1

    return nmer_count

def get_kmer_dict(text, k):
    kmer_dict = {}
    max_occurences = 0
    for i in range(0, len(text) - (k - 1)):
        # kmers.append(text[i:i+k])
        value = kmer_dict.get(text[i: i +k])
        if value is not None:
            kmer_dict[text[i: i +k]] += 1
        else:
            kmer_dict[text[i: i +k]] = 1

    return kmer_dict

def frequent_words(text, k):
    kmers = []
    kmer_dict = get_kmer_dict(text, k)

    max_count = max(kmer_dict.values())

    for i in range(0, len(text) - (k - 1)):
        kmers.append(kmer_dict.get(text[i: i +k]))

    return_values = []
    for k, v in kmer_dict.items():
        if v == max_count:
            return_values.append(k)
        print('%s - %s' % (k, v))

    return return_values

def reverse_complement(text):
    comp_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    reverse_text = text[::-1]
    compliment = ''
    for c in reverse_text:
        compliment = compliment + comp_map.get(c)

    return compliment

def pattern_match(text, pattern):
    k = len(pattern)
    found_match = []
    for i in range(0, len(text) - (k - 1)):
        if text[i: i +k] == pattern:
            found_match.append(str(i))

    return ' '.join(found_match)



run_test()

if False:
    with open('E_coli.txt', 'r') as ech:
        e_coli_text = ech.read()

    found_clumps = find_clumps(e_coli_text, 9, 500, 3)
    print(' '.join(found_clumps))

    with open('vibrio_cholerae.txt', 'r') as vch:
        vib_chol_text = vch.read()

    found_pattern = pattern_match(vib_chol_text, 'ATGATCAAG')
    print(found_pattern)
    rev_comp = reverse_complement(nda_seq)
    pattern_count(nda_seq, 'GTTAATAGT')
    frequent_words(nda_seq, 13)

    kmers = []
    kmer_dict = {}
    for i in range(0, len(nda_seq) - (n_mer_length - 1)):
        kmers.append(nda_seq[i: i + n_mer_length])
        value = kmer_dict.get(nda_seq[i: i + n_mer_length])
        if value is not None:
            kmer_dict[nda_seq[i: i + n_mer_length]] += 1
        else:
            kmer_dict[nda_seq[i: i + n_mer_length]] = 1

    for w in sorted(kmer_dict, key=kmer_dict.get, reverse=True):
        print(w, kmer_dict[w])

