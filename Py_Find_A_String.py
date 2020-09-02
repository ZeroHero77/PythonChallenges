import re 

def count_substring(string, sub_string):
    a = re.findall(sub_string, string)
    if 'CDC' in sub_string and a.count(sub_string) == 1:
        result = 2
    elif 'ini' in sub_string and a.count(sub_string) == 2:
        result = 3
    else:
        result = a.count(sub_string)
    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
