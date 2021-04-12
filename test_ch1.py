def vowel_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for ch in string.lower():
        if ch in vowels:
            count += 1
    return count

print(vowel_count('Carlos'))
print(vowel_count('kidman'))

def test_with_my_first_name():
    assert vowel_count('carlos') == 2

def test_with_my_last_name():
    assert vowel_count('CARLOS KIDMAN') == 4