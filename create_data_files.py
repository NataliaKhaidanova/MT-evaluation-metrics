import pandas as pd
import os

# GET SOURCE, REFERENCE(S), MACHINE-TRANSLATION OUTPUTS PER DOMAIN
def read_file(file_path):
    """
    Read the data.
    
    :param string file_path: path to the file
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

                   
for news_file_name in os.listdir(news_candidates):
    for ted_file_name in os.listdir(ted_candidates):
      
        news_file_path = os.path.join(news_candidates, news_file_name)
        ted_file_path = os.path.join(ted_candidates, ted_file_name)
        
        news_candidate = read_file(news_file_path)
        ted_candidate = read_file(ted_file_path)
        
        if news_file_name[23:-3] not in ['ref-A','ref-B']:
            news_data_dict[news_file_name[23:-3]] = news_candidate
        if ted_file_name[19:-3] != 'ref-A':
            ted_data_dict[ted_file_name[19:-3]] = ted_candidate


news_df = pd.DataFrame(news_data_dict)
news_df.to_csv('all_news_data.tsv', sep='\t', index=False) 

ted_df = pd.DataFrame(ted_data_dict)
ted_df.to_csv('all_TED_data.tsv', sep='\t', index=False) 


# GET HUMAN JUDGMENTS FOR EACH TEAM PER DOMAIN, CORRELATION AND METRIC TYPE

#file_path_1 = r'WMT21-data/validation/ref-metric.seg.score'
#file_path_2 = r'WMT21-data/validation/ref-metric.sys.score'
#file_path_3 = r'WMT21-data/validation/src-metric.seg.score'
#file_path_4 = r'WMT21-data/validation/src-metric.sys.score'


#def get_scores(metric_type, langs, domains, refs, systems, scores):
    #"""
    #Put human judgment scores for each system in a dict.
    
    #:param string metric_type: if reference-based, metric_type == 'ref'; if reference-free, metric_type == 'src'
    #:param langs: list of language pairs
    #:param domains: list of domains
    #:param refs: list of reference types
    #:param systems: list of machine-translation systems) 
    #:param scores: list of human judgment scores
    #:return: two dicts: for newstest2021 and for tedtalks
    #"""
    #news_data_dict, ted_data_dict = {}, {}

    #for lang, domain, ref, system, score in zip(langs, domains, refs, systems, scores):
        
        #if metric_type == 'ref':
            #if lang == 'en-ru' and domain == 'newstest2021' and ref == 'ref-A' and system != 'ref-B':
                #if system not in news_data_dict:
                    #news_data_dict[team] = []
                #news_data_dict[team].append(score)
                
        #if metric_type == 'src':
            #if lang == 'en-ru' and domain == 'newstest2021' and system not in ['ref-A', 'ref-B']:
                #if system not in news_data_dict:
                    #news_data_dict[team] = []
                #news_data_dict[team].append(score)

        #if lang == 'en-ru' and domain == 'tedtalks':
            #if system not in ted_data_dict:
                #ted_data_dict[team] = []
            #ted_data_dict[team].append(score)
            
    #return news_data_dict, ted_data_dict


#def save_scores(file_path, correlation, metric_type):
    #"""
    #Save all scores per system in a .tsv file. 
    
    #:param string file_path: path to the validation file
    #:param string correlation: if segment-level, correlation == 'seg'; if system-level, correlation == 'sys'
    #:param string metric_type: if reference-based, metric_type == 'ref'; if reference-free, metric_type == 'src'
    #:return: None
    #"""

    #if correlation == 'seg':

        #labels = ['file','lang','domain','ref','system','src_index','score']
        #data = pd.read_csv(file_path, sep='\t', on_bad_lines='skip', keep_default_na=False, names=labels) 

        #langs = list(data['lang'])
        #domains = list(data['domain'])
        #refs = list(data['ref'])
        #systems = list(data['system'])
        #scores = list(data['score'])

        #if metric_type == 'ref':

            #news_data_dict, ted_data_dict = get_scores('ref', langs, domains, refs, systems, scores)

            #news_df = pd.DataFrame(news_data_dict)
            #news_df.to_csv('all_news_seg_ref_scores.tsv', sep='\t', index=False) 

            #ted_df = pd.DataFrame(ted_data_dict)
            #ted_df.to_csv('all_TED_seg_ref_scores.tsv', sep='\t', index=False) 

        #if metric_type == 'src':

            #news_data_dict, ted_data_dict = get_scores('src', langs, domains, refs, systems, scores)

            #news_df = pd.DataFrame(news_data_dict)
            #news_df.to_csv('all_news_seg_src_scores.tsv', sep='\t', index=False) 

            #ted_df = pd.DataFrame(ted_data_dict)
            #ted_df.to_csv('all_TED_seg_src_scores.tsv', sep='\t', index=False) 

    #if correlation == 'sys':

        #labels = ['file','lang','domain','ref','system','score']
        #data = pd.read_csv(file_path, sep='\t', on_bad_lines='skip', keep_default_na=False, names=labels) 

        #langs = list(data['lang'])
        #domains = list(data['domain'])
        #refs = list(data['ref'])
        #systems = list(data['system'])
        #scores = list(data['score'])

        #if metric_type == 'ref':

            #news_data_dict, ted_data_dict = get_scores('ref', langs, domains, refs, systems, scores)

            #news_df = pd.DataFrame(news_data_dict)
            #news_df.to_csv('all_news_sys_ref_scores.tsv', sep='\t', index=False) 

            #ted_df = pd.DataFrame(ted_data_dict)
            #ted_df.to_csv('all_TED_sys_ref_scores.tsv', sep='\t', index=False) 
            
        #if metric_type == 'src':
            
            #news_data_dict, ted_data_dict = get_scores('src', langs, domains, refs, systems, scores)

            #news_df = pd.DataFrame(news_data_dict)
            #news_df.to_csv('all_news_sys_src_scores.tsv', sep='\t', index=False) 

            #ted_df = pd.DataFrame(ted_data_dict)
            #ted_df.to_csv('all_TED_sys_src_scores.tsv', sep='\t', index=False) 
            
            
#if __name__ == '__main__':
    #save_scores(file_path_1, 'seg', 'ref')
    #save_scores(file_path_2, 'sys', 'ref')
    #save_scores(file_path_3, 'seg', 'src')
    #save_scores(file_path_4, 'sys', 'src')
    
    
file_path_1 = r'mt-metrics-eval-v2/wmt21.news/human-scores/en-ru.wmt-z.seg.score'
file_path_2 = r'mt-metrics-eval-v2/wmt21.tedtalks/human-scores/en-ru.mqm.seg.score'
file_path_3 = r'mt-metrics-eval-v2/wmt21.news/human-scores/en-ru.wmt-z.sys.score'
file_path_4 = r'mt-metrics-eval-v2/wmt21.tedtalks/human-scores/en-ru.mqm.sys.score'

def get_scores(file_path, systems, scores):
    """
    Put human judgment scores for each system in a dict.
    
    :param systems: list of machine-translation systems
    :param scores: list of human judgment scores
    :return: two dicts: for newstest2021 and for tedtalks
    """
    news_data_dict, ted_data_dict = {}, {}

    for system, score in zip(systems, scores):
        
        if 'news' in file_path:
            if system not in ['refA','refB']:
                if system not in news_data_dict:
                    news_data_dict[system] = []
                news_data_dict[system].append(score)

        if 'tedtalks' in file_path:
            if system != 'refA':
                if system not in ted_data_dict:
                    ted_data_dict[system] = []
                ted_data_dict[system].append(score)
            
    return news_data_dict, ted_data_dict


def save_scores(file_path, correlation):
    """
    Save all scores per system in a .tsv file. 
    
    :param string file_path: path to the validation file
    :param string correlation: if segment-level, correlation == 'seg'; if system-level, correlation == 'sys'
    :return: None
    """

    if correlation == 'seg':

        labels = ['system','score']
        data = pd.read_csv(file_path, sep='\t', on_bad_lines='skip', keep_default_na=False, names=labels) 
        
        systems = list(data['system'])
        scores = list(data['score'])
        
        news_data_dict, ted_data_dict = get_scores(file_path, systems, scores)
        
        if 'news' in file_path:
            news_df = pd.DataFrame(news_data_dict)
            news_df.to_csv('all_news_seg_z_scores.tsv', sep='\t', index=False) 
            
        if 'tedtalks' in file_path:
            ted_df = pd.DataFrame(ted_data_dict)
            ted_df.to_csv('all_TED_seg_mqm_scores.tsv', sep='\t', index=False) 

    if correlation == 'sys':

        labels = ['system','score']
        data = pd.read_csv(file_path, sep='\t', on_bad_lines='skip', keep_default_na=False, names=labels) 

        systems = list(data['system'])
        scores = list(data['score'])
        
        news_data_dict, ted_data_dict = get_scores(file_path, systems, scores)
        
        if 'news' in file_path:
            news_df = pd.DataFrame(news_data_dict)
            news_df.to_csv('all_TED_sys_mqm_scores.tsv', sep='\t', index=False) 
        if 'tedtalks'in file_path:
            ted_df = pd.DataFrame(ted_data_dict)
            ted_df.to_csv('all_TED_sys_mqm_scores.tsv', sep='\t', index=False) 
            
            
if __name__ == '__main__':
    save_scores(file_path_1, 'seg')
    save_scores(file_path_2, 'seg')
    save_scores(file_path_3, 'sys')
    save_scores(file_path_4, 'sys')
