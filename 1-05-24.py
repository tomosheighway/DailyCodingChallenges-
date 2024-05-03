"""Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. 

You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid."""


def encoding(input_string):
    encoded_string = ""  
    counter = 1
    i = 1

    while i < len(input_string):
        if input_string[i] == input_string[i - 1]:
            counter += 1
        else:
            encoded_string += str(counter) + input_string[i - 1]
            counter = 1
        i += 1

    encoded_string = encoded_string +  str(counter) + input_string[i - 1] 
    return encoded_string    
    
def decoding(encoded_string):
    decoded_string = ""
    counter = 0
    i = 0

    while i < len(encoded_string):
        if encoded_string[i].isdigit():
            counter = counter * 10 + int(encoded_string[i])
        else:
            decoded_string = decoded_string + encoded_string[i] * counter
            counter = 0
        i += 1
    
    # Alternative approach 
    """
    string_counter = ""
    for char in encoded_string:
        if char.isdigit():
            string_counter += char
        else:
            decoded_string = decoded_string + char * int(string_counter)
            string_counter = ""
    """
    return decoded_string


input_string = "AAAABBBCCDAA"  # Ans 4A3B2C1D2A 
print(encoding(input_string))

encoded_string = "4A3B2C1D2A" # Ans AAAABBBCCDAA
print(decoding(encoded_string))