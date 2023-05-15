import csv
import os
import pandas as pd
from scipy.stats import pearsonr, spearmanr


domains = ['newstest2021','tedtalks']

for domain in domains:
    print()
    print(f'{domain}:')
    print('==================')
    if domain == 'newstest2021':
        ratings = r'newstest2021_en-ru.mqm.sys.score'
    if domain == 'tedtalks':
        ratings = r'tedtalks_en-ru.mqm.sys.score'
     
    ratings_df = pd.read_csv(ratings, sep='\t', header=None, names=['system', 'score'])
    
    for file_name in os.listdir(f'Data/{domain}/sys'):
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
