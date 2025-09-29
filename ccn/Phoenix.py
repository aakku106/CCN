# throwVal = 'throw00';
# def returnThrow():
#     global throwVal
#     if throwVal == 'throw00':
#         throwVal = 'throw11';
        
        
#     elif throwVal == 'throw11':
#         throwVal= 'throw00'
#     return throwVal
# returnThrow()


throwVal = 'throw'

def returnThrow():
    global throwVal
    if throwVal == 'throw00':
        throwVal = 'throw11'
    elif throwVal == 'throw11':
        throwVal = 'throw00'
    return throwVal

val = 0;
print(val);
vall = throwVal,val;
print(vall);