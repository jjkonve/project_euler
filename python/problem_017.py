units = ['','one','two','three','four','five','six','seven','eight','nine']
teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
         'seventeen','eighteen','nineteen']
tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
        'eighty','ninety']


def number_to_string(number):
    string = ''
    if number == 1000:
        return 'onethousand'
    number = str(number)
    if len(number) > 2 and number[-3] != 0:
        string += units[int(number[-3])] + 'hundred'
        if number[-2:] != '00':
            string += 'and'
    if len(number) > 1:
        if number[-2] == '1' and number[-1] != '0':
            string += teens[int(number[-1])]
        else:
            string += tens[int(number[-2])]
            string += units[int(number[-1])]
    else:
        string += units[int(number[-1])]
    return string


def test_number_to_string():
    assert number_to_string(1) == 'one'
    assert number_to_string(10) == 'ten'
    assert number_to_string(11) == 'eleven'
    assert number_to_string(21) == 'twentyone'
    assert number_to_string(100) == 'onehundred'
    assert number_to_string(101) == 'onehundredandone'
    assert number_to_string(120) == 'onehundredandtwenty'
    assert number_to_string(1000) == 'onethousand'


def characters_in_number_range(number_range):
    number_of_characters = 0
    for number in number_range:
        number_of_characters += len(number_to_string(number))
    return number_of_characters


def test_characters_in_number_range():
    assert characters_in_number_range([342]) == 23
    assert characters_in_number_range([115]) == 20
    assert characters_in_number_range([342, 115]) == 23 + 20


print(characters_in_number_range(range(1,1001)))
