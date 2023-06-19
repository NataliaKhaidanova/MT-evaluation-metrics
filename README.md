<h1>Machine-translation Quality Estimation: Comparing Traditional and Neural Machine-Translation Evaluation Metrics for English→Russian</h1>

<h2>A Thesis Project for Master's Degree in Linguistics: Text Mining, Vrije Universiteit Amsterdam 2022/2023. Done by Natalia Khaidanova.</h2>
  
The thesis project focuses on replicating and reproducing selected research conducted at the WMT21 Metrics Task. It involves evaluating the traditional (SacreBLEU, TER, and CHRF2) and best-performing reference-based (BLEURT-20, COMET-MQM_2021) and reference-free (COMET-QE-MQM_2021) neural metrics.

<h2>Content</h2>

<pre>
├── Data
│   ├── WMT21-data
│       ├── evaluation
│           ├── newstest2021
│               ├── en-ru.mqm.seg.score
│               ├── en-ru.mqm.sys.score
│               ├── en-ru.wmt-raw.seg.score
│               ├── en-ru.wmt-raw.sys.score
│               ├── en-ru.wmt-z.seg.score
│               └── en-ru.wmt-z.sys.score
│           └── tedtalks 
│               ├── en-ru.mqm.seg.score
│               └── en-ru.mqm.sys.score
│      ├── references 
│          ├── newstest2021.en-ru.ref.ref-A.ru
│          ├── newstest2021.en-ru.ref.ref-B.ru
│          └── tedtalks.en-ru.ref.ref-A.ru
│      ├── sources
│          ├── newstest2021.en-ru.src.en
│          └── tedtalks.en-ru.src.en
│      └── system-outputs 
│          ├── newstest2021
│              ├── newstest2021.en-ru.hyp.Facebook-AI.ru
│              ├── newstest2021.en-ru.hyp.Manifold.ru
│              ├── newstest2021.en-ru.hyp.Nemo.ru
│              ├── newstest2021.en-ru.hyp.NiuTrans.ru
│              ├── newstest2021.en-ru.hyp.Online-A.ru
│              ├── newstest2021.en-ru.hyp.Online-B.ru
│              ├── newstest2021.en-ru.hyp.Online-G.ru
│              ├── newstest2021.en-ru.hyp.Online-W.ru
│              ├── newstest2021.en-ru.hyp.Online-Y.ru
│              ├── newstest2021.en-ru.hyp.metricsystem1.ru
│              ├── newstest2021.en-ru.hyp.metricsystem2.ru
│              ├── newstest2021.en-ru.hyp.metricsystem3.ru
│              ├── newstest2021.en-ru.hyp.metricsystem4.ru
│              ├── newstest2021.en-ru.hyp.metricsystem5.ru
│              ├── newstest2021.en-ru.ref.ref-A.ru
│              └── newstest2021.en-ru.ref.ref-B.ru
</pre>

