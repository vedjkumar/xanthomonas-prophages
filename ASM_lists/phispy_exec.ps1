$dir = Get-ChildItem -Directory ".\CAM*"	# modified for each species
foreach ($i in $dir){
	cd $i
	phispy .\ncbi_dataset\data\GCA*\genomic.gbff -o .\ --phmms VOGs.hmm --color --keep_dropped_predictions --include_all_repeats
	cd ..
}
