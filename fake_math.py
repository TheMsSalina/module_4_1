res_ = 0
def divide(first, second):
    global res_
    if second != 0:
        res_ = first / second
        return res_
    else:
        return 'Ошибка'