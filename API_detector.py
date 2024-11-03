
def detect_in_line(line):
    if len(line)>20:
        return True,line[20:]
    else:
        return False,None

detection_message = "WARNING : Possible API_key detected ->"