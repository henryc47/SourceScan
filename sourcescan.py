import sys
import pickle #for storing objects

def command_handler(arguments):
    if len(arguments)<=1:
        print("please enter a command, type 'sourcescan help' for a list of valid commands ",file=sys.stderr)
        sys.exit(1)
    else:
        main_argument = sys.argv[1]
        extra_arguments = sys.argv[2:]
        if main_argument == "help":
            sourcescan_help()
        elif main_argument == "scan-init":
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

#scan each of the provided filenames
def scan_file(extra_arguments,clean=False):
    for file in extra_arguments:
        scan_single_file(file,clean)  

#scan all files in the provided directory, unless they are marked as not to be scanned
def scan_all(clean=False):
    files_to_scan = get_files_in_directory()
    scan_file(files_to_scan,clean)
    
#just a wrapper for scan_file, with the clean argument set to True
def scan_file_clean(extra_arguments):
    scan_file(extra_arguments,True)

#just a wrapper for scan_all, with the clean argument set to True
def scan_all_clean(ex):
    scan_all(True)

#reset the list of false positives
def false_positive_reset():
    pass

#view the current list of false positives
def view_marked_false_positives():
    pass

#scan an individual file
def scan_single_file(filename,clean):
    try:
        file = open(filename,mode="r") 
    except:
        print(filename," could not be found in the current directory",file=sys.stderr)
        return
    #TODO, actually scan the file
    print("scanning ",filename)


#find and return a list of filepaths in the directory
def get_files_in_directory():
    files = []
    #TODO, later, actually get the filenames
    return files

if __name__ == "__main__":
    command_handler(sys.argv)