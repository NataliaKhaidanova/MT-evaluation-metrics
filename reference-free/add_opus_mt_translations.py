import pandas as pd
from transformers import MarianMTModel, MarianTokenizer


model_name = 'Helsinki-NLP/opus-mt-en-ru'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

for file in ['baby_k.tsv', 'a_beautiful_mind.tsv']:

    df = pd.read_csv(file, sep='\t')
    sources = list(df['source'])
    
    translated = model.generate(**tokenizer(sources, return_tensors="pt", padding=True))

    opus_mt_translations = []
    for sentence in translated:
        opus_mt_translations.append(tokenizer.decode(sentence, skip_special_tokens=True))
        
    df['opus_mt_translation'] = opus_mt_translations
    df.to_csv(file, sep='\t', index=False)
