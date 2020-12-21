magician_name = ['a', 'b', 'c', 'd', 'e']

def show_magicians(print_list):
    print(print_list) 

show_magicians(magician_name)
print()

def make_great(add_name_great):
    add_great = []
    for p in add_name_great:
        add_great.append(f'훌륭한 + {p}')
    return add_great

show_magicians(make_great(magician_name))
print()

def two_list(original):
    total = [original, make_great(original)]
    return total

print(two_list(magician_name))