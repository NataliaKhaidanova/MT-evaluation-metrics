import pandas as pd
import os 
from scipy.stats import pearsonr, spearmanr, kendalltau


def compute_correlation(domain, metric, measure):
    """
    Compute Pearson's r, Spearman's, Kendall's tau for 
    SacreBLEU, SacreCHRF2, SacreTER, BLEURT-20, COMET-MQM_2021, COMET-QE-MQM_2021.
    Get the correlation for both newstest2021 and tedtalks datasets. 
    
    :param sting domain: domain to compute the correlation for ('newstest2021' or 'tedtalks')
    :param sting metric: the metric to compute the correlation for 
    ('sacre_BLEU', 'sacre_TER', 'sacre_CHRF2', 'BLEURT-20', 'COMET-MQM_2021', 'COMET-QE-MQM_2021')
    :param import from scipy.stats measure: the correlation coefficient (pearsonr, spearmanr, kendalltau)
    :return: None
    """
    # GET NUMBER OF ANNOTATED SENTENCES PER TEST FILE
    #if metric == 'sacre_BLEU':
        #path = f'Data/{domain}'
        #for file in os.listdir(path):
            #if file.endswith('.tsv'):
                #if domain == 'newstest2021':

                    #human_ratings_df = pd.read_csv(r'all_news_seg_mqm_scores.tsv', sep='\t', on_bad_lines='skip', keep_default_na=False)
                    #human_ratings = list(human_ratings_df[file[:-4]])
                    #annoated_human_ratings = []
                    #for human_rating in human_ratings:
                        #if human_rating != 'None':
                            #annoated_human_ratings.append(float(human_rating))
                    #print(f'Number of annoatate sentences for {file[:-4]}: {len(annoated_human_ratings)}')
                    
                #elif domain == 'tedtalks':  

                    #human_ratings_df = pd.read_csv(r'all_TED_seg_mqm_scores.tsv', sep='\t', on_bad_lines='skip', keep_default_na=False)
                    #human_ratings = list(human_ratings_df[file[:-4]])
                    #annoated_human_ratings = []
                    #for human_rating in human_ratings:
                        #if human_rating != 'None':
                            #annoated_human_ratings.append(float(human_rating))
                    #print(f'Number of annoatate sentences for {file[:-4]}: {len(annoated_human_ratings)}')
    
    # GET CORRELATION 
    path = f'Data/{domain}/{metric}'
    
    data_dict = {}
    
    if metric not in ['sacre_BLEU', 'sacre_CHRF2', 'sacre_TER']:
        for file in os.listdir(path):
            if file.endswith('.tsv'):

                file_df = pd.read_csv(f'Data/{domain}/{metric}/{file}', sep='\t', on_bad_lines='skip', keep_default_na=False) 

                if metric in ['BLEURT-20', 'COMET-MQM_2021']:
                    
                    if domain == 'newstest2021':
                        
                        ref_A = list(file_df[f'{metric}_ref_A'])
                        ref_B = list(file_df[f'{metric}_ref_B'])
                        human_ratings_df = pd.read_csv(r'all_news_seg_mqm_scores.tsv', sep='\t', on_bad_lines='skip', keep_default_na=False)
                        human_ratings = list(human_ratings_df[file.split('_')[0]])
                        annoated_human_ratings, corresponding_ref_A, corresponding_ref_B = [], [], []
                        for id, human_rating in enumerate(human_ratings):
                            if human_rating != 'None':
                                annoated_human_ratings.append(float(human_rating))
                                corresponding_ref_A.append(float(ref_A[id]))
                                corresponding_ref_B.append(float(ref_B[id]))
                                
                        cor_ref_A, p_value_ref_A = measure(corresponding_ref_A, annoated_human_ratings)
                        cor_ref_B, p_value_ref_B = measure(corresponding_ref_B, annoated_human_ratings)
                        cor = (cor_ref_A + cor_ref_B) / 2
                        data_dict[file.split('_')[0]] = f'{cor:.3f}'
                        
                    elif domain == 'tedtalks':
                        metric_scores = list(file_df[metric])
                        human_ratings_df = pd.read_csv(r'all_TED_seg_mqm_scores.tsv', sep='\t', on_bad_lines='skip', keep_default_na=False)
                        human_ratings = list(human_ratings_df[file.split('_')[0]])
                        annoated_human_ratings, corresponding_metric_scores = [], []
                        for id, human_rating in enumerate(human_ratings):
                            if human_rating != 'None':
                                annoated_human_ratings.append(float(human_rating))
                                corresponding_metric_scores.append(float(metric_scores[id]))
                        cor, p_value = measure(corresponding_metric_scores, annoated_human_ratings)
                        data_dict[file.split('_')[0]] = f'{cor:.3f}'
                        
                if metric == 'COMET-QE-MQM_2021':   
                    
                    if domain == 'newstest2021':
                        
                        metric_scores = list(file_df[metric])
                        human_ratings_df = pd.read_csv(r'all_news_seg_mqm_scores.tsv', sep='\t', on_bad_lines='skip', keep_default_na=False) 
                        human_ratings = list(human_ratings_df[file.split('_')[0]])
                        annoated_human_ratings, corresponding_metric_scores = [], []
                        for id, human_rating in enumerate(human_ratings):
                            if human_rating != 'None':
                                annoated_human_ratings.append(float(human_rating))
                                corresponding_metric_scores.append(float(metric_scores[id]))
                        cor, p_value = measure(corresponding_metric_scores, annoated_human_ratings)
                        data_dict[file.split('_')[0]] = f'{cor:.3f}'
                        
                    elif domain == 'tedtalks':
                        metric_scores = list(file_df[metric])
                        human_ratings_df = pd.read_csv(r'all_TED_seg_mqm_scores.tsv', sep='\t', on_bad_lines='skip', keep_default_na=False)
                        human_ratings = list(human_ratings_df[file.split('_')[0]])
                        annoated_human_ratings, corresponding_metric_scores = [], []
                        for id, human_rating in enumerate(human_ratings):
                            if human_rating != 'None':
                                annoated_human_ratings.append(float(human_rating))
                                corresponding_metric_scores.append(float(metric_scores[id]))
                        cor, p_value = measure(corresponding_metric_scores, annoated_human_ratings)
                        data_dict[file.split('_')[0]] = f'{cor:.3f}'
                                            
    else:
        path = f'Data/{domain}'
        for file in os.listdir(path):
            if file.endswith('.tsv'):
                
                file_path = f'Data/{domain}/{file.split("_")[0]}'
                file_df = pd.read_csv(file_path, sep='\t', on_bad_lines='skip', keep_default_na=False) 
                
                if domain == 'newstest2021':
                    metric_scores = list(file_df[metric])
                    human_ratings_df = pd.read_csv(r'all_news_seg_mqm_scores.tsv', sep='\t', on_bad_lines='skip', keep_default_na=False) 
                    human_ratings = list(human_ratings_df[file[:-4]])
                    annoated_human_ratings, corresponding_metric_scores = [], []
                    for id, human_rating in enumerate(human_ratings):
                        if human_rating != 'None':
                            annoated_human_ratings.append(float(human_rating))
                            corresponding_metric_scores.append(float(metric_scores[id]))
                    cor, p_value = measure(corresponding_metric_scores, annoated_human_ratings)
                    data_dict[file[:-4]] = f'{cor:.3f}'
                    
                elif domain == 'tedtalks':
                    metric_scores = list(file_df[metric])
                    human_ratings_df = pd.read_csv(r'all_TED_seg_mqm_scores.tsv', sep='\t', on_bad_lines='skip', keep_default_na=False) 
                    human_ratings = list(human_ratings_df[file[:-4]])
                    annoated_human_ratings, corresponding_metric_scores = [], []
                    for id, human_rating in enumerate(human_ratings):
                        if human_rating != 'None':
                            annoated_human_ratings.append(float(human_rating))
                            corresponding_metric_scores.append(float(metric_scores[id]))
                    cor, p_value = measure(metric_scores, human_ratings)
                    data_dict[file[:-4]] = f'{cor:.3f}'
                                        
    print(data_dict) 
    all_values = []
    for value in data_dict.values():
        all_values.append(float(value))
    average = sum(all_values) / 14
    print(f'Average: {average:.3f}')  
    
    
if __name__ == '__main__':

    metrics = ['sacre_BLEU', 'sacre_TER', 'sacre_CHRF2', 'BLEURT-20', 'COMET-MQM_2021', 'COMET-QE-MQM_2021']

    print('newstest2021:')
    print("Pearson's r")
    print('==================')
    for metric in metrics:
        print(metric)
        compute_correlation('newstest2021', metric, pearsonr)
        print('------------------')

    print("Spearman's p")
    print('==================')
    for metric in metrics:
        print(metric)
        compute_correlation('newstest2021', metric, spearmanr)
        print('------------------')

    print("Kendall's tau")
    print('==================')
    for metric in metrics:
        print(metric)
        compute_correlation('newstest2021', metric, kendalltau)
        print('------------------')

    print()
    print('tedtalks:')
    print("Pearson's r")
    print('==================')
    for metric in metrics:
        print(metric)
        compute_correlation('tedtalks', metric, pearsonr)
        print('------------------')

    print("Spearman's p")
    print('==================')
    for metric in metrics:
        print(metric)
        compute_correlation('tedtalks', metric, spearmanr)
        print('------------------')

    print("Kendall's tau")
    print('==================')
    for metric in metrics:
        print(metric)
        compute_correlation('tedtalks', metric, kendalltau)
        print('------------------')   
