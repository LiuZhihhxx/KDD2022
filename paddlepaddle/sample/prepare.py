# -*-Encoding: utf-8 -*-
################################################################################
#
# Copyright (c) 2022 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
Description: Prepare the experimental settings
"""
import paddle
import os


def prep_env():
    # type: () -> dict
    """
    Desc:
        Prepare the experimental settings
    Returns:
        The initialized arguments
    """
    settings = {
        "path_to_test_x": "./data/sdwpf_baidukddcup2022_test_toy/test_x",
        "path_to_test_y": "./data/sdwpf_baidukddcup2022_test_toy/test_y",
        "data_path": "./data",
        "filename": "wtdata_245days_knned.CSV",  # wtdata_245days_knned.CSV   sdwpf_baidukddcup2022_full.csv
        "task": "MS",
        "target": "Patv",
        "checkpoints": "checkpoints",
        "input_len": 144,
        "output_len": 288,
        "start_col": 3,
        "in_var": 10,
        "out_var": 1,
        "day_len": 144,
        "train_size": 200,
        "val_size": 45,
        "total_size": 245,
        "lstm_layer": 2,  # 2
        "dropout": 0.05,  # 0.05
        "num_workers": 5,
        "train_epochs": 1,  # 8
        "batch_size": 128,  # 64
        "patience": 3,
        "lr": 1e-4,# baseline 1e-4
        "lr_adjust": "type1",
        "gpu": 0,
        "turbs": [120, 106],# 73, 16, 29, 62
        "capacity": 134,
        "turbine_id": 0,
        "pred_file": "predict.py",
        "framework": "paddlepaddle",
        "is_debug": False
    }
    ###
    # Prepare the GPUs
    if paddle.device.is_compiled_with_cuda():
        settings["use_gpu"] = True
        paddle.device.set_device('gpu:{}'.format(settings["gpu"]))
    else:
        settings["use_gpu"] = False
        paddle.device.set_device('cpu')

    print("The experimental settings are: \n{}".format(str(settings)))
    return settings


def prep_env_search(bs=32, lr=1e-3, layers=2, in_len=144):
    # type: () -> dict
    """
    Desc:
        Prepare the experimental settings
    Returns:
        The initialized arguments
    """
    settings = {
        "path_to_test_x": "./data/sdwpf_baidukddcup2022_test_toy/test_x",
        "path_to_test_y": "./data/sdwpf_baidukddcup2022_test_toy/test_y",
        "data_path": os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]+'\\data\\',#"./data",
        "filename": "wtdata_245days_knned.CSV",  # wtdata_245days_knned.CSV   sdwpf_baidukddcup2022_full.csv
        "task": "MS",
        "target": "Patv",
        "checkpoints": "checkpoints",
        "input_len": in_len,
        "output_len": 288,
        "start_col": 3,
        "in_var": 10,
        "out_var": 1,
        "day_len": 144,
        "train_size": 200,
        "val_size": 45,
        "total_size": 245,
        "lstm_layer": layers,  # 2
        "dropout": 0.05,  # 0.05
        "num_workers": 5,
        "train_epochs": 8,  # 8
        "batch_size": bs,  # 64
        "patience": 3,
        "lr": lr,# baseline 1e-4
        "lr_adjust": "type1",
        "gpu": 0,
        "turbs": [121, 107, 74, 17, 30, 63],
        "capacity": 134,
        "turbine_id": 0,
        "pred_file": "predict.py",
        "framework": "paddlepaddle",
        "is_debug": False
    }
    ###
    # Prepare the GPUs
    if paddle.device.is_compiled_with_cuda():
        settings["use_gpu"] = True
        paddle.device.set_device('gpu:{}'.format(settings["gpu"]))
    else:
        settings["use_gpu"] = False
        paddle.device.set_device('cpu')

    print("The experimental settings are: \n{}".format(str(settings)))
    return settings
# print(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])
