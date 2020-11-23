# hàm backtracking để tạo ra các hàm chứa dấu ngẫu nhiên
# với các giá trị 0,1,2 lần lượt là none,'-','+'
def permute(list, s):
    if list == 1:
        return s
    else:
        return [ y + x
                 for y in permute(1, s)
                 for x in permute(list - 1, s)
                 ]
# hàm tạo ra các list [123456789] có dấu
def get_values(sign):
    v = 0
    values = []
    for i in range(9):
        s = sign[i]
        d = i + 1
        if s == 0:
            if v >= 0:
                v = v * 10 + d
            else:
                v = v * 10 - d
        elif s == 2:
            if v != 0:
                values.append(v)
            v = d
        elif s == 1:
            if v != 0:
                values.append(v)
            v = -d

    values.append(v)
    return values
# hàm in ra ngoài màn hình kết quả
def to_str(vals):
    s = ""
    for v in vals:
        if v > 0:
            if s:
                s = s + '+' + str(v)
            else:
                s = str(v)
        else:
            s = s + str(v)

    s = s + '=' + str(sum(vals))
    return s

a = permute(9, ["0","1","2"])


for i in range(len(a)):
    b = a[i]
    c = []
    for i in range(9):
        d = int(b[i])
        c.append(d)
    e = get_values(c)
    if  sum(e)== 100:
        print(to_str(e))
