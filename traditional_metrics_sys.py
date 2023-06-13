import pandas as pd
import os
from sacrebleu.metrics import BLEU, TER, CHRF


news_data = pd.read_csv('Data/all_news_data.tsv', sep='\t')
news_candidates = 'WMT21-data/system-outputs/newstest2021/en-ru'
news_references_A = list(news_data['news_ref_A'])
news_references_B = list(news_data['news_ref_B'])

all_news_references = [news_references_A, news_references_B]

ted_data = pd.read_csv('Data/all_TED_data.tsv', sep='\t')
ted_candidates = 'WMT21-data/system-outputs/tedtalks/en-ru'
ted_references = list(ted_data['TED_ref'])

bleu = BLEU()
ter = TER()
chrf2 = CHRF()

for domain in ['newstest2021', 'tedtalks']:
    for metric in ['sacre_BLEU', 'sacre_CHRF2', 'sacre_TER']:
        if domain == 'newstest2021':
            
            news_data_dict = {}

            for file_name in os.listdir(news_candidates):
                if file_name[23:-3] not in ['ref-A', 'ref-B', '']:
                    news_data = pd.read_csv('Data/all_news_data.tsv', sep='\t')
                    candidates = list(news_data[file_name[23:-3]])
                    candidates = [str(x) for x in candidates]
                    
                    if metric == 'sacre_BLEU':
                        sacre_bleu = bleu.corpus_score(candidates, all_news_references)
                        news_data_dict[file_name[23:-3]] = sacre_bleu.score

                    if metric == 'sacre_CHRF2':
                        sacre_chrf2 = chrf2.corpus_score(candidates, all_news_references)
                        news_data_dict[file_name[23:-3]] = sacre_chrf2.score

                    if metric == 'sacre_TER':
                        sacre_ter = ter.corpus_score(candidates, all_news_references)
                        news_data_dict[file_name[23:-3]] = sacre_ter.score

            news_data = pd.DataFrame(news_data_dict, index=[0])
            news_data.to_csv(f'Data/newstest2021/sys/sys_{metric}.tsv', sep='\t', index=False)
            
        if domain == 'tedtalks':
            ted_data_dict = {}
            sacre_references = []
            for reference in ted_references:
                sacre_references.append([reference])

            for file_name in os.listdir(ted_candidates):
                if file_name[19:-3] not in ['ref-A']:
                    ted_data = pd.read_csv('Data/all_TED_data.tsv', sep='\t')
                    candidates = list(ted_data[file_name[19:-3]])

                    if metric == 'sacre_BLEU':
                        sacre_bleu = bleu.corpus_score(candidates, sacre_references)
                        ted_data_dict[file_name[19:-3]] = sacre_bleu.score

                    if metric == 'sacre_CHRF2':
                        sacre_chrf2 = chrf2.corpus_score(candidates, sacre_references)
                        ted_data_dict[file_name[19:-3]] = sacre_chrf2.score

                    if metric == 'sacre_TER':
                        sacre_ter = ter.corpus_score(candidates, sacre_references)
                        ted_data_dict[file_name[19:-3]] = sacre_ter.score

            ted_data = pd.DataFrame(ted_data_dict, index=[0])
            ted_data.to_csv(f'Data/tedtalks/sys/sys_{metric}.tsv', sep='\t', index=False)
