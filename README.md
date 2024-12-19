
# Drug Discovery Project

## Overview
This project demonstrates a workflow for filtering drug candidates based on docking scores and visualizing chemical structures.

## Features
1. Load a dataset of drug candidates.
2. Filter molecules based on docking scores.
3. Visualize filtered molecules using RDKit.

## Files
1. `drug_candidates.csv`: Dataset of sample drug candidates with SMILES and Docking Scores.
2. `data_preprocessing.py`: Script for data loading and preprocessing.
3. `molecule_visualization.py`: Script for visualizing molecules.
4. `filter_candidates.py`: Script for filtering molecules based on docking scores.

## Usage
1. Clone the repository.

    ```bash
    git clone https://github.com/your-repo/drug-discovery.git
    ```
2. Navigate to the directory and install dependencies.
    ```bash
    pip install pandas rdkit
    ```
3. Run your main Python script (to be created as per your integration needs).

## Example Workflow
1. Load the dataset using `load_data` from `data_preprocessing.py`.
2. Filter molecules using `filter_by_score` from `filter_candidates.py`.
3. Visualize molecules using `visualize_molecules` from `molecule_visualization.py`.

## Dataset
- `drug_candidates.csv` contains sample drug candidates with columns:

  - Molecule: Name of the molecule.
  - SMILES: Chemical structure in SMILES format.
  - Docking_Score: Docking score of the molecule.

## Requirements
- Python 3.x
- RDKit
- Pandas

## License
This project is licensed under the MIT License.
