import os
import shutil
import numpy as np
import pandas as pd

from synspot.algorithm.base import BaseAlgorithm

from synspot.algorithm.utils import (
    makedir_exist_ok, 
    save,
)

from typing import List
    

class MakeDataset(BaseAlgorithm):

    def make_dataset(
        self, 
        root: str, 
        data_name: str, 
        num_users: int, 
        task_id: str, 
        match_rate: float = 0.5,
        normalize: int = 1,
    ) -> bool:

        np.random.seed(task_id)
        control = '_'.join([data_name, str(num_users), str(task_id), str(match_rate)])
        path = os.path.join(root, control)
        if os.path.exists(path):
            shutil.rmtree(path)
        feature_split = self.split_dataset(data_name, num_users)
        train_dataset, test_dataset = self.make_data(data_name, normalize)
        train_id, train_data, train_target = train_dataset.iloc[:, 0], train_dataset.iloc[:, 1:-1], \
                                            train_dataset.iloc[:, -1]
        test_id, test_data, test_target = test_dataset.iloc[:, 0], test_dataset.iloc[:, 1:-1], test_dataset.iloc[:, -1]
        for i in range(num_users):
            match_rate_i = 1. if i == 0 else match_rate
            train_match_size = int(len(train_dataset) * match_rate_i)
            test_match_size = int(len(test_dataset) * match_rate_i)
            train_random_i = np.random.choice(np.arange(len(train_dataset)), train_match_size, replace=False)
            test_random_i = np.random.choice(np.arange(len(test_dataset)), test_match_size, replace=False)

            # Train
            train_id_i = train_id.iloc[train_random_i]
            train_data_i = train_data.iloc[train_random_i, feature_split[i]]
            train_target_i = train_target.iloc[train_random_i]
            train_dataset_i = pd.concat([train_id_i, train_data_i, train_target_i], axis=1)
            train_path_i = os.path.join(path, str(i), 'train', 'dataset.csv')
            makedir_exist_ok(os.path.dirname(train_path_i))
            train_dataset_i.to_csv(train_path_i, index=False)

            # Test
            test_id_i = test_id.iloc[test_random_i]
            test_data_i = test_data.iloc[test_random_i, feature_split[i]]
            test_target_i = test_target.iloc[test_random_i]
            test_dataset_i = pd.concat([test_id_i, test_data_i, test_target_i], axis=1)
            test_path_i = os.path.join(path, str(i), 'test', 'dataset.csv')
            makedir_exist_ok(os.path.dirname(test_path_i))
            test_dataset_i.to_csv(test_path_i, index=False)

            # All
            all_id_i = pd.concat([train_id_i, test_id_i], axis=0)
            all_data_i = pd.concat([train_data_i, test_data_i], axis=0)
            all_target_i = pd.concat([train_target_i, test_target_i], axis=0)
            all_dataset_i = pd.concat([all_id_i, all_data_i, all_target_i], axis=1)
            all_path_i = os.path.join(path, str(i), 'all', 'dataset.csv')
            makedir_exist_ok(os.path.dirname(all_path_i))
            all_dataset_i.to_csv(all_path_i, index=False)

            # idx
            id_i_idx = '1'
            data_i_idx = '2-{}'.format(1 + train_data_i.shape[-1])
            target_i_idx = str(1 + train_data_i.shape[-1] + 1)
            save((id_i_idx, data_i_idx, target_i_idx), os.path.join(path, str(i), 'idx.pkl'), mode='pickle')
            print('Client: {}, Train: ({}, {}), Test: ({}, {}), All: ({}, {}), Idx: ({}, {}, {})'.format(i,
                                                                                                        train_data_i.shape,
                                                                                                        train_target_i.shape,
                                                                                                        test_data_i.shape,
                                                                                                        test_target_i.shape,
                                                                                                        all_data_i.shape,
                                                                                                        all_target_i.shape,
                                                                                                        id_i_idx,
                                                                                                        data_i_idx,
                                                                                                        target_i_idx))
        return True


    def split_dataset(
        self, data_name: str, num_users: int
    ) -> List[np.ndarray]:
        data_shape = {'Blob': [10], 'Iris': [4], 'Diabetes': [10], 'BostonHousing': [13], 'Wine': [13],
                    'BreastCancer': [30], 'KCHousing': [18], 'CreditCard': [29], 'MedicalInsurance': [6]}
        num_features = data_shape[data_name][-1]
        feature_split = list(np.array_split(np.random.permutation(num_features), num_users))
        return feature_split


    def make_data(
        self, data_name: str, normalize: int
    ) -> np.ndarray:
        if data_name == 'Blob':
            from sklearn.datasets import make_blobs
            n_samples, n_features = 100, 10
            X, y = make_blobs(n_samples=n_samples, n_features=n_features, centers=10, random_state=0)
            perm = np.random.permutation(len(X))
            X, y = X[perm], y[perm]
            split_idx = int(X.shape[0] * 0.8)
            train_data, test_data = X[:split_idx].astype(np.float32), X[split_idx:].astype(np.float32)
            train_target, test_target = y[:split_idx].astype(np.int64), y[split_idx:].astype(np.int64)
            columns = ['x_{}'.format(i) for i in range(n_features)]
            train_dataset = pd.DataFrame(train_data, columns=columns)
            test_dataset = pd.DataFrame(test_data, columns=columns)
            train_dataset['y'] = train_target
            test_dataset['y'] = test_target
            train_dataset_index = train_dataset.index.to_numpy()
            test_dataset_index = test_dataset.index.to_numpy() + len(train_dataset_index)
            train_dataset.insert(0, 'ID', train_dataset_index)
            test_dataset.insert(0, 'ID', test_dataset_index)
        elif data_name == 'Iris':
            from sklearn.datasets import load_iris
            loaded_dataset = load_iris()
            dataset = pd.DataFrame(loaded_dataset.data, columns=loaded_dataset.feature_names)
            dataset['class'] = loaded_dataset.target.astype(np.int64)
            perm = np.random.permutation(len(dataset))
            split_idx = int(len(perm) * 0.8)
            train_dataset = dataset.iloc[perm[:split_idx]].reset_index(drop=True)
            test_dataset = dataset.iloc[perm[split_idx:]].reset_index(drop=True)
            train_dataset_index = train_dataset.index.to_numpy()
            test_dataset_index = test_dataset.index.to_numpy() + len(train_dataset_index)
            train_dataset.insert(0, 'ID', train_dataset_index)
            test_dataset.insert(0, 'ID', test_dataset_index)
        elif data_name == 'Diabetes':
            from sklearn.datasets import load_diabetes
            loaded_dataset = load_diabetes()
            dataset = pd.DataFrame(loaded_dataset.data, columns=loaded_dataset.feature_names)
            dataset['y'] = loaded_dataset.target.astype(np.float32)
            perm = np.random.permutation(len(dataset))
            split_idx = int(len(perm) * 0.8)
            train_dataset = dataset.iloc[perm[:split_idx]].reset_index(drop=True)
            test_dataset = dataset.iloc[perm[split_idx:]].reset_index(drop=True)
            train_dataset_index = train_dataset.index.to_numpy()
            test_dataset_index = test_dataset.index.to_numpy() + len(train_dataset_index)
            train_dataset.insert(0, 'ID', train_dataset_index)
            test_dataset.insert(0, 'ID', test_dataset_index)
        elif data_name == 'BostonHousing':
            from sklearn.datasets import load_boston
            loaded_dataset = load_boston()
            dataset = pd.DataFrame(loaded_dataset.data, columns=loaded_dataset.feature_names)
            dataset['MEDV'] = loaded_dataset.target.astype(np.float32)
            perm = np.random.permutation(len(dataset))
            split_idx = int(len(perm) * 0.8)
            train_dataset = dataset.iloc[perm[:split_idx]].reset_index(drop=True)
            test_dataset = dataset.iloc[perm[split_idx:]].reset_index(drop=True)
            train_dataset_index = train_dataset.index.to_numpy()
            test_dataset_index = test_dataset.index.to_numpy() + len(train_dataset_index)
            train_dataset.insert(0, 'ID', train_dataset_index)
            test_dataset.insert(0, 'ID', test_dataset_index)
        elif data_name == 'Wine':
            from sklearn.datasets import load_wine
            loaded_dataset = load_wine()
            dataset = pd.DataFrame(loaded_dataset.data, columns=loaded_dataset.feature_names)
            dataset['class'] = loaded_dataset.target.astype(np.int64)
            perm = np.random.permutation(len(dataset))
            split_idx = int(len(perm) * 0.8)
            train_dataset = dataset.iloc[perm[:split_idx]].reset_index(drop=True)
            test_dataset = dataset.iloc[perm[split_idx:]].reset_index(drop=True)
            train_dataset_index = train_dataset.index.to_numpy()
            test_dataset_index = test_dataset.index.to_numpy() + len(train_dataset_index)
            train_dataset.insert(0, 'ID', train_dataset_index)
            test_dataset.insert(0, 'ID', test_dataset_index)
        elif data_name == 'BreastCancer':
            from sklearn.datasets import load_breast_cancer
            loaded_dataset = load_breast_cancer().astype(np.int64)
            dataset = pd.DataFrame(loaded_dataset.data, columns=loaded_dataset.feature_names)
            dataset['class'] = loaded_dataset.target
            perm = np.random.permutation(len(dataset))
            split_idx = int(len(perm) * 0.8)
            train_dataset = dataset.iloc[perm[:split_idx]].reset_index(drop=True)
            test_dataset = dataset.iloc[perm[split_idx:]].reset_index(drop=True)
            train_dataset_index = train_dataset.index.to_numpy()
            test_dataset_index = test_dataset.index.to_numpy() + len(train_dataset_index)
            train_dataset.insert(0, 'ID', train_dataset_index)
            test_dataset.insert(0, 'ID', test_dataset_index)
        elif data_name == 'KCHousing':
            # https://www.kaggle.com/harlfoxem/housesalesprediction
            dataset = pd.read_csv('./data/raw/KCHousing/kc_house_data.csv')
            dataset = dataset.drop(['id', 'date'], axis=1)
            target = dataset.pop('price')
            dataset.insert(len(dataset.columns), 'price', target.astype(np.int64))
            perm = np.random.permutation(len(dataset))
            split_idx = int(len(perm) * 0.8)
            train_dataset = dataset.iloc[perm[:split_idx]].reset_index(drop=True)
            test_dataset = dataset.iloc[perm[split_idx:]].reset_index(drop=True)
            train_dataset_index = train_dataset.index.to_numpy()
            test_dataset_index = test_dataset.index.to_numpy() + len(train_dataset_index)
            train_dataset.insert(0, 'ID', train_dataset_index)
            test_dataset.insert(0, 'ID', test_dataset_index)
        elif data_name == 'CreditCard':
            # https://www.kaggle.com/mlg-ulb/creditcardfraud
            dataset = pd.read_csv('./data/raw/CreditCard/creditcard.csv')
            dataset = dataset.drop(['Time'], axis=1)
            negative = dataset[dataset['Class'] == 0].index.to_numpy()
            positive = dataset[dataset['Class'] == 1].index.to_numpy()
            undersample = np.random.choice(negative, len(positive), replace=False)
            dataset = dataset.loc[np.concatenate([undersample, positive])].reset_index(drop=True)
            perm = np.random.permutation(len(dataset))
            split_idx = int(len(perm) * 0.8)
            train_dataset = dataset.iloc[perm[:split_idx]].reset_index(drop=True)
            test_dataset = dataset.iloc[perm[split_idx:]].reset_index(drop=True)
            train_dataset_index = train_dataset.index.to_numpy()
            test_dataset_index = test_dataset.index.to_numpy() + len(train_dataset_index)
            train_dataset.insert(0, 'ID', train_dataset_index)
            test_dataset.insert(0, 'ID', test_dataset_index)
        elif data_name == 'MedicalInsurance':
            from sklearn.preprocessing import OrdinalEncoder
            # https://www.kaggle.com/mirichoi0218/insurance
            dataset = pd.read_csv('./data/raw/MedicalInsurance/insurance.csv')
            categorical_data = dataset[['sex', 'smoker', 'region']]
            categorical_transform = OrdinalEncoder()
            dataset[['sex', 'smoker', 'region']] = categorical_transform.fit_transform(categorical_data.to_numpy())
            perm = np.random.permutation(len(dataset))
            split_idx = int(len(perm) * 0.8)
            train_dataset = dataset.iloc[perm[:split_idx]].reset_index(drop=True)
            test_dataset = dataset.iloc[perm[split_idx:]].reset_index(drop=True)
            train_dataset_index = train_dataset.index.to_numpy()
            test_dataset_index = test_dataset.index.to_numpy() + len(train_dataset_index)
            train_dataset.insert(0, 'ID', train_dataset_index)
            test_dataset.insert(0, 'ID', test_dataset_index)
        else:
            raise ValueError('Not valid data name')
        if normalize:
            from sklearn.preprocessing import StandardScaler
            train_data = train_dataset.iloc[:, 1:-1].to_numpy()
            test_data = test_dataset.iloc[:, 1:-1].to_numpy()
            normalizer = StandardScaler().fit(train_data)
            train_dataset.iloc[:, 1:-1] = normalizer.transform(train_data)
            test_dataset.iloc[:, 1:-1] = normalizer.transform(test_data)
        return train_dataset, test_dataset





       