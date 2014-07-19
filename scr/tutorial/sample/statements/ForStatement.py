word = ['cat','window','defenestrate']
for w in word:
    print w, len(w)


for w in word[:]:
    if len(w) > 6:
        word.insert(0,w)

print word