import pprint

list_ = [{"bin": bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(16)]

pprint.pprint(list_)

# {num: bin(num) for num in range(16)},
# {num: num for num in range(16)},
# {num: hex(num) for num in range(16)},
# {num: oct(num) for num in range(16)}
