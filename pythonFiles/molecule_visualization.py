
from rdkit import Chem
from rdkit.Chem import Draw

def visualize_molecules(smiles_list, legends=None):
    """Visualize molecules from SMILES strings."""
    mols = [Chem.MolFromSmiles(smiles) for smiles in smiles_list]
    return Draw.MolsToGridImage(mols, legends=legends)
