from scipy.stats import chi2_contingency
import numpy as np
cont_table = [[12,0],[24,0]]



sample_table = [[3, 3], [3, 9]]

print(chi2_contingency(sample_table)[0:3])

# a = ["Record_number", "Animal_DEG_No", "Animal", "Tissue",\
#         "Domestic_form", "Wild_form", "Experiment", "Animal_DEG",\
#         "Log2_Domestic_WT", "p_value", "Padj_value", "PMID_animal",\
#         "Underexpression_versus_most_recent_common_ancestor",\
#         "Overexpression_versus_most_recent_common_ancestor",\
#         "Human_gene_homolog", "UniqueNCBIEntrezGeneID", "human_feature",\
#         "Effects_of_underexpression_of_the_gene_on_the_feature_in_human", \
#         "underexpression_sign", "PMID_deficit", "Effects_of_overexpressions_of_the_gene_on_the_feature_in_human", \
#         "overexpression_sign", "PMID_excess", "PMID_record"]
# dict_of_number = dict()
# for i in range(len(a)):
#     dict_of_number[i] = a[i]
# print(dict_of_number)




# crit_value, p_value, degrees_of_freedom
