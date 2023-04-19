import pandas as pd
import tarfile
import os
from comet.models.regression.regression_metric import RegressionMetric
import time


news_data = pd.read_csv(r'all_news_data.tsv', sep='\t') 
news_candidates = r'WMT21-data/system-outputs/newstest2021/en-ru'
news_source = list(news_data['news_source'])
news_references_A = list(news_data['news_ref_A'])
news_references_B = list(news_data['news_ref_B'])

all_news_references = []
for A, B in zip(news_references_A, news_references_B):
    all_news_references.append([A.split(), B.split()])

model_checkpoint_path = r'/wmt21-comet-mqm/checkpoints/model.ckpt'
comet_mqm_2021_model = RegressionMetric.load_from_checkpoint(model_checkpoint_path)


for file_name in os.listdir(news_candidates):
    if file_name[23:-3] not in ['ref-A','ref-B','']:

        data_dict, comet_mqm_2021_scores_ref_A, comet_mqm_2021_scores_ref_B = {}, [], []
        start_time = time.time()
        count = 0
        print(f'computing scores for {file_name[23:-3]}:')
        candidates = list(news_data[file_name[23:-3]])

        for source, references, candidate in zip(news_source, all_news_references, candidates):
            count += 1
            references = [' '.join(x) for x in references]  
            inputs_ref_A, inputs_ref_B = [], []
            data_ref_A_dict = {'src':source,'mt':candidate,'ref':references[0]}
            data_ref_B_dict = {'src':source,'mt':candidate,'ref':references[1]}
            inputs_ref_A.append(data_ref_A_dict)
            inputs_ref_B.append(data_ref_B_dict)
            try:
                # compute COMET-MQM_2021 scores for reference A
                comet_mqm_2021_score_ref_A = comet_mqm_2021_model.predict(inputs_ref_A, batch_size=8, gpus=1)
                comet_mqm_2021_scores_ref_A.append(f'{comet_mqm_2021_score_ref_A[0][0]:.2f}')
                # compute COMET-MQM_2021 scores for reference B
                comet_mqm_2021_score_ref_B = comet_mqm_2021_model.predict(inputs_ref_B, batch_size=8, gpus=1)
                comet_mqm_2021_scores_ref_B.append(f'{comet_mqm_2021_score_ref_B[0][0]:.2f}')
            except Exception:
                comet_mqm_2021_scores_ref_A.append('0.00')
                comet_mqm_2021_scores_ref_B.append('0.00')
                          
        data_dict['COMET-MQM_2021_ref_A'] = comet_mqm_2021_scores_ref_A 
        data_dict['COMET-MQM_2021_ref_B'] = comet_mqm_2021_scores_ref_B  

        end_time = time.time()
        total_time = end_time - start_time
        print(f'COMET-MQM_2021 runtime on the newstest2021 data for {file_name[23:-3]}: {total_time:.2f} seconds')
        print('==================')
          
        news_comet_mqm_2021_data = pd.DataFrame(data_dict)
        news_comet_mqm_2021_data.to_csv(f'Data/newstest2021/{file_name[23:-3]}_COMET-MQM_2021.tsv', sep='\t', index=False) 
