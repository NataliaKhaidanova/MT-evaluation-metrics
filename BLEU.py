from nltk.translate.bleu_score import sentence_bleu


news_data = 'all_news_data.tsv'

df = pd.read_csv(news_data, sep='\t') 
references_A = list(df['news_ref_A'])
references_B = list(df['news_ref_B'])

all_references = []
for A, B in zip(references_A, references_B):
    all_references.append([A.split(), B.split()])

candidates = list(df['Facebook-AI'])

for references, candidate in zip(all_references, candidates):
    candidate = candidate.split()  
    # print('BLEU score -> {}'.format(sentence_bleu(references, candidate))) # get full score
    print(f'BLEU score -> {sentence_bleu(references, candidate):.2f}') # get shortened score 
