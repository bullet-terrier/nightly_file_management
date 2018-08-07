#
"""
Abbreviated Log-Purging script.
Making it minimalist for some of our more embedded pieces of software.

I'm going to expand on this contraption for my geics process - it will be called as a module,
emitting a function that will then truncate what we're looking for.
Every time that "main.py" runs, we should d a check... or I could set up a "main prune/ main purge function."
"""

import sys;
import os;
import time;

# needs to simply emit the functionality.

def prune(age_in_seconds, file_patterns, *scan_paths, **kwargs):
    """
    allow an override for log_file, use the kwargs as an extension to the 
    base functionality of the process.
    """
    pass;
    log_file="./truncate_logs.log";
    if "scan_paths" in kwargs.keys(): scan_paths = kwargs["scan_paths"]; # this will help to allow access from other programs.
    if "log_file" in kwargs.keys(): log_file = kwargs['log_file'];
    exceptions = []
    killed_recently = []
    print(scan_paths)
    for path in scan_paths:
        print(path);
        try:
            if not os.path.isdir(path): raise Exception("Invalid argument - scan_path must be a valid directory.")
            for _file_ in os.listdir(path):
                __file__ = path+os.sep+_file_;
                print(__file__);
                try:
                    # may need to specify the full path.
                    print(file_patterns)
                    for file_pattern in file_patterns:
                        print("ATTEMPTING: \t"+_file_+"\t"+file_pattern);
                        if file_pattern in _file_ and os.path.getctime(__file__) > age_in_seconds:
                            os.remove(__file__);
                            killed_recently.append(__file__); # __file__ != _file_
                except Exception as EX:
                    exceptions.append(EX);
                    print("Inner exception.");
                    print(str(EX))
        except Exception as E:
            print("outer Exception");
            exceptions.append(E);
            print(str(E));
        #
    with open("./truncate_logs.log",'w') as lgs:
        for a in exceptions: lgs.write(time.strftime("%Y-%m-%d %H:%M")+"\t"+str(a)+"\r\n");
        for b in killed_recently: lgs.write(time.strftime(":%Y-%m-%d %H:%M")+"\t"+b+"\r\n");
    return len(exceptions); # if it returns >0 then we know that there were errors.
        

# this maintains the original functionality of the truncate_logs script,
# but also expands the capacity to emit the underlying fuunctions.
if __name__=="__main__":
    print("Pruning local logs")
    scan_path = "";
    file_pattern = ".log";
    file_age = (7*24)*(60)*(60)
    killed_recently = []
    exceptions = []
    # foreach file in the scan_path, check for file_pattern
    if not os.isdir(scan_path): raise Exception("Invalid Argument, scan_path must be a valid directory")
    for _file_ in os.listdir(scan_path):
        try:
            if file_pattern in _file_ and os.path.getctime(_file_) > file_age:
                os.remove(_file_);
                killed_recently.append(_file_);
        except Exception as E:
            exceptions.append(E);
            print(str(E));
    with open("./truncate_logs.log",'w') as lgs:
        for a in exceptions: lgs.write(time.strftime("%Y-%m-%d %H:%M")+"\t"+str(a)+"\r\n");
        for b in killed_recently: lgs.write(time.strftime("%Y-%m-%d %H:%M")+"\t"+b+"\r\n");

