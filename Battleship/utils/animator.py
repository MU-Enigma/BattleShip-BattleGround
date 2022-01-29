
class AnimatedValue:

    def __init__(self, initial_value, FPS):
        self.val = initial_value
        self.animated = False
        self.increment = 0
        self.target = 0
        self.FPS = FPS
        self.tick = 0

    def animate(self, target_value, duration):
        self.animated = True
        self.target = target_value
        self.increment = (target_value-self.val)/(self.FPS*duration)

    def __call__(self, dT=1):
        if self.animated:
            if abs(self.target-self.val) < abs(self.increment*dT):
                self.increment = 0
                self.animated = False
                self.val = self.target
            self.val += self.increment*dT


        self.tick += 1
        return self.val


class AnimationStateMachine:

    def __init__(self, states):
        """States is a list of state(s) (also lists)
        Each state consists of state_actions, termination functions list
        A state action consists of:
            An instance of an animatedValue
            target_value and duration
        A termination functions list consits of functions that will run during the termination of that state.
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

        #TODO: Add state termination functions (or something).

        if self.curr_state == len(self.states):
            return True

        state = self.states[self.curr_state]

        # initializing state if not initialized already
        if not self.curr_initialize:
            for action in state[0]:
                action[0].animate(action[1], action[2])
            self.curr_initialize = True

        if self.is_complete(state[0]):
            self.curr_state += 1
            self.curr_initialize = False
            for function in state[1]:
                function()

        return False


