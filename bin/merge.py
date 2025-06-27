import nbformat
import sys
import re

def merge_notebooks(notebook_files, output_file):
    merged = None
    
    for notebook_file in notebook_files:
        with open(notebook_file, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Generate unique cell IDs with valid characters only
        for i, cell in enumerate(nb.cells):
            # Clean the notebook filename to only contain valid characters
            clean_name = re.sub(r'[^a-zA-Z0-9_-]', '_', notebook_file.replace('.ipynb', ''))
            cell['id'] = f"{clean_name}_{i}"
        
        if merged is None:
            merged = nb
        else:
            merged.cells.extend(nb.cells)
    
    # Write merged notebook
    with open(output_file, 'w', encoding='utf-8') as f:
        nbformat.write(merged, f)

# Usage
merge_notebooks([
    'notebooks/task-1.ipynb', 
    'notebooks/task-1-2.ipynb',
    'notebooks/task-1-3.ipynb',
    'notebooks/task-1-4.ipynb',
    'notebooks/task-2.ipynb',
    'notebooks/task-3.ipynb',
    'notebooks/task-4.ipynb',
    'notebooks/task-5.ipynb',
    ],
    'WQD7005_Project_Khor_Kean_Teng.ipynb')