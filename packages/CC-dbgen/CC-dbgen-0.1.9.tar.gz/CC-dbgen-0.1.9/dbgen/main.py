# External Modules
from os             import environ
from argparse       import ArgumentParser
from pprint         import pformat
from distutils.util import strtobool
from ast            import literal_eval
from json           import load

# Internal Modules
from dbgen.support.utils   import ConnectInfo
from dbgen.core.misc       import levenshteinDistance
from dbgen.inputs.main     import dbg
"""
Command line interface for executing a database update

Requires DB_JSON environment variable to specify database that will be modified

The following flags control program behavior:
    - db
    - local
    - reset
    - add
    - meta
    - only
    - xclude
    - jobs
    - catalog
    - test
    - parallel
"""

################################################################################
##########
# Settings
#---------
parser = ArgumentParser(description  = 'Run a DBG update'
                       ,allow_abbrev = True)

parser.add_argument('--db'
                   ,default = ''
                   ,help    = "Override the schema defined in DB_JSON")

parser.add_argument('--local'
                   ,default = False
                   ,type    = lambda x:bool(strtobool(x))
                   ,help    = 'Default: if on sherlock, don\'t run local')

parser.add_argument('--reset'
                   ,default = False
                   ,type    = lambda x:bool(strtobool(x))
                   ,help    = 'Nuke the DB first - needed if you make schema changes')

parser.add_argument('--add'
                   ,default = False
                   ,type    = lambda x:bool(strtobool(x))
                   ,help    = 'Try to add columns (if you make benign schema additions)')

parser.add_argument('--meta'
                   ,default = False
                   ,type    = lambda x:bool(strtobool(x))
                   ,help    = 'Make a meta.db')

parser.add_argument('--only'
                   ,default = ''
                   ,help    = 'Run only the (space separated) rules')

parser.add_argument('--xclude'
                   ,default = 'underlying ads_triple'
                   ,help    = 'Do not run the (space separated) rules')

parser.add_argument('--jobs'
                   ,default = False
                   ,type    = lambda x:bool(strtobool(x))
                   ,help    = '''Run all job_loading rules
                                (takes time to rerun even if no new jobs)''')

parser.add_argument('--catalog'
                   ,default = False
                   ,type    = lambda x:bool(strtobool(x))
                   ,help    = 'Run the catalog job loading rule ')

parser.add_argument('--parallel'
                   ,default = True
                   ,type    = lambda x:bool(strtobool(x))
                   ,help    = '''Parallelize processing of multiple Query inputs.
                                 (Turn off if using pdb)''')
################################################################################
def load_jobs(jobs     : bool = False
             ,catalog  : bool = True
             ,add      : bool = False
             ,reset    : bool = False
             ,parallel : bool = True
             ,only     : str  = ''
             ,xclude   : str  = ''
             ) -> None:
        """
        Calls the main function from within Python (bypass command line args)
        See parser description for input variable meanings
        """

        main({'jobs':jobs,'catalog':catalog,'add':add,'reset':reset
             ,'parallel':parallel,'only':only,'xclude':xclude})

def main(direct_args : dict = {})->None:
    """
    Executes DB modifying procedure described by a DBG instance
    """
    # Get args
    #------------
    parser.set_defaults(**direct_args)
    args = parser.parse_args() # get args from command line
    print('args are: \n'+pformat(args))

    if args.local:
        db = ConnectInfo()
    else:
        with open(environ['DB_JSON'],'r') as f:
            db = ConnectInfo(**load(f))

    if args.db:
        db.db = args.db

    if args.meta:
        dbg.test_meta() # create a meta-db

    # Determine which job-loading rules to include
    #------------------------------------------------------------
    if not args.jobs:
        args.xclude+=''' stray_gpaw
                         stray_qe
                         stray_chargemol ''' # these T's ONLY run if --jobs

    if (not args.reset) and (not (args.catalog or args.jobs)):
        args.xclude+=''' catalog ''' # this run if EITHER --jobs OR --catalog...provided we didn't just nuke DB

    # # Process string inputs
    #------------------------
    only   = set(args.only.split())
    xclude = set(args.xclude.split()) - only

    # Verify every rule excluded/included by name actually exists
    # if first 5 chars match or within edit distance of 5, suggest alternatives
    #------------------------------------------------------------------------------------
    for w in (only | xclude):
        match = False
        close = []
        for n in [t.name for t in dbg.rules]:
            d = levenshteinDistance(w,n)
            upW,upN = max(len(w),5), max(len(n),5) # variables for safe indexing
            if d == 0:
                match = True
                break
            elif d < 5 or w[:upW] == n[:upN]:
                close.append(n) # keep track of near-misses
        if not match:
            did_you = "Did you mean %s"%close if close else ''
            raise ValueError("No match found for %s\n%s"%(w,did_you))

    dbg.run_all(db
               ,only    = only
               ,xclude  = xclude
               ,reset   = args.reset
               ,add     = args.add
               ,parallel= args.parallel)

if __name__ == '__main__':
    main()
