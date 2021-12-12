japanese_fruits = {
    'orange',
    'nashi pear',
    'satonishiki cherries',
    'sudachi',
    'kinkan'
}
popular_fruits = {
    'banana',
    'orange',
    'apple',
    'watermelon',
    'pineapple'
}

spanish_fruits = {
    'peach',
    'tangerine',
    'orange',
    'damask',
    'pear',
    'watermelon'
}
brazilian_fruits = {
    'strawberry',
    'apple',
    'orange',
    'tangerine',
    'mango',
    'jenipapo',
    'pineapple',
    'cambuci',
    'banana',
    'mandacaru'
}

def spanish_and_brazilian_fruits(spanish_fruits, brazilian_fruits):
    output = spanish_fruits.intersection(brazilian_fruits)
    return list(output)

print(spanish_and_brazilian_fruits(spanish_fruits, brazilian_fruits))

################################################################################################

def spanish_and_japan_fruits(spanish_fruits, japanese_fruits):
    return list(spanish_fruits & japanese_fruits)

print(spanish_and_brazilian_fruits(spanish_fruits, japanese_fruits))

################################################################################################

def brazilian_and_japan_fruits(brazilian_fruits, japanese_fruits):
    return list(brazilian_fruits & japanese_fruits)

print(spanish_and_brazilian_fruits(brazilian_fruits, japanese_fruits))

################################################################################################

def popular_spanish_or_brazilian_fruits(popular_fruits, spanish_fruits, brazilian_fruits):
    union = spanish_fruits.union(brazilian_fruits)
    output = popular_fruits & union
    return list(output)

print(popular_spanish_or_brazilian_fruits(popular_fruits, spanish_fruits, brazilian_fruits))
