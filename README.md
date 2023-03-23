# Mini bioinformatics project: Genotypes PCA Analysis
This is a Python script for performing principal component analysis (PCA) on genotypic data from a Variant Call Format (VCF) file and sample population information from a panel file. It then outputs a transformed matrix and a CSV file containing the transformed matrix with sample population information.
## Getting Started
To use this script, you will need to have Python 3 installed, as well as the following libraries:

•	pysam

•	numpy

•	scikit-learn

•	pandas

To install these libraries, you can use pip:
```
pip install pysam numpy scikit-learn pandas
```

You will also need to download the input files, which should be in the same directory as the script:

•	VCF file containing genotypic data

•	Panel file containing sample population information

## URLs to download files
```
curl -O ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20110521/ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz

curl -O ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20110521/ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz.tbi

curl -O ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20110521/phase1_integrated_calls.20101123.ALL.panel
```
## Running the Script
To run the script, simply open a terminal or command prompt and navigate to the directory where the script and input files are located. Then, run the following command:
```
python genomics_pca.py
```

This will generate a transformed matrix and a CSV file containing the transformed matrix with sample population information.
## Output
The output CSV file will contain the following columns:

•	Sample IDs

•	Variant IDs

•	Sample population code

You can use this file to visualize the PCA results and explore the relationship between the genotypic data and sample population information.

