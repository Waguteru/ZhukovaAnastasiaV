def replace_p_in_first_half(s):
    n = len(s)
    half_index = n // 2  # Индекс середины строки
    result = ''

    for i in range(n):
        if i < half_index and s[i] == 'п':
            result += '*'
        else:
            result += s[i]
    
    return result

string1 = 'попугай сидит на подоконнике'
print(replace_p_in_first_half(string1))
