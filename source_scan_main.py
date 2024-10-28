import sys

#process a caught diff
def process_diff(diff):
    added_lines = extract_added_lines(diff)
    print("num lines =",len(added_lines),"lines")
    for line in added_lines:
        print(line)

#TODO
def extract_added_lines(diff):
    return diff

#process diff data intercepted by a git hook
if __name__ == "__main__":
    # Read diff data from stdin
    diff_data = sys.stdin.readlines()
    process_diff(diff_data)