import unidecode as ud

def pinyin_converter(pinyin_to_convert):
    """
    Converts pinyin into numeric pinyin.

    Parameters: 
        pinyin_to_convert(str): the pinyin you want to convert e.g. 'nǐhǎo'
    
    Returns: 
        formatted_word(str): the pinyin in numeric format e.g. 'ni3hao3'
    """
    word_beginnings = ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 
                       'z', 'c', 's', 'zh', 'ch', 'sh', 'r', 'j', 'q', 'w',
                       'x', 'y']

    word_endings = ['ueng', 'uang', 'iong', 'iang', 'üan', 'uan', 'uai',
                     'ing', 'ian', 'iao', 'ong', 'eng', 'ang', 'ün', 'üe',
                      'un', 'ui', 'uo', 'ua', 'in', 'iu', 'ie', 'ia', 'en',
                      'an', 'ou', 'ao', 'ei', 'ai', 'er', 'ü', 'u', 'i', 'e',
                       'o', 'a']

    first_tones = ['ā', 'ē', 'ī', 'ō', 'ū', 'ǖ']
    second_tones = ['á', 'é', 'í', 'ó', 'ú', 'ǘ']
    third_tones = ['ǎ', 'ă', 'ě', 'ĕ', 'ǐ', 'ĭ', 'ǒ', 'ŏ', 'ǔ', 'ŭ', 'ǚ']
    fourth_tones = ['à', 'è', 'ì', 'ò', 'ù', 'ǜ']
    pinyin_vowels = ['a', 'e', 'i', 'o', 'u']

    converted_word = ""
    next_valid_index = 0
    pinyin_to_convert = pinyin_to_convert.lower()
    pinyin_to_convert = ''.join(pinyin_to_convert.split())

    # For each index value/letter in pinyin_to_convert, check the first four 
    # letters then three...two...and finally one letter to see if the 
    # letter(s) are in the word_endings list.
    for i, pinyin_letter in enumerate(pinyin_to_convert):
        if i < next_valid_index:
            continue
        substring_one = pinyin_to_convert[i:i + 1]
        substring_two = pinyin_to_convert[i:i + 2]
        substring_three = pinyin_to_convert[i:i + 3]
        substring_four = pinyin_to_convert[i:i + 4]
        ending_match_found = False

        for ending in word_endings:
            # If the letter(s) are in word_endings, append the letters to
            # converted_word, update the value of next_valid_index and then
            # continue iterating from the index value of next_valid_index.
            if ud.unidecode(substring_four) == ending:
                converted_word += substring_four + " "
                next_valid_index = i + 4
                ending_match_found = True
                break
            elif ud.unidecode(substring_three) == ending:
                converted_word += substring_three + " "
                next_valid_index = i + 3
                ending_match_found = True
                break
            elif ud.unidecode(substring_two) == ending:
                converted_word += substring_two + " "
                next_valid_index = i + 2
                ending_match_found = True
                break
            elif ud.unidecode(substring_one) == ending:
                converted_word += substring_one + " "
                next_valid_index = i + 1
                ending_match_found = True
                break
            # If the letter(s) from the current index position are not in
            # word_endings, append the letter at the current index position to
            # converted_word and then continue iterating from the next
            # immediate index value.
        if not ending_match_found:
            converted_word += pinyin_letter

    converted_words = converted_word.split()

    # Check each letter in each word of converted_words and see if any of them
    # are in the following tones lists. If they are, append the corresponding
    # number of the tone to the end of the word.
    formatted_word = ""
    for word in converted_words:
        formatted_word += ud.unidecode(word)
        for letter in word:
            if letter in first_tones:
                formatted_word += '1'
            elif letter in second_tones:
                formatted_word += '2'
            elif letter in third_tones:
                formatted_word += '3'
            elif letter in fourth_tones:
                formatted_word += '4'
    return formatted_word   
             
