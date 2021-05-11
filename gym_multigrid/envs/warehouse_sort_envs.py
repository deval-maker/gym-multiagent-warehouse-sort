from gym_multigrid.envs.warehouse_sort import *


for n_agents in range(1,21): 

    v0=f'''
class WarehouseSortEnvN{n_agents}V0(WarehouseSortEnv):
    def __init__(self):
        w = 5
        n_agents={n_agents}
        super().__init__(size=None,
        height=7,
        width=w,
        goal_pst = [[w-1,2], [w-1,4]],
        goal_index = [1,2],
        agents_index = [i+1 for i in range(n_agents)],
        num_balls=1,
        balls_pst=[[0,3]],
        zero_sum=False)


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
        n_agents={n_agents}
        super().__init__(size=None,
        height=h,
        width=w,
        goal_pst = [[w-1,2], [w-1,h-3]],
        goal_index = [1,2],
        agents_index = [i+1 for i in range(n_agents)],
        num_balls=2,
        balls_pst=[[0,2], [0,5]],
        zero_sum=False)

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
        n_agents={n_agents}
        super().__init__(size=None,
        height=h,
        width=w,
        goal_pst = [[w-1,4], [0,4]],
        goal_index = [1,2],
        agents_index = [i+1 for i in range(n_agents)],
        num_balls=2,
        balls_pst=[[4,0], [4,h-1]],
        zero_sum=False)

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
        n_agents={n_agents}
        super().__init__(size=None,
        height=h,
        width=w,
        goal_pst = [[w-1,3], [w-1,6], [w-1,9]],
        goal_index = [1,2,3],
        agents_index = [i+1 for i in range(n_agents)],
        num_balls=2,
        balls_pst=[[3,0], [3,h-1]],
        zero_sum=False)

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
        n_agents={n_agents}
        super().__init__(size=None,
        height=h,
        width=w,
        goal_pst = [[w-1,3], [w-1,6], [w-1,9]],
        goal_index = [1,2,3],
        agents_index = [i+1 for i in range(n_agents)],
        num_balls=2,
        balls_pst=[[0,3], [0,h-4]],
        zero_sum=False)

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
        n_agents={n_agents}
        super().__init__(size=None,
        height=h,
        width=w,
        goal_pst = [[5,0], [5,h-1], [w-1,4]],
        goal_index = [1,2,3],
        agents_index = [i+1 for i in range(n_agents)],
        num_balls=2,
        balls_pst=[[0,3], [0,h-4]],
        zero_sum=False)

register(
    id=f'MultiGrid-WarehouseSort-n{n_agents}-v5',
    entry_point=f'gym_multigrid.envs:WarehouseSortEnvN{n_agents}V5'
)
    '''
    exec(v5)


    v6 = f'''
class WarehouseSortEnvN{n_agents}V6(WarehouseSortEnv):
    def __init__(self):
        w = 9
        h = 9
        n_agents={n_agents}
        super().__init__(size=None,
        height=h,
        width=w,
        goal_pst = [[5,2], [5,6], [w-6,4]],
        goal_index = [1,2,3],
        agents_index = [i+1 for i in range(n_agents)],
        num_balls=2,
        balls_pst=[[0,3], [w-1,h-4]],
        zero_sum=False)

register(
    id=f'MultiGrid-WarehouseSort-n{n_agents}-v6',
    entry_point=f'gym_multigrid.envs:WarehouseSortEnvN{n_agents}V6'
)
    '''
    exec(v6)
