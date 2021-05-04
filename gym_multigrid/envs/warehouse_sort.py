from gym_multigrid.multigrid import *
from gym_multigrid.register import register

class WarehouseSortEnv(MultiGridEnv):
    """
    Environment in which the agents have to sort the packages and drop them into respective destinations.
    """

    def __init__(
        self,
        size=10,
        view_size=13,
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

        self.world = WarehouseWorld

        self.chutes = []
        self.inducts = []

        agents = []
        for i in agents_index:
            agents.append(Agent(self.world, view_size=view_size))

        for i in range(len(self.goal_pst)):
            ch = Chute(self.world,self.goal_index[i], target_type='ball')
            self.chutes.append(ch)

        for i in range(self.num_balls):
            ind = Induct(self.world, induct_index=i+1, n_packages=len(self.goal_index))
            self.inducts.append(ind)

        super().__init__(
            grid_size=size,
            width=width,
            height=height,
            max_steps= 400,
            actions_set=WarehouseActions,
            partial_obs=True,
            # Set this to True for maximum speed
            see_through_walls=True,
            agents=agents,
            agent_view_size=view_size,
            objects_set=self.world,
        )

    def _gen_grid(self, width, height):
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.horz_wall(self.world, 0, 0)
        self.grid.horz_wall(self.world, 0, height-1)
        self.grid.vert_wall(self.world, 0, 0)
        self.grid.vert_wall(self.world, width-1, 0)

        for i, ch in enumerate(self.chutes):
            self.put_obj(ch, *self.goal_pst[i])
            ch.get_target_poses(self.grid)

        for i, ind in enumerate(self.inducts):
            self.put_obj(ind, *self.balls_pst[i])
            ind.get_target_poses(self.grid)

        # Randomize the player start position and orientation
        for a in self.agents:
            self.place_agent(a)

    # def _reward(self, i, rewards, fwd_cell, package, is_pickup=False):
    #     """ 
    #     Reward for the warehouse_sort. DO NOT CHANGE ORDER OF `if` statements.
    #     """

    #     # Package picked up
    #     if is_pickup:
    #         rewards[i]+=100
    #         return

    #     # Package dropped correctly
    #     if fwd_cell.index == package.index:
    #         rewards[i]+=250
    #         print("Good Job !!")
    #         return

    #     # Package dropped at a wrong chute 
    #     if fwd_cell.index != package.index:
    #         rewards[i]+=-20
    #         return
    
    def _handle_pickup(self, i, rewards, induct_cell, fwd_cell):
        # if tuple(self.agents[i].target_pos) == tuple(self.agents[i].pos):
        # induct_pos = self.agents[i].pos + np.array([-1,0])
        # induct_cell = self.grid.get(*induct_pos)
        if induct_cell and induct_cell.type=="induct":
            # (1 - 0.9 * (self.agents[i].steps_before_pick_put / self.max_steps))
            # rewards[i]+=random.randrange(2, 5)
            self.agents[i].carrying = induct_cell.give_package()
            if self.agents[i].carrying:
                rewards[i]+=(1 - 0.9 * (self.agents[i].steps_before_pick_put/self.max_steps))
                # rewards[i]+=1
            # self.agents[i].carrying.cur_pos = np.array([-1, -1])
            # self._reward(i, rewards, induct_cell, self.agents[i].carrying, is_pickup=True)
            # chute_index = self.agents[i].carrying.index
            # self.agents[i].target_pos = self.chutes[chute_index].target_pos

            self.agents[i].steps_before_pick_put = 0

        else:
            assert False, "Target position set wrongly somewhere, Pickup"

    def _handle_drop(self, i, rewards, chute_cell, fwd_cell):
        
        # chute_pos = self.agents[i].pos + np.array([1,0])
        # chute_cell = self.grid.get(*chute_pos)
        if chute_cell and chute_cell.type == 'chute' and chute_cell.target_type == self.agents[i].carrying.type:

            if self.agents[i].carrying.index == chute_cell.index:
                rewards[i]+=(1 - 0.9 * (self.agents[i].steps_before_pick_put/self.max_steps))
                # rewards[i]+=1
                # self._reward(i, rewards, chute_cell, self.agents[i].carrying)
                chute_cell.drop_package(self.agents[i].carrying)
                self.agents[i].carrying.cur_pos = chute_cell.cur_pos
                self.agents[i].carrying = None
                # self.agents[i].target_pos = None
            else:
                rewards[i]+=-0.25 #random.random()
            
            self.agents[i].steps_before_pick_put = 0

        else:
            assert False, "Target position set wrongly somewhere, Drop"


    def step(self, actions):
        obs, rewards, done, info = MultiGridEnv.step(self, actions)
        obs = {
            "image": obs[0],
            "global": obs[1],
        }
        return obs, rewards, done, info

    def reset(self):
        obs = MultiGridEnv.reset(self)
        obs = {
            "image": obs[0],
            "global": obs[1],
        }
        return obs

