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