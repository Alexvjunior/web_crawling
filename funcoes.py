def str_to_float(dezenas, centavos):
    result = []
    for x in range(0, len(dezenas)):
        dezena = (dezenas[x].text).replace(',', '.')
        c = centavos[x].text
        r = float(f'{dezena}{c}')
        result.append(r)
    return result