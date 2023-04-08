from nltk.translate.bleu_score import sentence_bleu
import os
import pandas as pd


news_data = r'all_news_data.tsv'
ted_data = r'all_TED_data.tsv'
news_candidates = r'WMT21-data/system-outputs/newstest2021/en-ru'
ted_candidates = r'WMT21-data/system-outputs/tedtalks/en-ru'

news_df = pd.read_csv(news_data, sep='\t') 
ted_df = pd.read_csv(ted_data, sep='\t') 

news_references_A = list(news_df['news_ref_A'])
news_references_B = list(news_df['news_ref_B'])
ted_references = list(ted_df['TED_ref'])

all_news_references = []
for A, B in zip(news_references_A, news_references_B):
    all_news_references.append([A.split(), B.split()])

news_data_dict, ted_data_dict = {}, {}

for news_file_name in os.listdir(news_candidates):
    for ted_file_name in os.listdir(ted_candidates):
        
        news_scores, ted_scores = [], []
        
        news_candidates = list(news_df[news_file_name[23:-3]])
        ted_candidates = list(ted_df[ted_file_name[19:-3]])
        
        for new_references, news_candidate in zip(all_news_references, news_candidates):
            try:
                news_candidate = news_candidate.split()  
                news_scores.append(f'{sentence_bleu(new_references, news_candidate):.2f}')
            except AttributeError:
                news_candidate = None
                news_scores.append(f'0.00')
        
        for ted_reference, ted_candidates in zip(ted_references, ted_candidates):
            ted_candidate = ted_candidates.split()  
            ted_scores.append(f'{sentence_bleu(ted_reference, ted_candidate):.2f}')

        news_data_dict[news_file_name[23:-3]] = news_scores
        ted_data_dict[ted_file_name[23:-3]] = ted_scores
        
news_df = pd.DataFrame(news_data_dict)
news_df.to_csv('news_BLEU_scores.tsv', sep='\t', index=False) 

ted_df = pd.DataFrame(ted_data_dict)
ted_df.to_csv('ted_BLEU_scores.tsv', sep='\t', index=False) 
