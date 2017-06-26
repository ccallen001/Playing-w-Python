names = ['Johnny', 'Steve', 'Martha', 'Sam', 'Todd']
amounts = [3.22233, 4.6695, 10.4, 3, 100.27]

def create_map(keys, values, key_val_map):
    if len(keys) != len(values):
        print("ERROR: length of the iterable arguments to create_map must match")
    else:
        for i, key in enumerate(keys):
            key_val_map[key] = values[i]

    return key_val_map


names_amounts_map = create_map(names, amounts, {})

for key in names_amounts_map:
    print("""
    Hi, {}!
    
    Thanks for your purchase!
    Your total is %.2f.
    """.format(key) % names_amounts_map[key])
