import pandas as pd
import csv
import os
from scipy.stats import pearsonr, spearmanr


def compute_sys_correlation(domain, human_judgment):
    """
    Compute system-level Pearson's r and Spearman's p for 
    SacreBLEU, CHRF2, TER, BLEURT-20, COMET-MQM_2021, COMET-QE-MQM_2021.
    Get the correlation for both newstest2021 and tedtalks datasets. 
    
    :param sting domain: domain to compute the correlation for ('newstest2021' or 'tedtalks')
    :param sting human_judgment: human judgment type ('mqm', 'raw', 'z') 
    :return: None
    """
    if domain == 'newstest2021':
        ratings = f'human_judgments_sys/newstest2021_en-ru.{human_judgment}.sys.score'
    if domain == 'tedtalks':
        ratings = f'human_judgments_sys/tedtalks_en-ru.mqm.sys.score'
    
    ratings_df = pd.read_csv(ratings, sep='\t', header=None, names=['system', 'score'])

    for file_name in os.listdir(f'../Data/{domain}/sys'):
        if file_name.endswith('.tsv'):

            with open(f'../Data/{domain}/sys/{file_name}', 'r', newline='') as file:
                reader = csv.reader(file, delimiter='\t')
                systems = next(reader)
                for row in reader:
                    scores = [float(x) for x in row]

                rating_scores, metric_scores = [], []

                for rating_system, rating_score in zip(list(ratings_df['system']), list(ratings_df['score'])):
                    for metric_system, metric_score in zip(systems, scores):
                        if rating_system == metric_system:
                            rating_scores.append(rating_score)
                            metric_scores.append(metric_score)

                r, p_value = pearsonr(metric_scores, rating_scores)
                p, p_value = spearmanr(metric_scores, rating_scores)

                print(f"{file_name[4:-4]}: Pearson's r - {r:.3f}, Spearman's - {p:.3f}")

    
if __name__ == '__main__':
    print('System-level correlation with MQM scores:')
    print('newstest2021:')
    print('==================')
    compute_sys_correlation('newstest2021', 'mqm')
    print('------------------')
    
    print()
    print('tedtalks:')
    print('==================')
    compute_sys_correlation('tedtalks', 'mqm')
    print('------------------')
    
    print()
    print('System-level correlation with raw DA scores:')
    print('newstest2021:')
    print('==================')
    compute_sys_correlation('newstest2021', 'raw')
    print('------------------')
    
    print()
    print('System-level correlation with z-normalized DA scores:')
    print('newstest2021:')
    print('==================')
    compute_sys_correlation('newstest2021', 'z')
    print('------------------')
