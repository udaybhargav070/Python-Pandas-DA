# Approach-1

def encode_sentence(sentence):
    words = sentence.split()
    encoded_words = []

    for word in words:
        if len(word) > 3:
            encoded_words.append(word[::-1])
        else:
            encoded_words.append(word)

    encoded_sentence = ' '.join(encoded_words)
    return encoded_sentence

# Example usage:
input_sentence = "AT DAWN LOOK TO THE EAST"
result = encode_sentence(input_sentence)
print(result)


# Approach-2

def enc_sen(sen):
    enc_wor = [word[::-1] if len(word) > 3 else word for word in sen.split()]
    enc_sen = ' '.join(enc_wor)
    return enc_sen
  
# Example Usage:  
input_sentence = "AT DAWN LOOK TO THE EAST"
result = enc_sen(input_sentence)
print(result)