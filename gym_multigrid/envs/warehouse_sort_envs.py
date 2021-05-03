from gym_multigrid.envs.warehouse_sort import *


class WarehouseSortEnvV0(WarehouseSortEnv):
    def __init__(self):
        w = 5
        n_agents = 1
        super().__init__(size=None,
        height=7,
        width=w,
        goal_pst = [[w-1,2], [w-1,4]],
        goal_index = [1,2],
        agents_index = [i+1 for i in range(n_agents)],
        num_balls=1,
        balls_pst=[[0,3]],
        zero_sum=False)

class WarehouseSortEnvV1(WarehouseSortEnv):
    def __init__(self):
        w = 8
        h = 8
        n_agents = 1
        super().__init__(size=None,
        height=h,
        width=w,
        goal_pst = [[w-1,2], [w-1,h-3]],
        goal_index = [1,2],
        agents_index = [i+1 for i in range(n_agents)],
        num_balls=2,
        balls_pst=[[0,2], [0,5]],
        zero_sum=False)

class WarehouseSortEnvN12V3(WarehouseSortEnv):
    def __init__(self):
        w = 13
        h = 13
        n_agents = 12
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
    id=f'MultiGrid-WarehouseSort-n12-v3',
    entry_point=f'gym_multigrid.envs:WarehouseSortEnvN12V3'
)

class WarehouseSortEnvN16V4(WarehouseSortEnv):
    def __init__(self):
        w = 13
        h = 13
        n_agents = 16
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
    id=f'MultiGrid-WarehouseSort-n16-v4',
    entry_point=f'gym_multigrid.envs:WarehouseSortEnvN16V4'
)



class WarehouseSortEnvN8V2(WarehouseSortEnv):
    def __init__(self):
        w = 9
        h = 9
        n_agents = 8
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
    id=f'MultiGrid-WarehouseSort-n8-v2',
    entry_point=f'gym_multigrid.envs:WarehouseSortEnvN8V2'
)

class WarehouseSortEnvN4V2(WarehouseSortEnv):
    def __init__(self):
        w = 9
        h = 9
        n_agents = 4
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
    id=f'MultiGrid-WarehouseSort-n4-v2',
    entry_point=f'gym_multigrid.envs:WarehouseSortEnvN4V2'
)


class WarehouseSortEnvN12V2(WarehouseSortEnv):
    def __init__(self):
        w = 9
        h = 9
        n_agents = 12
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
    id=f'MultiGrid-WarehouseSort-n12-v2',
    entry_point=f'gym_multigrid.envs:WarehouseSortEnvN12V2'
)

######

class WarehouseSortEnvN1V0(WarehouseSortEnv):
    def __init__(self):
        w = 5
        super().__init__(size=None,
        height=7,
        width=w,
        goal_pst = [[w-1,2], [w-1,4]],
        goal_index = [1,2],
        agents_index = [1],
        num_balls=1,
        balls_pst=[[0,3]],
        zero_sum=False)

class WarehouseSortEnvN2V0(WarehouseSortEnv):
    def __init__(self):
        w = 5
        super().__init__(size=None,
        height=7,
        width=w,
        goal_pst = [[w-1,2], [w-1,4]],
        goal_index = [1,2],
        agents_index = [1,2],
        num_balls=1,
        balls_pst=[[0,3]],
        zero_sum=False)

class WarehouseSortEnvN3V0(WarehouseSortEnv):
    def __init__(self):
        w = 5
        super().__init__(size=None,
        height=7,
        width=w,
        goal_pst = [[w-1,2], [w-1,4]],
        goal_index = [1,2],
        agents_index = [1,2,3],
        num_balls=1,
        balls_pst=[[0,3]],
        zero_sum=False)


class WarehouseSortEnvN4V0(WarehouseSortEnv):
    def __init__(self):
        w = 5
        super().__init__(size=None,
        height=7,
        width=w,
        goal_pst = [[w-1,2], [w-1,4]],
        goal_index = [1,2],
        agents_index = [1,2,3,4],
        num_balls=1,
        balls_pst=[[0,3]],
        zero_sum=False)

class WarehouseSortEnvN5V0(WarehouseSortEnv):
    def __init__(self):
        w = 5
        super().__init__(size=None,
        height=7,
        width=w,
        goal_pst = [[w-1,2], [w-1,4]],
        goal_index = [1,2],
        agents_index = [1,2,3,4,5],
        num_balls=1,
        balls_pst=[[0,3]],
        zero_sum=False)


class WarehouseSortEnvN6V0(WarehouseSortEnv):
    def __init__(self):
        w = 5
        super().__init__(size=None,
        height=7,
        width=w,
        goal_pst = [[w-1,2], [w-1,4]],
        goal_index = [1,2],
        agents_index = [1,2,3,4,5,6],
        num_balls=1,
        balls_pst=[[0,3]],
        zero_sum=False)


class WarehouseSortEnvN1V1(WarehouseSortEnv):
    def __init__(self):
        w = 8
        h = 8
        n_agents = 1
        super().__init__(size=None,
        height=h,
        width=w,
        goal_pst = [[w-1,2], [w-1,h-3]],
        goal_index = [1,2],
        agents_index = [i+1 for i in range(n_agents)],
        num_balls=2,
        balls_pst=[[0,2], [0,5]],
        zero_sum=False)


class WarehouseSortEnvN2V1(WarehouseSortEnv):
    def __init__(self):
        w = 8
        h = 8
        n_agents = 2
        super().__init__(size=None,
        height=h,
        width=w,
        goal_pst = [[w-1,2], [w-1,h-3]],
        goal_index = [1,2],
        agents_index = [i+1 for i in range(n_agents)],
        num_balls=2,
        balls_pst=[[0,2], [0,5]],
        zero_sum=False)

class WarehouseSortEnvN3V1(WarehouseSortEnv):
    def __init__(self):
        w = 8
        h = 8
        n_agents = 3
        super().__init__(size=None,
        height=h,
        width=w,
        goal_pst = [[w-1,2], [w-1,h-3]],
        goal_index = [1,2],
        agents_index = [i+1 for i in range(n_agents)],
        num_balls=2,
        balls_pst=[[0,2], [0,5]],
        zero_sum=False)

class WarehouseSortEnvN4V1(WarehouseSortEnv):
    def __init__(self):
        w = 8
        h = 8
        n_agents = 4
        super().__init__(size=None,
        height=h,
        width=w,
        goal_pst = [[w-1,2], [w-1,h-3]],
        goal_index = [1,2],
        agents_index = [i+1 for i in range(n_agents)],
        num_balls=2,
        balls_pst=[[0,2], [0,5]],
        zero_sum=False)

class WarehouseSortEnvN5V1(WarehouseSortEnv):
    def __init__(self):
        w = 8
        h = 8
        n_agents = 5
        super().__init__(size=None,
        height=h,
        width=w,
        goal_pst = [[w-1,2], [w-1,h-3]],
        goal_index = [1,2],
        agents_index = [i+1 for i in range(n_agents)],
        num_balls=2,
        balls_pst=[[0,2], [0,5]],
        zero_sum=False)

class WarehouseSortEnvN6V1(WarehouseSortEnv):
    def __init__(self):
        w = 8
        h = 8
        n_agents = 6
        super().__init__(size=None,
        height=h,
        width=w,
        goal_pst = [[w-1,2], [w-1,h-3]],
        goal_index = [1,2],
        agents_index = [i+1 for i in range(n_agents)],
        num_balls=2,
        balls_pst=[[0,2], [0,5]],
        zero_sum=False)

# v0s
for i in range(6):
    register(
        id=f'MultiGrid-WarehouseSort-n{i+1}-v0',
        entry_point=f'gym_multigrid.envs:WarehouseSortEnvN{i+1}V0'
    )

#v1s
for i in range(6):
    register(
        id=f'MultiGrid-WarehouseSort-n{i+1}-v1',
        entry_point=f'gym_multigrid.envs:WarehouseSortEnvN{i+1}V1'
    )