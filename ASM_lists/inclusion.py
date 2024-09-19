# Sets out inclusion criteria for assemblies

# from pathlib import Path
import pandas as pd
from re import match, search
import glob as gl

dropped_cols = [
  "Organism Infraspecific Names Breed", "Organism Infraspecific Names Cultivar", "Organism Infraspecific Names Ecotype", "Organism Infraspecific Names Isolate",
  "Organism Infraspecific Names Sex", "Annotation Name", "WGS project accession", "Assembly Stats Number of Scaffolds",
  "Annotation BUSCO Complete", "Annotation BUSCO Single Copy", "Annotation BUSCO Duplicated", "Annotation BUSCO Fragmented",
  "Annotation BUSCO Missing", "Annotation BUSCO Lineage"
]

renamed_cols = {
  "Assembly Accession": "accession", "Assembly Name": "assembly",
  "Organism Name": "organism", "Organism Intraspecific Names Strain": "strain",
  "Assembly Level": "level", "Assembly Release Date": "date",
  "Assembly Sequencing Tech": "platform", "Assembly BioSample Accession": "sample",
  "CheckM completeness": "completeness", "CheckM contamination": "contamination"
}

with open("Genus_ASMs.tsv") as f:
  
  df = pd.read_table(f)

df.rename(columns=renamed_cols)

# Remove unnecessary metadata
df.drop(columns=dropped_cols)

# Remove RefSeq and short-read assemblies
for i in df.index:

  if match("GCF", df["accession"]) or search("(Illumina)|(454)|(Torrent)|(ABI)|(BGI)", df["platform"]):

    df.drop(i)

print(df)

'''
dir = "ASM_lists"
files = Path(dir).glob("*.tsv")
for file in files:
  
  with open(file) as f:
    #
'''
