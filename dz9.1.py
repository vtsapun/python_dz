def popular_words(text, words):
    words_list = text.lower().split()
    word_count = {}
    for word in words:
        count = words_list.count(word.lower())
        word_count[word] = count
    return word_count
input_text = '''When I was One I had just begun When I was Two I was nearly new '''
input_words = ['i', 'was', 'three', 'near']
result = popular_words(input_text, input_words)
print(result)
