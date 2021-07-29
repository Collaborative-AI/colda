# prepare dataset (oracle)
python3 make_dataset.py --num_users 2

# round 0
# make residual (sponsor)
python3 make_residual.py --task_id 123 --round 0
# distribute to assistors (sponsor)
python3 distribute.py --task_id 123 --round 0
# train two clients round 1 （sponsor and assistors)
python3 train.py --client_id 0 --task_id 123 --round 0
python3 train.py --client_id 1 --task_id 123 --round 0
# gather output from assistors (sponsor)
python3 gather.py --task_id 123 --round 0 --run train
# make result for round 0 (sponsor)
python3 make_result.py --task_id 123 --round 0

# round 1
# make residual (sponsor)
python3 make_residual.py --task_id 123 --round 1
# distribute to assistors (sponsor)
python3 distribute.py --task_id 123 --round 1
# train two clients round 2 （sponsor and assistors)
python3 train.py --client_id 0 --task_id 123 --round 1
python3 train.py --client_id 1 --task_id 123 --round 1
# gather output from assistors (sponsor)
python3 gather.py --task_id 123 --round 1 --run train
# make result for round 1 (sponsor)
python3 make_result.py --task_id 123 --round 1

# test sponsor and assistors
python3 test.py --client_id 0 --task_id 123 --round 0
python3 test.py --client_id 0 --task_id 123 --round 1
python3 test.py --client_id 1 --task_id 123 --round 0
python3 test.py --client_id 1 --task_id 123 --round 1
# gather output from assistors (sponsor)
python3 gather.py --task_id 123 --round 0 --run test
python3 gather.py --task_id 123 --round 1 --run test
python3 eval.py --task_id 123 --round -1
python3 eval.py --task_id 123 --round 0
python3 eval.py --task_id 123 --round 1

# baseline
python3 baseline.py --client_id oracle
python3 baseline.py --client_id 0
python3 baseline.py --client_id 1


