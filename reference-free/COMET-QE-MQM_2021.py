import pandas as pd
from comet import download_model, load_from_checkpoint


model_path = download_model('NataliaKhaidanova/wmt21-comet-qe-mqm')
comet_qe_mqm_2021_model = load_from_checkpoint(model_path)

for file in [r'Data/baby_k.tsv', r'Data/a_beautiful_mind.tsv']:
    
    seg_data_dict, sys_data_dict = {}, {}
    comet_qe_mqm_2021_human_scores, comet_qe_mqm_2021_opus_mt_scores = {}, [], []
    
    df = pd.read_csv(file, sep='\t') 
    sources = list(df['source'])
    human_translations = list(df['human_translation'])
    opus_mt_translations = list(df['opus_mt_translation'])

    for source, human_translation in zip(sources, human_translations):
        inputs = [{'src':source,'mt':human_translation}]
            
        comet_qe_mqm_2021_score = comet_qe_mqm_2021_model.predict(inputs, batch_size=8, gpus=1)
        comet_qe_mqm_2021_human_scores.append(f'{comet_qe_mqm_2021_score[0][0]:.3f}')
        
    for source, opus_mt_translation in zip(sources, opus_mt_translations):
        inputs = [{'src':source,'mt':opus_mt_translation}]
            
        comet_qe_mqm_2021_score = comet_qe_mqm_2021_model.predict(inputs, batch_size=8, gpus=1)
        comet_qe_mqm_2021_opus_mt_scores.append(f'{comet_qe_mqm_2021_score[0][0]:.3f}')

    seg_data_dict['human_scores'] = comet_qe_mqm_2021_human_scores    
    seg_data_dict['opus_mt_scores'] = comet_qe_mqm_2021_opus_mt_scores   
    
    sys_data_dict['human_scores'] = f'{sum([float(x) for x in comet_qe_mqm_2021_human_scores]) / len(comet_qe_mqm_2021_human_scores):.3f}'
    sys_data_dict['opus_mt_scores'] = f'{sum([float(x) for x in comet_qe_mqm_2021_opus_mt_scores]) / len(comet_qe_mqm_2021_opus_mt_scores):.3f}'
    # save segment level scores
    seg_comet_qe_mqm_2021_data = pd.DataFrame(seg_data_dict)
    seg_comet_qe_mqm_2021_data.to_csv(f'Data/seg_COMET-QE-MQM_2021_{file[5:-4]}.tsv', sep='\t', index=False) 
    # save system level scores 
    sys_comet_qe_mqm_2021_data = pd.DataFrame(sys_data_dict, index=[0])
    sys_comet_qe_mqm_2021_data.to_csv(f'Data/sys_COMET-QE-MQM_2021_{file[5:-4]}.tsv', sep='\t', index=False) 
