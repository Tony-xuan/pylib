#coding=utf-8
from common_import import *
from model import AlexNet

from nnet.solver import MomentumGradientDescentSolver
dump_path = '~/temp/results/MomentumGradientDescentSolverTest'
util.log.init_logger(util.io.join_path(dump_path,'momentum_alexnet.log'));

batch_size = 100
image_shape = (224, 224)
train_iter, val_iter = get_iter(image_shape = image_shape, batch_size = batch_size, prefetch = 5, num_threads = 8)

net = AlexNet('MomentumGradientDescentSolver')
solver = MomentumGradientDescentSolver(
        #epochs = 0.01,
        momentum = 0.9,
        decay = 0.0005,
        total_iterations = 2000,
        learning_rate = 0.0001,
        dump_path = dump_path,
        dump_interval = 2000,
 #       val_interval = 5000, 
        train_iter = train_iter, 
        val_iter = None
        )
solver.fit(model = net)
