dict = {"Google" :1480,"Email":300,"Natural Traffic":440,"TV Spot":700}
print(dict['Email'])

dict2 = {"Natural Traffic" :520,"News":600}

dict.update(dict2)
dict.pop('Email')
print(dict.keys())
print(dict)
