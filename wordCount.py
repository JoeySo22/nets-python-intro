# Author: Jose Eduardo Soto JoeySo22

import sys, re

l_args = len(sys.argv)

# Assert we have two plus one arguements
if (len(sys.argv) != 3):
    print('Error: Requires 1 input filename and 1 output filename')
else:
    input_file = ''
    output_file = ''
    try:
        input_file = open(sys.argv[1], 'r')
    except:
        print('Error: Cannot open input file %s' % sys.argv[1])
        sys.exit(-1)
    try: 
        output_file = open(sys.argv[2], 'w')
    except:
        print('Error: Cannot write to output file %s' % sys.argv[2])
        sys.exit(-1)


    word_dictionary = {}
    while True:
        line = input_file.readline()
        if (len(line) == 0):
            break
        line = line.lower()
        line = re.sub('[^ a-z]', '', line)
        word_vector = line.split()
        for word in word_vector:
            if word in word_dictionary:
                word_dictionary[word] += 1
            else:
                word_dictionary.add(word, 1)

    # Write results into file in descending order (greatest to lowest)
    
                
    
