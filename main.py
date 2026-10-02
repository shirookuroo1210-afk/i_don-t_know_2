def count_words(text):
    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count
kata = input("masukkan teks: ").split()
hitung = {}

for hasil in kata:
    if hasil in hitung:
        hitung[hasil] += 1
    else:
        hitung[hasil] = 1

for k, v in hitung.items():
    print(f"{k} : {v}")
count_words
