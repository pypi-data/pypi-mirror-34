"""
DNA tables and other stuff

.
"""
# Codon Usage probability for each scpecie'
USAGE_FREQ = {'E.coli': {u'GGG': 0.15, u'GGA': 0.11, u'GGT': 0.34, u'GGC': 0.4,
                         u'GAG': 0.31, u'GAA': 0.69, u'GAT': 0.63, u'GAC': 0.37,
                         u'GTG': 0.37, u'GTA': 0.15, u'GTT': 0.26, u'GTC': 0.22,
                         u'GCG': 0.36, u'GCA': 0.21, u'GCT': 0.16, u'GCC': 0.27,
                         u'AGG': 0.02, u'AGA': 0.04, u'CGG': 0.1, u'CGA': 0.06,
                         u'CGT': 0.38, u'CGC': 0.4, u'AAG': 0.23, u'AAA': 0.77,
                         u'AAT': 0.45, u'AAC': 0.55, u'ATG': 1.0, u'ATA': 0.07,
                         u'ATT': 0.51, u'ATC': 0.42, u'ACG': 0.27, u'ACA': 0.13,
                         u'ACT': 0.17, u'ACC': 0.44, u'TGG': 1.0, u'TGT': 0.45,
                         u'TGC': 0.55, u'TAG': 0.07, u'TAA': 0.64, u'TGA': 0.29,
                         u'TAT': 0.57, u'TAC': 0.43, u'TTT': 0.57, u'TTC': 0.43,
                         u'AGT': 0.15, u'AGC': 0.28, u'TCG': 0.15, u'TCA': 0.12,
                         u'TCT': 0.15, u'TCC': 0.15, u'CAG': 0.65, u'CAA': 0.35,
                         u'CAT': 0.57, u'CAC': 0.43, u'TTG': 0.13, u'TTA': 0.13,
                         u'CTG': 0.5, u'CTA': 0.04, u'CTT': 0.1, u'CTC': 0.1,
                         u'CCG': 0.52, u'CCA': 0.19, u'CCT': 0.16, u'CCC': 0.12
                         },
              'human': {'CTT': 0.13, 'ACC': 0.36, 'ACA': 0.28,
                        'AAA': 0.42, 'ATC': 0.48, 'AAC': 0.54, 'ATA': 0.16,
                        'AGG': 0.2, 'CCT': 0.28, 'ACT': 0.24, 'AGC': 0.24,
                        'AAG': 0.58, 'AGA': 0.2, 'CAT': 0.41, 'AAT': 0.46,
                        'ATT': 0.36, 'CTG': 0.41, 'CTA': 0.07, 'CTC': 0.2,
                        'CAC': 0.59, 'ACG': 0.12, 'CAA': 0.25, 'AGT': 0.15,
                        'CCA': 0.27, 'CCG': 0.11, 'CCC': 0.33, 'TAT': 0.43,
                        'GGT': 0.16, 'TGT': 0.45, 'CGA': 0.11, 'CAG': 0.75,
                        'TCT': 0.18, 'GAT': 0.46, 'CGG': 0.21, 'TTT': 0.45,
                        'TGC': 0.55, 'GGG': 0.25, 'TAG': 0.2, 'GGA': 0.25,
                        'TGG': 1.0, 'GGC': 0.34, 'TAC': 0.57, 'TTC': 0.55,
                        'TCG': 0.06, 'TTA': 0.07, 'TTG': 0.13, 'CGT': 0.08,
                        'GAA': 0.42, 'TAA': 0.28, 'GCA': 0.23, 'GTA': 0.11,
                        'GCC': 0.4, 'GTC': 0.24, 'GCG': 0.11, 'GTG': 0.47,
                        'GAG': 0.58, 'GTT': 0.18, 'GCT': 0.26, 'TGA': 0.52,
                        'GAC': 0.54, 'TCC': 0.22, 'TCA': 0.15, 'ATG': 1.0,
                        'CGC': 0.19
                        }}


# Aminoacid to codon translation table
A2C_DICT = {'I': [u'ATT', u'ATC', u'ATA'],
            'L': [u'CTT', u'CTC', u'CTA', u'CTG', u'TTA', u'TTG'],
            'V': [u'GTT', u'GTC', u'GTA', u'GTG'],
            'F': [u'TTT', u'TTC'],
            'M': [u'ATG'],
            'C': [u'TGT', u'TGC'],
            'A': [u'GCT', u'GCC', u'GCA', u'GCG'],
            'G': [u'GGT', u'GGC', u'GGA', u'GGG'],
            'P': [u'CCT', u'CCC', u'CCA', u'CCG'],
            'T': [u'ACT', u'ACC', u'ACA', u'ACG'],
            'S': [u'TCT', u'TCC', u'TCA', u'TCG', u'AGT', u'AGC'],
            'Y': [u'TAT', u'TAC'],
            'W': [u'TGG'],
            'Q': [u'CAA', u'CAG'],
            'N': [u'AAT', u'AAC'],
            'H': [u'CAT', u'CAC'],
            'E': [u'GAA', u'GAG'],
            'D': [u'GAT', u'GAC'],
            'K': [u'AAA', u'AAG'],
            'R': [u'CGT', u'CGC', u'CGA', u'CGG', u'AGA', u'AGG'],
            '*': [u'TAA', u'TAG', u'TGA']}

# Aminoacid to codon translation table
A2C_NNS_DICT = {'I': [u'ATC'],
                'L': [u'CTC', u'CTG', u'TTG'],
                'V': [u'GTC', u'GTG'],
                'F': [u'TTC'],
                'M': [u'ATG'],
                'C': [u'TGC'],
                'A': [u'GCC', u'GCG'],
                'G': [u'GGC', u'GGG'],
                'P': [u'CCC', u'CCG'],
                'T': [u'ACC', u'ACG'],
                'S': [u'TCC', u'TCG', u'AGC'],
                'Y': [u'TAC'],
                'W': [u'TGG'],
                'Q': [u'CAG'],
                'N': [u'AAC'],
                'H': [u'CAC'],
                'E': [u'GAG'],
                'D': [u'GAC'],
                'K': [u'AAG'],
                'R': [u'CGC', u'CGG', u'AGG'],
                '*': [u'TAG']}


# codon to Aminoacid translation table
C2A_DICT = {u'ATT': 'I', u'ATC': 'I', u'ATA': 'I',
            u'CTT': 'L', u'CTC': 'L', u'CTA': 'L', u'CTG': 'L', u'TTA': 'L', u'TTG': 'L',
            u'GTT': 'V', u'GTC': 'V', u'GTA': 'V', u'GTG': 'V',
            u'TTT': 'F', u'TTC': 'F',
            u'ATG': 'M',
            u'TGT': 'C', u'TGC': 'C',
            u'GCT': 'A', u'GCC': 'A', u'GCA': 'A', u'GCG': 'A',
            u'GGT': 'G', u'GGC': 'G', u'GGA': 'G', u'GGG': 'G',
            u'CCT': 'P', u'CCC': 'P', u'CCA': 'P', u'CCG': 'P',
            u'ACT': 'T', u'ACC': 'T', u'ACA': 'T', u'ACG': 'T',
            u'TCT': 'S', u'TCC': 'S', u'TCA': 'S', u'TCG': 'S', u'AGT': 'S', u'AGC': 'S',
            u'TAT': 'Y', u'TAC': 'Y',
            u'TGG': 'W',
            u'CAA': 'Q', u'CAG': 'Q',
            u'AAT': 'N', u'AAC': 'N',
            u'CAT': 'H', u'CAC': 'H',
            u'GAA': 'E', u'GAG': 'E',
            u'GAT': 'D', u'GAC': 'D',
            u'AAA': 'K', u'AAG': 'K',
            u'CGT': 'R', u'CGC': 'R', u'CGA': 'R', u'CGG': 'R', u'AGA': 'R', u'AGG': 'R',
            u'TAA': '*', u'TAG': '*', u'TGA': '*'}


# Stop codons dict
STOP_DICT = {u'TAA': '*', u'TAG': '*', u'TGA': '*'}
STOP_CODONS = [u'TAA', u'TAG', u'TGA']
