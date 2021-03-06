#Method 1:
    
def run_len_encode_str_compr (string):
    count = 1
    result = []
    final_res = []
    for i in range(len(string)):
        if i == len(string) - 1:
            result.append([string[i], count])
        elif string[i] == string[i+1]:
            count += 1
        else:
            result.append([string[i], count])
            count = 1
    for i in result:
        final_res.append(i[0]+str(i[1]))
    final_res = ''.join(final_res)
    return final_res

# Method 2:

# Efficient way

def compressBetter(string):
    last = string[0]
    result = []
    count = 1
    for c in string[1:]:
        if c == last:
            count += 1
        else:
            result.append(last + str(count))
            count = 1
            last = c

    result.append(last + str(count))
    return ''.join(result)
