import re
from math import log2
import pandas as pd


with open('data.txt', 'r', encoding='utf-8') as file:
    data_str = file.read().replace('\n', ' ')
data_str.lower()
pattern1 = '[^а-я ]+'  #паттерн для очистки від зайвих символів
pattern2 = '[^а-я]+'  #паттерн для очистки від пробілів
data_str = re.sub(pattern1, '', data_str)
data_str_spaces = ' '.join(data_str.split())  #чистий текст з пробілами
data_str_no_spaces = re.sub(pattern2, '', data_str)  #чистий текст без пробілів
alph_spaces = 'абвгдеёэжзиыйклмнопрстуфхцчшщъьюя '
alph_no_spaces = 'абвгдеёэжзиыйклмнопрстуфхцчшщъьюя'



def frequency_letters(string):
    text_len = len(string)
    freq_chars = {}
    for i in string:    #отримуєм словник з абсолютними частотами
        if i in freq_chars:
            freq_chars[i] += 1
        else:
            freq_chars[i] = 1
    rel_freq_chars = {}
    for letter in freq_chars.keys():    #отримуєм словник з відносними частотами
        rel_freq_chars[letter] = round((freq_chars[letter]) / text_len, 4)
    return rel_freq_chars
    # analitics = Counter(strings)
    # analitics = {key: value for key, value in analitics.items() if key.isalpha()}
    # return analitics


def frequency_bigrams(string):
    bi1 = re.findall('..', string)
    cl_data_str_r = string[1:] + string[0]
    #bi2 = re.findall('..', cl_data_str_r)  #враховуєм перехресні біграми
    bi2 = []  #не враховуєм перехресні біграми
    bigrams = bi1 + bi2
    bi_count = len(string)
    freq_bi = {}
    for i in bigrams:   #отримуєм словник з абсолютними частотами
        if i in freq_bi:
            freq_bi[i] += 1
        else:
            freq_bi[i] = 1
    rel_freq_bi = {}
    for pair in freq_bi.keys():   #отримуєм словник з відносними частотами
         rel_freq_bi[pair] = round((freq_bi[pair]) / bi_count, 10)
    return rel_freq_bi


def h1(string):
    h1 = 0
    vals = frequency_letters(string).values()
    for i in vals:
        h1 += - i * log2(i)
    return h1


def h2(string):
    h2 = 0
    vals = list(frequency_bigrams(string).values())
    for i in vals:
        h2 += - i * log2(i)
    return h2


def r_(string, h, alphabet):
    h0 = log2(len(alphabet))
    r = 0
    if h == 1:
        h = h1(string)
        r = 1 - (h / h0)
    elif h == 2:
        h = h2(string)
        r = 1 - (h / h0)
    return r


# fl_ws = frequency_letters(data_str_spaces)  #freqency letters - text with spaces
# fl_ns = frequency_letters(data_str_no_spaces)  #frequency letters - text without spaces
# bi_x_sp = frequency_bigrams(data_str_spaces)  #frequency crossed bigrams - text with spaces
# bi_x_nosp = frequency_bigrams(data_str_no_spaces) #frequency crossed bigrams - text without spaces
# bi_sp = frequency_bigrams(data_str_spaces)
# bi_nosp = frequency_bigrams(data_str_no_spaces)
# df = pd.DataFrame(data=bi_nosp, index=['bi freq without spaces'])
# df = (df.T)
# df.to_excel('df6.xlsx')
# h1_sp = h1(data_str_spaces)
# h1_nosp = h1(data_str_no_spaces)
# h2_x_sp = h2(data_str_spaces)
# h2_x_nosp = h2(data_str_no_spaces)
# h2_sp = h2(data_str_spaces)
# h2_nosp = h2(data_str_no_spaces)
# print(f'Н1 with spaces: {h1_sp}')
# print(f'H1 without spaces {h1_nosp}')
# print(f'h2 x with spaces: {h2_sp}')
# print(f'h2 x without spaces: {h2_nosp}')


r1 = r_(data_str_spaces, 1, alph_spaces)
r1_nosp = r_(data_str_no_spaces, 1, alph_no_spaces)
print(r1, r1_nosp)
r2 = r_(data_str_spaces, 2, alph_spaces)
r2_nosp = r_(data_str_no_spaces, 2, alph_no_spaces)
print(r2, r2_nosp)
