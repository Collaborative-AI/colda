# make dataset
python make_dataset.py --root ./data --data_name BostonHousing --task_id 123 --num_users 1 --match_rate 1
python make_dataset.py --root ./data --data_name BostonHousing --task_id 123 --num_users 2 --match_rate 1
python make_dataset.py --root ./data --data_name BostonHousing --task_id 123 --num_users 2 --match_rate 0.5

# baseline
python baseline.py --root ./data --data_name BostonHousing --task_id 123 --num_users 1 --match_rate 1
python baseline.py --root ./data --data_name BostonHousing --task_id 123 --num_users 2 --match_rate 1
python baseline.py --root ./data --data_name BostonHousing --task_id 123 --num_users 2 --match_rate 0.5

# default
# hash id
./dist/run/run.exe make_hash --id_path ./data/BostonHousing/2/123/1.0/0/all/id.csv --root ./exp --self_id 0 --mode default
./dist/run/run.exe make_hash --id_path ./data/BostonHousing/2/123/1.0/1/all/id.csv --root ./exp --self_id 1 --mode default

# Train
# hash id
./dist/run/run.exe make_hash --id_path ./data/BostonHousing/2/123/1.0/0/train/id.csv --root ./exp --self_id 0 --task_id abc --mode train
./dist/run/run.exe make_hash --id_path ./data/BostonHousing/2/123/1.0/1/train/id.csv --root ./exp --self_id 1 --task_id abc --mode train

# match id
./dist/run/run.exe save_match_id --root ./exp --self_id 0 --task_id abc --mode train --from_id 1
./dist/run/run.exe save_match_id --root ./exp --self_id 1 --task_id abc --mode train --from_id 0
python save_match_id_exe.py --root ./exp --self_id 0 --task_id abc --mode train --from_id 1
./dist/run/run.exe  make_match_idx --root ./exp --self_id 0 --task_id abc --mode train --from_id 1
./dist/run/run.exe  make_match_idx --root ./exp --self_id 1 --task_id abc --mode train --from_id 0

# round 0
# make residual
./dist/run/run.exe make_residual --root ./exp --self_id 0 --task_id abc --round 0 --target_path ./data/BostonHousing/2/123/1.0/0/train/target.csv
./dist/run/run.exe save_residual --root ./exp --self_id 1 --task_id abc --round 0
python save_residual_exe.py --root ./exp --self_id 1 --task_id abc --from_id 0 --round 0

# train
./dist/run/run.exe make_train --root ./exp --self_id 0 --task_id abc --round 0 --data_path ./data/BostonHousing/2/123/1.0/0/train/data.csv
./dist/run/run.exe make_train --root ./exp --self_id 1 --task_id abc --round 0 --from_id 0 --data_path ./data/BostonHousing/2/123/1.0/1/train/data.csv

# output
./dist/run/run.exe save_output --root ./exp --self_id 0 --task_id abc --mode train --from_id 1 --round 0
python save_output_exe.py --root ./exp --self_id 0 --task_id abc --mode train --from_id 1 --round 0
./dist/run/run.exe make_result --root ./exp --self_id 0 --task_id abc --round 0 --target_path ./data/BostonHousing/2/123/1.0/0/train/target.csv

# round 1
# make residual
./dist/run/run.exe make_residual --root ./exp --self_id 0 --task_id abc --round 1 --target_path ./data/BostonHousing/2/123/1.0/0/train/target.csv
./dist/run/run.exe save_residual --root ./exp --self_id 1 --task_id abc --round 1
python save_residual_exe.py --root ./exp --self_id 1 --task_id abc --from_id 0 --round 1

# train
./dist/run/run.exe make_train --root ./exp --self_id 0 --task_id abc --round 1 --data_path ./data/BostonHousing/2/123/1.0/0/train/data.csv
./dist/run/run.exe make_train --root ./exp --self_id 1 --task_id abc --round 1 --from_id 0 --data_path ./data/BostonHousing/2/123/1.0/1/train/data.csv

# output
./dist/run/run.exe save_output --root ./exp --self_id 0 --task_id abc --mode train --from_id 1 --round 1
python save_output_exe.py --root ./exp --self_id 0 --task_id abc --mode train --from_id 1 --round 1
./dist/run/run.exe make_result --root ./exp --self_id 0 --task_id abc --round 1 --target_path ./data/BostonHousing/2/123/1.0/0/train/target.csv

# Test
# hash id
./dist/run/run.exe make_hash --id_path ./data/BostonHousing/2/123/1.0/0/test/id.csv --root ./exp --self_id 0 --task_id abc --mode test --test_id def
./dist/run/run.exe make_hash --id_path ./data/BostonHousing/2/123/1.0/1/test/id.csv --root ./exp --self_id 1 --task_id abc --mode test --test_id def

# match id 
./dist/run/run.exe save_match_id --root ./exp --self_id 0 --task_id abc --from_id 1 --mode test --test_id def
./dist/run/run.exe save_match_id --root ./exp --self_id 1 --task_id abc --from_id 0 --mode test --test_id def
python save_match_id_exe.py --root ./exp --self_id 0 --task_id abc --from_id 1 --mode test --test_id def
./dist/run/run.exe make_match_idx --root ./exp --self_id 0 --task_id abc --from_id 1 --mode test --test_id def
./dist/run/run.exe make_match_idx --root ./exp --self_id 1 --task_id abc --from_id 0 --mode test --test_id def

# test
./dist/run/run.exe make_test --root ./exp --self_id 0 --task_id abc --test_id def --round 1 --data_path ./data/BostonHousing/2/123/1.0/0/test/data.csv
./dist/run/run.exe make_test --root ./exp --self_id 1 --task_id abc --test_id def --round 1 --from_id 0 --data_path ./data/BostonHousing/2/123/1.0/1/test/data.csv

# output
./dist/run/run.exe save_output --root ./exp --self_id 0 --task_id abc --mode test --test_id def --from_id 1 --round 0
./dist/run/run.exe save_output --root ./exp --self_id 0 --task_id abc --mode test --test_id def --from_id 1 --round 1
python save_output_exe.py --root ./exp --self_id 0 --task_id abc --mode test --test_id def --from_id 1 --round 0
python save_output_exe.py --root ./exp --self_id 0 --task_id abc --mode test --test_id def --from_id 1 --round 1

# eval
./dist/run/run.exe make_eval --root ./exp --self_id 0 --task_id abc --test_id def --round 1 --target_path ./data/BostonHousing/2/123/1.0/0/test/target.csv

echo "$(cat ./exp/0/task/abc/train/log.txt)"
echo "$(cat ./exp/0/task/abc/test/def/log.txt)"