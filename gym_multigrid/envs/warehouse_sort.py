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
            max_steps= 10000,
            actions_set=WarehouseActions,
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
            self.put_obj(Chute(self.world,self.goal_index[i], 'ball'), *self.goal_pst[i])

        for number in range(self.num_balls):
            self.put_obj(Induct(self.world, n_packages=len(self.goal_index)), *self.balls_pst[number])

        # Randomize the player start position and orientation
        for a in self.agents:
            self.place_agent(a)

    def _reward(self, i, rewards,reward=1):
        for j,a in enumerate(self.agents):
            if a.index==i or a.index==0:
                rewards[j]+=reward
            if self.zero_sum:
                if a.index!=i or a.index==0:
                    rewards[j] -= reward

    def _handle_pickup(self, i, rewards, fwd_pos, fwd_cell):
        if fwd_cell:
            if fwd_cell.can_pickup():
                if self.agents[i].carrying is None and fwd_cell.type=="induct":
                    self.agents[i].carrying = fwd_cell.give_package()
                    self.agents[i].carrying.cur_pos = np.array([-1, -1])
                    # self.grid.set(*fwd_pos, None)

    def _handle_drop(self, i, rewards, fwd_pos, fwd_cell):
        if self.agents[i].carrying:
            if fwd_cell:
                if fwd_cell.type == 'chute' and fwd_cell.target_type == self.agents[i].carrying.type:
                    # if self.agents[i].carrying.index in [0, fwd_cell.index]:
                    # self._reward(fwd_cell.index, rewards, fwd_cell.reward)
                    fwd_cell.drop_package(self.agents[i].carrying)
                    self.agents[i].carrying.cur_pos = fwd_pos
                    self.agents[i].carrying = None
            else:
                self.grid.set(*fwd_pos, self.agents[i].carrying)
                self.agents[i].carrying.cur_pos = fwd_pos
                self.agents[i].carrying = None


    def step(self, actions):
        obs, rewards, done, info = MultiGridEnv.step(self, actions)
        return obs, rewards, done, info


class WarehouseSortEnvN1(WarehouseSortEnv):
    def __init__(self):
        super().__init__(size=None,
        height=7,
        width=6,
        goal_pst = [[5,2], [5,4]],
        goal_index = [0,1],
        agents_index = [0],
        num_balls=1,
        balls_pst=[[0,3]],
        zero_sum=False)
