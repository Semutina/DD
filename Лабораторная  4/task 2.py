def get_count_char(str_):
    letter_ = {

    }
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for letter in str_:
        if letter.isalpha():
            if letter in letter_:
                letter_[letter] += 1
            else:
                letter_[letter] = 1
    return letter_



def letter_percentage(letter_):
    letters_ = {

    }
    for letter, count in letter_.items():
        letters_[letter] = round(count / sum(letter_.values()) * 100, 2)

    return letters_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
