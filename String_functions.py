def replace(string, old, new):
    result = ''
    i = 0
    while i < len(string):
        if string[i:i+len(old)] == old:
            result = result + new
            i = i + len(old)
        else:
            result = result + string[i]
            i += 1
        return result


def count(string, substring):
    count = 0
    i = 0
    while i <= len(string) - len(substring):
        if string[i:i+len(substring)] == substring:
            count += 1
            i += len(substring)
        else:
            i += 1
    return count

def my_startswith(string, start):
    if len(start) > len(string):
        return False
    for i in range(len(start)):
        if string[i] != start[i]:
            return False
    return True

