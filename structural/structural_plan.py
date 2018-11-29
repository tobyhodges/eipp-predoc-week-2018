from Bio import PDB

pdbl = PDB.PDBList()
pdbl.retrieve_pdb_file('1FAT')

parser = PDB.MMCIFParser()
structure = parser.get_structure('fa/1fat.cif')

for model in structure:
    for chain in model:
        for residue in chain:
            for atom in residue:
                print atom

# Iterate over all atoms in a structure
for atom in structure.get_atoms():
    print atom

# Iterate over all residues in a model
for residue in model.get_residues():
    print residue

# get a single atom
# the long, clear way
model = structure[0]
chain = model['A']
residue = chain[100]
atom = residue['CA']

#the shorter, less clear way
a = structure[0]['A'][100]['CA']

a.get_name()       # atom name (spaces stripped, e.g. 'CA')
a.get_id()         # id (equals atom name)
a.get_coord()      # atomic coordinates
a.get_vector()     # atomic coordinates as Vector object
a.get_bfactor()    # isotropic B factor
a.get_occupancy()  # occupancy
a.get_altloc()     # alternative location specifier
a.get_sigatm()     # std. dev. of atomic parameters
a.get_siguij()     # std. dev. of anisotropic B factor
a.get_anisou()     # anisotropic B factor
a.get_fullname()   # atom name (with spaces, e.g. '.CA.')
