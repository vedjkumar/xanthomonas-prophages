# Sets out inclusion criteria for assemblies

# from pathlib import Path
import pandas as pd

accepted = pd.DataFrame(columns=["Assembly Name", "Organism Name", "Organism Intraspecific Names Strain", "Assembly Level", "Assembly Release Date", "Assembly Sequencing Tech", "CheckM completeness", "CheckM contamination"])

'''
dir = "ASM_lists"
files = Path(dir).glob("*.tsv")
for file in files:
  
  with open(file) as f:
    #
'''

import glob as gl

dropped_cols = [
  "Organism Infraspecific Names Breed", "Organism Infraspecific Names Cultivar", "Organism Infraspecific Names Ecotype", "Organism Infraspecific Names Isolate",
  "Organism Infraspecific Names Sex", "Annotation Name", "WGS project accession", "Assembly Stats Number of Scaffolds",
  "Annotation BUSCO Complete", "Annotation BUSCO Single Copy", "Annotation BUSCO Duplicated", "Annotation BUSCO Fragmented",
  "Annotation BUSCO Missing", "Annotation BUSCO Lineage"
]

files = gl.glob("*.tsv")
for i in files:

  f = open(i)
  df = pd.read_table(f)

  # Remove unnecessary metadata
  df.drop(columns=dropped_cols)
