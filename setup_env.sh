set -e

env_name="${1:-decompositions}"

if ! command -v conda &>/dev/null; then
    echo "'conda' not found; install it here: https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

if ! { conda env list | grep "${env_name}"; } >/dev/null 2>&1; then
    conda create -y -n "${env_name}" python=3.10
fi

eval "$(conda shell.bash hook)"
conda activate ${env_name}

# huggingface installs
pip install --no-cache transformers==4.35.2 datasets==2.15.0

# notebook stuff
pip install --no-cache ipywidgets ipykernel 

# nb_conda_kernels is required for jupyterlab to see the conda env
conda install -c conda-forge nb_conda_kernels

# if you prefer jupyterlab, uncomment the following line
# pip install --no-cache jupyterlab

# install openai and langchain
pip install --no-cache openai==1.3.6 langchain==0.0.344

# if you prefer the classic notebook interface, uncomment the following line
pip install --no-cache notebook 

# Torch installs
pip install torch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 --index-url https://download.pytorch.org/whl/cu118

# install sentence-transformers
pip install --no-cache sentence-transformers

# NLP tools
pip install --no-cache nltk

# misc other standard-ish packages (if not already installed as dependencies)
pip install --no-cache numpy pandas scipy scikit-learn matplotlib 

# outputs 
pip install --no-cache rich loguru jsonlines
