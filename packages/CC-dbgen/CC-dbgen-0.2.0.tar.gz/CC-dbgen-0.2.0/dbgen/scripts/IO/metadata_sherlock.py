# External Modules
from typing import Tuple
import subprocess,os
from os.path import join
from json import loads,dumps
from subprocess import getstatusoutput
# Internal Modules
from dbgen.scripts.IO.get_file import get_file
################################################################################
def metadata_sherlock(stordir : str
                    ,code    : str
                    ,raw_pdict : str
                    ) -> Tuple[str,int,str,str,str,str]:
    """
    Takes a path to a DFT calculation and extracts information from runtime.json
    Also keeps a record of where the information was taken from.
    """
    try:
        with open(join(stordir,"runtime.json"),'r') as f:
            runtime   = loads(f.read())
        pdict     = {k:v for k,v in loads(raw_pdict).items()
                     if 'pckl' not in k and 'project' not in k} # discard binary
        jobkind   =  pdict.get('jobkind','<no jobkind>')

        if 'kwargs' in pdict.keys():
            kwargs  = loads(pdict['kwargs'])
            jobname = kwargs.get('job_name','<no jobname>')
        else:
            jobname =  pdict.get('job_name')
            if jobname is None:
                jobname =  pdict.get('name','<no jobname>')

        return (runtime.get('user') # type: ignore
               ,runtime.get('timestamp')
               ,runtime.get('working_directory')
               ,jobkind
               ,jobname) # type: ignore

    except IOError: # job NOT produced by CataLog

        usr    = getstatusoutput('stat -c %U {}'.format(stordir))[1]
        tstamp = getstatusoutput('stat -c %Y {}'.format(stordir))[1]

        if code=='chargemol':
            jk = 'chargemol'
        else:
            jk = 'relax'
        # WE DON'T SAVE ANYTHING TO IDENTIFY WHETHER JOB IS VIBJOB!!!
        return (usr,int(tstamp),stordir,jk,stordir) # type: ignore

if __name__=='__main__':
    import sys
    print(metadata_sherlock(sys.argv[1],'',''))
