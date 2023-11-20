def count_substring(string, sub_string):
    c=0
    n=len(sub_string)
    for i in range(0,len(string)):
        if string[i]==sub_string[0]:
            if string[i:i+n]==sub_string:
                c=c+1
    return c

    string = input()
    sub_string = input()
    count = count_substring(string, sub_string)
    print(count)
