def correct_sentence(text):
    sentences = text.split('. ')
    corrected_sentences = []
    for sentence in sentences:
        if sentence:
            sentence = sentence.strip()
            sentence = sentence[0].upper() + sentence[1:]
            if not sentence.endswith('.'):
                sentence += '.'
            corrected_sentences.append(sentence)
    corrected_text = ' '.join(corrected_sentences)
    return corrected_text
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
