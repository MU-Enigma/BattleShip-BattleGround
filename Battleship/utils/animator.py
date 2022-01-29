
class animatedValue:

    def __init__(self, initial_value, FPS):
        self.val = initial_value
        self.animated = False
        self.increment = 0
        self.FPS = FPS

    def animate(self, target_value, duration):
        self.animated = True
        self.target = target_value
        self.increment = (target_value-self.val)/(self.FPS*duration)

    def __call__(self, dT=1):
        if self.animated:
            if self.target-self.val < self.increment*dT:
                self.increment = 0
                self.animated = False
                self.val=self.target
            self.val += self.increment*dT
        return self.val

class animationStateMachine:

    def __init__(self, states):
        """States is a list of state(s) (also lists)
        Each state consists of state_actions
        A state action consists of:
            An instance of an animatedValue
            target_value and duration
        """
        self.states = states
        self.complete = []
        self.curr_state = 0
        self.curr_initialize = False

    def is_complete(self, state):
        for action in state:
            if action[0].animated:
                return False
        return True

    def run(self):

        if self.curr_state == len(self.states):
            return True

        state = self.states[self.curr_state]

        # initializing state if not initialized already
        if not self.curr_initialize:
            for action in state:
                action[0].animate(action[1], action[0])

        if self.is_complete(state):
            self.curr_state += 1
            self.curr_initialize = False

        return False


