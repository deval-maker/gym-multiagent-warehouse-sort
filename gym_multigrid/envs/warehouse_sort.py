from gym_multigrid.multigrid import *

class WarehouseSortEnv(MultiGridEnv):
    """
    Environment in which the agents have to sort the packages and drop them into respective destinations.
    """

    def __init__(
        self,
        size=10,
        view_size=3,
        width=None,
        height=None,
        goal_pst = [],
        goal_index = [],
        num_balls=[],
        agents_index = [],
        balls_index=[],
        balls_pst=[],
        zero_sum = False,

    ):
        self.num_balls = num_balls
        self.goal_pst = goal_pst
        self.goal_index = goal_index
        self.balls_index = balls_index
        self.balls_pst = balls_pst
        self.zero_sum = zero_sum

        self.world = World

        agents = []
        for i in agents_index:
            agents.append(Agent(self.world, view_size=view_size))

        super().__init__(
            grid_size=size,
            width=width,
            height=height,
            max_steps= 250,
            actions_set=WarehouseActions,
            partial_obs=False,
            # Set this to True for maximum speed
            see_through_walls=True,
            agents=agents,
            agent_view_size=view_size
        )

    def _gen_grid(self, width, height):
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.horz_wall(self.world, 0, 0)
        self.grid.horz_wall(self.world, 0, height-1)
        self.grid.vert_wall(self.world, 0, 0)
        self.grid.vert_wall(self.world, width-1, 0)

        for i in range(len(self.goal_pst)):
            ch = Chute(self.world,self.goal_index[i], target_type='ball')
            self.put_obj(ch, *self.goal_pst[i])
            self.chutes.append(ch)

        for number in range(self.num_balls):
            ind = Induct(self.world, n_packages=len(self.goal_index))
            self.put_obj(ind, *self.balls_pst[number])
            self.inducts.append(ind)
            
        # Randomize the player start position and orientation
        for a in self.agents:
            self.place_agent(a)

    def _handle_pickup(self, i, rewards, fwd_pos, fwd_cell):
        # if tuple(self.agents[i].target_pos) == tuple(self.agents[i].pos):
        induct_pos = self.agents[i].pos + np.array([-1,0])
        induct_cell = self.grid.get(*induct_pos)
        if induct_cell and induct_cell.type=="induct":
            rewards[i]+=10
            self.agents[i].carrying = induct_cell.give_package()
            self.agents[i].carrying.cur_pos = np.array([-1, -1])
            # self._reward(i, rewards, induct_cell, self.agents[i].carrying, is_pickup=True)
            chute_index = self.agents[i].carrying.index
            self.agents[i].target_pos = self.chutes[chute_index].target_pos
        else:
            assert False, "Target position set wrongly somewhere, Pickup"

    def _handle_drop(self, i, rewards, fwd_pos, fwd_cell):

        chute_pos = self.agents[i].pos + np.array([1,0])
        chute_cell = self.grid.get(*chute_pos)
        if chute_cell and chute_cell.type == 'chute' and chute_cell.target_type == self.agents[i].carrying.type:
            rewards[i]+=10
            # self._reward(i, rewards, chute_cell, self.agents[i].carrying)
            chute_cell.drop_package(self.agents[i].carrying)
            self.agents[i].carrying.cur_pos = fwd_pos
            self.agents[i].carrying = None
            self.agents[i].target_pos = None
        else:
            assert False, "Target position set wrongly somewhere, Drop"


    def step(self, actions):
        obs, rewards, done, info = MultiGridEnv.step(self, actions)
        return obs, rewards, done, info


class WarehouseSortEnvN1(WarehouseSortEnv):
    def __init__(self):
        w = 5
        super().__init__(size=None,
        height=7,
        width=w,
        goal_pst = [[w-1,2], [w-1,4]],
        goal_index = [0,1],
        agents_index = [0],
        num_balls=1,
        balls_pst=[[0,3]],
        zero_sum=False)
