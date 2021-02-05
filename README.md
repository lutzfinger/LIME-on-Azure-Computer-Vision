# XAI is an important tool for AI Transparency
Artificial Intelligence (AI) is everywhere. No longer is AI only used by Netflix to serve you your next best evening entertainment. It helps determine whether you should get an interview, assess jail time, score your credit application, and give a medical diagnosis.

Transparency of algorithms will often lead to interpretability questions. E.g., why did the algorithm reject my credit application? Explainable AI or XAI is a new field in research. Some machine learning algorithms such as decision trees, Bayesian classifiers, and linear models are easy to interpret since the data/features used are explainable by themselves. For example, an algorithm predicting the odds of being 'overweight' might use age, type of residence, education level, wealth index, etc... Those variables will be weighted during model training. The combination of weights and variables can explain later predictions. Deep learning models, on the other hand, can not be explained so easily. In Deep Learning, the algorithms create their own variables, which might not make immediate sense for us humans. 

Since this is the cutting edge of research, many new tools get developed to help with explainability. LIME is one of them. To understand where Microsoft Azure sees for example a Guitar, LIME creates many different versions of the same image by removing some pixels. If the AI stops seeing the "Guitar," we can assume that this area was linked to the guitar. 

Read more about XAI and why it's needed for the success of AI [here](https://www.forbes.com/sites/lutzfinger/2021/02/04/president-biden-is-man-woman-and-40-years-oldwhy-we-need-algorithmic-transparency/)

# LIME-on-Azure-Computer-Vision

Analysing Microsoft Cognitive Services Computer Vision software's predictions using LIME
We're not yet at a stage where AI can take complete control of daily processes. Transparency into AI's working mechanisms is a great first step.

[Presentation](https://docs.google.com/presentation/d/1dsar5sA3D1ofe7SD9kDvyD5TIXRUlRGAAlNTV-m_N70/edit?usp=sharing) 
## Try some examples from the "try it yourself folder":

[Azure Cognitive Services:](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/#features)


PS: It's very likely that the description & tags of these images get's changed in the future, once MSFT realises them.


## What is LIME?

LIME is a tool used for explaining predictions of machine learning models. The following resource to [LIME](https://github.com/marcotcr/lime) is a great starting point to understand it.

LIME is based on the work presented in [this paper](https://arxiv.org/abs/1602.04938).

<a href="https://www.youtube.com/watch?v=hUnRCxnydCc" target="_blank"><img src="video_start.png" width="450" alt="KDD promo video"/></a>

## Installation

The lime package is on [PyPI](https://pypi.python.org/pypi/lime). Use the following to install:

```sh
pip install lime
```

Install [PIL](https://pypi.python.org/pypi/Pillow/2.2.1):

```sh
pip install Pillow
```

Besides LIME and PIL, we use matplotlib, numpy and skimage.segmentation

## Instructions to run the code
1. Have images in .jpeg or .jpg format.
2. Have a temporary folder with the image and the copy of the image you want to test
3. Run the following code with a (very :P) stable internet connection.
4. Increase the number of features to increase LIME's complexity.

```
python3 <file_name>.py <subscription_key> <endpoint> <image_path> <image_copy_path> <tag/caption/celebrity> <number_of_samples> 
```


## Examples

## Donald Trump 

![LIME can't see the smile](Examples/Donald%20Trump%20Smiling.png)



![Results](Examples/Results_Donald%20Trump%20Smiling.png)



## Satya Nadella - Missing Tie

![Identifying the Tie](Examples/Satya%20tie.jpg)



![Results](Examples/Results%20satya_tie_10000.png)



## Hillary Clinton - with a Guitar

![Ah, there it is!](Examples/Performing%20Hillary.png)



![Results](Examples/Results_Performing%20Hillary.png)

