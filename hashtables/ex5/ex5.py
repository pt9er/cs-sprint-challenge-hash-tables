# Your code here



def finder(files, queries):
    table ={}

    for path in files:
        cmpt = path.split('/')
        
        if table.get(cmpt[-1]):
            table[cmpt[-1]].append(path)
            
        else:
            table[cmpt[-1]] = [path]

    result = []
    
    for values in queries:
        if table.get(values):
            result.extend(table.get(values))
            
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
