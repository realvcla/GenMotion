class TrainingConfig():
    def __init__(self) -> None:
        self.arbitrary_len = False 
        self.batch_size = 100 
        self.checkpoints_dir = "./checkpoints/vae"
        self.clip_set = "./dataset/pose_clip_full.csv"
        self.coarse_grained = False 
        self.dataset_type = None 
        self.decoder_hidden_layers = 2 
        self.dim_z = 30 
        self.eval_every = 500 
        self.gpu_id = 0 
        self.hidden_size = 128 
        self.isTrain = True 
        self.is_continue = False 
        self.iters = 20 
        self.lambda_align = 0.5 
        self.lambda_kld = 0.0001 
        self.lambda_trajec = 0.8 
        self.lie_enforce = False 
        self.motion_length = 60 
        self.name = "test" 
        self.no_trajectory = False 
        self.plot_every = 500 
        self.posterior_hidden_layers = 1 
        self.print_every = 50 
        self.prior_hidden_layers = 1 
        self.save_every = 500 
        self.save_latest = 500 
        self.skip_prob = 0 
        self.tf_ratio = 0.6 
        self.time_counter = False 
        self.use_geo_loss = False 
        self.use_lie = False

        self.name = "act2motion"
        self.dataset_type = "humanact12"
        self.batch_size = 8 
        self.motion_length = 60 
        self.coarse_grained = True 
        self.lambda_kld = 0.001 
        self.eval_every = 2000 
        self.plot_every = 50 
        self.print_every = 20 
        self.save_every = 2000 
        self.save_latest = 50 
        self.time_counter = True 
        self.use_lie = True 
        self.gpu_id = 0 
        self.iters = 50000