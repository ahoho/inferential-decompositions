# Inferential Decompositions

Repository for [Natural Language Decompositions of Implicit Content Enable Better Text Representations](https://arxiv.org/abs/2305.14583), accepted to EMNLP 2023.

### Update 02/08/2024: 

* We have released step-by-step instructions to create the environment required to run the tutorial below, for MacOS and Linux. Please refer to the "Setting up the environment" section for more details. 

### Update 11/17/2023: 

* We have released a notebook with a step-by-step process to generate inferential decompositions. Please refer to [decomposition_tutorial.ipynb](./decomposition_tutorial.ipynb) for more details.
* We have also released the text and inferential decompositions from the legislative tweets dataset used in Section 5 in our paper for analyzing legislator behaviour.

### Environment Setup
----
We recommend using a conda environment to run the notebook. If you don't have conda installed, you can download it [here](https://docs.conda.io/en/latest/miniconda.html). Install the required packages using the following commands:
  
**Linux**:  ```conda env create -f environment.yml```\
**OSX**:  ```conda env create -f environment_mac.yml```

Note: The CUDA version assumed in the torch installation is 12.x, please change to the version you have installed or use CPU. Check the [PyTorch website](https://pytorch.org/get-started/previous-versions/) for compatibilities on previous versions.

For manual installation, please refer to the instructions below.

<details>
<summary>Instructions for Manual Installation</summary>

- Create an environment using conda: 
```conda create --name decompositions -c conda-forge python=3.10 ipykernel ipywidgets jupyterlab notebook nb_conda_kernels```
- Activate the environment: 
```conda activate decompositions```
- Install pytorch dependencies : 
  - **For OSX (Tested on Apple Silicon)**: ```conda install pytorch::pytorch==2.2.0 torchvision==0.17.0 torchaudio=2.2.0 -c pytorch```
  - **For Linux**: ```conda install pytorch==2.2.0 torchvision==0.17.0 torchaudio=2.2.0 pytorch-cuda=12.1 -c pytorch -c nvidia``` [IMPORTANT: Please check the appropriate CUDA version for your system, or remove the ```pytorch-cuda``` part if you don't have a GPU.]
- Install sentence_transformers to meausre embedding distance: ```conda install -c conda-forge sentence-transformers==2.3.1```
- [OPTIONAL] Set your transformers cache!:  ```export TRANSFORMERS_CACHE=<your cache folder>```
- ```conda install conda-forge::transformers==4.31.0 datasets==2.16.1```
- Install specific versions of ```openai``` and ```langchain```:  ```pip install openai==0.28 langchain==0.0.186```
- Install remaining dependencies: ```pip install matplotlib nltk jsonlines simple_colors```
</details>

---
#### Final Steps

- Set OpenAI API key: ```conda env config vars set OPENAI_API_KEY=<your key>```
- Finally, deactivate and reactivate the environment: ```conda deactivate``` and ```conda activate decompositions```\

After setting up the repo, run the [decomposition_tutorial.ipynb](./decomposition_tutorial.ipynb) to see the method in action (and to use your own prompts and exemplars on your own dataset.). Don't forget to select the kernel for the `decompositions` environment in the notebook!

We're excited to hear what you use our method for! Please reach out with any questions or comments, or create an issue. 

The COVID vaccine comment dataset is available upon request (all comments are publicly available, but we elected not to re-host data out of concern for commenters' privacy).

---- 

If you find our work useful, please cite us:

```
@inproceedings{hoyle-etal-2023-natural,
    title = "Natural Language Decompositions of Implicit Content Enable Better Text Representations",
    author = "Hoyle, Alexander  and
      Sarkar, Rupak  and
      Goel, Pranav  and
      Resnik, Philip",
    editor = "Bouamor, Houda  and
      Pino, Juan  and
      Bali, Kalika",
    booktitle = "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.emnlp-main.815",
    doi = "10.18653/v1/2023.emnlp-main.815",
    pages = "13188--13214",
}
```
