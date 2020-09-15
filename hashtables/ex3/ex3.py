def intersection(arrays):
    cross = {}
    
    for singles in arrays:
        for value in singles:
            if value not in cross:
                cross[value] = 1
            else:
                cross[value] += 1
                
    reserve = {}
                
    for key, value in cross.items():
        if value not in reserve:
            reserve[value] = [key]
        else:
            reserve[value].append(key)
            
    result = reserve[len(arrays)]
                
    

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
