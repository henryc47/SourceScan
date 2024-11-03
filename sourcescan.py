import sys
import os
import pickle #for storing objects
import API_detector


class CommandHandler():
    def __init__(self):
        self.line_scan_types = [API_detector] #currently available scan types
        #load the known false-positive patterns from file
        if os.path.exists("sourcescan_patterns.pkl"):
            with open("sourcescan_patterns.pkl", "rb") as file:
                self.known_patterns = pickle.load(file)
        #if no file storing known false-positive patterns from file
        else:
            self.known_patterns = set() #set storing all the known false-positive patterns for this project   
        #load the known blocked file types from file
        if os.path.exists("sourcescan_config.pkl"):
            with open("sourcescan_blocked_files.pkl", "rb") as file:
                self.blocked_files = pickle.load(file)
        else:
            self.blocked_files = set()
             
    #store known false positive patterns on program exit
    def store_known_patterns(self):
        with open("sourcescan_patterns.pkl", "wb") as file:
            pickle.dump(self.known_patterns,file)

    #store blocked file patterns on program exit
    def store_block_file_types(self):
        with open("sourcescan_blocked_files.pkl", "wb") as file:
            pickle.dump(self.blocked_files,file)

    def run(self,arguments):
        if len(arguments)<=1:
            print("please enter a command, type 'sourcescan help' for a list of valid commands ",file=sys.stderr)
            sys.exit(1)
        else:
            main_argument = sys.argv[1]
            extra_arguments = sys.argv[2:]
            if main_argument == "help":
                self.sourcescan_help()
            elif main_argument == "init":
                self.scan_init()
            elif main_argument == "scan-file":
                self.scan_file(extra_arguments)
            elif main_argument == "scan-all":
                self.scan_all()
            elif main_argument == "scan-file-clean":
                self.scan_file_clean(extra_arguments)
            elif main_argument == "scan-all-clean":
                self.scan_all_clean()
            elif main_argument == "false-positive-reset":
                self.false_positive_reset()
            elif main_argument == "view-marked-false-positives":
                self.view_marked_false_positives()
            elif main_argument == "add-blocked-file-type":
                self.add_blocked_file_pattern(extra_arguments)
            elif main_argument == "remove-blocked-file-type":
                self.remove_blocked_file_pattern(extra_arguments)
            elif main_argument == "view-blocked-file-type":
                self.view_blocked_file_patterns()
            else:
                print(main_argument," is not a valid command")
                sys.exit(1)
            #do stuff on file exit
            self.store_known_patterns()
            self.store_block_file_types()
            sys.exit(0) #default exit without error

    def sourcescan_help(self):
        print("Valid commands for sourcescan are")
        print("help - provides a list of valid commands")
        print("init - setup rules for source scanning in this project")
        print("scan-file - scan a file for any security errors")
        print("scan-all - scan all files in the current directory")
        print("scan-file-clean - scan a file for any security errors, disregarding existing confirmed false positives")
        print("scan-all-clean - scan all files in the current directory, disregarding existing confirmed false positives")
        print("false-positive-reset - reset the list of false positives for this directory")
        print("view-marked-false-positives - view all the strings which have been marked as false positives")
        print("add-blocked-file-type - add a type of file to block")
        print("remove-blocked-file-type - stop blocking a type of file")
        print("view-blocked-file-type - print out all the file types that are currently blocked")

    #setup the configuration files for SourceScan
    def scan_init(self):
        
        print("Welcome to the SourceScan Initialization Wizard")
        if os.path.exists("sourcescanconfig.pkl"):
            user_input = input("You have already initialized SourceScan in this directory, Type y to reinitalize: ")
            if not user_input=="y":
                print("SourceScan initialization cancelled")
                return
        user_input = input("Do you want to prevent SourceScan from analyzing it's own configuration files? (Recommended) Type y to confirm : ")
        if user_input=="y":
            self.blocked_files.add(".pkl")
        user_input = input("Do you want to add SourceScan configuration files to your .gitignore file (Recommended) Type y to confirm : ")
        if user_input=="y":
            self.update_gitignore()
        user_input = input("Do you want to automatically run SourceScan before git commits? Type y to confirm : ")
        if user_input=="y":
            pass
            #TODO
        print("Initialization complete")

    #scan each of the provided filenames
    def scan_file(self,extra_arguments,clean=False):
        for file in extra_arguments:
            self.scan_single_file(file,clean)  

    #scan all files in the provided directory, unless they are marked as not to be scanned
    def scan_all(self,clean=False):
        files_to_scan = self.get_files_in_directory()
        self.scan_file(files_to_scan,clean)
        
    #just a wrapper for scan_file, with the clean argument set to True
    def scan_file_clean(self,extra_arguments):
        self.scan_file(extra_arguments,True)

    #just a wrapper for scan_all, with the clean argument set to True
    def scan_all_clean(self):
        self.scan_all(True)

    #reset the list of false positives
    def false_positive_reset(self):
        self.known_patterns = set()

    #view the current list of false positives
    def view_marked_false_positives(self):
        for pattern in self.known_patterns:
            pattern_copy = pattern.rstrip()
            print(pattern_copy)

    #scan an individual file
    def scan_single_file(self,filename,clean):
        try:
            file = open(filename,mode="r") 
        except:
            print(filename," could not be found in the current directory",file=sys.stderr)
            return
        print("scanning ",filename)
        for line_number,line in enumerate(file):
            line = line.rstrip()
            for scan_type in self.line_scan_types:
                detected,dodgy_pattern = scan_type.detect_in_line(line)
                if detected:
                    if not clean: #if we are "scanning" clean, we don't care if a pattern has been marked false positive before
                        if dodgy_pattern in self.known_patterns: #no need to detect a pattern multiple times
                            continue
                    print(scan_type.detection_message,dodgy_pattern," Detected on line ",line_number,"-> ",line)
                    user_input = input("Type y to confirm that this is intentional and you are happy with this being in your source code: ")
                    if (user_input=="y"): #if it is intentional, store it in list of known false positive patterns
                        self.known_patterns.add(dodgy_pattern)
                else:
                    continue


    #find and return a list of filepaths in the directory
    def get_files_in_directory(self):
        files = []
        #TODO, later, actually get the filenames
        return files

    #update a gitignore to ignore sourcescans configuration files
    def update_gitignore(self): #yes if you keep reinitalizing the file, these same patterns will keep being added to the gitignore which is kind of silly, but should be fairly harmless
        file = open('.gitignore','a')
        file.write("sourcescan_patterns.pkl\n")
        file.write("sourcescan_config.pkl\n")

    def add_blocked_file_pattern(self,patterns):
        for pattern in patterns:
            self.blocked_files.add(pattern)

    def remove_blocked_file_pattern(self,patterns):
        for pattern in patterns:
            self.blocked_files.discard(pattern)

    def view_blocked_file_patterns(self):
        for pattern in self.block_files:
            print(pattern)   


if __name__ == "__main__":
    command_handler = CommandHandler()
    command_handler.run(sys.argv)