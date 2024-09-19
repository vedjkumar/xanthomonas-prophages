# Sets out inclusion criteria for assemblies

from pathlib import Path
import pandas as pd

accepted = pd.DataFrame(columns=["Assembly Name", "Organism Name", "Organism Intraspecific Names Strain", "Assembly Level", "Assembly Release Date", "Assembly Sequencing Tech", "CheckM completeness", "CheckM contamination"])

dir = "ASM_lists"
files = Path(dir).glob("*.tsv")
for file in files:
  
  with open(file) as f:
    #
