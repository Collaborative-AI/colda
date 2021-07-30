Log: utils.log
'?' for multiple outputs
user_id, default(assistor): (data, id)
sponsor: train (data, id, target), test (data , id)

Train:
1. Unread Match id:
  1. Save received Match id (Both):
    1. python save_match_id.py --self_id 1 --task_id 123 --from_id 2 --run train (return file location)
    2. write user_id_to_assistor_random_id.csv to above location
    3. python make_match_idx.py --self_id 1 --task_id 123 --from_id 2 --run train (change id to index, return None)

  2. Make Residual (Sponsor):
    1. python make_residual.py --self_id 1 --task_id 123 --round 0 --target_path xxx(return file location, multiple outputs)

2. Unread Situation:
  1. python save_residual.py --self_id 1 --task_id 123 --from_id 2 --round 0 (return file location, single output, Assistor)
  2. python train.py --self_id 2 --task_id 123 --from_id 1 --round 0 --data_path xxx (return file location, single output, Both, no from_id if Sponsor)

3. Unread Output (Sponsor):
  1. python save_output.py --self_id 1 --task_id 123 --from_id 2 --run train --round 0 (return file location)
  2. write user_id_to_assistor_random_id.csv to above location (single output)
  3. python make_result.py --self_id 1 --task_id 123 --round 1 --target_path xxx (return None)

Test:
1. Unread Test Match id:
  1. Save Test received Match id (Both):
    1. python save_match_id.py --self_id 1 --task_id 123 --from_id 2 --run test --test_id 123 (return file location)
    2. write user_id_to_assistor_random_id.csv to above location
    3. python make_match_idx.py --self_id 1 --task_id 123 --from_id 2 --run test --test_id 123 (change id to index, return None)

  2. Test (Both):
    1. python test.py --self_id 1 --task_id 123 --from_id 2 --test_id 123 --round 2 --data_path xxx (return file location, multiple outputs)

2. Unread Test Output (Sponsor):
  1. python save_match_id.py --self_id 1 --task_id 123 --from_id 2 --run test --test_id 123 (return file location)
  2. write user_id_to_assistor_random_id.csv to above location
  3. python eval.py --self_id 1 --task_id 123 --test_id 123 --round 2 --target_path (one file location per round, target_path for evaluation)

