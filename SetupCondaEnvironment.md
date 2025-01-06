conda env list

conda deactivate


conda remove -n subscribe --all

source activate spyder-env

source activate topicenviroment 


python -m pip install pandas_gpt

python -m pip install -r requirements.txt
python -m pip install bertopic


pip install spacy


python -m pip install --upgrade numpy
python -m pip install --upgrade requirements.txt


# set up vitual environment
conda create -n BRenv python=3.8

conda activate BRenv  

conda install -c conda-forge hdbscan

pip install bertopic

# facilitate manipulation




import subprocess
import sys

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}")

# Example usage
packages_to_install = ["bertopic"]

for package in packages_to_install:
    install_package(package)


# gpt

mergeprobabiliyt = results.ask('drop word as an index')

