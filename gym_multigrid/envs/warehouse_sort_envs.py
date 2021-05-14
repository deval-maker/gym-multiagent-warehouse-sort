from gym_multigrid.envs.warehouse_sort import *


for n_agents in range(1,21):

    v0=f'''
class WarehouseSortEnvN{n_agents}V0(WarehouseSortEnv):
    def __init__(self):
        w = 5
        super().__init__(size=None,
        height=7,
        width=w,
        n_agents={n_agents},
        chute_pos = [[w-1,2], [w-1,4]],
        induct_pos=[[0,3]],
    )


register(
        id=f'MultiGrid-WarehouseSort-n{n_agents}-v0',
        entry_point=f'gym_multigrid.envs:WarehouseSortEnvN{n_agents}V0'
)
    '''
    exec(v0)

    v1=f'''
class WarehouseSortEnvN{n_agents}V1(WarehouseSortEnv):
    def __init__(self):
        w = 8
        h = 8
        super().__init__(size=None,
        height=h,
        width=w,
        n_agents={n_agents},
        chute_pos = [[w-1,2], [w-1,h-3]],
        induct_pos=[[0,2], [0,5]],
    )

register(
        id=f'MultiGrid-WarehouseSort-n{n_agents}-v1',
        entry_point=f'gym_multigrid.envs:WarehouseSortEnvN{n_agents}V1'
    )
    '''

    exec(v1)

    v2=f'''
class WarehouseSortEnvN{n_agents}V2(WarehouseSortEnv):
    def __init__(self):
        w = 9
        h = 9
        super().__init__(size=None,
        height=h,
        width=w,
        n_agents={n_agents},
        chute_pos = [[w-1,4], [0,4]],
        induct_pos=[[4,0], [4,h-1]],
    )

register(
    id=f'MultiGrid-WarehouseSort-n{n_agents}-v2',
    entry_point=f'gym_multigrid.envs:WarehouseSortEnvN{n_agents}V2'
)
    '''

    exec(v2)
    
    v3=f'''
class WarehouseSortEnvN{n_agents}V3(WarehouseSortEnv):
    def __init__(self):
        w = 13
        h = 13
        super().__init__(size=None,
        height=h,
        width=w,
        n_agents={n_agents},
        chute_pos = [[w-1,3], [w-1,6], [w-1,9]],
        induct_pos=[[3,0], [3,h-1]],
    )

register(
    id=f'MultiGrid-WarehouseSort-n{n_agents}-v3',
    entry_point=f'gym_multigrid.envs:WarehouseSortEnvN{n_agents}V3'
)
    '''

    exec(v3)


    v4=f'''
class WarehouseSortEnvN{n_agents}V4(WarehouseSortEnv):
    def __init__(self):
        w = 13
        h = 13
        super().__init__(size=None,
        height=h,
        width=w,
        n_agents={n_agents},
        chute_pos = [[w-1,3], [w-1,6], [w-1,9]],
        induct_pos=[[0,3], [0,h-4]],
    )

register(
    id=f'MultiGrid-WarehouseSort-n{n_agents}-v4',
    entry_point=f'gym_multigrid.envs:WarehouseSortEnvN{n_agents}V4'
)
    '''
    exec(v4)

    v5=f'''
class WarehouseSortEnvN{n_agents}V5(WarehouseSortEnv):
    def __init__(self):
        w = 9
        h = 9
        super().__init__(size=None,
        height=h,
        width=w,
        n_agents={n_agents},
        chute_pos = [[5,0], [5,h-1], [w-1,4]],
        induct_pos=[[0,3], [0,h-4]],
    )

register(
    id=f'MultiGrid-WarehouseSort-n{n_agents}-v5',
    entry_point=f'gym_multigrid.envs:WarehouseSortEnvN{n_agents}V5'
)
    '''
    exec(v5)


    v6 = f'''
class WarehouseSortEnvN{n_agents}V6(WarehouseSortEnv):
    def __init__(self):
        w = 11
        h = 9
        super().__init__(size=None,
        height=h,
        width=w,
        n_agents={n_agents},
        induct_pos=[[0,6], [0,h-7]],
        chute_pos = [[6,2], [6,6], [4,4], [8,4]],
    )

register(
    id=f'MultiGrid-WarehouseSort-n{n_agents}-v6',
    entry_point=f'gym_multigrid.envs:WarehouseSortEnvN{n_agents}V6'
)
    '''
    exec(v6)


# Random Environment
class WarehouseSortRandomV0(WarehouseSortEnv):
    def __init__(self):
        w = 9
        h = 9
        super().__init__(size=None,
        height=h,
        width=w,
        n_agents=1,
        induct_pos=[[0,0], [0,0]],
        chute_pos=[[0,0], [0,0], [0,0], [0,0]],
        is_random=True,
        seed=123,
    )

register(
    id=f'MultiGrid-WarehouseSort-Random-v0',
    entry_point=f'gym_multigrid.envs:WarehouseSortRandomV0'
)

