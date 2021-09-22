def spell(txt):
    if len(txt)==1:
        print(txt)
        return ''
    else:
        print(txt[-1])
        txt=spell(txt[:-1])


txt="hello" #input()
spell(txt)