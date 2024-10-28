import sys

#process a caught diff
def process_diff(diff):
    diff_lines = extract_added_lines(diff)
    print("num lines =",len(diff_lines),"lines")
    new_lines_in_diff = extract_new_lines_in_diff(diff_lines)
    for line in diff_lines:
        print(line)

def extract_new_lines_in_diff(diff_lines):
    new_lines = []
    for line in diff_lines:
        #if len(line)>
        #hoohar
        pass

#TODO
def extract_added_lines(diff):
    return diff

#process diff data intercepted by a git hook
if __name__ == "__main__":
    # Read diff data from stdin
    diff_data = sys.stdin.readlines()
    process_diff(diff_data)