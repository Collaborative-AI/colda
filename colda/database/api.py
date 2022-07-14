from __future__ import annotations

import collections

from colda.database.utils import get_user_id

from typing import(
    List
)

from colda.database.strategy.api import DatabaseOperator

from typeguard import typechecked


def get_all_train_id() -> list[str]:
    '''
    Get all train ids that store
    in all db

    Returns
    -------
    list[str]
    '''
    return get_all_train_id_as_sponsor() + get_all_train_id_as_assistor()

def get_all_test_id() -> list[str]:
    '''
    Get all test ids that store
    in all db

    Returns
    -------
    list[str]
    '''
    return get_all_test_id_as_sponsor() + get_all_test_id_as_assistor()

def get_all_train_id_as_sponsor() -> list[str]:
    '''
    Get all train ids as sponsor that store
    in all db

    Returns
    -------
    list[str]
    '''
    user_id = get_user_id()
    all_train_ids = []
    DatabaseOperator.set_database(database_type='train_sponsor_metadata')
    for record_key, record_val in DatabaseOperator.get_all_records().items():
        if user_id == record_key[0]:
            all_train_ids.append(record_val['train_id'])

    return all_train_ids

def get_all_test_id_as_sponsor() -> list[str]:
    '''
    Get all test ids as sponsor that store
    in all db

    Returns
    -------
    list[str]
    '''
    user_id = get_user_id()
    all_test_ids = []
    DatabaseOperator.set_database(database_type='test_sponsor_metadata')
    for record_key, record_val in DatabaseOperator.get_all_records().items():
        if user_id == record_key[0]:
            all_test_ids.append(record_val['test_id'])

    return all_test_ids


def get_all_train_id_as_assistor() -> list[str]:
    '''
    Get all train ids as assistor that store
    in all db

    Returns
    -------
    list[str]
    '''
    user_id = get_user_id()
    all_train_ids = []
    DatabaseOperator.set_database(database_type='train_assistor_metadata')
    for record_key, record_val in DatabaseOperator.get_all_records().items():
        if user_id == record_key[0]:
            all_train_ids.append(record_val['train_id'])

    return all_train_ids

def get_all_test_id_as_assistor() -> list[str]:
    '''
    Get all test ids as assistor that store
    in all db

    Returns
    -------
    list[str]
    '''
    user_id = get_user_id()
    all_test_ids = []
    DatabaseOperator.set_database(database_type='test_assistor_metadata')
    for record_key, record_val in DatabaseOperator.get_all_records().items():
        if user_id == record_key[0]:
            all_test_ids.append(record_val['test_id'])

    return all_test_ids

def logout(self):
    '''
    Clean all database

    Returns
    -------
    None
    '''
    try:
        self.__temp_database = collections.defaultdict(dict)
    except:
        print('Logout procedure wrong')
