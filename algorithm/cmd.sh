# prepare dataset (full)
python make_dataset.py --num_users 2 --match_rate 1
# prepare dataset (half)
python make_dataset.py --num_users 2 --match_rate 0.5

# train
# match id
python match_id.py --task_id 123 --run train
# round 0
# make residual (sponsor)
python make_residual.py --task_id 123 --round 0
# distribute to assistors (sponsor)
python distribute.py --task_id 123 --round 0
# train two clients round 1 （sponsor and assistors)
python train.py --client_id 0 --task_id 123 --round 0
python train.py --client_id 1 --task_id 123 --round 0
# gather output from assistors (sponsor)
python gather.py --task_id 123 --round 0 --run train
# make result for round 0 (sponsor)
python make_result.py --task_id 123 --round 0

# round 1
# make residual (sponsor)
python make_residual.py --task_id 123 --round 1
# distribute to assistors (sponsor)
python distribute.py --task_id 123 --round 1
# train two clients round 2 （sponsor and assistors)
python train.py --client_id 0 --task_id 123 --round 1
python train.py --client_id 1 --task_id 123 --round 1
# gather output from assistors (sponsor)
python gather.py --task_id 123 --round 1 --run train
# make result for round 1 (sponsor)
python make_result.py --task_id 123 --round 1

# test
# match id
python match_id.py --task_id 123 --run test
# test sponsor and assistors
python test.py --client_id 0 --task_id 123 --round 0
python test.py --client_id 0 --task_id 123 --round 1
python test.py --client_id 1 --task_id 123 --round 0
python test.py --client_id 1 --task_id 123 --round 1
# gather output from assistors (sponsor)
python gather.py --task_id 123 --round 0 --run test
python gather.py --task_id 123 --round 1 --run test
# evaluation (sponsor)
python eval.py --task_id 123 --round -1
python eval.py --task_id 123 --round 0
python eval.py --task_id 123 --round 1

# baseline
python baseline.py --client_id oracle
python baseline.py --client_id 0
python baseline.py --client_id 1