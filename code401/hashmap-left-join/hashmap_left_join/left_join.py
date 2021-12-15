
h1 = {
    'diligent':'employed',
    'fond':'enamored',
    'guide': 'usher',
    'outfit': 'garb',
    'wrath':'anger'
}

h2 = {
    'diligent':'idle',
    'fond':'averse',
    'guide': 'follow',
    'flow': 'jam',
    'wrath':'delight'
}

def left_join(h1,h2):

    res =[]
    if h1 is None:
        return res
    
    for i,k in enumerate(h1):
        anto_word = h2[k] if k in h2 else None
        res.append([k,h1[k],anto_word])
    return res
