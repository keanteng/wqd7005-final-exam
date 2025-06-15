import nbformat
import sys

def merge_notebooks(notebook_files, output_file):
    merged = None
    
    for notebook_file in notebook_files:
        with open(notebook_file, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Generate unique cell IDs
        for i, cell in enumerate(nb.cells):
            cell['id'] = f"{notebook_file.replace('.ipynb', '')}_{i}"
        
        if merged is None:
            merged = nb
        else:
            merged.cells.extend(nb.cells)
    
    # Write merged notebook
    with open(output_file, 'w', encoding='utf-8') as f:
        nbformat.write(merged, f)

# Usage
merge_notebooks([
    'task_1_1.ipynb', 
    'task_1_2.ipynb'
    ],
    'WQD7005_Project_Khor_Kean_Teng.ipynb')