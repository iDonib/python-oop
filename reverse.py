def reverse_words(Sentence):
    words = Sentence.split(" ")

    new_words = [words[::-1] for words in words]

    res_str = " ".join(new_words)

    return res_str

str1 = "My name is Binod"
print(reverse_words(str1))