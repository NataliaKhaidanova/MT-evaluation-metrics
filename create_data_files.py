import pandas as pd
import os


def read_file(file_path):
    """
    Read the data.
    :param list string: path to the file
    :return: list of strings (sentences)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = [line.strip() for line in f.readlines()]
    return data
  
  
news_source = r'WMT21-data/sources/newstest2021.en-ru.src.en'
news_reference_A = r'WMT21-data/references/newstest2021.en-ru.ref.ref-A.ru'
news_reference_B = r'WMT21-data/references/newstest2021.en-ru.ref.ref-B.ru'
news_candidates = r'WMT21-data/system-outputs/newstest2021/en-ru'

ted_source = r'WMT21-data/sources/tedtalks.en-ru.src.en'
ted_reference = r'WMT21-data/references/tedtalks.en-ru.ref.ref-A.ru'
ted_candidates = r'WMT21-data/system-outputs/tedtalks/en-ru'


news_source = read_file(news_source)
news_reference_A = read_file(news_reference_A)
news_reference_B = read_file(news_reference_B)

ted_source = read_file(ted_source)
ted_reference = read_file(ted_reference)


news_data_dict = {'news_source':news_source,
                  'news_ref_A':news_reference_A,
                  'news_ref_B':news_reference_B}

ted_data_dict = {'TED_source':ted_source,
                 'TED_ref':ted_reference}

                   
for new_file_name in os.listdir(news_candidates):
    for ted_file_name in os.listdir(ted_candidates):
      
        new_file_path = os.path.join(news_candidates, new_file_name)
        ted_file_path = os.path.join(ted_candidates, ted_file_name)
        
        news_candidate = read_file(new_file_path)
        ted_candidate = read_file(ted_file_path)
        
        if new_file_name[23:-3] not in ['ref.ref-A','ref.ref-B']:
            news_data_dict[new_file_name[23:-3]] = news_candidate
        if ted_file_name[19:-3] != 'ref.ref-A':
            ted_data_dict[ted_file_name[19:-3]] = ted_candidate


news_df = pd.DataFrame(news_data_dict)
news_df.to_csv('all_news_data.tsv', sep='\t', index=False) 

ted_df = pd.DataFrame(ted_data_dict)
ted_df.to_csv('all_TED_data.tsv', sep='\t', index=False) 
