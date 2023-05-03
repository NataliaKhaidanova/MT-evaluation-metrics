import pandas as pd
import os 
from scipy.stats import pearsonr, spearmanr, kendalltau


def compute_correlation(domain, metric, measure):
    """
    """
    path = f'Data/{domain}/{metric}'
    
    data_dict = {}
    
    if metric not in ['sacre_BLEU', 'sacre_CHRF2', 'sacre_TER']:
        for file in os.listdir(path):
            if file.endswith('.tsv'):

                file_path = f'Data/{domain}/{metric}/{file}'
                file_df = pd.read_csv(file_path, sep='\t', on_bad_lines='skip', keep_default_na=False) 

                if metric in ['BLEURT-20', 'COMET-MQM_2021']:
                    human_ratings_path = r'Data/all_news_seg_ref_scores.tsv'
                    human_ratings_df = pd.read_csv(human_ratings_path, sep='\t', on_bad_lines='skip', keep_default_na=False) 
                    ref_A = list(file_df[f'{metric}_ref_A'])
                    ref_B = list(file_df[f'{metric}_ref_B'])
                    human_ratings = list(human_ratings_df[file.split('_')[0]])

                    r_ref_A, p_value_ref_A = measure(ref_A, human_ratings)
                    r_ref_B, p_value_ref_B = measure(ref_B, human_ratings)
                    p_value = (p_value_ref_A + p_value_ref_B) / 2
                    # print(r) # extract correlation coefficient
                    data_dict[file.split('_')[0]] = f'{p_value:.3f}' # extract p-value of the correlation coefficient

                if metric == 'COMET-QE-MQM_2021':    
                    human_ratings_path = r'all_news_seg_src_scores.tsv'
                    human_ratings_df = pd.read_csv(human_ratings_path, sep='\t', on_bad_lines='skip', keep_default_na=False) 
                    scores = list(file_df[metric])
                    human_ratings = list(human_ratings_df[file.split('_')[0]])

                    r, p_value = measure(scores, human_ratings)
                    data_dict[file.split('_')[0]] = f'{p_value:.3f}'
                
    else:
        path = f'Data/{domain}'
        for file in os.listdir(path):
            if file.endswith('.tsv'):
                
                file_path = f'Data/{domain}/traditional_metrics/{file.split('_')[0]}.tsv'
                file_df = pd.read_csv(file_path, sep='\t', on_bad_lines='skip', keep_default_na=False) 

                human_ratings_path = r'all_news_seg_ref_scores.tsv'
                human_ratings_df = pd.read_csv(human_ratings_path, sep='\t', on_bad_lines='skip', keep_default_na=False) 
                scores = list(file_df[metric])
                human_ratings = list(human_ratings_df[file[:-4]])

                r, p_value = measure(scores, human_ratings)
                data_dict[file[:-4]] = f'{p_value:.3f}'
                
    print(data_dict) 
    all_values = []
    for value in data_dict.values():
        all_values.append(float(value))
    average = sum(all_values) / 14
    print(f'Average: {average:.3f}')
    
    
if __name__ == '__main__':
  
    metrics = ['BLEURT-20','COMET-MQM_2021','COMET-QE-MQM_2021','sacre_BLEU','sacre_CHRF2','sacre_TER']

    print("Pearson's r")
    print('===================')
    for metric in metrics:
        print(metric)
        compute_correlation('newstest2021', metric, pearsonr)
        print('-------------------')

    print("Spearman's p")
    print('===================')
    for metric in metrics:
        print(metric)
        compute_correlation('newstest2021', metric, spearmanr)
        print('-------------------')

    print("Kendall's tau")
    print('===================')
    for metric in metrics:
        print(metric)
        compute_correlation('newstest2021', metric, kendalltau)
        print('-------------------')
