def has_negatives(a):
    crossover = {}

    for number in a:
        absolute = abs(number)
        if absolute not in crossover:
            crossover[absolute] = 1
        else: 
            crossover[absolute] += 1

    expects = {} 
  
    for key, value in crossover.items(): 
        if value not in expects: 
            expects[value] = [key] 
        else: 
            expects[value].append(key) 

    result = []

    if 2 in expects:
        result = expects[2]

    return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
