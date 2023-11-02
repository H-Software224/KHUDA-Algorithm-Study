def solution(code):
    mode = 0
    ret = ''
    for i in range(len(code)):
        if mode == 0:
            if code[i] != '1' and i % 2 == 0:
                ret += ''.join(code[i])
            elif code[i] == '1':
                mode = 1
        elif mode == 1:
            if code[i] != '1' and i % 2 == 1:
                ret += ''.join(code[i])
            elif code[i] == '1':
                mode = 0

    if ret == '':
        return "EMPTY"
    else:
        return ret