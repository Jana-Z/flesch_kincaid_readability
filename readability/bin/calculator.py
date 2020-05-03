from bin.fundementals import count_words, \
    split_words, split_sentences, \
    count_sentences, count_syllables

def get_reading_ease(text, lang='en'):
    syllable_count, word_count, sentence_count = _get_counts(text, lang)
    if sentence_count == 0: sentence_count = 1
    if word_count == 0: word_count = 1
    return (206.835 - (1.015 * (word_count / sentence_count))) - (84.6 * (syllable_count / word_count))

def get_reading_level(text, lang='en'):
    syllable_count, word_count, sentence_count = _get_counts(text, lang)
    if sentence_count == 0: sentence_count = 1
    if word_count == 0: word_count = 1
    return (0.39 * (word_count/sentence_count)) + (11.8 * (syllable_count/word_count)) - 15.59

def _get_counts(text, lang='en'):
    word_count = count_words(text)
    words = split_words(text)
    sentence_count = count_sentences(text)
    syllable_count = 0
    for word in words:
        syllable_count += count_syllables(word, lang)
    return syllable_count, word_count, sentence_count

def convert_to_grade_level(score):
    if 0.0 > score or 100.0 < score:
        return {
            'level': 'None',
            'notes': 'not on the scale'
        }
    if 0.0 <= score < 30.0:
        return {
            'level': 'College graduate',
            'notes': 'Very difficult to read. Best understood by university graduates.'
        }
    if 30.0 <= score < 50.0:
        return {
            'level': 'College',
            'notes': 'Difficult to read.'
        }
    if 50.0 <= score < 60.0:
        return {
            'level': '10th to 12th grade',
            'notes': 'Fairly difficult to read.'
        }
    if 60.0 <= score < 70.0:
        return {
            'level': '8th & 9th grade',
            'notes': 'Plain English. Easily understood by 13- to 15-year-old students.'
        }
    if 70.0 <= score < 80.0:
        return {
            'level': '7th grade',
            'notes': 'Fairly easy to read.'
        }
    if 80.0 <= score < 90.0:
        return {
            'level': '6th grade',
            'notes': 'Easy to read. Conversational English for consumers.'
        }
    if 90.0 <= score <= 100.0:
        return {
            'level': '5th grade',
            'notes': 'Very easy to read. Easily understood by an average 11-year-old student.'
        }