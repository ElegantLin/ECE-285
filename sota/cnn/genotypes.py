from collections import namedtuple

Genotype = namedtuple('Genotype', 'normal normal_concat reduce reduce_concat')

PRIMITIVES = [
    'none',
    'noise',
    'max_pool_3x3',
    'avg_pool_3x3',
    'skip_connect',
    'sep_conv_3x3',
    'sep_conv_5x5',
    'dil_conv_3x3',
    'dil_conv_5x5'
]
DARTS_V2 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('skip_connect', 0), ('skip_connect', 0), ('dil_conv_3x3', 2)], normal_concat=[2, 3, 4, 5], reduce=[('max_pool_3x3', 0), ('max_pool_3x3', 1), ('skip_connect', 2), ('max_pool_3x3', 1), ('max_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 2), ('max_pool_3x3', 1)], reduce_concat=[2, 3, 4, 5])



# PixelDARTS = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('dil_conv_5x5', 2), ('sep_conv_3x3', 2), ('sep_conv_5x5', 0), ('dil_conv_3x3', 2), ('max_pool_3x3', 1)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_3x3', 0), ('sep_conv_5x5', 2), ('sep_conv_5x5', 0), ('dil_conv_5x5', 3), ('dil_conv_5x5', 2), ('sep_conv_5x5', 3)], reduce_concat=range(2, 6))

# PixelDARTS = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('dil_conv_3x3', 0), ('max_pool_3x3', 1), ('dil_conv_3x3', 0), ('dil_conv_3x3', 0), ('sep_conv_5x5', 1)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 0), ('max_pool_3x3', 1), ('max_pool_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_5x5', 3), ('dil_conv_5x5', 2), ('avg_pool_3x3', 0), ('sep_conv_5x5', 2)], reduce_concat=range(2, 6))

# PixelDARTS = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_5x5', 1), ('skip_connect', 0), ('sep_conv_3x3', 2), ('dil_conv_5x5', 2), ('sep_conv_5x5', 3), ('sep_conv_3x3', 2), ('dil_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('skip_connect', 0), ('sep_conv_5x5', 2), ('dil_conv_3x3', 1), ('skip_connect', 2), ('dil_conv_3x3', 1), ('sep_conv_3x3', 2)], reduce_concat=range(2, 6))



##########################################################################
# cifar10_darts:
c10_darts = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('skip_connect', 2), ('skip_connect', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('dil_conv_5x5', 2), ('sep_conv_5x5', 0)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 2), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_5x5', 2), ('sep_conv_3x3', 1), ('sep_conv_3x3', 3)], reduce_concat=range(2, 6))

# cifar100_darts:
c100_darts = Genotype(
  normal=[
    ('sep_conv_3x3', 0), 
    ('dil_conv_3x3', 1), 
    ('skip_connect', 0), 
    ('sep_conv_3x3', 1), 
    ('skip_connect', 0), 
    ('skip_connect', 2), 
    ('sep_conv_5x5', 0), 
    ('dil_conv_3x3', 3)
    ], 
  normal_concat = [2, 3, 4, 5], 
  reduce=[
    ('dil_conv_5x5', 1), 
    ('sep_conv_5x5', 0), 
    ('sep_conv_3x3', 2), 
    ('sep_conv_3x3', 1), 
    ('sep_conv_3x3', 2), 
    ('sep_conv_3x3', 0), 
    ('dil_conv_3x3', 1), 
    ('sep_conv_5x5', 2)
    ], 
  reduce_concat = [2, 3, 4, 5]
  )




c100_darts2 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('dil_conv_3x3', 0), ('max_pool_3x3', 1), ('dil_conv_3x3', 0), ('dil_conv_3x3', 0), ('sep_conv_5x5', 1)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 0), ('max_pool_3x3', 1), ('max_pool_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_5x5', 3), ('dil_conv_5x5', 2), ('avg_pool_3x3', 0), ('sep_conv_5x5', 2)], reduce_concat=range(2, 6))

# # train:
PixelDARTS = Genotype(normal=[('skip_connect', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('dil_conv_3x3', 2), ('sep_conv_3x3', 0), ('skip_connect', 1), ('skip_connect', 0), ('dil_conv_3x3', 4)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('max_pool_3x3', 1), ('skip_connect', 0), ('max_pool_3x3', 1), ('max_pool_3x3', 0), ('dil_conv_5x5', 3), ('max_pool_3x3', 1), ('sep_conv_5x5', 4)], reduce_concat=range(2, 6))

# c10_s3_pcdarts = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_3x3', 1), ('sep_conv_3x3', 3), ('sep_conv_3x3', 2), ('skip_connect', 4), ('sep_conv_3x3', 2)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_3x3', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 0), ('sep_conv_3x3', 4)], reduce_concat=range(2, 6))

# c10_s3_pgd = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('skip_connect', 0)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 3)], reduce_concat=range(2, 6))

# # c10_s5_pgd = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('skip_connect', 0), ('sep_conv_5x5', 0), ('dil_conv_3x3', 3), ('dil_conv_3x3', 4), ('skip_connect', 0)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('skip_connect', 2), ('max_pool_3x3', 0), ('skip_connect', 3), ('skip_connect', 2), ('skip_connect', 2), ('sep_conv_5x5', 4)], reduce_concat=range(2, 6))

#PixelDARTS = c100_darts2

c10_20_layers_s1_darts = Genotype(normal=[('dil_conv_5x5', 1), ('dil_conv_3x3', 0), ('dil_conv_3x3', 2), ('dil_conv_5x5', 0), ('skip_connect', 0), ('skip_connect', 1), ('dil_conv_3x3', 2), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 1), ('max_pool_3x3', 0), ('avg_pool_3x3', 1), ('dil_conv_5x5', 2), ('dil_conv_3x3', 2), ('max_pool_3x3', 1), ('dil_conv_5x5', 4), ('dil_conv_5x5', 2)], reduce_concat=range(2, 6))

c10_20_layers_s2_darts = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('skip_connect', 2), ('skip_connect', 0)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('skip_connect', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 3)], reduce_concat=range(2, 6))

c10_20_layers_s3_darts = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 1), ('skip_connect', 0)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('skip_connect', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 3), ('sep_conv_3x3', 4)], reduce_concat=range(2, 6))

c10_20_layers_s4_darts = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('noise', 0), ('sep_conv_3x3', 1), ('noise', 2), ('noise', 0), ('noise', 3), ('noise', 0)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('noise', 2), ('sep_conv_3x3', 2), ('sep_conv_3x3', 0), ('sep_conv_3x3', 4), ('noise', 1)], reduce_concat=range(2, 6))

c10_20_layers_s5_darts = Genotype(normal=[('dil_conv_5x5', 1), ('avg_pool_3x3', 0), ('dil_conv_5x5', 2), ('skip_connect', 0), ('dil_conv_5x5', 1), ('sep_conv_3x3', 2), ('sep_conv_5x5', 2), ('sep_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('avg_pool_3x3', 1), ('skip_connect', 2), ('dil_conv_5x5', 0), ('skip_connect', 3), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))

c100_20_layers_s1_darts = Genotype(normal=[('dil_conv_5x5', 1), ('skip_connect', 0), ('skip_connect', 2), ('skip_connect', 0), ('skip_connect', 0), ('skip_connect', 3), ('dil_conv_5x5', 4), ('skip_connect', 0)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('max_pool_3x3', 1), ('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('max_pool_3x3', 1), ('max_pool_3x3', 0), ('dil_conv_5x5', 2), ('skip_connect', 4)], reduce_concat=range(2, 6))

c100_20_layers_s2_darts = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 1), ('sep_conv_3x3', 4), ('sep_conv_3x3', 2)], normal_concat=range(2, 6), reduce=[('skip_connect', 1), ('sep_conv_3x3', 0), ('skip_connect', 1), ('skip_connect', 0), ('skip_connect', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 2), ('skip_connect', 1)], reduce_concat=range(2, 6))

c100_20_layers_s3_darts = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('skip_connect', 1), ('sep_conv_3x3', 2), ('skip_connect', 3), ('sep_conv_3x3', 2)], normal_concat=range(2, 6), reduce=[('skip_connect', 0), ('skip_connect', 1), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 0), ('skip_connect', 1), ('skip_connect', 0), ('skip_connect', 2)], reduce_concat=range(2, 6))

c100_20_layers_s4_darts = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('noise', 0), ('noise', 3), ('noise', 3), ('noise', 0)], normal_concat=range(2, 6), reduce=[('noise', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('noise', 2), ('sep_conv_3x3', 1), ('sep_conv_3x3', 3), ('noise', 3), ('sep_conv_3x3', 1)], reduce_concat=range(2, 6))

c100_20_layers_s5_darts = Genotype(normal=[('dil_conv_3x3', 0), ('skip_connect', 1), ('skip_connect', 2), ('skip_connect', 1), ('dil_conv_5x5', 2), ('dil_conv_3x3', 0), ('dil_conv_5x5', 3), ('sep_conv_3x3', 0)], normal_concat=range(2, 6), reduce=[('dil_conv_3x3', 1), ('skip_connect', 0), ('sep_conv_3x3', 0), ('dil_conv_5x5', 1), ('sep_conv_5x5', 2), ('dil_conv_5x5', 1), ('skip_connect', 4), ('sep_conv_5x5', 2)], reduce_concat=range(2, 6))

c10_s1_pcdarts = Genotype(normal=[('dil_conv_3x3', 0), ('skip_connect', 1), ('dil_conv_5x5', 0), ('skip_connect', 2), ('sep_conv_3x3', 1), ('dil_conv_3x3', 3), ('skip_connect', 1), ('dil_conv_5x5', 3)], normal_concat=range(2, 6), reduce=[('avg_pool_3x3', 0), ('max_pool_3x3', 1), ('avg_pool_3x3', 0), ('dil_conv_5x5', 2), ('max_pool_3x3', 1), ('avg_pool_3x3', 0), ('max_pool_3x3', 1), ('dil_conv_5x5', 4)], reduce_concat=range(2, 6))

c10_s2_pcdarts = Genotype(normal=[('skip_connect', 1), ('skip_connect', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 3), ('skip_connect', 1), ('skip_connect', 4), ('skip_connect', 2)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('skip_connect', 1), ('skip_connect', 0), ('sep_conv_3x3', 2), ('skip_connect', 0), ('skip_connect', 1), ('sep_conv_3x3', 0), ('skip_connect', 3)], reduce_concat=range(2, 6))

c10_s3_pcdarts = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 2), ('skip_connect', 2), ('skip_connect', 3), ('skip_connect', 4), ('sep_conv_3x3', 2)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('skip_connect', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 2), ('skip_connect', 4)], reduce_concat=range(2, 6))

c10_s4_pcdarts = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('noise', 0), ('noise', 1), ('noise', 0), ('noise', 3), ('noise', 0), ('noise', 3)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('noise', 1), ('noise', 1), ('noise', 0), ('noise', 2), ('noise', 3), ('sep_conv_3x3', 0), ('sep_conv_3x3', 4)], reduce_concat=range(2, 6))

c10_s5_pcdarts = Genotype(normal=[('dil_conv_5x5', 1), ('sep_conv_5x5', 0), ('sep_conv_5x5', 2), ('dil_conv_5x5', 0), ('dil_conv_5x5', 2), ('dil_conv_5x5', 0), ('dil_conv_3x3', 0), ('skip_connect', 4)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 1), ('dil_conv_3x3', 0), ('dil_conv_3x3', 0), ('avg_pool_3x3', 1), ('skip_connect', 3), ('max_pool_3x3', 1), ('avg_pool_3x3', 1), ('dil_conv_5x5', 3)], reduce_concat=range(2, 6))

c100_s1_pcdarts = Genotype(normal=[('skip_connect', 1), ('dil_conv_3x3', 0), ('skip_connect', 1), ('dil_conv_3x3', 2), ('skip_connect', 1), ('skip_connect', 0), ('sep_conv_3x3', 0), ('dil_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('max_pool_3x3', 0), ('dil_conv_3x3', 1), ('avg_pool_3x3', 1), ('avg_pool_3x3', 0), ('skip_connect', 2), ('avg_pool_3x3', 0), ('max_pool_3x3', 1), ('max_pool_3x3', 0)], reduce_concat=range(2, 6))

c100_s2_pcdarts = Genotype(normal=[('skip_connect', 0), ('skip_connect', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 0), ('skip_connect', 1), ('sep_conv_3x3', 3), ('sep_conv_3x3', 4), ('sep_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 2), ('sep_conv_3x3', 3), ('skip_connect', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 4)], reduce_concat=range(2, 6))

c100_s3_pcdarts = Genotype(normal=[('skip_connect', 1), ('sep_conv_3x3', 0), ('skip_connect', 1), ('sep_conv_3x3', 0), ('skip_connect', 1), ('sep_conv_3x3', 0), ('skip_connect', 1), ('sep_conv_3x3', 3)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 0), ('sep_conv_3x3', 2), ('skip_connect', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 3), ('sep_conv_3x3', 4)], reduce_concat=range(2, 6))

c100_s4_pcdarts = Genotype(normal=[('sep_conv_3x3', 0), ('noise', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 0), ('noise', 0), ('noise', 2)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 2), ('noise', 0), ('noise', 1), ('sep_conv_3x3', 0)], reduce_concat=range(2, 6))

c100_s5_pcdarts = Genotype(normal=[('sep_conv_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 1), ('skip_connect', 0), ('dil_conv_5x5', 3), ('skip_connect', 4), ('sep_conv_5x5', 2)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 0), ('skip_connect', 1), ('sep_conv_3x3', 2), ('skip_connect', 1), ('skip_connect', 3), ('skip_connect', 2), ('skip_connect', 2), ('skip_connect', 3)], reduce_concat=range(2, 6))
