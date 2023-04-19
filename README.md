# Traditional Vs. Neural Metrics (In progress)

Update (19.04.23):

Traditional metrics (computed):

- NLTK BLEU (ranges from 0 to 1) gives only zeros for the TEDtalks data probably because there is only one reference. SacreBLEU gives something as it ranges from 0 to 100.

- Torch CHRF is TOO SLOW + I don't know which version of CHRF is being calculated. Parameters are not supported for some reason resulting in no errors but zero output.

BLEURT-20:

- does not support more than one reference. Therefore, the scores for the newstest2021 data are cumputed separatelly for each reference. 
- on CPU (local): ca. 33 hours 40 minutes; on CPU (via GoogleColab): ca. 17 hours 31 minutes; on GPU (via GoogleColab, standard): unknown 

COMET-MQM_2021:

- the scores are very low (reason unknown)



