# LIME-on-Azure-Computer-Vision

Analysing Microsoft Cognitive Services Computer Vision software's predictions using LIME
We're not yet at a stage where AI can take complete control of daily processes. Transparency into AI's working mechanisms is a great first step.

## Try some examples from the "try it yourself folder":

[Azure Cognitive Services:](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/#features)
PS: It's very likely that the description/tags of these images get's changed in the future, once MSFT realises them.

## Examples

## Satya Nadella - Missing Tie

![Identifying the Tie](Examples/Satya%20tie.jpg)



![Results](Examples/Results%20satya_tie_10000.png)



## President Donald Trump 

![LIME can't see the smile](Examples/Donald%20Trump%20Smiling.png)



![Results](Examples/Results_Donald%20Trump%20Smiling.png)



## Hillary Clinton - with a Guitar

![Ah, there it is!](Examples/Performing%20Hillary.png)



![Results](Examples/Results_Performing%20Hillary.png)



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

Besides LIME and PIL, we utilise, matplotlib, numpy and skimage.segmentation

## Instructions to run the code
1. Have images in .jpeg or .jpg format.
2. Have a temporary folder with the image and the copy of the image you want to test
3. Run the following code with a stable internet connection.

```
python3 <file_name>.py <subscription_key> <endpoint> <image_path> <image_copy_path> <tag/caption/celebrity> <number_of_samples> 
```
