exp_config = {
    'env': {
        'manager': {
            'episode_num': float("inf"),
            'max_retry': 1,
            'retry_type': 'reset',
            'auto_reset': True,
            'step_timeout': None,
            'reset_timeout': None,
            'retry_waiting_time': 0.1,
            'cfg_type': 'BaseEnvManagerDict',
            'type': 'base'
        },
        'stop_value': 195,
        'type': 'cartpole',
        'import_names': ['dizoo.classic_control.cartpole.envs.cartpole_env'],
        'collector_env_num': 8,
        'evaluator_env_num': 5,
        'n_evaluator_episode': 5
    },
    'policy': {
        'model': {
            'v_min': -10,
            'v_max': 10,
            'n_atom': 51,
            'obs_shape': 4,
            'action_shape': 2,
            'encoder_hidden_size_list': [128, 128, 64]
        },
        'learn': {
            'learner': {
                'train_iterations': 1000000000,
                'dataloader': {
                    'num_workers': 0
                },
                'log_policy': True,
                'hook': {
                    'load_ckpt_before_run': '',
                    'log_show_after_iter': 100,
                    'save_ckpt_after_iter': 10000,
                    'save_ckpt_after_run': True
                },
                'cfg_type': 'BaseLearnerDict'
            },
            'multi_gpu': False,
            'update_per_collect': 3,
            'batch_size': 64,
            'learning_rate': 0.001,
            'target_update_freq': 100,
            'ignore_done': False
        },
        'collect': {
            'collector': {
                'deepcopy_obs': False,
                'transform_obs': False,
                'collect_print_freq': 100,
                'cfg_type': 'SampleSerialCollectorDict',
                'type': 'sample'
            },
            'unroll_len': 1,
            'n_sample': 80
        },
        'eval': {
            'evaluator': {
                'eval_freq': 1000,
                'render': {
                    'render_freq': -1,
                    'mode': 'train_iter'
                },
                'cfg_type': 'InteractionSerialEvaluatorDict',
                'n_episode': 5,
                'stop_value': 195
            }
        },
        'other': {
            'replay_buffer': {
                'type': 'advanced',
                'replay_buffer_size': 20000,
                'max_use': float("inf"),
                'max_staleness': float("inf"),
                'alpha': 0.6,
                'beta': 0.4,
                'anneal_step': 100000,
                'enable_track_used_data': False,
                'deepcopy': False,
                'thruput_controller': {
                    'push_sample_rate_limit': {
                        'max': float("inf"),
                        'min': 0
                    },
                    'window_seconds': 30,
                    'sample_min_limit_ratio': 1
                },
                'monitor': {
                    'sampled_data_attr': {
                        'average_range': 5,
                        'print_freq': 200
                    },
                    'periodic_thruput': {
                        'seconds': 60
                    }
                },
                'cfg_type': 'AdvancedReplayBufferDict'
            },
            'eps': {
                'type': 'exp',
                'start': 0.95,
                'end': 0.1,
                'decay': 10000
            },
            'commander': {
                'cfg_type': 'BaseSerialCommanderDict'
            }
        },
        'type': 'c51',
        'cuda': False,
        'on_policy': False,
        'priority': True,
        'discount_factor': 0.97,
        'nstep': 3,
        'cfg_type': 'C51PolicyDict'
    },
    'exp_name': 'cartpole_c51_deploy',
    'seed': 0
}
