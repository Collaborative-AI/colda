# make dataset
python make_dataset.py --root ./data/processed/CreditCard --data_name CreditCard --task_id 123 --num_users 1 --match_rate 1 --normalize 1
python make_dataset.py --root ./data/processed/CreditCard --data_name CreditCard --task_id 123 --num_users 2 --match_rate 1 --normalize 1
python make_dataset.py --root ./data/processed/CreditCard --data_name CreditCard --task_id 123 --num_users 2 --match_rate 0.5 --normalize 1

# baseline
python baseline.py --root ./data/processed/CreditCard --data_name CreditCard --task_id 123 --num_users 1 --match_rate 1 --task_mode classification --model_name linear --metric_name Accuracy_F1_AUCROC
python baseline.py --root ./data/processed/CreditCard --data_name CreditCard --task_id 123 --num_users 2 --match_rate 1 --task_mode classification --model_name linear --metric_name Accuracy_F1_AUCROC
python baseline.py --root ./data/processed/CreditCard --data_name CreditCard --task_id 123 --num_users 2 --match_rate 0.5 --task_mode classification --model_name linear --metric_name Accuracy_F1_AUCROC

# local
python run.py make_train_local --root ./exp --self_id 0 --task_id xyz --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/0/train/dataset.csv --data_idx 2-16 --target_idx 17 --task_mode classification --model_name linear --metric_name Accuracy_F1_AUCROC
python run.py make_test_local --root ./exp --self_id 0 --task_id xyz --test_id uvw --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/0/test/dataset.csv --data_idx 2-16 --target_idx 17 --task_mode classification --metric_name Accuracy_F1_AUCROC

# default
# hash id
python run.py make_hash --root ./exp --self_id 0 --mode default --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/0/all/dataset.csv --id_idx 1
python run.py make_hash --root ./exp --self_id 1 --mode default --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/1/all/dataset.csv --id_idx 1

# Train
# hash id
python run.py make_hash --root ./exp --self_id 0 --task_id xyz --mode train --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/0/train/dataset.csv --id_idx 1
python run.py make_hash --root ./exp --self_id 1 --task_id xyz --mode train --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/1/all/dataset.csv --id_idx 1

# match id
python run.py save_match_id --root ./exp --self_id 0 --task_id xyz --mode train --from_id 1
python run.py save_match_id --root ./exp --self_id 1 --task_id xyz --mode train --from_id 0
python save_match_id_exe.py --root ./exp --self_id 0 --task_id xyz --mode train --from_id 1
python run.py make_match_idx --root ./exp --self_id 0 --task_id xyz --mode train --from_id 1
python run.py make_match_idx --root ./exp --self_id 1 --task_id xyz --mode train --from_id 0

# round 1
# make residual
python run.py make_residual --root ./exp --self_id 0 --task_id xyz --round 1 --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/0/train/dataset.csv --target_idx 17 --task_mode classification --metric_name Accuracy_F1_AUCROC
python run.py save_residual --root ./exp --self_id 1 --task_id xyz --round 1
python save_residual_exe.py --root ./exp --self_id 1 --task_id xyz --from_id 0 --round 1

# train
python run.py make_train --root ./exp --self_id 0 --task_id xyz --round 1 --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/0/train/dataset.csv --data_idx 2-16 --task_mode regression --model_name linear
python run.py make_train --root ./exp --self_id 1 --task_id xyz --round 1 --from_id 0 --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/1/all/dataset.csv --data_idx 2-15 --task_mode regression --model_name linear

# output
python run.py save_output --root ./exp --self_id 0 --task_id xyz --mode train --from_id 1 --round 1
python save_output_exe.py --root ./exp --self_id 0 --task_id xyz --mode train --from_id 1 --round 1
python run.py make_result --root ./exp --self_id 0 --task_id xyz --round 1 --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/0/train/dataset.csv --target_idx 17 --task_mode classification --metric_name Accuracy_F1_AUCROC

# round 2
# make residual
python run.py make_residual --root ./exp --self_id 0 --task_id xyz --round 2 --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/0/train/dataset.csv --target_idx 17 --task_mode classification --metric_name Accuracy_F1_AUCROC
python run.py save_residual --root ./exp --self_id 1 --task_id xyz --round 2
python save_residual_exe.py --root ./exp --self_id 1 --task_id xyz --from_id 0 --round 2

# train
python run.py make_train --root ./exp --self_id 0 --task_id xyz --round 2 --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/0/train/dataset.csv --data_idx 2-16 --task_mode regression --model_name linear
python run.py make_train --root ./exp --self_id 1 --task_id xyz --round 2 --from_id 0 --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/1/all/dataset.csv --data_idx 2-15 --task_mode regression --model_name linear

# output
python run.py save_output --root ./exp --self_id 0 --task_id xyz --mode train --from_id 1 --round 2
python save_output_exe.py --root ./exp --self_id 0 --task_id xyz --mode train --from_id 1 --round 2
python run.py make_result --root ./exp --self_id 0 --task_id xyz --round 2 --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/0/train/dataset.csv --target_idx 17 --task_mode classification --metric_name Accuracy_F1_AUCROC

# Test
# hash id
python run.py make_hash --root ./exp --self_id 0 --task_id xyz --mode test --test_id uvw --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/0/test/dataset.csv --id_idx 1
python run.py make_hash --root ./exp --self_id 1 --task_id xyz --mode test --test_id uvw --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/1/all/dataset.csv --id_idx 1

# match id 
python run.py save_match_id --root ./exp --self_id 0 --task_id xyz --from_id 1 --mode test --test_id uvw
python run.py save_match_id --root ./exp --self_id 1 --task_id xyz --from_id 0 --mode test --test_id uvw
python save_match_id_exe.py --root ./exp --self_id 0 --task_id xyz --from_id 1 --mode test --test_id uvw
python run.py make_match_idx --root ./exp --self_id 0 --task_id xyz --from_id 1 --mode test --test_id uvw
python run.py make_match_idx --root ./exp --self_id 1 --task_id xyz --from_id 0 --mode test --test_id uvw

# test
python run.py make_test --root ./exp --self_id 0 --task_id xyz --test_id uvw --round 2 --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/0/test/dataset.csv --data_idx 2-16
python run.py make_test --root ./exp --self_id 1 --task_id xyz --test_id uvw --round 2 --from_id 0 --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/1/all/dataset.csv --data_idx 2-15

# output
python run.py save_output --root ./exp --self_id 0 --task_id xyz --mode test --test_id uvw --from_id 1 --round 1
python run.py save_output --root ./exp --self_id 0 --task_id xyz --mode test --test_id uvw --from_id 1 --round 2
python save_output_exe.py --root ./exp --self_id 0 --task_id xyz --mode test --test_id uvw --from_id 1 --round 1
python save_output_exe.py --root ./exp --self_id 0 --task_id xyz --mode test --test_id uvw --from_id 1 --round 2

# eval
python run.py make_eval --root ./exp --self_id 0 --task_id xyz --test_id uvw --round 2 --dataset_path ./data/processed/CreditCard/CreditCard_2_123_1.0/0/test/dataset.csv --target_idx 17 --task_mode classification --metric_name Accuracy_F1_AUCROC

echo "$(cat ./exp/0/task/xyz/train/log.txt)"
echo "$(cat ./exp/0/task/xyz/test/uvw/log.txt)"