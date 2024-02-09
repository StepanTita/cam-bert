# Space Fake

## Fake

Data (20k): https://www.kaggle.com/c/fake-news/data?select=train.csv

| Model            | Epochs | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1 | precision | recall |
|------------------|--------|--------------|--------|----------|-------------|--------|-------|-----------|--------|
| DistilBERT       | 0?     | 592130       | 0.6182 | 0.7478   | N/A         | 0.7372 | N/A   | 0.8549    | 0.5707 |
| Space-DistilBERT | 0?     | 197122 (128) | 0.5986 | 0.7407   | 0.          | 0.7281 | 0.    | 0.8602    | 0.5481 |
| Space-DistilBERT | 0?     | 394242 (256) | 0.5714 | 0.7655   | 0.          | 0.7578 | 0.    | 0.8566    | 0.6133 |

## Fake 2 (not used since mainly a subset of Fake 1)

Data (6k): https://www.kaggle.com/datasets/rajatkumar30/fake-news

| Model            | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1 | precision | recall |
|------------------|--------------|--------|----------|-------------|--------|-------|-----------|--------|
| DistilBERT       | 592130       | 0.6453 | 0.7572   | N/A         | 0.7567 | N/A   | 0.7848    | 0.7106 |
| Space-DistilBERT | 197122 (128) | 0.6356 | 0.7749   | 0.          | 0.7691 | 0.    | 0.9069    | 0.6142 |
| Space-DistilBERT | 394242 (256) | 0.6113 | 0.7976   | 0.          | 0.7942 | 0.    | 0.9040    | 0.6673 |

## Zero-Shot

(train on 20k)

| Model            | Train Params | loss   | accuracy | f1     | precision | recall |
|------------------|--------------|--------|----------|--------|-----------|--------|
| DistilBERT       | 592130       | 0.6287 | 0.7704   | 0.7704 | 0.7820    | 0.7494 |
| Space-DistilBERT | 197122 (128) | 0.6175 | 0.7313   | 0.7231 | 0.8521    | 0.5591 |
| Space-DistilBERT | 394242 (256) | 0.6014 | 0.7501   | 0.7467 | 0.8246    | 0.6346 |

## Covid Fake News Data

| Model            | Epochs    | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1  | precision | recall | Inter-space weight | Intra-space weight |
|------------------|-----------|--------------|--------|----------|-------------|--------|--------|-----------|--------|--------------------|--------------------|
| DistilBERT       | 5         | 592130       | 0.6287 | 0.8107   | N/A         | 0.8027 | N/A    | 0.9462    | 0.6392 | N/A                | N/A                |
| DistilBERT       | 750/1800  | 592130       | 0.1572 | 0.9313   | N/A         | 0.9310 | N/A    | 0.9431    | 0.9108 | N/A                | N/A                |
| Space-DistilBERT | 1450/1800 | 6162 (4)     | 0.3134 | 0.9285   | 0.8706      | 0.9283 | 0.8690 | 0.9348    | 0.9137 | 0.1                | 1e-5               |
| Space-DistilBERT | 1450/1800 | 197122 (128) | 0.3645 | 0.9304   | 0.7850      | 0.9302 | 0.7799 | 0.9333    | 0.9196 | 0.1                | 1e-5               |
| Space-DistilBERT | 5         | 394242 (256) | 0.5810 | 0.7962   | 0.          | 0.7867 | 0.     | 0.9371    | 0.6137 | 0                  | 0                  |
| Space-DistilBERT | 5         | 788482 (512) | 0.5550 | 0.7888   | 0.          | 0.7834 | 0.     | 0.8622    | 0.6627 | 0                  | 0                  |
| Space-DistilBERT | 5         | 788482 (512) | 0.7514 | 0.7929   | 0.          | 0.7875 | 0.     | 0.8712    | 0.6637 | 0.1                | 0                  |
| Space-BERT       | 70        | 197122 (128) | 0.2498 | 0.8957   | 0.          | 0.8950 | 0.     | 0.9217    | 0.8539 | 0                  | 0                  |
| Space-BERT       | 70        | 6162 (4)     | 0.5506 | 0.7991   | 0.          | 0.7935 | 0.     | 0.8831    | 0.6667 | 0                  | 0                  |
| Space-BERT       | 500       | 4622 (3)     | 0.4145 | 0.8995   | 0.8860      | 0.8988 | 0.8844 | 0.9305    | 0.8529 | 0.1                | 1e-5               |
| Space-BERT       | 500       | 4622 (3)     | 0.2780 | 0.9051   | 0.4453      | 0.9045 | 0.4438 | 0.9295    | 0.8667 | 0                  | 0                  |
| Space-BERT       | 250       | 98562 (64)   | 0.3907 | 0.9182   | 0.7976      | 0.9179 | 0.7905 | 0.9316    | 0.8941 | 0.1                | 1e-5               |
| BERT             | 250       | 1538         | 0.5175 | 0.7897   | N/A         | 0.7861 | N/A    | 0.8376    | 0.6931 | N/A                | N/A                |
| BERT             | 5         | 108311810    | 0.0846 | 0.9752   | N/A         | 0.9752 | N/A    | 0.9736    | 0.9745 | N/A                | N/A                |
| BERT             | 50        | 1538         | 0.6338 | 0.7145   | N/A         | 0.6966 | N/A    | 0.7528    | 0.7047 | N/A                | N/A                |
| Space-BERT       | 50        | 4622 (3)     | 0.7875 | 0.7949   | 0.5234      | 0.7828 | 0.3436 | 0.8478    | 0.7855 | 0.1                | 1e-5               |
| Space-BERT       | 50        | 98562 (64)   | 0.5877 | 0.8645   | 0.7743      | 0.8627 | 0.7637 | 0.8725    | 0.8610 | 0.1                | 1e-5               |
| Space-BERT       | 50        | 197122 (128) | 0.5727 | 0.8808   | 0.6528      | 0.8797 | 0.5967 | 0.8859    | 0.8782 | 0.1                | 1e-5               |

Notes: for the journal version we want to prove that either we are better with short training and eventually, or we are
better eventually.
We need to present the results for both cases.
For the small fake news dataset, we need to show that we are better with at least one of the two training.

## Zero-Shot with CS Loss

(test on 6k) (this is a data leakage)
these results are cross-dataset without any specific topic

| Model       | Epochs | Train Params | loss   | accuracy   | cs accuracy | f1         | cs f1  | precision | recall | Inter-space weight | Intra-space weight |
|-------------|--------|--------------|--------|------------|-------------|------------|--------|-----------|--------|--------------------|--------------------|
| BERT        | 50     | 1538         | 0.6544 | 0.6230     | N/A         | 0.6028     | N/A    | 0.7227    | 0.3979 | N/A                | N/A                |
| Space-BERT  | 50     | 4622 (3)     | 0.5722 | 0.7679     | 0.5958      | 0.7657     | 0.5902 | 0.8322    | 0.6707 | 0.1                | 1e-5               |
| Space-BERT* | 50     | 98562 (64)   | 0.4534 | **0.7975** | **0.6148**  | **0.7974** | 0.5809 | 0.8040    | 0.7860 | 0.1                | 1e-5               |
| Space-BERT  | 50     | 197122 (128) | 0.4567 | 0.7964     | 0.5863      | 0.7963     | 0.5299 | 0.7822    | 0.8208 | 0.1                | 1e-5               |

this is after intersection removal:

| Model      | Epochs | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1  | precision | recall | Inter-space weight | Intra-space weight |
|------------|--------|--------------|--------|----------|-------------|--------|--------|-----------|--------|--------------------|--------------------|
| BERT       | 50     | 1538         | 0.6035 | 0.7736   | N/A         | 0.6044 | N/A    | 0.5985    | 0.6132 | N/A                | N/A                |
| Space-BERT | 50     | 4622 (3)     | 0.5544 | 0.8292   | 0.5154      | 0.7180 | 0.4711 | 0.6985    | 0.7515 | 0.1                | 1e-5               |
| Space-BERT | 50     | 98562 (64)   | 0.4666 | 0.7997   | 0.8071      | 0.7069 | 0.6153 | 0.6847    | 0.7798 | 0.1                | 1e-5               |
| Space-BERT | 50     | 197122 (128) | 0.5079 | 0.7750   | 0.8201      | 0.6892 | 0.5904 | 0.6729    | 0.7816 | 0.1                | 1e-5               |

\* - our assumption was right, the model with less parameters but higher CS scores is better in terms of generalization

(test on covid-fake)
these results are cross-dataset with specific (covid) topic

| Model      | Epochs | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1  | precision | recall | Inter-space weight | Intra-space weight |
|------------|--------|--------------|--------|----------|-------------|--------|--------|-----------|--------|--------------------|--------------------|
| BERT       | 50     | 1538         | 0.7692 | 0.4763   | N/A         | 0.3308 | N/A    | 0.4762    | 0.9889 | N/A                | N/A                |
| Space-BERT | 50     | 4622 (3)     | 0.9535 | 0.4716   | 0.4766      | 0.3215 | 0.3233 | 0.4740    | 0.9882 | 0.1                | 1e-5               |
| Space-BERT | 50     | 98562 (64)   | 2.1427 | 0.4597   | 0.4709      | 0.3169 | 0.3214 | 0.4675    | 0.9618 | 0.1                | 1e-5               |
| Space-BERT | 50     | 197122 (128) | 2.5363 | 0.4530   | 0.4092      | 0.3149 | 0.3116 | 0.4638    | 0.9461 | 0.1                | 1e-5               |

# Cross-dataset benchmarking

| Dataset                          | Total true news | Total fake news | Images used | Public availability |
|----------------------------------|-----------------|-----------------|-------------|---------------------|
| ~~FakeCovid (twitter)~~          | 3360            | 3060            | No          | Yes                 |
| ~~LIAR (multi-label)~~           | 6400            | 6400            | No          | Yes                 |
| ~~LIAR (binary-label)~~          | 6400            | 6400            | No          | Yes                 |
| ~~Fake News Kaggle Competition~~ | 10387           | 10413           | No          | Yes                 |
| ~~FakeNewsNet~~                  | 18,000          | 6,000           | Yes         | Yes                 |

## Kaggle Fake News Competition

| Model      | Epochs | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1  | precision | recall | Inter-space weight | Intra-space weight |
|------------|--------|--------------|--------|----------|-------------|--------|--------|-----------|--------|--------------------|--------------------|
| BERT       | 50     | 1538         | 0.6251 | 0.6550   | N/A         | 0.6337 | N/A    | 0.7400    | 0.4319 | N/A                | N/A                |
| Space-BERT | 50     | 4622 (3)     | 0.7444 | 0.8069   | 0.6408      | 0.8030 | 0.6396 | 0.8769    | 0.6946 | 0.1                | 1e-5               |
| Space-BERT | 50     | 98562 (64)   | 0.5305 | 0.8685   | 0.6834      | 0.8672 | 0.6497 | 0.9132    | 0.8018 | 0.1                | 1e-5               |
| Space-BERT | 50     | 197122 (128) | 0.5016 | 0.8868   | 0.6436      | 0.8859 | 0.5900 | 0.9228    | 0.8334 | 0.1                | 1e-5               |

## LIAR (multi-label)

| Model      | Epochs | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1  | precision | recall | Inter-space weight | Intra-space weight |
|------------|--------|--------------|--------|----------|-------------|--------|--------|-----------|--------|--------------------|--------------------|
| BERT       | 50     | 4614         | 1.7426 | 0.2221   | N/A         | 0.1211 | N/A    | 0.1261    | 0.1815 | N/A                | N/A                |
| Space-BERT | 50     | 13938 (3)    | 2.2877 | 0.2362   | 0.1824      | 0.1540 | 0.1079 | 0.1542    | 0.1977 | 0.1                | 1e-5               |
| Space-BERT | 50     | 297222 (64)  | 2.3192 | 0.2580   | 0.2362      | 0.2034 | 0.1590 | 0.2201    | 0.2227 | 0.1                | 1e-5               |
| Space-BERT | 50     | 594438 (128) | 2.3651 | 0.2572   | 0.2081      | 0.2120 | 0.1267 | 0.2527    | 0.2248 | 0.1                | 1e-5               |

## LIAR (binary-label)

| Model      | Epochs | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1  | precision | recall | Inter-space weight | Intra-space weight |
|------------|--------|--------------|--------|----------|-------------|--------|--------|-----------|--------|--------------------|--------------------|
| BERT       | 50     | 1538         | 0.7026 | 0.5666   | N/A         | 0.3617 | N/A    | 0.2833    | 0.5000 | N/A                | N/A                |
| Space-BERT | 50     | 4622 (3)     | 0.8476 | 0.5900   | 0.5838      | 0.5280 | 0.5825 | 0.5778    | 0.5515 | 0.1                | 1e-5               |
| Space-BERT | 50     | 98562 (64)   | 0.8591 | 0.6267   | 0.5877      | 0.6002 | 0.5855 | 0.6185    | 0.6031 | 0.1                | 1e-5               |
| Space-BERT | 50     | 197122 (128) | 0.8747 | 0.6251   | 0.5744      | 0.5971 | 0.4194 | 0.6170    | 0.6007 | 0.1                | 1e-5               |

## FakeNewsNet (GossipCop)

| Model      | Epochs | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1  | precision | recall | Inter-space weight | Intra-space weight |
|------------|--------|--------------|--------|----------|-------------|--------|--------|-----------|--------|--------------------|--------------------|
| BERT       | 50     | 1538         | 0.5480 | 0.7566   | N/A         | 0.4307 | N/A    | 0.3783    | 0.5000 | N/A                | N/A                |
| Space-BERT | 50     | 4622 (3)     | 0.7111 | 0.7575   | 0.2620      | 0.4344 | 0.2238 | 0.8786    | 0.5017 | 0.1                | 1e-5               |
| Space-BERT | 50     | 98562 (64)   | 0.6771 | 0.7933   | 0.6378      | 0.6620 | 0.6037 | 0.7275    | 0.6427 | 0.1                | 1e-5               |
| Space-BERT | 50     | 197122 (128) | 0.6847 | 0.7987   | 0.7143      | 0.6776 | 0.6361 | 0.7353    | 0.6573 | 0.1                | 1e-5               |

## FakeNewsNet (PolitiFact + GossipCop)

| Model      | Epochs | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1  | precision | recall | Inter-space weight | Intra-space weight |
|------------|--------|--------------|--------|----------|-------------|--------|--------|-----------|--------|--------------------|--------------------|
| BERT       | 50     | 1538         | 0.5502 | 0.7548   | N/A         | 0.4302 | N/A    | 0.3774    | 0.5000 | N/A                | N/A                |
| Space-BERT | 50     | 4622 (3)     | 0.7124 | 0.7557   | 0.2732      | 0.4336 | 0.2400 | 0.8777    | 0.5016 | 0.1                | 1e-5               |
| Space-BERT | 50     | 98562 (64)   | 0.6754 | 0.7955   | 0.6468      | 0.6654 | 0.6090 | 0.7359    | 0.6453 | 0.1                | 1e-5               |
| Space-BERT | 50     | 197122 (128) | 0.6826 | 0.8028   | 0.7131      | 0.6833 | 0.6302 | 0.7475    | 0.6616 | 0.1                | 1e-5               |

## FakeNewsNet (GossipCop predict> Covid Fake)

| Model      | Epochs | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1  | precision | recall | Inter-space weight | Intra-space weight |
|------------|--------|--------------|--------|----------|-------------|--------|--------|-----------|--------|--------------------|--------------------|
| BERT       | 50     | 1538         | 0.8384 | 0.5234   | N/A         | 0.3436 | N/A    | 0.2616    | 0.5000 | N/A                | N/A                |
| Space-BERT | 50     | 4622 (3)     | 0.7862 | 0.5234   | 0.6145      | 0.3436 | 0.6052 | 0.2617    | 0.5000 | 0.1                | 1e-5               |
| Space-BERT | 50     | 98562 (64)   | 0.8823 | 0.5375   | 0.6064      | 0.3806 | 0.5874 | 0.6911    | 0.5151 | 0.1                | 1e-5               |
| Space-BERT | 50     | 197122 (128) | 0.9444 | 0.5373   | 0.5691      | 0.3797 | 0.4712 | 0.6954    | 0.5149 | 0.1                | 1e-5               |

## FakeNewsNet (GossipCop predict> PolitiFact)

| Model      | Epochs | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1  | precision | recall | Inter-space weight | Intra-space weight |
|------------|--------|--------------|--------|----------|-------------|--------|--------|-----------|--------|--------------------|--------------------|
| BERT       | 50     | 1538         | 0.5990 | 0.5909   | N/A         | 0.3714 | N/A    | 0.2955    | 0.5000 | N/A                | N/A                |
| Space-BERT | 50     | 4622 (3)     | 0.5621 | 0.5909   | 0.4403      | 0.3714 | 0.3699 | 0.2955    | 0.5000 | 0.1                | 1e-5               |
| Space-BERT | 50     | 98562 (64)   | 0.5385 | 0.6695   | 0.6259      | 0.6085 | 0.6258 | 0.6812    | 0.6181 | 0.1                | 1e-5               |
| Space-BERT | 50     | 197122 (128) | 0.5312 | 0.6941   | 0.6468      | 0.6395 | 0.6155 | 0.7172    | 0.6447 | 0.1                | 1e-5               |

## FakeNewsNet (PolitiFact + GossipCop predict> Covid Fake)

| Model      | Epochs | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1  | precision | recall | Inter-space weight | Intra-space weight |
|------------|--------|--------------|--------|----------|-------------|--------|--------|-----------|--------|--------------------|--------------------|
| BERT       | 50     | 1538         | 0.8171 | 0.5234   | N/A         | 0.3436 | N/A    | 0.2617    | 0.5000 | N/A                | N/A                |
| Space-BERT | 50     | 4622 (3)     | 0.7652 | 0.5234   | 0.6024      | 0.3436 | 0.5881 | 0.2617    | 0.5000 | 0.1                | 1e-5               |
| Space-BERT | 50     | 98562 (64)   | 0.8256 | 0.5482   | 0.6191      | 0.4064 | 0.6116 | 0.6983    | 0.5265 | 0.1                | 1e-5               |
| Space-BERT | 50     | 197122 (128) | 0.8719 | 0.5480   | 0.5956      | 0.4056 | 0.5354 | 0.7008    | 0.5263 | 0.1                | 1e-5               |

# Ablation Study with inter-space and intra-space losses only

## FakeNewsNet (PolitiFact + GossipCop)

| Model      | Epochs | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1  | precision | recall | Inter-space weight | Intra-space weight |
|------------|--------|--------------|--------|----------|-------------|--------|--------|-----------|--------|--------------------|--------------------|
| Space-BERT | 10     | 4622 (3)     | 1.7721 | 0.7548   | 0.6196      | 0.4302 | 0.5962 | 0.3774    | 0.5000 | 1.0                | 1e-5               |
| Space-BERT | 10     | 98562 (64)   | 0.7079 | 0.7815   | 0.7055      | 0.6016 | 0.6325 | 0.7203    | 0.5928 | 1.0                | 1e-5               |
| Space-BERT | 10     | 197122 (128) | 0.6910 | 0.7973   | 0.7321      | 0.6703 | 0.6370 | 0.7350    | 0.6500 | 1.0                | 1e-5               |
| Space-BERT | 10     | 4622 (3)     | 1.9239 | 0.7548   | 0.7152      | 0.4301 | 0.6437 | 0.3774    | 0.5000 | 1.0                | 0                  |
| Space-BERT | 10     | 98562 (64)   | 1.9734 | 0.2565   | 0.6616      | 0.2145 | 0.6254 | 0.5756    | 0.5056 | 1.0                | 0                  |
| Space-BERT | 10     | 197122 (128) | 1.9751 | 0.7349   | 0.7637      | 0.4343 | 0.6567 | 0.4329    | 0.4909 | 1.0                | 0                  |

## FakeNewsNet (GossipCop)

| Model      | Epochs | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1  | precision | recall | Inter-space weight | Intra-space weight |
|------------|--------|--------------|--------|----------|-------------|--------|--------|-----------|--------|--------------------|--------------------|
| Space-BERT | 10     | 4622 (3)     | 1.9304 | 0.7566   | 0.7053      | 0.4307 | 0.6387 | 0.3783    | 0.5000 | 1.0                | 1e-5               |
| Space-BERT | 10     | 98562 (64)   | 2.0755 | 0.2818   | 0.6857      | 0.2538 | 0.6366 | 0.5683    | 0.5175 | 1.0                | 1e-5               |
| Space-BERT | 10     | 197122 (128) | 2.0751 | 0.7448   | 0.7442      | 0.4436 | 0.6522 | 0.4861    | 0.4985 | 1.0                | 1e-5               |
| Space-BERT | 10     | 4622 (3)     | 1.9255 | 0.7566   | 0.7055      | 0.4307 | 0.6387 | 0.3783    | 0.5000 | 1.0                | 0                  |
| Space-BERT | 10     | 98562 (64)   | 1.9739 | 0.2549   | 0.6761      | 0.2137 | 0.6361 | 0.5737    | 0.5057 | 1.0                | 0                  |
| Space-BERT | 10     | 197122 (128) | 1.9754 | 0.7369   | 0.7651      | 0.4335 | 0.6659 | 0.4277    | 0.4905 | 1.0                | 0                  |

## FakeNewsNet (PolitiFact + GossipCop predict> Covid Fake)

| Model      | Epochs | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1  | precision | recall | Inter-space weight | Intra-space weight |
|------------|--------|--------------|--------|----------|-------------|--------|--------|-----------|--------|--------------------|--------------------|
| Space-BERT | 10     | 4622 (3)     | 0.7046 | 0.5234   | 0.5379      | 0.3436 | 0.3830 | 0.2617    | 0.5000 | 1.0                | 1e-5               |
| Space-BERT | 10     | 98562 (64)   | 0.6888 | 0.4761   | 0.6260      | 0.3238 | 0.6039 | 0.4200    | 0.4993 | 1.0                | 1e-5               |
| Space-BERT | 10     | 197122 (128) | 0.7055 | 0.4338   | 0.5778      | 0.3467 | 0.4927 | 0.3457    | 0.4177 | 1.0                | 1e-5               |
| Space-BERT | 10     | 4622 (3)     | 0.7034 | 0.5234   | 0.5384      | 0.3436 | 0.3849 | 0.2617    | 0.5000 | 1.0                | 0                  |
| Space-BERT | 10     | 98562 (64)   | 0.6915 | 0.4762   | 0.6305      | 0.3229 | 0.6049 | 0.3493    | 0.4995 | 1.0                | 0                  |
| Space-BERT | 10     | 197122 (128) | 0.7039 | 0.4349   | 0.5969      | 0.3252 | 0.5276 | 0.3042    | 0.4169 | 1.0                | 0                  |

## FakeNewsNet (GossipCop predict> PolitiFact)

| Model      | Epochs | Train Params | loss   | accuracy | cs accuracy | f1     | cs f1  | precision | recall | Inter-space weight | Intra-space weight |
|------------|--------|--------------|--------|----------|-------------|--------|--------|-----------|--------|--------------------|--------------------|
| Space-BERT | 10     | 4622 (3)     | 0.7034 | 0.5234   | 0.5292      | 0.3436 | 0.3606 | 0.2617    | 0.5000 | 1.0                | 1e-5               |
| Space-BERT | 10     | 98562 (64)   | 0.6892 | 0.4759   | 0.5967      | 0.3238 | 0.5549 | 0.4112    | 0.4991 | 1.0                | 1e-5               |
| Space-BERT | 10     | 197122 (128) | 0.7052 | 0.4401   | 0.5543      | 0.3472 | 0.4312 | 0.3468    | 0.4234 | 1.0                | 1e-5               |
| Space-BERT | 10     | 4622 (3)     | 0.6918 | 0.4762   | 0.5947      | 0.3229 | 0.5399 | 0.3493    | 0.4995 | 1.0                | 0                  |
| Space-BERT | 10     | 98562 (64)   | 0.7022 | 0.5234   | 0.5289      | 0.3436 | 0.3598 | 0.2617    | 0.5000 | 1.0                | 0                  |
| Space-BERT | 10     | 197122 (128) | 0.7037 | 0.4546   | 0.5653      | 0.3290 | 0.4510 | 0.3046    | 0.4353 | 1.0                | 0                  |

# Explanation Benchmark

**********************************************************************************************************************
Explanation:

- Train the model on some dataset (e.g. Fake News Kaggle Competition, or Covid Fake News Dataset)
- Let's embed the whole fact-checking dataset into the same space (not the embeddings, but the centroid of the
  embeddings).
- Let's try to predict the news to be fake or true.
- After we've predicted let's use the embedding centroid and extract k nearest neighbors from the knowledge base.
- Let's see how well this nearest neighbors match the original fact-checking articles (this we will measure by
  max/average cosine/euclidian similarity of the neighbors embedding with the original fact-checking articles,
  and by the number of exact matches, e.g. recall and precision).

Notes: we should actually compare this with S-BERT. For now we just use Mean of BERT embeddings as a centroid.
We should also think how we can deal with the fact that to use concept space similarity we need to use `N` knowledge
bases - one for each label. Since otherwise vectors that fall in different spaces will be compared (since we force
them to be orthogonal only with those from the different concept spaces).

**********************************************************************************************************************

tp / (tp + fp) = precision (how well we identify true explanation)
tp / (tp + fn) = recall (how well we distinguish true explanation from false explanation)

| Model        | Train Dataset    | Epochs | Train Params | Mean Cosine Similarity | Max Cosine Similarity | Mean Euclidean Distance | Max Euclidean Distance | precision | recall |
|--------------|------------------|--------|--------------|------------------------|-----------------------|-------------------------|------------------------|-----------|--------|
| BERT ✅       | Covid Fake       | 50     | 1538         | 0.                     | 0.                    | 0.                      | 0.                     | 0.        | 0.     |
| BERT ✅       | Fake News Kaggle | 50     | 1538         | 0.                     | 0.                    | 0.                      | 0.                     | 0.        | 0.     |
| Space-BERT ✅ | Covid Fake       | 50     | 4622 (3)     | 0.                     | 0.                    | 0.                      | 0.                     | 0.        | 0.     |
| Space-BERT ✅ | Covid Fake       | 50     | 98562 (64)   | 0.                     | 0.                    | 0.                      | 0.                     | 0.        | 0.     |
| Space-BERT ✅ | Covid Fake       | 50     | 197122 (128) | 0.                     | 0.                    | 0.                      | 0.                     | 0.        | 0.     |
| Space-BERT ✅ | Fake News Kaggle | 50     | 4622 (3)     | 0.                     | 0.                    | 0.                      | 0.                     | 0.        | 0.     |
| Space-BERT ✅ | Fake News Kaggle | 50     | 98562 (64)   | 0.                     | 0.                    | 0.                      | 0.                     | 0.        | 0.     |
| Space-BERT ✅ | Fake News Kaggle | 50     | 197122 (128) | 0.                     | 0.                    | 0.                      | 0.                     | 0.        | 0.     |

# Some tests that are used to make sure that model works as expected

## IMDB

| Experiment                               | Epochs | Train Params | Loss   | Accuracy | F1-score (macro) | Precision | Recall | Inter-space weight | Intra-space weight |
|------------------------------------------|--------|--------------|--------|----------|------------------|-----------|--------|--------------------|--------------------|
| Space-DistilBERT (CE + inter-space loss) | 5      | 4622         | 0.8804 | 0.6141   | 0.5587           | 0.8957    | 0.2594 | 0                  | 0                  |
| Space-DistilBERT (CE loss)               | 5      | 4622         | 0.4883 | 0.8080   | 0.8079           | 0.8262    | 0.7808 | 0                  | 0                  |
| Space-DistilBERT (CE loss)               | 5      | 197122       | 0.3855 | 0.8322   | 0.8320           | 0.8093    | 0.8663 | 0                  | 0                  |
| Space-DistilBERT (CE + inter-space loss) | 5      | 197122       | 0.7847 | 0.7890   | 0.7889           | 0.8016    | 0.7687 | 0.1                | 0                  |
| DistilBERT-base-cased                    | 5      | 592130       | 0.4612 | 0.7852   | 0.7819           | 0.8799    | 0.6614 | N/A                | N/A                |

# Paper tables:

## Same dataset benchmarking

| Data                | Model      | # Latent Dimensions | loss   | accuracy   | cs accuracy | f1         | cs f1      | precision  | recall     |
|---------------------|------------|---------------------|--------|------------|-------------|------------|------------|------------|------------|
| Fake COVID News     | BERT       | N/A                 | 0.6338 | 0.7145     | N/A         | 0.6966     | N/A        | 0.7528     | 0.7047     |
|                     | Space-BERT | 3                   | 0.7875 | 0.7949     | 0.5234      | 0.7828     | 0.3436     | 0.8478     | 0.7855     |
|                     | Space-BERT | 64                  | 0.5877 | **0.8645** | **0.7743**  | 0.8627     | **0.7637** | 0.8725     | 0.8610     |
|                     | Space-BERT | 128                 | 0.5727 | 0.8808     | 0.6528      | **0.8797** | 0.5967     | **0.8859** | **0.8782** |
| Liar (multi-label)  | BERT       | N/A                 | 1.7426 | 0.2221     | N/A         | 0.1211     | N/A        | 0.1261     | 0.1815     |
|                     | Space-BERT | 3                   | 2.2877 | 0.2362     | 0.1824      | 0.1540     | 0.1079     | 0.1542     | 0.1977     |
|                     | Space-BERT | 64                  | 2.3192 | **0.2580** | **0.2362**  | 0.2034     | **0.1590** | 0.2201     | **0.2227** |
|                     | Space-BERT | 128                 | 2.3651 | 0.2572     | 0.2081      | **0.2120** | 0.1267     | **0.2527** | 0.2248     |
| Liar (binary-label) | BERT       | N/A                 | 0.7026 | 0.5666     | N/A         | 0.3617     | N/A        | 0.2833     | 0.5000     |
|                     | Space-BERT | 3                   | 0.8476 | 0.5900     | 0.5838      | 0.5280     | 0.5825     | 0.5778     | 0.5515     |
|                     | Space-BERT | 64                  | 0.8591 | **0.6267** | **0.5877**  | **0.6002** | **0.5855** | **0.6185** | **0.6031** |
|                     | Space-BERT | 128                 | 0.8747 | 0.6251     | 0.5744      | 0.5971     | 0.4194     | 0.6170     | 0.6007     |
| Kaggle Fake News    | BERT       | N/A                 | 0.6251 | 0.6550     | N/A         | 0.6337     | N/A        | 0.7400     | 0.4319     |
|                     | Space-BERT | 3                   | 0.7444 | 0.8069     | 0.6408      | 0.8030     | 0.6396     | 0.8769     | 0.6946     |
|                     | Space-BERT | 64                  | 0.5305 | 0.8685     | **0.6834**  | 0.8672     | **0.6497** | 0.9132     | 0.8018     |
|                     | Space-BERT | 128                 | 0.5016 | **0.8868** | 0.6436      | **0.8859** | 0.5900     | **0.9228** | **0.8334** |
| Fake News Net       | BERT       | N/A                 | 0.5502 | 0.7548     | N/A         | 0.4302     | N/A        | 0.3774     | 0.5000     |
|                     | Space-BERT | 3                   | 0.7124 | 0.7557     | 0.2732      | 0.4336     | 0.2400     | **0.8777** | 0.5016     |
|                     | Space-BERT | 64                  | 0.6754 | 0.7955     | 0.6468      | 0.6654     | 0.6090     | 0.7359     | 0.6453     |
|                     | Space-BERT | 128                 | 0.6826 | **0.8028** | **0.7131**  | **0.6833** | **0.6302** | 0.7475     | **0.6616** |

## Cross-dataset benchmarking

| (Train) -> (Test)            | Model      | # Dims. | loss   | accuracy   | cs accuracy | f1         | cs f1      | precision  | recall     |
|------------------------------|------------|---------|--------|------------|-------------|------------|------------|------------|------------|
| (GossipCop) -> (CovidFake)   | BERT       | N/A     | 0.8384 | 0.5234     | N/A         | 0.3436     | N/A        | 0.2616     | 0.5000     |
|                              | Space-BERT | 3       | 0.7862 | 0.5234     | **0.6145**  | 0.3436     | **0.6052** | 0.2617     | 0.5000     |
|                              | Space-BERT | 64      | 0.8823 | **0.5375** | 0.6064      | **0.3806** | 0.5874     | 0.6911     | **0.5151** |
|                              | Space-BERT | 128     | 0.9444 | 0.5373     | 0.5691      | 0.3797     | 0.4712     | **0.6954** | 0.5149     |
| (GossipCop) -> (Politifact)  | BERT       | N/A     | 0.5990 | 0.5909     | N/A         | 0.3714     | N/A        | 0.2955     | 0.5000     |
|                              | Space-BERT | 3       | 0.5621 | 0.5909     | 0.4403      | 0.3714     | 0.3699     | 0.2955     | 0.5000     |
|                              | Space-BERT | 64      | 0.5385 | 0.6695     | 0.6259      | 0.6085     | **0.6258** | 0.6812     | 0.6181     |
|                              | Space-BERT | 128     | 0.5312 | **0.6941** | **0.6468**  | **0.6395** | 0.6155     | **0.7172** | **0.6447** |
| (FakeNewsNet) -> (CovidFake) | BERT       | N/A     | 0.8171 | 0.5234     | N/A         | 0.3436     | N/A        | 0.2617     | 0.5000     |
|                              | Space-BERT | 3       | 0.7652 | 0.5234     | 0.6024      | 0.3436     | 0.5881     | 0.2617     | 0.5000     |
|                              | Space-BERT | 64      | 0.8256 | **0.5482** | **0.6191**  | **0.4064** | **0.6116** | 0.6983     | **0.5265** | <--- this is the same as training inter-space loss for only 10 epochs
|                              | Space-BERT | 128     | 0.8719 | 0.5480     | 0.5956      | 0.4056     | 0.5354     | **0.7008** | 0.5263     |

| (Train) -> (Test)        | Model      | # Dims. | loss   | accuracy   | cs accuracy | f1         | cs f1      |
|--------------------------|------------|---------|--------|------------|-------------|------------|------------|
| (Gossip) -> (CovidFake)  | BERT       | N/A     | 0.8384 | 0.5234     | N/A         | 0.3436     | N/A        |
|                          | Space-BERT | 3       | 0.7862 | 0.5234     | **0.6145**  | 0.3436     | **0.6052** |
|                          | Space-BERT | 64      | 0.8823 | **0.5375** | 0.6064      | **0.3806** | 0.5874     |
|                          | Space-BERT | 128     | 0.9444 | 0.5373     | 0.5691      | 0.3797     | 0.4712     |
| (Gossip) -> (Politifact) | BERT       | N/A     | 0.5990 | 0.5909     | N/A         | 0.3714     | N/A        |
|                          | Space-BERT | 3       | 0.5621 | 0.5909     | 0.4403      | 0.3714     | 0.3699     |
|                          | Space-BERT | 64      | 0.5385 | 0.6695     | 0.6259      | 0.6085     | **0.6258** |
|                          | Space-BERT | 128     | 0.5312 | **0.6941** | **0.6468**  | **0.6395** | 0.6155     |
| (NewsNet) -> (CovidFake) | BERT       | N/A     | 0.8171 | 0.5234     | N/A         | 0.3436     | N/A        |
|                          | Space-BERT | 3       | 0.7652 | 0.5234     | 0.6024      | 0.3436     | 0.5881     |
|                          | Space-BERT | 64      | 0.8256 | **0.5482** | **0.6191**  | **0.4064** | **0.6116** |
|                          | Space-BERT | 128     | 0.8719 | 0.5480     | 0.5956      | 0.4056     | 0.5354     |

# Ablation Study

## Same dataset inter-space and intra-space loss ablation study

| Data          | Model      | # Latent Dimensions | loss   | accuracy   | cs accuracy | f1         | cs f1      | precision  | recall     |
|---------------|------------|---------------------|--------|------------|-------------|------------|------------|------------|------------|
| GossipCop     | Space-BERT | 3                   | 1.9304 | 0.7566     | 0.7053      | 0.4307     | 0.6387     | 0.3783     | 0.5000     |
|               | Space-BERT | 64                  | 2.0755 | 0.2818     | 0.6857      | 0.2538     | 0.6366     | 0.5683     | 0.5175     |
|               | Space-BERT | 128                 | 2.0751 | 0.7448     | **0.7442**  | 0.4436     | **0.6522** | 0.4861     | 0.4985     |
| Fake News Net | Space-BERT | 3                   | 1.7721 | 0.7548     | 0.6196      | 0.4302     | 0.5962     | 0.3774     | 0.5000     |
|               | Space-BERT | 64                  | 0.7079 | 0.7815     | 0.7055      | 0.6016     | 0.6325     | 0.7203     | 0.5928     |
|               | Space-BERT | 128                 | 0.6910 | **0.7973** | 0.7321      | **0.6703** | 0.6370     | **0.7350** | **0.6500** |

## Cross-dataset inter-space and intra-space loss ablation study

| (Train) -> (Test)            | Model      | # Dims. | loss   | accuracy | cs accuracy | f1     | cs f1      | precision | recall |
|------------------------------|------------|---------|--------|----------|-------------|--------|------------|-----------|--------| 
| (GossipCop) -> (CovidFake)   | Space-BERT | 3       | 0.7034 | 0.5234   | 0.5292      | 0.3436 | 0.3606     | 0.2617    | 0.5000 |
|                              | Space-BERT | 64      | 0.6892 | 0.4759   | 0.5967      | 0.3238 | 0.5549     | 0.4112    | 0.4991 |
|                              | Space-BERT | 128     | 0.7052 | 0.4401   | 0.5543      | 0.3472 | 0.4312     | 0.3468    | 0.4234 |
| (FakeNewsNet) -> (CovidFake) | Space-BERT | 3       | 0.7046 | 0.5234   | 0.5379      | 0.3436 | 0.3830     | 0.2617    | 0.5000 |
|                              | Space-BERT | 64      | 0.6888 | 0.4761   | **0.6260**  | 0.3238 | **0.6039** | 0.4200    | 0.4993 | <---
|                              | Space-BERT | 128     | 0.7055 | 0.4338   | 0.5778      | 0.3467 | 0.4927     | 0.3457    | 0.4177 |