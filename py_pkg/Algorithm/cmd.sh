# make dataset
python make_dataset.py --root ./data --data_name BostonHousing --task_id 123 --num_users 1 --match_rate 1
python make_dataset.py --root ./data --data_name BostonHousing --task_id 123 --num_users 2 --match_rate 1
python make_dataset.py --root ./data --data_name BostonHousing --task_id 123 --num_users 2 --match_rate 0.5

# baseline
python baseline.py --root ./data --data_name BostonHousing --task_id 123 --num_users 1 --match_rate 1
python baseline.py --root ./data --data_name BostonHousing --task_id 123 --num_users 2 --match_rate 1
python baseline.py --root ./data --data_name BostonHousing --task_id 123 --num_users 2 --match_rate 0.5

# local
./dist/run/run make_train_local --root ./exp --self_id 0 --task_id abc --dataset_path ./data/BostonHousing_2_123_1.0/0/train/dataset.csv --data_idx 2-8 --target_idx 9
./dist/run/run make_test_local --root ./exp --self_id 0 --task_id abc --test_id kdg --dataset_path ./data/BostonHousing_2_123_1.0/0/test/dataset.csv --data_idx 2-8 --target_idx 9

# default
# hash id
./dist/run/run make_hash --root ./exp --self_id 0 --mode default --dataset_path ./data/BostonHousing_2_123_1.0/0/all/dataset.csv --id_idx 1
./dist/run/run make_hash --root ./exp --self_id 1 --mode default --dataset_path ./data/BostonHousing_2_123_1.0/1/all/dataset.csv --id_idx 1

# Train
# hash id
./dist/run/run make_hash --root ./exp --self_id 0 --task_id abc --mode train --dataset_path ./data/BostonHousing_2_123_1.0/0/train/dataset.csv --id_idx 1
./dist/run/run make_hash --root ./exp --self_id 1 --task_id abc --mode train --dataset_path ./data/BostonHousing_2_123_1.0/1/train/dataset.csv --id_idx 1

# match id
./dist/run/run save_match_id --root ./exp --self_id 0 --task_id abc --mode train --from_id 1
./dist/run/run save_match_id --root ./exp --self_id 1 --task_id abc --mode train --from_id 0
python save_match_id_exe.py --root ./exp --self_id 0 --task_id abc --mode train --from_id 1
./dist/run/run make_match_idx --root ./exp --self_id 0 --task_id abc --mode train --from_id 1
./dist/run/run make_match_idx --root ./exp --self_id 1 --task_id abc --mode train --from_id 0

# round 0
# make residual
./dist/run/run make_residual --root ./exp --self_id 0 --task_id abc --round 0 --dataset_path ./data/BostonHousing_2_123_1.0/0/train/dataset.csv --target_idx 9
./dist/run/run save_residual --root ./exp --self_id 1 --task_id abc --round 0
python save_residual_exe.py --root ./exp --self_id 1 --task_id abc --from_id 0 --round 0

# train
./dist/run/run make_train --root ./exp --self_id 0 --task_id abc --round 0 --dataset_path ./data/BostonHousing_2_123_1.0/0/train/dataset.csv --data_idx 2-8
./dist/run/run make_train --root ./exp --self_id 1 --task_id abc --round 0 --from_id 0 --dataset_path ./data/BostonHousing_2_123_1.0/1/train/dataset.csv --data_idx 2-7

# output
./dist/run/run save_output --root ./exp --self_id 0 --task_id abc --mode train --from_id 1 --round 0
python save_output_exe.py --root ./exp --self_id 0 --task_id abc --mode train --from_id 1 --round 0
./dist/run/run make_result --root ./exp --self_id 0 --task_id abc --round 0 --dataset_path ./data/BostonHousing_2_123_1.0/0/train/dataset.csv --target_idx 9

# round 1
# make residual
./dist/run/run make_residual --root ./exp --self_id 0 --task_id abc --round 1 --dataset_path ./data/BostonHousing_2_123_1.0/0/train/dataset.csv --target_idx 9
./dist/run/run save_residual --root ./exp --self_id 1 --task_id abc --round 1
python save_residual_exe.py --root ./exp --self_id 1 --task_id abc --from_id 0 --round 1

# train
./dist/run/run make_train --root ./exp --self_id 0 --task_id abc --round 1 --dataset_path ./data/BostonHousing_2_123_1.0/0/train/dataset.csv --data_idx 2-8
./dist/run/run make_train --root ./exp --self_id 1 --task_id abc --round 1 --from_id 0 --dataset_path ./data/BostonHousing_2_123_1.0/1/train/dataset.csv --data_idx 2-7

# output
./dist/run/run save_output --root ./exp --self_id 0 --task_id abc --mode train --from_id 1 --round 1
python save_output_exe.py --root ./exp --self_id 0 --task_id abc --mode train --from_id 1 --round 1
./dist/run/run make_result --root ./exp --self_id 0 --task_id abc --round 1 --dataset_path ./data/BostonHousing_2_123_1.0/0/train/dataset.csv --target_idx 9

# Test
# hash id
./dist/run/run make_hash --root ./exp --self_id 0 --task_id abc --mode test --test_id def --dataset_path ./data/BostonHousing_2_123_1.0/0/test/dataset.csv --id_idx 1
./dist/run/run make_hash --root ./exp --self_id 1 --task_id abc --mode test --test_id def --dataset_path ./data/BostonHousing_2_123_1.0/1/test/dataset.csv --id_idx 1

# match id 
./dist/run/run save_match_id --root ./exp --self_id 0 --task_id abc --from_id 1 --mode test --test_id def
./dist/run/run save_match_id --root ./exp --self_id 1 --task_id abc --from_id 0 --mode test --test_id def
python save_match_id_exe.py --root ./exp --self_id 0 --task_id abc --from_id 1 --mode test --test_id def
./dist/run/run make_match_idx --root ./exp --self_id 0 --task_id abc --from_id 1 --mode test --test_id def
./dist/run/run make_match_idx --root ./exp --self_id 1 --task_id abc --from_id 0 --mode test --test_id def

# test
./dist/run/run make_test --root ./exp --self_id 0 --task_id abc --test_id def --round 1 --dataset_path ./data/BostonHousing_2_123_1.0/0/test/dataset.csv --data_idx 2-8
./dist/run/run make_test --root ./exp --self_id 1 --task_id abc --test_id def --round 1 --from_id 0 --dataset_path ./data/BostonHousing_2_123_1.0/1/test/dataset.csv --data_idx 2-7

# output
./dist/run/run save_output --root ./exp --self_id 0 --task_id abc --mode test --test_id def --from_id 1 --round 0
./dist/run/run save_output --root ./exp --self_id 0 --task_id abc --mode test --test_id def --from_id 1 --round 1
python save_output_exe.py --root ./exp --self_id 0 --task_id abc --mode test --test_id def --from_id 1 --round 0
python save_output_exe.py --root ./exp --self_id 0 --task_id abc --mode test --test_id def --from_id 1 --round 1

# eval
./dist/run/run make_eval --root ./exp --self_id 0 --task_id abc --test_id def --round 1 --dataset_path ./data/BostonHousing_2_123_1.0/0/test/dataset.csv --target_idx 9

echo "$(cat ./exp/0/task/abc/train/log.txt)"
echo "$(cat ./exp/0/task/abc/test/def/log.txt)"