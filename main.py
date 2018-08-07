#
"""

alrighty - going to change up how it's calling the mechanism, it doesn't seem to want to line up correctly.
"""

import subprocess;
import os;
import sys;
import time;
import pdb;

from urllib import request;
from log_management.truncate_logs import *;
from settings import *;





def main(args):
    """
    """
    pass;
    # so this is deleting itself... let's see what we can do...
    try: os.remove("truncate_logs.log");
    except Exception as e: print(str(e));
    #for a in PATH_AGES.keys():
    #    prune(PATH_AGES[a],a[1],a[0]);
    for a in FILE_PATHS:
        for b in FILE_PATTERNS:
            prune(FILE_AGE,b,a); 31
    # that's really all it needs to do.
    request.urlopen(HEALTHCHECK_URL);  
    

if __name__=="__main__":
    if DEBUG:
        try:
            with open("local_settings.py") as j:
                print(j.read());
                input();
        except Exception as Bravo: print(str(Bravo));
        pdb.run('main(sys.argv[1:])');
    else:
        main(sys.argv[1:]);# unless I need to restructure this, I should be good.