def remove_char(s1,s2):
    dict = {ord(s2) : None}
    print(s1.translate(dict))
def removeee_char(s1,s2):
    print(s1.replace(s2, ''))
s1 = 'queesr'
s2 = 'e'
removeee_char(s1,s2) 
