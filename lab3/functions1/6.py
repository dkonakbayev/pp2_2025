def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

user_input = "We are ready"
result = reverse_words(user_input)
print(result)