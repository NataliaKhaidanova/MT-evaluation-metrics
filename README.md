# Traditional Vs. Neural Metrics (In progress)

Update (15.04.23):

- NLTK BLEU (ranges from 0 to 1) gives only zeros for the TEDtalks data probably because there is only one reference. SacreBLEU gives something because it ranges from 0 to 100 -> Use metrics within this range? 

- Torch CHRF is TOO SLOW + I don't know which version of CHRF is being calculated! Parameters are not supported for some reason resulting in no errors but zero output.

Observations:

- TER is VERY SLOW

- BLEURT-20 does not support more than one reference. Therefore, the scores for the newstest2021 data are cumputed separatelly for each reference. 




