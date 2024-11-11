# throwVal = 'throw00';
# def returnThrow():
#     global throwVal
#     if throwVal == 'throw00':
#         throwVal = 'throw11';
        
        
#     elif throwVal == 'throw11':
#         throwVal= 'throw00'
#     return throwVal
# returnThrow()


throwVal = 'throw00'

def returnThrow():
    global throwVal
    if throwVal == 'throw00':
        throwVal = 'throw11'
    elif throwVal == 'throw11':
        throwVal = 'throw00'
    return throwVal
