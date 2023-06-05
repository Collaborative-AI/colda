# Algorithm

### Instructions
Use `data/make_dataset.py` to split csv files
Use command in `run_[dataset]_[number_of_sponsor]s_[number of assistor]a.sh` to run experiments

### PyInstaller
```bash
conda create --name myenv python --no-default-packages  
conda activate myenv  
pip install pyinstaller  
pip install numpy  
pip install -U scikit-learn  
cd algorithm
pyinstaller run.spec  # To one folder
pyinstaller -F run.py  # To one folder
```
