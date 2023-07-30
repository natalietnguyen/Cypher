#  File: TestCipher.py

#  Description: Encodes and decodes text using rail fence cipher and vigenere cipher

#  Student's Name: Natalie Nguyen

#  Student's UT EID: ntn687
 
#  Partner's Name: Ethan Harris

#  Partner's UT EID: ejh2947

#  Course Name: CS 313E 

#  Unique Number: 52038

#  Date Created: 24 January, 2023

#  Date Last Modified: 25 January, 2023

import sys

#  Input: none
#  Output: a string indicating all tests have been passed
def test_cases():
  # test create_array()
  assert create_array('', 0) == []
  assert create_array('hello', 2) == [['-','-','-','-','-'],
                                      ['-','-','-','-','-']]
  assert create_array('', 3) == [[],
                                 [],
                                 []]
  assert create_array('hello', 0) == []

  # test rail_fence_encode()
  assert rail_fence_encode('helloworld', 3) == 'holelwrdlo'
  assert rail_fence_encode('', 3) == ''
  assert rail_fence_encode('helloworld', 1) == 'helloworld'
  assert rail_fence_encode('helloworld', 0) == ''


  # test rail_fence_decode()
  assert rail_fence_decode('holelwrdlo', 3) == 'helloworld'
  assert rail_fence_decode('', 3) == ''
  assert rail_fence_decode('holelwrdlo', 1) == 'holelwrdlo'
  assert rail_fence_decode('holelwrdlo', 0) == ''

  # test filter_string()
  assert filter_string('') == ''
  assert filter_string('12$609(') == ''
  assert filter_string('7E3thaN') == 'ethan'

  # test encode_character()
  assert encode_character('a', 'a') == 'a'
  assert encode_character('g', 'y') == 'e'

  # test decode_character()
  assert decode_character('s', 's') == 'a'
  assert decode_character('g', 'm') == 'g'

  # test extend_pass_phrase()
  assert extend_pass_phrase('natalie','ethan') == 'ethanet'
  assert extend_pass_phrase('ethan', 'natalie') == 'natal'
  assert extend_pass_phrase('ethanethanethan', 'o') == 'ooooooooooooooo'

  # test vigenere_encode()
  assert vigenere_encode('helloworld', 'seal') == 'zilwgaocdh'
  assert vigenere_encode('hello', 'a') == 'hello'
  assert vigenere_encode('h','ethan') == 'l'

  # test vigenere_decode()
  assert vigenere_decode('zilwgaocdh', 'seal') == 'helloworld'
  assert vigenere_decode('hello', 'a') == 'hello'
  assert vigenere_decode('l','ethan') == 'h'

  return 'all test cases passed'


#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns an array with the number of rows
#          equal to key and number of columns equal to the
#          length of strng
def create_array(strng, key):
  # initalize array
  array = []

  # insert new list into array for number of key
  for i in range(key):
    array.append([])

    # insert placeholder into each row for the length of strng
    for j in range(len(strng)):
      array[i].append('-')

  return array

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ):
  # create array
  array = create_array(strng, key)

  # define variables
  direction = 'down'
  col = 0
  row = 0

  # account for key of 1 or 0
  if key == 1:
    return strng

  if key == 0:
    return ''

  # iterate over string
  for i in range(len(strng)):
    # edit array
    array[row][col] = strng[i]

    # detect direction
    if row == key - 1:
      direction = 'up'
    elif row == 0:
      direction = 'down'

    # edit coordinates
    if direction == 'down':
      row += 1
    else:
      row -= 1
    col += 1

  # initialize variable
  rail_fence_encoded = ''

  # iterate through array
  for y in array:
    for x in y:
      # test for character and conditionally add to encoded string
      if x != '-':
        rail_fence_encoded += x

  return rail_fence_encoded

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ):
  # create array
  array = create_array(strng, key)

  # define variables
  direction = 'down'
  col = 0
  row = 0

  # account for key of 1 or 0
  if key == 1:
    return strng

  if key == 0:
    return ''


  # iterate over string
  for i in range(len(strng)):
    # edit array
    array[row][col] = '*'

    # detect direction
    if row == key - 1:
      direction = 'up'
    elif row == 0:
      direction = 'down'

    # edit coordinates
    if direction == 'down':
      row += 1
    else:
      row -= 1
    col += 1

  # initialize index
  i = 0

  # iterate through array
  for y in range(len(array)):
    for x in range(len(strng)):
      # test if space is occupied
      if array[y][x] == '*':
        # replace character of decoded text
        array[y][x] = strng[i]

        # increase index
        i += 1
  
  # resets variables
  col = 0
  row = 0
  direction = 'down'

  # initialize variable
  rail_fence_decoded = ''

  # iterate over string
  for i in range(len(strng)):
    # test if element in array is a letter
    if array[row][col] != '-':
      # adds to rail_fence_decoded
      rail_fence_decoded += array[row][col]

    # detect direction
    if row == key - 1:
      direction = 'up'
    elif row == 0:
      direction = 'down'

    # edit coordinates
    if direction == 'down':
      row += 1
    else:
      row -= 1
    col += 1

  return rail_fence_decoded

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
  # initalize filtered_string
  filtered_string = ''

  # iterate across length of strng
  for i in range(len(strng)):
    # check if strng[i] is a letter and adds to filtered_string if True
    if strng[i].isalpha() == True:
      filtered_string += strng[i]
  
  # makes filtered_string all lowercase
  filtered_string = filtered_string.lower()

  return filtered_string

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def encode_character (p, s):
  # distance of character p from character a
  row_count = ord(p) - 97
  # ascii of character s
  column = ord(s)

  # initializes encoded_char
  encoded_char = ''

  # tests if distance of character p from character a plus ascii of 
  # character s is greater than the ascii of character z
  if row_count + column > 122:
    # finds encoded character
    encoded_char = chr((row_count - (122 - column)) + 96)
  else:
    # finds encoded character
    encoded_char = chr(row_count + column)

  return encoded_char

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character (p, s):
  # ascii of character p
  column = ord(p)
  # ascii of character s
  encoded_char = ord(s)

  # initializes decoded_char
  decoded_char = ''

  # tests if the ascii of character s if greater than or equal to ascii of character p
  if encoded_char >= column:
    # finds decoded character
    decoded_char = chr((encoded_char - column) + 97)
  else:
    # finds decoded character
    decoded_char = chr(123 - (column - encoded_char))

  return decoded_char

# Input: string, pass phrase
# Output: pass phrase repeated until the length of the string
def extend_pass_phrase(strng, phrase):
  # repeats phrase n times, with n equal to the number of times phrase can fit into 
  # strng plus 1
  extended_phrase = phrase * (len(strng)//len(phrase)+1)
  # slice extended_phrase up until the length of strng
  extended_phrase = extended_phrase[:len(strng)]

  return extended_phrase


#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode ( strng, phrase ):
  # filters strng to only contain lowercase letters
  strng = filter_string(strng)
  # initializes extended_phrase, which is the same length as strng
  extended_phrase = extend_pass_phrase(strng, phrase)

  # initalizes encoded_string
  encoded_string = ""

  # iterates across length of strng
  for i in range(len(strng)):
    # encodes each character and adds to encoded_string
    encoded_string += encode_character(extended_phrase[i], strng[i])

  return encoded_string

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ):
  # filters strng to only contain lowercase letters
  strng = filter_string(strng)
  # initializes extended_phrase, which is the same length as strng
  extended_phrase = extend_pass_phrase(strng, phrase)

  # initializes decoded_string
  decoded_string = ""

  # iterates across length of strng
  for i in range(len(strng)):
    # decodes each character and adds to decoded_string
    decoded_string += decode_character(extended_phrase[i], strng[i])

  return decoded_string

def main():
  # tests all functions
  # print(test_cases())

  # print Rail Fence Cipher
  print('\nRail Fence Cipher\n')

  # read the plain text from stdin
  plain_text = sys.stdin.readline().strip()

  # print plain text
  print('Plain Text: ' + plain_text)

  # read the key from stdin
  key = int(sys.stdin.readline().strip())

  # print key
  print('Key: ' + str(key))

  # encrypt and print the encoded text using rail fence cipher
  print('Encoded Text: ' + rail_fence_encode(plain_text, key))

  # read encoded text from stdin
  encoded_text = sys.stdin.readline().strip()
  
  # print encoded text
  print('\nEncoded Text: ' + encoded_text)
   
  # read the key from stdin
  key = int(sys.stdin.readline())

  # print key
  print('Key: ' + str(key))

  # decrypt and print the plain text using rail fence cipher
  print('Decoded Text: ' + rail_fence_decode(encoded_text, key))

  # print Vigenere cipher
  print('\nVigenere Cipher\n')

  # read the plain text from stdin
  plain_text = sys.stdin.readline().strip()

  # print plain text
  print('Plain Text: ' + plain_text)

  # read the pass phrase from stdin
  phrase = sys.stdin.readline().strip()

  # print pass phrase
  print('Pass Phrase: ' + phrase)

  # encrypt and print the encoded text using Vigenere cipher
  print('Encoded Text: ' + vigenere_encode(plain_text, phrase))

  # read the encoded text from stdin
  encoded_text = sys.stdin.readline().strip()

  # print encoded text
  print('\nEncoded Text: ' + encoded_text)

  # read the pass phrase from stdin
  phrase = sys.stdin.readline().strip()

  # print pass phrase
  print('Pass Phrase: ' + phrase)

  # decrypt and print the plain text using Vigenere cipher
  print('Decoded Text: ' + vigenere_decode(encoded_text, phrase) + '\n')

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
