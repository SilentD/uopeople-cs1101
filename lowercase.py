def any_lowercase4(s):
     flag = False
     for c in s:
          flag = flag or c.islower()
     return flag
    
s='flag'

print('is flag lowercase4 ', any_lowercase4(s))
