import pandas as pd
import os 
from nltk.translate.bleu_score import sentence_bleu
import sacrebleu
#from torchmetrics import CHRFScore


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


news_scores, ted_scores = [], []

#chrf = CHRFScore()

for file_name in os.listdir(news_candidates):
    
    data_dict = {}
    #chrf2_scores = []
    bleu_scores, sacre_bleu_scores, sacre_chrf2_scores, sacre_ter_scores = [], [], [], []
    
    if file_name[23:-3] not in ['ref-A','ref-B','']:
        candidates = list(news_data[file_name[23:-3]])

        for references, candidate in zip(all_news_references, candidates):
            try:
                # nltk BLEU
                bleu_candidate = candidate.split()  
                bleu_scores.append(f'{sentence_bleu(references, bleu_candidate):.2f}')
                
                # torch CHRF2 (TOO SLOW, gives scores in range from 0 to 1,
                ### doesn't support parameters https://torchmetrics.readthedocs.io/en/stable/text/chrf_score.html)
                #chrf2_references = [' '.join(x) for x in references]
                #chrf2 = chrf([candidate], chrf2_references)
                #chrf2 = chrf2.item()
                #chrf2_scores.append(f'{chrf2:.2f}')
                
                # THE SCORES ARE EQUAL FOR Facebook-AI??? (NOT ANY MORE???)
                sacre_references = [' '.join(x) for x in references]  
                # sacreBLEU
                sacre_bleu = sacrebleu.sentence_bleu(candidate, sacre_references)
                sacre_bleu_scores.append(f'{sacre_bleu.score:.2f}')
                # sacreCHRF2
                sacre_chrf2 = sacrebleu.sentence_chrf(candidate, sacre_references)
                sacre_chrf2_scores.append(f'{sacre_chrf2.score:.2f}')
                # sacreTER
                sacre_ter = sacrebleu.sentence_ter(candidate, sacre_references)
                sacre_ter_scores.append(f'{sacre_ter.score:.2f}')
                
            except AttributeError:
                bleu_scores.append('0.00')
                sacre_bleu_scores.append('0.00')
                #chrf2_scores.append('0.00')
                sacre_chrf2_scores.append('0.00')
                sacre_ter_scores.append('0.00')
            except TypeError:
                bleu_scores.append('0.00')
                sacre_bleu_scores.append('0.00')
                #chrf2_scores.append('0.00')
                sacre_chrf2_scores.append('0.00')
                sacre_ter_scores.append('0.00')
                
        data_dict['BLEU'] = bleu_scores   
        data_dict['sacre_BLEU'] = sacre_bleu_scores   
        #data_dict['CHRF2'] = chrf2_scores   
        data_dict['sacre_CHRF2'] = sacre_chrf2_scores 
        data_dict['sacre_TER'] = sacre_ter_scores  
        news_scores.append(data_dict)
        
    
for file_name in os.listdir(ted_candidates):
    
    data_dict = {}
    #chrf2_scores = []
    bleu_scores, sacre_bleu_scores, sacre_chrf2_scores, sacre_ter_scores = [], [], [], []
    
    if file_name[19:-3] != 'ref-A':
        candidates = list(ted_data[file_name[19:-3]])

        for reference, candidate in zip(ted_references, candidates):
            # nltk BLEU (GIVES ZEROS FOR EVERYTHING probably because there is only one reference)
            bleu_candidate = candidate.split()  
            bleu_scores.append(f'{sentence_bleu(references, bleu_candidate):.2f}')

            # sacreBLEU
            sacre_bleu = sacrebleu.sentence_bleu(candidate, reference)
            sacre_bleu_scores.append(f'{sacre_bleu.score:.2f}')
            # sacreCHRF2
            sacre_chrf2 = sacrebleu.sentence_chrf(candidate, reference)
            sacre_chrf2_scores.append(f'{sacre_chrf2.score:.2f}')
            # sacreTER
            sacre_ter = sacrebleu.sentence_ter(candidate, reference)
            sacre_ter_scores.append(f'{sacre_ter.score:.2f}')
                
        data_dict['BLEU'] = bleu_scores   
        data_dict['sacre_BLEU'] = sacre_bleu_scores    
        data_dict['sacre_CHRF2'] = sacre_chrf2_scores  
        data_dict['sacre_TER'] = sacre_ter_scores  
        ted_scores.append(data_dict)

        
for file_name, data_dict in zip(os.listdir(news_candidates), news_scores):
    
    news_data = pd.DataFrame(data_dict)
    news_data.to_csv(f'Data/newstest2021/{file_name[23:-3]}.tsv', sep='\t', index=False) 

for file_name, data_dict in zip(os.listdir(ted_candidates), ted_scores):
    
    ted_data = pd.DataFrame(data_dict)
    ted_data.to_csv(f'Data/tedtalks/{file_name[19:-3]}.tsv', sep='\t', index=False)   
