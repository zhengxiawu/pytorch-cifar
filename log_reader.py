'''
read the result from the log
'''
import os


def get_folder_list(walk_dir):
    folder_list = []
    walk_dir = os.path.abspath(walk_dir)
    method_list = os.listdir(walk_dir)
    print(method_list)
    # for method in method_list:
    #     model_list = os.listdir(os.path.join(walk_dir, method))
    #     if len(method_list) > 0:
    #         for model in model_list:
    #             dataset_list = os.listdir(
    #                 os.path.join(walk_dir, method, model))
    #             for dataset in dataset_list:
    #                 train_name_list = os.listdir(
    #                     os.path.join(walk_dir, method, model, dataset))
    #                 for train_name in train_name_list:
    #                     this_train_folder = os.path.join(
    #                         walk_dir, method, model, dataset, train_name)
    #                     folder_list.append(this_train_folder)
    return folder_list


def read_result(walk_dir):
    folder_list = get_folder_list(walk_dir)
    for this_train_folder in folder_list:
        log_file = os.path.join(this_train_folder, 'logger.log')
        with open(log_file) as f:
            log_lines = f.readlines()
        if 'Final' in log_lines[-1]:
            if 'dali' in this_train_folder.split('/')[-1]:
                print(this_train_folder)
                print(log_lines[-1])


if __name__ == "__main__":
    experiment_path = os.path.abspath('./experiment')
    model_list = os.listdir(experiment_path)
    for model in model_list:
        if not model[0] == '.':
            model_log_path = os.path.join(experiment_path, model, 'logger.log')
            if os.path.isfile(model_log_path):
                with open(model_log_path) as f:
                    log_lines = f.readlines()
                _temp = []
                for line in log_lines:
                    if 'parameter size' in line:
                        print(line)
                    if 'FLOPS' in line:
                        print(line)
                    if 'Current best' in line:
                        _temp.append(line)
                print(_temp[-1])

