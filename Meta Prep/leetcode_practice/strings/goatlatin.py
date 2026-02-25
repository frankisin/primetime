def goatLatin(s:str):
    vowels = set("aeiouAEIOU")

    res = []

    sentence = s.split(" ")

    for i,word in enumerate(sentence):
        if word[0] in vowels:
            res.append(word + "ma" + ("a" * (i+1)))
        else:
            res.append(word[1:]+word[0]+"ma" + ("a" * (i+1)))
    return " ".join(res)