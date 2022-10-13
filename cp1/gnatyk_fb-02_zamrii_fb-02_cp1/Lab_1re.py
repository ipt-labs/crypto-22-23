import re
import math

text_with_spaces1 = open("withSpaces.txt", "r", encoding='utf-8')
text_with_spaces = text_with_spaces1.read()
text_with_spaces = text_with_spaces.lower()
text_with_spaces = re.sub(r"[\W\d]", " ", text_with_spaces)
text_with_spaces = re.sub(r"[A-Za-z]", " ", text_with_spaces)
no_spaces_text = text_with_spaces.replace(" ", "")

file = open("noSpaces.txt", "w")
file.write(no_spaces_text)
file.close()
text_with_spaces1.close()

print(len(text_with_spaces))
#---------------Без пробілів---------------#
print('#Для тексту без пробілів', '\n')

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

dict1 = {}
for i in alphabet:
    count_1 = no_spaces_text.count(i)
    len_1 = len(no_spaces_text)
    dict1[i] = count_1 / len_1
#print('Частота символів в тексті: ', dict1)

bigram_for_alphabet = []
for i in alphabet:
    for k in alphabet:
        bigram_for_alphabet.append(i + k)
#print('Список біграм для алфавіту без пробілів: ', bigram_for_alphabet)

text_bigrams_without_spaces = []
for i in range(0, len(no_spaces_text)-1, 1):
    n1 = no_spaces_text[i]
    n1_s = no_spaces_text[i + 1]
    text_bigrams_without_spaces.append(n1 + n1_s)
#print('Всі біграми з тексту без пробілів: ', text_bigrams_without_spaces)

text_bigrams_without_spaces_reply = []
for i in range(0, len(no_spaces_text)-1, 2):
    n1_1 = no_spaces_text[i]
    n1_1_s = no_spaces_text[i + 1]
    text_bigrams_without_spaces_reply.append(n1_1 + n1_1_s)
#print('Всі біграми з тексту без пробілів з кроком 2: ', text_bigrams_without_spaces_reply)

dict_b1 = {}
for i in bigram_for_alphabet:
    count_2 = text_bigrams_without_spaces.count(i)
    len_2 = len(text_bigrams_without_spaces)
    dict_b1[i] = count_2 / (len_2)
#print('Частота біграм в тексті без пробілів: ', dict_b1)

dict1_b1 = {}
for i in bigram_for_alphabet:
    count2_2 = text_bigrams_without_spaces_reply.count(i)
    len2_2 = len(text_bigrams_without_spaces_reply)
    dict1_b1[i] = count2_2 / (len2_2)
#print('Частота біграм в тексті без пробілів з кроком 2: ', dict1_b1)

counter1 = 0
for j in dict1.values():
    counter1 = counter1 + (j * math.log2(j))
H1_without_space = -counter1
print("H1 для букв без пробілів: ", H1_without_space)

def H2(xx):
    counter = 0
    for i in xx.values():
        if i != 0:
            counter = counter + (i * math.log2(i)) / 2
    return -counter
print("H2 для біграм без пробілів: ", H2(dict_b1))
print("H2 для біграм без пробілів  кроком 2: ", H2(dict1_b1))

def H(H, B):
    return (1 - (H / (math.log2(len(B)))))

R_H1_without_space = H(H1_without_space, alphabet)
print('Надлишковість для H1 без пробілів: ', R_H1_without_space)
R_H2_without_space = H(H2(dict_b1), alphabet)
print('Надлишковість для H2 без пробілів: ', R_H2_without_space)
R_H2_without_space_step_2 = H(H2(dict1_b1), alphabet)
print('Надлишковість для H2 без пробілів з кроком 2: ', R_H2_without_space_step_2, '\n')

#------------З пробілами------------#
print('#Для тексту з пробілами', '\n')

alphabet_p = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']

dict2 = {}
for i in alphabet_p:
    count_3 = text_with_spaces.count(i)
    len_3 = len(text_with_spaces)
    dict2[i] = count_3 / len_3
#print("Частота букв з пробілами: ", dict2)

bigram_for_alphabet1 = []
for i in alphabet_p:
    for j in alphabet_p:
        bigram_for_alphabet1.append(i + j)
#print('Список біграм для алфавіту з пробілами: ', bigram_for_alphabet1)

text_bigram_with_spaces = []
for i in range(0, len(text_with_spaces) - 1, 1):
    n2 = text_with_spaces[i]
    n2_s = text_with_spaces[i + 1]
    text_bigram_with_spaces.append(n2 + n2_s)
#print('Всі біграми в тексті з пробілами: ', text_bigram_with_spaces)

text_bigram_with_spaces_without_reply = []
for i in range(0, len(text_with_spaces) - 1, 2):
    n2_2 = text_with_spaces[i]
    n2_2_s = text_with_spaces[i + 1]
    text_bigram_with_spaces_without_reply.append(n2_2 + n2_2_s)
#print('Всі біграми в тексті з пробілами з кроком 2: ', text_bigram_with_spaces_without_reply)

dict_b2 = {}
for i in bigram_for_alphabet1:
    count_4 = text_bigram_with_spaces.count(i)
    len_4 = len(text_bigram_with_spaces)
    dict_b2[i] = count_4 / (len_4)
#print('Частота біграм в тексті з пробілами', dict_b2)

dict2_b2 = {}
for i in bigram_for_alphabet1:
    count4_4 = text_bigram_with_spaces_without_reply.count(i)
    len4_4 = len(text_bigram_with_spaces_without_reply)
    dict2_b2[i] = count4_4 / (len4_4)
#print('Частота біграм в тексті з пробілами з кроком 2', dict2_b2)

counter2 = 0
for i in dict2.values():
    counter2 = counter2 + (i*math.log2(i))
H1_with_space = -counter2
print("H1 для букв з пробілами: ", H1_with_space)
print("H2 для біграм без пробілів: ", H2(dict_b2))
print("H2 для біграм без пробілів з кроком 2: ", H2(dict2_b2))

R_H1_with_space = H(H1_with_space, alphabet_p)
print('Надлишковість для H1 з пробілами: ', R_H1_with_space)
R_H2_with_space = H(H2(dict_b2), alphabet_p)
print('Надлишковість для H2 з пробілами: ', R_H2_with_space)
R_H2_with_space_step_2 = H(H2(dict2_b2), alphabet_p)
print('Надлишковість для H2 з пробілами: ', R_H2_with_space_step_2, '\n')
