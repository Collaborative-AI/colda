# Algorithm
Algorithm


conda create --name myenv python --no-default-packages  
conda activate myenv  
pip install pyinstaller  
pip install numpy  
pip install -U scikit-learn  
cd package  
#### To one folder
<!-- pyinstaller run.py   -->
pyinstaller run.spec
#### To one file
pyinstaller -F run.py  
#### follow cmd.sh after that
