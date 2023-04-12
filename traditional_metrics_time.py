import pandas as pd
import os 
import time
import sacrebleu


news_data = pd.read_csv(r'all_news_data.tsv', sep='\t') 
news_candidates = r'WMT21-data/system-outputs/newstest2021/en-ru'
news_references_A = list(news_data['news_ref_A'])
news_references_B = list(news_data['news_ref_B'])

all_news_references = []
for A, B in zip(news_references_A, news_references_B):
    all_news_references.append([A.split(), B.split()])
    
ted_data = pd.read_csv(r'all_TED_data.tsv', sep='\t') 
ted_candidates = r'WMT21-data/system-outputs/tedtalks/en-ru'
ted_references = list(ted_data['TED_ref'])


def get_traditional_metrics_time(data, candidates, references, metric):
    """
    Get metric's scores for all candidates and systems in the systems-output folder,
    get the time needed to produce these scores. 
    
    :param pandas.core.frame.DataFrame data: pandas dataframe of either all_news_data.tsv or all_TED_data.tsv
    :param str candidates: path to the folder with system outputs 
    :param list references: list (of lists) of reference translations 
    :param str metric: metric's name (BLEU, CHRF2, or TER)  
    :return: None
    """
    start_time = time.time()
    all_scores, count = [], []
    
    for file_name in os.listdir(candidates):
        # get the scores for the newstest2021 data
        if 'newstest2021' in candidates and file_name[23:-3] not in ['ref-A','ref-B','']:
            
            count.append('file processed')
            data_dict, scores = {}, []
            file_candidates = list(data[file_name[23:-3]])
            
            for reference, candidate in zip(references, file_candidates):
                
                if metric == 'BLEU':
                    try:
                        reference = [' '.join(x) for x in reference]  
                        bleu = sacrebleu.sentence_bleu(candidate, reference)
                        scores.append(f'{bleu.score:.2f}')
                    
                    except TypeError:
                        scores.append('0.00')
                        
                if metric == 'CHRF2':
                    try:
                        reference = [' '.join(x) for x in reference]  
                        chrf = sacrebleu.sentence_chrf(candidate, reference)
                        scores.append(f'{chrf.score:.2f}')
                    
                    except TypeError:
                        scores.append('0.00')
                        
                if metric == 'TER':
                    try:
                        reference = [' '.join(x) for x in reference]  
                        ter = sacrebleu.sentence_ter(candidate, reference)
                        scores.append(f'{ter.score:.2f}')
                    
                    except TypeError:
                        scores.append('0.00')
                        
                    if len(count) == 3:
                        print('Three files are processed.')    
                    if len(count) == 7:
                        print('Half of the files is processed.')
                    if len(count) == 11:
                        print('Almost done.')
                        
            data_dict[metric] = scores 
            all_scores.append(data_dict)
            
        # get the scores for the tedtalks data    
        if 'tedtalks' in candidates and file_name[19:-3] not in ['ref-A','']:
            
            count.append('file processed')
            data_dict, scores = {}, []
            file_candidates = list(data[file_name[19:-3]])
            
            for reference, candidate in zip(references, file_candidates):
                
                reference = [' '.join(x) for x in reference]  
                
                if metric == 'BLEU':
                    bleu = sacrebleu.sentence_bleu(candidate, reference)
                    scores.append(f'{bleu.score:.2f}')
            
                if metric == 'CHRF2':
                    chrf = sacrebleu.sentence_chrf(candidate, reference)
                    scores.append(f'{chrf.score:.2f}')
                        
                if metric == 'TER':
                    ter = sacrebleu.sentence_ter(candidate, reference)
                    scores.append(f'{ter.score:.2f}')
                    
                    if len(count) == 3:
                        print('Three files are processed.')    
                    if len(count) == 7:
                        print('Half of the files is processed.')
                    if len(count) == 11:
                        print('Almost done.')
                        
            data_dict[metric] = scores 
            all_scores.append(data_dict)
            
    end_time = time.time()
    total_time = end_time - start_time
    print('Time taken', f'for {metric}:', f'{total_time:.2f}', 'seconds')
    
    
if __name__ == '__main__':
    print('newstest2021 data:')
    get_traditional_metrics_time(news_data, news_candidates, all_news_references, 'BLEU')
    get_traditional_metrics_time(news_data, news_candidates, all_news_references, 'CHRF2')
    get_traditional_metrics_time(news_data, news_candidates, all_news_references, 'TER')
    print('tedtalks data:')
    get_traditional_metrics_time(ted_data, ted_candidates, ted_references, 'BLEU')
    get_traditional_metrics_time(ted_data, ted_candidates, ted_references, 'CHRF2')
    get_traditional_metrics_time(ted_data, ted_candidates, ted_references, 'TER')
