<h1>Machine-translation Quality Estimation: Comparing Traditional and Neural Machine-Translation Evaluation Metrics for English→Russian</h1>

<h2>A Thesis Project for Master's Degree in Linguistics: Text Mining, Vrije Universiteit Amsterdam 2022/2023. Done by Natalia Khaidanova.</h2>
  
The thesis project focuses on replicating and reproducing selected research conducted at the WMT21 Metrics Task. It involves evaluating the traditional (SacreBLEU, TER, and CHRF2) and best-performing reference-based (BLEURT-20, COMET-MQM_2021) and reference-free (COMET-QE-MQM_2021) neural metrics.

<h2>Content</h2>

<h2>\Data</h2>

The [data](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data) folder contains the following subfolders:

- [WMT21-data](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/WMT21-data) stores source sentences ([sources](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/WMT21-data/sources)), reference translations ([references](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/WMT21-data/references)), machine translations ([system-outputs](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/WMT21-data/system-outputs)), and human judgment scores ([evaluation](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/WMT21-data/evaluation)) for each domain, i.e., news (newstest2021) or TED talks (tedtalks). 

- [newstest2021](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021) contains segment-level scores for each implemented neural metric ([BLEURT-20](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/BLEURT-20), [COMET-MQM_2021](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/COMET-MQM_2021), and [COMET-QE-MQM_2021](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/COMET-QE-MQM_2021)) and all utilized traditional metrics ([traditional metrics](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/traditional_metrics)), as well as [system-level scores](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/newstest2021/sys) for each of these metrics. Domain: news. 

- [tedtalks](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks) contains segment-level scores for each implemented neural metric ([BLEURT-20](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/BLEURT-20), [COMET-MQM_2021](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/COMET-MQM_2021), and [COMET-QE-MQM_2021](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/COMET-QE-MQM_2021)) and all utilized traditional metrics ([traditional metrics](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/traditional_metrics)), as well as [system-level scores](https://github.com/NataliaKhaidanova/MT_evaluation_metrics/tree/main/Data/tedtalks/sys) for each of these metrics. Domain: TED talks. 

