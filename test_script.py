import sys

def process_diff(diff):
    # Process the diff lines
    print("num lines =",len(diff),"lines")
    for line in diff:
        print(line)

if __name__ == "__main__":
    # Read diff data from stdin
    diff_data = sys.stdin.readlines()
    process_diff(diff_data)