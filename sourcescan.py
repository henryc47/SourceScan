import sys


def command_handler(arguments):
    if len(arguments)<=1:
        print("please enter a command, type 'sourcescan help' for a list of valid commands ",file=sys.stderr)
        sys.exit(1)
    else:
        main_argument = sys.argv[1]
        extra_arguments = sys.argv[2:]
        if main_argument == "help":
            sourcescan_help()
        elif main_argument == "scan_init":
            scan_init()
        elif main_argument == "scan-file":
            scan_file(extra_arguments)
        elif main_argument == "scan-all":
            scan_all()
        elif main_argument == "scan-file-clean":
            scan_file_clean(extra_arguments)
        elif main_argument == "scan-all-clean":
            scan_all_clean(extra_arguments)
        elif main_argument == "false-positive-reset":
            false_positive_reset(extra_arguments)
        elif main_argument == "view-marked-false-positives":
            view_marked_false_positives(extra_arguments)
        else:
            print(main_argument," is not a valid command")
            sys.exit(1)
        sys.exit(0) #default exit without error

def sourcescan_help():
    print("Valid commands for sourcescan are")
    print("help - provides a list of valid commands")
    print("scan-init - setup rules for source scanning in this project")
    print("scan-file - scan a file for any security errors")
    print("scan-all - scan all files in the current directory")
    print("scan-file-clean - scan a file for any security errors, disregarding existing confirmed false positives")
    print("scan-all-clean - scan all files in the current directory, disregarding existing confirmed false positives")
    print("false-positive-reset - reset the list of false positives for this directory")
    print("view-marked-false-positives - view all the strings which have been marked as false positives")
    sys.exit(0)

def scan_init():
    pass

def scan_file(extra_arguments):
    pass
    #for file in extra_arguments:  


def scan_all():
    pass

def scan_file_clean(extra_arguments):
    pass

def scan_all_clean():
    pass

def false_positive_reset():
    pass

def view_marked_false_positives():
    pass

def scan_single_file(filename):
    try 

#
if __name__ == "__main__":
    command_handler(sys.argv)