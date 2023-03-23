# Import necessary libraries
from pysam import VariantFile  # for reading VCF file
import numpy as np  # for numerical operations
from sklearn import decomposition  # for PCA
import pandas as pd  # for data manipulation and output

# Set file names for input files
vcf_file_name = "ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf"
panel_file_name = "phase1_integrated_calls.20101123.ALL.panel"

# Initialize empty lists for storing genotypes, sample IDs, and variant IDs
genotypes = []
samples = []
variants_ids = []

# Read VCF file
with VariantFile(vcf_file_name) as vcf_reader:
    counter = 0
    # Loop through each record in the VCF file
    for record in vcf_reader:
        counter += 1
        # Process every 100th record to save memory
        if counter % 100 == 0:
            # Extract genotype information and sample IDs
            alleles = [record.samples[x].allele_indices for x in record.samples]
            samples = [sample for sample in record.samples]
            # Append genotype information and variant IDs to lists
            genotypes.append(alleles)
            variants_ids.append(record.id)

# Read panel file
with open(panel_file_name) as panel_file:
    labels = {}  # Initialize empty dictionary for sample population information
    # Loop through each line in the panel file
    for line in panel_file:
        line = line.strip().split('\t')
        # Map sample IDs to population codes
        labels[line[0]] = line[1]

# Convert genotype list to numpy array
genotypes = np.array(genotypes)
print(genotypes.shape)  # Print shape of genotype array

# Count number of non-zero elements in genotype array to create a matrix
matrix = np.count_nonzero(genotypes, axis=2)
print(matrix.shape)  # Print shape of matrix

# Transpose matrix to switch sample and variant dimensions
matrix = matrix.T

# Perform PCA with 2 components on the matrix
pca = decomposition.PCA(n_components=2)
pca.fit(matrix)
# Transform matrix with PCA
to_plot = pca.transform(matrix)

# Create a pandas dataframe from the matrix, with variants as columns and samples as rows
df = pd.DataFrame(matrix, columns=variants_ids, index=samples)
# Add a column for sample population codes
df['Population code'] = df.index.map(labels)
# Save dataframe as a CSV file
df.to_csv("matrix.csv")
