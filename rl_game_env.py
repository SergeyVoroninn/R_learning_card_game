import random
class game_env:
    def __init__(self):
        self.deck = [1]*26+[0]*26
        random.shuffle(self.deck)
        self.curr = 0
        self.reward = 0
        self.game_over = 0
    def step(self,action):
        if action == 'open_card':
            answer = f"Card is {'Red' if self.deck[self.curr] == 1 else 'Black'}"
            if 'Red' in answer:
                self.reward = 1
            else:
                self.reward = -1
            self.game_over = 1
        elif action == 'show_next':
            answer = f"Card is {'Red' if self.deck[self.curr] == 1 else 'Black'}"
            self.curr+=1
        else:
            print('wrong action')
            exit(1)
        return answer,self.reward,self.game_over
    def give_actions(self,state):
        r = int(state[0])
        b = int(state[1])
        if r+b == 0:
            answer = ['error']
        elif r+b == 1:
            answer = ['open_card']
        elif r+b >1:
            answer = ['open_card','show_next']
        else:
            answer = ['error']
        return answer
    def reset(self,tuple_of_r_b=(26,26)):
        r = tuple_of_r_b[0]
        b = tuple_of_r_b[1]
        self.deck = [1]*r+[0]*b
        random.shuffle(self.deck)
        self.curr = 0
        self.reward = 0
        self.game_over = 0