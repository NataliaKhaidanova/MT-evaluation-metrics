<h1>Machine-translation Quality Estimation: Comparing Traditional and Neural Machine-Translation Evaluation Metrics for English→Russian</h1>

<h2>A Thesis Project for Master's Degree in Linguistics: Text Mining, Vrije Universiteit Amsterdam 2022/2023. Done by Natalia Khaidanova.</h2>
  
The thesis project focuses on replicating and reproducing selected research conducted at the WMT21 Metrics Task. It involves evaluating the traditional (SacreBLEU, TER, and CHRF2) and best-performing reference-based (BLEURT-20, COMET-MQM_2021) and reference-free (COMET-QE-MQM_2021) neural metrics.

<h2>Content</h2>

<h2>\Data</h2>

The [data](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data) folder contains:

<h3>Files:</h3>

- all_news_data.tsv stores all source sentences, reference translations, and machine translations for the news domain.  

- all_TED_data.tsv contains all source sentences, reference translations, and machine translations for the TED talks domain.  

<h3>Subfolders:</h3>

- [WMT21-data](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/WMT21-data) stores source sentences ([sources](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/WMT21-data/sources)), reference translations ([references](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/WMT21-data/references)), machine translations ([system-outputs](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/WMT21-data/system-outputs)), and human judgment scores ([evaluation](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/WMT21-data/evaluation)) for each domain, i.e., news (newstest2021) or TED talks (tedtalks). 

- [newstest2021](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021) contains segment-level scores for each implemented neural metric ([BLEURT-20](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/BLEURT-20), [COMET-MQM_2021](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/COMET-MQM_2021), and [COMET-QE-MQM_2021](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/COMET-QE-MQM_2021)) and all utilized traditional metrics ([traditional metrics](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/traditional_metrics)), as well as [system-level scores](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/sys) for each of these metrics. Domain: news. 

- [tedtalks](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks) contains segment-level scores for each implemented neural metric ([BLEURT-20](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/BLEURT-20), [COMET-MQM_2021](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/COMET-MQM_2021), and [COMET-QE-MQM_2021](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/COMET-QE-MQM_2021)) and all utilized traditional metrics ([traditional metrics](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/traditional_metrics)), as well as [system-level scores](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/sys) for each of these metrics. Domain: TED talks. 

<h2>\eval</h2>

The [eval](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/eval) folder contains: 

<h3>Files:</h3>

- get_nr_annotations.py checks the number of annotated segments per type of human judgment (MQM, raw DA, or z-normalized DA). 

- seg_eval.py runs a segment-level evaluation of the implemented neural and traditional metrics. 

- sys_eval.py runs a system-level evaluation of the implemented neural and traditional metrics. 

<h3>Subfolders:</h3>

- [human_judgments_seg](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/eval/human_judgments_seg) stores segment-level human judgment scores of each type (MQM, raw DA, or z-normalized DA). Domain: both news and TED talks. 

- [human_judgments_sys](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/eval/human_judgments_sys) contains system-level human judgment scores of each type (MQM, raw DA, or z-normalized DA). Domain: both news and TED talks.

<h2>\metrics</h2>

The [metrics](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/metrics) folder contains: 

<h3>Files:</h3>

- BLEURT-20.py computes segment-level scores for the reference-based neural metric BLEURT-20 on the WMT21 Metrics Task data and calculates the metric's runtime per MT system. The resulting segment-level scores and metric's runtime are stored in [BLEURT-20 (newstest2021)](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/BLEURT-20) and [BLEURT-20 (tedtalks)](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/BLEURT-20). 

- COMET-MQM_2021.py computes segment-level scores for the reference-based neural metric COMET-MQM_2021 on the WMT21 Metrics Task data and calculates the metric's runtime per MT system. The resulting segment-level scores and metric's runtime are stored in [COMET-MQM_2021 (newstest2021)](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/COMET-MQM_2021) and [COMET-MQM_2021 (tedtalks)](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/COMET-MQM_2021). 
  
- COMET-QE-MQM_2021.py computes segment-level scores for the reference-free neural metric COMET-QE-MQM_2021 on the WMT21 Metrics Task data and calculates the metric's runtime per MT system. The resulting segment-level scores and metric's runtime are stored in [COMET-QE-MQM_2021 (newstest2021)](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/COMET-QE-MQM_2021) and [COMET-QE-MQM_2021 (tedtalks)](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/COMET-QE-MQM_2021).

- get_sys_scores.py computes system-level scores for the neural metrics (BLEURT-20, COMET-MQM_2021, and COMET-QE-MQM_2021) on the WMT21 Metrics Task data. The system-level scores are obtained by averaging the metrics' segment-level scores. The resulting system-level scores are stored in [sys (newstest2021)](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/sys) and [sys (tedtalks)](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/sys). 

- traditional_metrics_seg.py computes segment-level scores for the traditional metrics (SacreBLEU, TER, and CHRF2) on the WMT21 Metrics Task data. The resulting segment-level scores are stored in [traditional_metrics (newstest2021)](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/traditional_metrics) and [traditional_metrics (tedtalks)](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/traditional_metrics).

- traditional_metrics_sys.py computes system-level scores for the traditional metrics (SacreBLEU, TER, and CHRF2) on the WMT21 Metrics Task data. The resulting system-level scores are stored in [sys (newstest2021)](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/sys) and [sys (tedtalks)](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/sys). 

- traditional_metrics_runtime.py calculates the traditional metrics' (SacreBLEU, TER, and CHRF2) runtimes for segment-level evaluation. The runtimes are determined for all MT systems per domain. The metrics' runtimes are stored in [traditional_metrics (newstest2021)](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/traditional_metrics) and [traditional_metrics (tedtalks)](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/traditional_metrics).

