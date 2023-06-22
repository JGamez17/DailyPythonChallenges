fname = input("Enter file name: ")
fh = open(fname)
# unique_words = []
for line in fh:
    print(line)
    word_list = line.split()
# print(word_list)


# for line in words_list:
#     if line not in unique_words:
#         unique_words.append(line)
# unique_words.sort()
# print(unique_words)
