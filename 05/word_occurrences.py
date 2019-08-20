print("------------------Text:-----------------------------------")
print("Text: this is a collection of words of nice words this is a fun thing it is")
print("-----------------------------------------------------")
print("Which word above you would like to count? Please enter: ")
word_dic = {
    "a": "2",
    "collection": "1",
    "fun": "1",
    "is": "3",
    "it": "1",
    "nice": "1",
    "of": "2",
    "thing": "1",
    "this": "2",
    "words": "2"
}
times = int(input("How many times you would like to search? >>> "))
for i in range(times):
    word_in = input(">>")
    index = 0
    for key in word_dic:
        if key == word_in:
            print("{:{}} = {}".format(word_in, 7, word_dic[key]))
            index = 1
            break
    if index == 0:
        print("NOT FOUND !!")