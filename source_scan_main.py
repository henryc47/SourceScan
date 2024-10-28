import sys

#process a caught diff
def process_diff(diff):
    diff_lines = extract_added_lines(diff)
    print("num lines =",len(diff_lines),"lines")
    new_lines_in_diff = extract_new_lines_in_diff(diff_lines)
    for line in new_lines_in_diff:
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
    diff_data = sys.stdin.readlines()
    process_diff(diff_data)