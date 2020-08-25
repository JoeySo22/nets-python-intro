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


    # Contain the word counting in a dictionary.
    word_dictionary = {}
    # Iterate through the input file until there are no more lines.
    while True:

        
        # Read each line to digest.
        line = input_file.readline()
        '''
        An empty string will tell us when readline() has reached the EOF.
        If the text document as a vertical spacing by paragraph seperation
        then there is a new-line character. Therefore, the empty string IS the 
        EOF.
        '''
        if (len(line) == 0):
            break
        # Make line into all lowercase
        line = line.lower()
        # Substitute all non-alphabet characters into empty strings
        line = re.sub('[^ a-z]', '', line)
        # Seperate all strings by whitespace
        word_vector = line.split()

        
        # 
        for word in word_vector:
            if word in word_dictionary:
                word_dictionary[word] += 1
            else:
                word_dictionary.add(word, 1)

    # Write results into file in descending order (greatest to lowest)
    
                
    
