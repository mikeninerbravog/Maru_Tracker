from twisted_fate import Deck

def getChampion(deckCode):
    cards = Deck.decode(deckCode).cards
    heros = ''
    for card in cards:
        if card.isChampion:
            heros += '(' + str(card.count) + ') '
            heros += card.name + ' '
    if heros == '':
        heros = 'No champion '
    print(heros)
    return heros




#print(getChampion('CICACAQDBEAQGBARAIAQGFBOAQAQIAJEGQ5AIAIDAMGQCAYEAUBACAZTG'))
#getChampion('CICACAQDBEAQGBARAIAQGFBOAQAQIAJEGQ5AIAIDAMGQCAYEAUBACAZTG4CACBA3D4TCOAA')
#getChampion('CEAQYAYJBEOCGOBZJFGFIVKWMBSAEAIBAUMQCAYJAIAA')
#getChampion('CEBAEAIAAMOQOAICAIFRUKBMGE4QEAYBAIDAYFICAEAB4KICAIAQAEJFAEAQEGA')
#getChampion('CIBQCAICGEBAEAQGBECAGCI3EMZVYAYBAMBBIAQCAIBQKBADBEESQKKVAMAQCAQJAEBAECADAMERGKTC')