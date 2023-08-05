from typing   import List,Tuple
from ase.data import chemical_symbols # type: ignore
from imp      import load_source
from re       import findall
from os       import environ
from os.path  import join
from subprocess import check_output
from json       import loads
################################################################################

def parse_keld() -> Tuple[List[str]
                         ,List[int]
                         ,List[str]
                         ,List[str]
                         ,List[int]
                         ,List[int]
                         ,List[float]
                         ,List[str]
                         ,List[float]]:
    """
    Extracts information of materials into triples for struct_dataset_element
    If the species doesn't exist in the database, we need to add it.
    """
    # Constants
    #----------
    struct_dict = {'fcc'    :'A_1_a_225'
                  ,'bcc'    :'A_1_a_229'
                  ,'hcp'    :'A_2_c_194'
                  ,'diamond':'A_2_a_227'
                  ,'b1'     :'AB_1_a_b_225'  # rocksalt
                  ,'b2'     :'AB_1_a_b_221'  # cesium chloride
                  ,'b3'     :'AB_1_a_c_216'} # zincblende

    # Initialize Variables
    #----------------------

    dataset     = [] # type: List[Tuple[str,str,float]] # speciesname, property, value
    bulkspecies = [] # type: List[Tuple[str,str]]       # speciesname, pure_struct
    composition = [] # type: List[Tuple[str,int,int]]   # speciesname,number,count

    # Get data from public JSON file
    #--------------------------------
    json = '/scratch/users/ksb/share/reference/solids.json'
    user = environ['SHERLOCK2_USERNAME']
    sher = '%s@login.sherlock.stanford.edu'%user
    data = check_output('ssh %s cat %s'%(sher,json),shell=True)
    keld = loads(data)
    cols      = ['lattice parameter'
                ,'cohesive energy'
                ,'bulk modulus'
                ,'magmom']

    # Extract data
    #------------
    for k,v in keld.items():
        elemstr,crystal = k.split('-')                  # 'LiH','b1'
        pure_struct  = struct_dict[crystal]             # 'b1' -> 'AB_1_a_b_225'
        elems = findall('[A-Z][^A-Z]*', elemstr)        # ['Li','H']

        bulkspecies.append((k,pure_struct))
        for elem in elems:
            num = chemical_symbols.index(elem)
            composition.append((k,num,1))

        for c in cols:
            val = v.get(c)
            if val is None:
                val = 0
            dataset.append((k,c,val))  # ('LiH-b1','magmom',0)


    # Organize data for output
    #-------------------------
    sp_short,struc     = zip(*bulkspecies)
    sp_mid,numb,count  = zip(*composition)
    sp_long,prop,value = zip(*dataset)
    spacegroups        = [int(x.split('_')[-1]) for x in struc]
    output             = [sp_short, struc,  spacegroups
                         ,sp_mid,   numb,   count
                         ,sp_long,  prop,   value]
    return tuple(map(list,output))# type: ignore

if __name__=='__main__':
    print(parse_keld())
