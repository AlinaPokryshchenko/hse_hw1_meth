import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

SRR5836473 = pd.read_csv('SRR5836473_1_bismark_bt2_pe.bam.dedup.deduplicated.bismark.cov', sep='\t', names=['chr', 'start','stop', '% methylation', 'met', 'unmet'])
SRR3824222 = pd.read_csv('SRR3824222_1_bismark_bt2_pe.bam.dedup.deduplicated.bismark.cov', sep='\t', names=['chr', 'start','stop', '% methylation', 'met', 'unmet'])
SRR5836475 = pd.read_csv('SRR5836475_1_bismark_bt2_pe.bam.dedup.deduplicated.bismark.cov', sep='\t', names=['chr', 'start','stop', '% methylation', 'met', 'unmet'])
sns.histplot(data=SRR3824222, x="% methylation", bins=10, kde=True, kde_kws={'bw_adjust': 2})
plt.title("Epiblast")
plt.savefig('Epiblast.png')
sns.histplot(data=SRR5836473, x="% methylation", bins=10, kde=True, kde_kws={'bw_adjust': 2})
plt.title("8 cell")
plt.savefig('8_cell.png')
sns.histplot(data=SRR5836475, x="% methylation", bins=10, kde=True, kde_kws={'bw_adjust': 2})
plt.title("ICM")
plt.savefig('ICM.png')
