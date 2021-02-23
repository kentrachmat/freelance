def isfloat(data):
    try:
        float(data)
        return True
    except ValueError:
        return False

def check_datatype (data, datatype, message):
    try:
        if datatype == "Int":
            if isinstance(int(data),int):
                return (True,"")

        elif datatype == "Float":
            if not data.isdigit() or type(data) != str:
                return (True,"")
            else:
                return (False,message)

        elif datatype == "String":
            if data != "":
                return (True,"")
            else:
                return (False,message)

    except ValueError:
        return (False,message)

def check_interval (data, start, end, message):
    if type(int(data)) != int or type(int(start)) != int or type(int(data)) != int or start > end:
        return message
    return (start <= int(data) <= end,"")

#Q1
#data     = input("data : ")
#start    = input("start : ")
#end      = input("end : ")
#message  = input("message : ")
#print(check_interval (data, start, end, message))

#Q2
#data     = input("data : ")
#datatype = input("datatype : ")
#message  = input("message : ")
#print(check_datatype (data, datatype, message))