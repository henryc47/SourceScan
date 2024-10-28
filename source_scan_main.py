import sys

#process a caught diff
def process_data(data,is_diff):
    if is_diff:
        lines = extract_new_lines_in_diff(data)
    else: #default just read a whole file
        lines = data
    for line in lines:
        print(line,end="")

#There are probably ways of having a line falsely register as a new line from this function, hopefully that will be pretty rare. 
def extract_new_lines_in_diff(diff_lines):
    new_lines = []
    for line in diff_lines: #for each line in diff, check if it is a new line in the diff
        if len(line)>=1:
            if line[0]=="+": #found possible new line added
                if len(line)>=3:
                    if line[0:3]=="+++": #actually just a new file added
                        continue

                #add the new line
                new_lines.append(line[1:])
    return new_lines

#TODO
def extract_added_lines(diff):
    return diff

#process diff data intercepted by a git hook
if __name__ == "__main__":
    # Read diff data from stdin
    data = sys.stdin.readlines()
    is_diff=False
    if len(sys.argv)>1:#there are additional arguments
        if sys.argv[1]=="diff":
            is_diff = True
    
    process_data(data,is_diff)