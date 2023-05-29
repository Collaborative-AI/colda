<p align="center">
    <br>
    <img src="asset/img/colda.png" width="400"/>
    <br>
<p align="center"><em><strong>Col</strong>laborative <strong>D</strong>ata  <strong>A</strong>nalysis for All</em></p>

## Introduction
ColDA  is an open source project aimed at providing distributed machine learning tools for data analysis and machine learning based on [Assisted Learning](https://assisted-learning.org/).

## Features

- Algorithm
- Frontend
- Backend
- Package

## Algorithm

The project uses [Gradient Assisted Learning](https://github.com/diaoenmao/GAL-Gradient-Assisted-Learning-for-Decentralized-Multi-Organization-Collaborations) as the fundamental algorithm for collaboratively training distributed models.

### Get started
- Use `data/make_dataset.py` to split csv files
- Use command in `run_[dataset]_[number_of_sponsor]s_[number of assistor]a.sh` to run experiments

### Instructions
 - files ends with `_exe.py` are local operations
 - `baseline.py` produces baseline results on joint datasets
 - `make_train_local.py` produces baseline results on joint datasets
 - `make_hash.py` uses `sha256` to encode identification for alignment
 - `save_match_id.py` saves hash results
 - `make_match_idx.py` match identification with hash results
 - `make_residual.py` computes residuals
 - `save_residual.py` saves residuals
 - `make_train.py` locally fits the residuals
 - `save_output.py` saves outputs of trained models
 - `make_result.py` produces aggregated results
 - `make_test.py` produces inference results
 - `make_eval.py` evaluates inference results

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

## Frontend

### Get started

Run the following command to launch the software for the first time:

```bash
sudo apt install npm

# update node
sudo npm cache clean -f
dudo npm install -g n
sudo n stable
PATH = "$PATH"

sudo snap install vue

npm install

npm run electron:serve

./node_modules/.bin/electron-rebuild # If there is bug on windows: .\node_modules\.bin\electron-rebuild

```

Run the following command to launch the software after first time:

```bash
npm install

npm run electron:serve
```

Run the following command to package the software:

```bash
npm install

npm run electron:build
```

Run the following command to run unittest:

```bash
npm run test
```

### Instructions

 - `Navbar.vue` presents the software navigation bar, and the communication between the software and the backend is mainly completed by the functions in this file
 - `assets` folder contains image, font, css resources used in the software
 - `components` folder contains reusable interface components
 - `network` folder contains request sending and interception configuration
 - `router` folder conatins routing configuration file
 - `store` folder is used for storing some local information
 - `Notifications` folder contains functions that handle notifications and history
 - `Auth` folder contains functions that handle user registration and login
 - `Settings` folder contains functions that handle user customized settings
 - `tests` folder contains unittest function
 
## Backend
### Getting Started
- launch procedures
    - export FLASK_APP=application.py (first time you clone the github)
    - pipenv install
    - pipenv shell
    - flask run

- Unittest:
    - flask test (test all files, use this command in top file level)
    - notes: You could switch the test framework to pytest, which is more convenient
    - notes: tests/test_unread_test_output.py contains most the logic for your reference

- Deploy:
    - Install some dependencies first follow [this](https://www.youtube.com/watch?v=D2GLVoiEZyE&ab_channel=ArpanNeupane)
    - heroku login (Use username and pwd in google drive key file)
    - git add .
    - git commit -m 'Commit_Name'
    - git push 
    - git push heroku Current_branch_name
    - heroku open (view our app)


## Package

### Getting Started

### Use case

- Instruction can be found in Sponsor_User_Guide_bos.py and Assistor_User_Guide_bos.py

### Package Stucture

- Basic package structure can be found in [Github repository](https://github.com/AlexIoannides/py-package-template)

- Compared to the Basic package structure, ``docs/`` will contain different element. But at this point, you can follow the template

- ``py-pkg`` is the main part of the package, you can add more modules (with ``__init__.py``) in this part. For example, if you add ``temp`` module, you can import ``temp`` module by:

```bash
import temp from py-pkg
```

- This package structure can be improved by learning [PyTorch](https://github.com/pytorch/pytorch) package structure.

- Basic Structure: 

```bash
py-package-tempate/
 |-- docs/
 |-- |-- build_html/
 |-- |-- build_latex/
 |-- |-- source/
 |-- py-pkg/
 |-- |-- __init__.py
 |-- |-- __version__.py
 |-- |-- curves.py
 |-- |-- entry_points.py
 |-- tests/
 |-- |-- test_data/
 |-- |   |-- supply_demand_data.json
 |-- |   __init__.py
 |-- |   conftest.py
 |-- |   test_curves.py
 |-- .env
 |-- .gitignore
 |-- Pipfile
 |-- Pipfile.lock
 |-- README.md
 |-- setup.py
```


### How to Manage Package Environment

- ``pipenv`` is used to manage package. You can install ``pipenv`` by:

```bash
pip3 install pipenv
```

- Use ``pipenv`` to install package. The first command is to install the package for development. The second command is to install the package for production.

```bash
pipenv install --dev
pipenv install 
```

- Use ``pipenv`` to uninstall package:

```bash
pipenv uninstall
```

### Pipenv Shells

- Entering into a Pipenv-managed shell. Remeber doing this **every time** before running the project. 

```bash
cd py-package-tempate
pipenv install
pipenv shell
```


## License

ColDA is licensed under the [Apache 2.0 License](LICENSE).

## Code of Conduct

Please review and adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) when contributing to ColDA.



## Reference
Please use the following reference
```bibtex
@article{diao2022gal,
  title={GAL: Gradient Assisted Learning for Decentralized Multi-Organization Collaborations},
  author={Diao, Enmao and Ding, Jie and Tarokh, Vahid},
  journal={Advances in Neural Information Processing Systems},
  volume={35},
  pages={11854--11868},
  year={2022}
}
```


