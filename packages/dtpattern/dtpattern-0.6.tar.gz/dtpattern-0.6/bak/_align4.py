#!/usr/bin/python -tt
#
# Affine Gap Penalty
# Gotoh algorithm
# Copyleft (c) 2013. Ridlo W. Wibowo
#
import sys, math


def affine_gap(seq1,seq2):

    gap_open = -15
    gap_extend = -1
    match = 5.
    mismatch = -4.


    #### initiate and calculate value
    lseq1 = len(seq1);
    lseq2 = len(seq2)
    row = lseq2 + 1;
    col = lseq1 + 1

    xval = [[0. for j in range(col)] for i in range(row)]
    yval = [[0. for j in range(col)] for i in range(row)]
    val = [[0. for j in range(col)] for i in range(row)]

    for i in range(row):
        val[i][0] = gap_open + i * gap_extend
        yval[i][0] = -10000.

    for j in range(col):
        val[0][j] = gap_open + j * gap_extend
        xval[0][j] = -10000.  # assign -INF

    val[0][0] = 0.

    for i in range(1, row):
        for j in range(1, col):
            xval[i][j] = max(xval[i - 1][j] + gap_extend, val[i - 1][j] + gap_open + gap_extend)
            yval[i][j] = max(yval[i][j - 1] + gap_extend, val[i][j - 1] + gap_open + gap_extend)
            cople = 0.
            if (seq1[j - 1] == seq2[i - 1]):
                cople = val[i - 1][j - 1] + match
            else:
                cople = val[i - 1][j - 1] + mismatch

            val[i][j] = max(cople, xval[i][j], yval[i][j])

    #### print value
    for i in range(row):
        for j in range(col):
            print(val[i][j], '\t',)
        print('')


    #### traceback
    sequ1 = ''
    sequ2 = ''
    i = lseq2
    j = lseq1
    ITER_MAX = 1000000
    iteration = 0
    while ((i > 0 or j > 0) and iteration < ITER_MAX):
        if (i > 0 and j > 0 and val[i][j] == val[i - 1][j - 1] + (match if seq2[i - 1] == seq1[j - 1] else mismatch)):
            sequ1 += seq1[j - 1]
            sequ2 += seq2[i - 1]
            i -= 1;
            j -= 1
        elif (i > 0 and val[i][j] == xval[i][j]):
            sequ1 += '_'
            sequ2 += seq2[i - 1]
            i -= 1
        elif (j > 0 and val[i][j] == yval[i][j]):
            sequ1 += seq1[j - 1]
            sequ2 += '_'
            j -= 1

        iteration += 1

    sequ1r = ' '.join([sequ1[j] for j in range(-1, -(len(sequ1) + 1), -1)])
    sequ2r = ' '.join([sequ2[j] for j in range(-1, -(len(sequ2) + 1), -1)])

    score = 0.
    for j in range(len(sequ1)):
        if (sequ1[j] == sequ2[j]):
            score += match
        else:
            score += mismatch

    return sequ1r,sequ2r,score


if __name__ == "__main__":
    sequ1r, sequ2r, score =  affine_gap("http://deri.org/","https://deri.com")
    print("Sequence 1: ", sequ1r)
    print("Sequence 2: ", sequ2r)
    print("Score     : ", score)
