# make dataset
python make_dataset.py --root ./data --data_name BostonHousing --task_id 123 --num_users 1 --match_rate 1
python make_dataset.py --root ./data --data_name BostonHousing --task_id 123 --num_users 2 --match_rate 1
python make_dataset.py --root ./data --data_name BostonHousing --task_id 123 --num_users 2 --match_rate 0.5

# baseline
python baseline.py --root ./data --data_name BostonHousing --task_id 123 --num_users 1 --match_rate 1 --task_mode regression --model_name linear --metric_name MAD_RMSE_R2
python baseline.py --root ./data --data_name BostonHousing --task_id 123 --num_users 2 --match_rate 1 --task_mode regression --model_name linear --metric_name MAD_RMSE_R2
python baseline.py --root ./data --data_name BostonHousing --task_id 123 --num_users 2 --match_rate 0.5 --task_mode regression --model_name linear --metric_name MAD_RMSE_R2

# local
python run.py make_train_local --root ./exp --self_id 0 --task_id abc --dataset_path ./data/BostonHousing_2_123_1.0/0/train/dataset.csv --data_idx 2-8 --target_idx 9 --task_mode regression --model_name linear --metric_name MAD_RMSE_R2
python run.py make_test_local --root ./exp --self_id 0 --task_id abc --test_id def --dataset_path ./data/BostonHousing_2_123_1.0/0/test/dataset.csv --data_idx 2-8 --target_idx 9 --task_mode regression --metric_name MAD_RMSE_R2

# default
# hash id
python run.py make_hash --root ./exp --self_id 0 --mode default --dataset_path ./data/BostonHousing_2_123_1.0/0/all/dataset.csv --id_idx 1
python run.py make_hash --root ./exp --self_id 1 --mode default --dataset_path ./data/BostonHousing_2_123_1.0/1/all/dataset.csv --id_idx 1

# Train
# hash id
python run.py make_hash --root ./exp --self_id 0 --task_id abc --mode train --dataset_path ./data/BostonHousing_2_123_1.0/0/train/dataset.csv --id_idx 1
python run.py make_hash --root ./exp --self_id 1 --task_id abc --mode train --dataset_path ./data/BostonHousing_2_123_1.0/1/train/dataset.csv --id_idx 1

# match id
python run.py save_match_id --root ./exp --self_id 0 --task_id abc --mode train --from_id 1
python run.py save_match_id --root ./exp --self_id 1 --task_id abc --mode train --from_id 0
python save_match_id_exe.py --root ./exp --self_id 0 --task_id abc --mode train --from_id 1
python run.py make_match_idx --root ./exp --self_id 0 --task_id abc --mode train --from_id 1
python run.py make_match_idx --root ./exp --self_id 1 --task_id abc --mode train --from_id 0

# round 1
# make residual
python run.py make_residual --root ./exp --self_id 0 --task_id abc --round 1 --dataset_path ./data/BostonHousing_2_123_1.0/0/train/dataset.csv --target_idx 9 --task_mode regression --metric_name MAD_RMSE_R2
python run.py save_residual --root ./exp --self_id 1 --task_id abc --round 1
python save_residual_exe.py --root ./exp --self_id 1 --task_id abc --from_id 0 --round 1

# train
python run.py make_train --root ./exp --self_id 0 --task_id abc --round 1 --dataset_path ./data/BostonHousing_2_123_1.0/0/train/dataset.csv --data_idx 2-8 --task_mode regression --model_name linear
python run.py make_train --root ./exp --self_id 1 --task_id abc --round 1 --from_id 0 --dataset_path ./data/BostonHousing_2_123_1.0/1/train/dataset.csv --data_idx 2-7 --task_mode regression --model_name linear

# output
python run.py save_output --root ./exp --self_id 0 --task_id abc --mode train --from_id 1 --round 1
python save_output_exe.py --root ./exp --self_id 0 --task_id abc --mode train --from_id 1 --round 1
python run.py make_result --root ./exp --self_id 0 --task_id abc --round 1 --dataset_path ./data/BostonHousing_2_123_1.0/0/train/dataset.csv --target_idx 9 --task_mode regression --metric_name MAD_RMSE_R2

# round 2
# make residual
python run.py make_residual --root ./exp --self_id 0 --task_id abc --round 2 --dataset_path ./data/BostonHousing_2_123_1.0/0/train/dataset.csv --target_idx 9 --task_mode regression --metric_name MAD_RMSE_R2
python run.py save_residual --root ./exp --self_id 1 --task_id abc --round 2
python save_residual_exe.py --root ./exp --self_id 1 --task_id abc --from_id 0 --round 2

# train
python run.py make_train --root ./exp --self_id 0 --task_id abc --round 2 --dataset_path ./data/BostonHousing_2_123_1.0/0/train/dataset.csv --data_idx 2-8 --task_mode regression --model_name linear
python run.py make_train --root ./exp --self_id 1 --task_id abc --round 2 --from_id 0 --dataset_path ./data/BostonHousing_2_123_1.0/1/train/dataset.csv --data_idx 2-7 --task_mode regression --model_name linear

# output
python run.py save_output --root ./exp --self_id 0 --task_id abc --mode train --from_id 1 --round 2
python save_output_exe.py --root ./exp --self_id 0 --task_id abc --mode train --from_id 1 --round 2
python run.py make_result --root ./exp --self_id 0 --task_id abc --round 2 --dataset_path ./data/BostonHousing_2_123_1.0/0/train/dataset.csv --target_idx 9 --task_mode regression --metric_name MAD_RMSE_R2

# Test
# hash id
python run.py make_hash --root ./exp --self_id 0 --task_id abc --mode test --test_id def --dataset_path ./data/BostonHousing_2_123_1.0/0/test/dataset.csv --id_idx 1
python run.py make_hash --root ./exp --self_id 1 --task_id abc --mode test --test_id def --dataset_path ./data/BostonHousing_2_123_1.0/1/test/dataset.csv --id_idx 1

# match id 
python run.py save_match_id --root ./exp --self_id 0 --task_id abc --from_id 1 --mode test --test_id def
python run.py save_match_id --root ./exp --self_id 1 --task_id abc --from_id 0 --mode test --test_id def
python save_match_id_exe.py --root ./exp --self_id 0 --task_id abc --from_id 1 --mode test --test_id def
python run.py make_match_idx --root ./exp --self_id 0 --task_id abc --from_id 1 --mode test --test_id def
python run.py make_match_idx --root ./exp --self_id 1 --task_id abc --from_id 0 --mode test --test_id def

# test
python run.py make_test --root ./exp --self_id 0 --task_id abc --test_id def --round 2 --dataset_path ./data/BostonHousing_2_123_1.0/0/test/dataset.csv --data_idx 2-8
python run.py make_test --root ./exp --self_id 1 --task_id abc --test_id def --round 2 --from_id 0 --dataset_path ./data/BostonHousing_2_123_1.0/1/test/dataset.csv --data_idx 2-7

# output
python run.py save_output --root ./exp --self_id 0 --task_id abc --mode test --test_id def --from_id 1 --round 1
python run.py save_output --root ./exp --self_id 0 --task_id abc --mode test --test_id def --from_id 1 --round 2
python save_output_exe.py --root ./exp --self_id 0 --task_id abc --mode test --test_id def --from_id 1 --round 1
python save_output_exe.py --root ./exp --self_id 0 --task_id abc --mode test --test_id def --from_id 1 --round 2

# eval
python run.py make_eval --root ./exp --self_id 0 --task_id abc --test_id def --round 2 --dataset_path ./data/BostonHousing_2_123_1.0/0/test/dataset.csv --target_idx 9 --task_mode regression --metric_name MAD_RMSE_R2

echo "$(cat ./exp/0/task/abc/train/log.txt)"
echo "$(cat ./exp/0/task/abc/test/def/log.txt)"