## Example
Sample code in `AL_Notebook.ipynb` notebook

## Install
- `pip install active_learning`
- OR
- `python setup.py sdist`
- `python setup.py install`

## Environment Setup
 - Make sure that
   [conda](https://conda.io/docs/user-guide/install/index.html#regular-installation) is
   installed.
 - Run the following command in the root directory to build the conda
   environment "trews": `conda env create -f environment.yml`
 - Run `source activate trews` before executing the Jupyter
   notebook.
 - "trews" has a package nb\_conda which allows you to specify the
   conda env you want as a Jupyter kernel. __You must have "trews"
   activated for the Jupyter notebook server to manage conda
   environments__

## Objective
 - Provide justification for custom sepsis definition generated from
   soliciting rich feedback from physicians.
 - Create an AL implementation that incorporates rich feedback from
   physicians to improve the TREWS tool.
 - Long-term goal: Create a library of active learning tools for any
   CDSS we design for new clinical problems.

## Code Organization
 - General functions should be written in .py files under folder
   'python_scripts'
 - Experiments should load these python files into iPython notebooks
   for visualization/output neatness and reproducibility.
   - Large experimental datasets should be stored locally and tracked
     using plaintext files or logs.
 - Datasets used for testing implementation should be kept under
   repository 'dev_data'



