# make dataset (dont need task_id)
python3 make_dataset.py --root ./data --task_id 123 --num_users 1 --match_rate 1
python3 make_dataset.py --root ./data --task_id 123 --num_users 2 --match_rate 1
python3 make_dataset.py --root ./data --task_id 123 --num_users 2 --match_rate 0.5

# baseline
python3 baseline.py --root ./data --task_id 123 --num_users 1 --match_rate 1
python3 baseline.py --root ./data --task_id 123 --num_users 2 --match_rate 1
python3 baseline.py --root ./data --task_id 123 --num_users 2 --match_rate 0.5

# default
# hash id
python3 hash_id.py --id_path ./data/BostonHousing/2/123/1.0/0/all/id.csv --root ./exp --self_id 0 --run default
python3 hash_id.py --id_path ./data/BostonHousing/2/123/1.0/1/all/id.csv --root ./exp --self_id 1 --run default

# Train
# hash id
python3 hash_id.py --id_path ./data/BostonHousing/2/123/1.0/0/train/id.csv --root ./exp --self_id 0 --task_id abc --run train
python3 hash_id.py --id_path ./data/BostonHousing/2/123/1.0/1/train/id.csv --root ./exp --self_id 1 --task_id abc --run train

# match id
python3 save_match_id.py --root ./exp --self_id 0 --task_id abc --run train --from_id 1
python3 save_match_id.py --root ./exp --self_id 1 --task_id abc --run train --from_id 0
python3 save_match_id_exe.py --root ./exp --self_id 0 --task_id abc --run train --from_id 1
python3 make_match_idx.py --root ./exp --self_id 0 --task_id abc --run train --from_id 1
python3 make_match_idx.py --root ./exp --self_id 1 --task_id abc --run train --from_id 0

# round 0
# make residual
python3 make_residual.py --root ./exp --self_id 0 --task_id abc --round 0 --target_path ./data/BostonHousing/2/123/1.0/0/train/target.csv
python3 save_residual.py --root ./exp --self_id 1 --task_id abc --from_id 0 --round 0
python3 save_residual_exe.py --root ./exp --self_id 1 --task_id abc --from_id 0 --round 0

# train
python3 train.py --root ./exp --self_id 0 --task_id abc --round 0 --data_path ./data/BostonHousing/2/123/1.0/0/train/data.csv
python3 train.py --root ./exp --self_id 1 --task_id abc --round 0 --from_id 0 --data_path ./data/BostonHousing/2/123/1.0/1/train/data.csv

# output
python3 save_output.py --root ./exp --self_id 0 --task_id abc --run train --from_id 1 --round 0
python3 save_output_exe.py --root ./exp --self_id 0 --task_id abc --run train --from_id 1 --round 0
python3 make_result.py --root ./exp --self_id 0 --task_id abc --round 0 --target_path ./data/BostonHousing/2/123/1.0/0/train/target.csv

# round 1
# make residual
python3 make_residual.py --root ./exp --self_id 0 --task_id abc --round 1 --target_path ./data/BostonHousing/2/123/1.0/0/train/target.csv
python3 save_residual.py --root ./exp --self_id 1 --task_id abc --from_id 0 --round 1
python3 save_residual_exe.py --root ./exp --self_id 1 --task_id abc --from_id 0 --round 1

# train
python3 train.py --root ./exp --self_id 0 --task_id abc --round 1 --data_path ./data/BostonHousing/2/123/1.0/0/train/data.csv
python3 train.py --root ./exp --self_id 1 --task_id abc --round 1 --from_id 0 --data_path ./data/BostonHousing/2/123/1.0/1/train/data.csv

# output
python3 save_output.py --root ./exp --self_id 0 --task_id abc --run train --from_id 1 --round 1
python3 save_output_exe.py --root ./exp --self_id 0 --task_id abc --run train --from_id 1 --round 1
python3 make_result.py --root ./exp --self_id 0 --task_id abc --round 1 --target_path ./data/BostonHousing/2/123/1.0/0/train/target.csv

# Test
# hash id
python3 hash_id.py --id_path ./data/BostonHousing/2/123/1.0/0/test/id.csv --root ./exp --self_id 0 --task_id abc --run test --test_id def
python3 hash_id.py --id_path ./data/BostonHousing/2/123/1.0/1/test/id.csv --root ./exp --self_id 1 --task_id abc --run test --test_id def

# match id 
python3 save_match_id.py --root ./exp --self_id 0 --task_id abc --from_id 1 --run test --test_id def
python3 save_match_id.py --root ./exp --self_id 1 --task_id abc --from_id 0 --run test --test_id def
python3 save_match_id_exe.py --root ./exp --self_id 0 --task_id abc --from_id 1 --run test --test_id def
python3 make_match_idx.py --root ./exp --self_id 0 --task_id abc --from_id 1 --run test --test_id def
python3 make_match_idx.py --root ./exp --self_id 1 --task_id abc --from_id 0 --run test --test_id def

# test (round number is max_round?)
python3 test.py --root ./exp --self_id 0 --task_id abc --test_id def --round 1 --data_path ./data/BostonHousing/2/123/1.0/0/test/data.csv
python3 test.py --root ./exp --self_id 1 --task_id abc --test_id def --round 1 --from_id 0 --data_path ./data/BostonHousing/2/123/1.0/1/test/data.csv

# output (each output calls one time?)
python3 save_output.py --root ./exp --self_id 0 --task_id abc --run test --test_id def --from_id 1 --round 0
python3 save_output.py --root ./exp --self_id 0 --task_id abc --run test --test_id def --from_id 1 --round 1
python3 save_output_exe.py --root ./exp --self_id 0 --task_id abc --run test --test_id def --from_id 1 --round 0
python3 save_output_exe.py --root ./exp --self_id 0 --task_id abc --run test --test_id def --from_id 1 --round 1

# eval
python3 eval.py --root ./exp --self_id 0 --task_id abc --test_id def --round 1 --target_path ./data/BostonHousing/2/123/1.0/0/test/target.csv

echo "$(cat ./exp/0/task/abc/train/log.txt)"
echo "$(cat ./exp/0/task/abc/test/def/log.txt)"