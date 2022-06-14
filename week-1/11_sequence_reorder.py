word_sequence = input("Enter a sequence of hyphen-separated words: ")
words_list = []

# print("-".join(sorted(word_sequence)))
single_word = ""
for i in word_sequence:
    
    if i == '-':
        words_list.append(single_word)
        single_word = ""
        continue
    single_word += i
words_list.append(single_word)



for i in range(len(words_list)):
    for j in range((i+1), len(words_list)):
        if words_list[i] > words_list[j]:
            words_list[i], words_list[j] = words_list[j], words_list[i]

print(words_list)