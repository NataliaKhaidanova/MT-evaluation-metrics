# Traditional Vs. Neural Metrics

Update (12.04.23):

- NLTK BLEU (ranges from 0 to 1) gives only zeros for the TEDtalks data probably because there is only one reference. SacreBLEU gives something because it ranges from 0 to 100 -> Use metrics within this range? 

- Torch CHRF is TOO SLOW + I don't know which version of CHRF is being calculated! Parameters are not supported for some reason resulting in no errors but zero output.

Observations:

- TER is VERY SLOW

Runtime on CPU:

newstest2021:

BLEURT-20:

Facebook-AI - 6089.12 seconds (101.48 minutes)



