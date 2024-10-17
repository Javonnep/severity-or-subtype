# Intro

Autism Spectrum Disorder (ASD) is a disorder known for having high levels of inter-group variation, otherwise known as heterogeneity. This has led to an active field of study investigating models that can make sense of heterogeneity in ASD. The ideal model allows us to observe what unites autistic people together as a group, while also indicating how they differ. This repository contains the code I used to study heterogeneity in ASD. Starting from the raw version of the ABIDE II dataset, I detail the creation of 5 datasets that make studying heterogeneity in ASD accessible to even students on an Introductory Machine Learning course. I then use these datasets to investigate heterogeneity in ASD by applying KMeans clustering to Structural MRI data from 367 Autistic and Allistic subjects and following that up with a post-hoc analysis of phenotypic (behavioural) data regarding the clusters found. My initial results show no evidence for clusters in ASD that possess a Neurobiological origin (An origin in the brain). However, with my easy-to-use datasets, further study still has the potential to suggest the existence of these clusters.

# To participate
There are a few steps before you can get involved.


## Tools

This project has quite an expansive tech stack. The required tools (and download links are):

1. [Python](https://www.python.org/)
2. [CCS](https://github.com/zuoxinian/CCS) (And associated dependencies)
3. [ComBat](https://github.com/Jfortin1/ComBatHarmonization) 

## Data

You also need a lot of data. 

You can start with raw data from the [ABIDE II Website](http://fcon_1000.projects.nitrc.org/indi/abide/abide_II.html)

You can also start from some of the datasets I created and uploaded [here](https://imperiallondon-my.sharepoint.com/:f:/g/personal/jp2923_ic_ac_uk/Evn-uxGaeDNCt9-6DZc-PkQBVJ8iFF1DiGTz4pu7e_lrRA) (Send an email to javonne.porter@gmail.com for access)

You can get most of the data on [kaggle](https://www.kaggle.com/datasets/javonne/abide-ii-sequential)

And you can get the unprocessed fmri data on [google drive](https://drive.google.com/file/d/1oqxdGFPdzVSj0zBHJdbbXl6UVswHqrtC/view?usp=sharing)


# Setting up

## Data preprocessing

Firstly create the abide environment.

``````
conda env create abide python=3.9
conda create --name abide python=3.9
conda activate abide
pip install -r requirements.txt
``````

From this point, assuming you'd like to preprocess your own data, you should look at the CCS README in the repo.

