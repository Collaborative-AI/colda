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

- Python
- Flask

### Getting Started

To set up and run the backend portion of the project, follow these steps:

1. Navigate to the backend directory: `cd colda/backend`
2. Create a virtual environment: `python3 -m venv env`
3. Activate the virtual environment:
   - For macOS/Linux: `source env/bin/activate`
   - For Windows: `env\Scripts\activate.bat`
4. Install the required dependencies: `pip install -r requirements.txt`
5. Start the backend server: `python app.py`
6. The backend server should now be running on `http://localhost:5000`.

## Package

- Python

### Installation

To install the coda package, use the following command:

```shell
pip install colda
```

## License

ColDA is licensed under the [Apache 2.0 License](LICENSE).

## Code of Conduct

Please review and adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) when contributing to ColDA.



## Citation
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


