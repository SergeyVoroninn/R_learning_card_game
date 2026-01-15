import random

class agent:
    def __init__(self,game_env):
        self.env = game_env()

    def make_q_policy(self):
        state = []
        self.q_policy=dict()
        for r in range(0,27):
            for b in range(0,27):
                if r + b >0:
                    state.append((r,b))

        for elem in state:
            actions = self.env.give_actions(elem)
            dict_of_actions = dict()
            for act in actions:
                dict_of_actions[act] = 0
            self.q_policy[elem] = dict_of_actions

    def take_action(self,state,epsiolon): 
        possible_actions = self.env.give_actions(state)
        if 'error' in possible_actions:
            print('error in possible_actions')
            exit(1)

        if random.random() < epsiolon:
            answer = random.choice(possible_actions)
        else:
            answer = max(self.q_policy[state], key=self.q_policy[state].get)
        return answer
    
    def epsilon_calc(self,episode,dec_mode,num_episodes):
        # ВСЕ ВЫЧИСЛЕНИЯ ВЫПОЛНЕНЫ ДЛЯ 500 ЭПИЗОДОВ НА КАЖДУЮ ТОЧКУ!!
        if dec_mode == 0:
            epsilon_decay_rate = 4 * 10 ** -6
            current_epsilon = max(0.01,epsilon_decay_rate * (episode-num_episodes)**2)
        elif dec_mode ==1:
            epsilon_decay_rate = 0.995
            current_epsilon = max(0.01,epsilon_decay_rate**episode)
        elif dec_mode == 2:
            current_epsilon = max(0.01,num_episodes*2/(num_episodes+episode)-1)
        else:
            print('error in epsilon calc')
            exit(1)
        
        return current_epsilon
 
    def q_learning(self,num_episodes,alpha,gamma,dec_mode=0):
        ep = 0
        for r in range(26,-1,-1):
            for b in range(26,-1,-1):
                for sub_ep in range(num_episodes):
                    if r + b > 0:
                        start_state = (r,b)
                        self.env.reset(start_state)
                        terminated = False

                        current_epsilon = self.epsilon_calc(sub_ep,dec_mode,num_episodes)

                        rem_r = r
                        rem_b = b
                        while not terminated:
                            state = (rem_r,rem_b)
                            action = self.take_action(state,current_epsilon)
                            answer,reward,terminated = self.env.step(action)
                            if 'Red' in answer:
                                rem_r=rem_r -1
                            else:
                                rem_b=rem_b -1
                            if not terminated:
                                next_state = (rem_r,rem_b)
                                max_action = max(self.q_policy[next_state], key=self.q_policy[next_state].get)
                                max_q = self.q_policy[next_state][max_action]
                            else:
                                max_q = 0
                            
                            # Q[s,a] = Q[s,a] + alpha * (reward + gamma * max(Q[s',a']) - Q[s,a])
                            self.q_policy[state][action]= self.q_policy[state][action] + alpha*(reward + gamma * max_q - self.q_policy[state][action])
                    ep = ep + 1

    def hand_mode_operations(self):
        start_state = (26,26)
        self.env.reset(start_state)
        terminated = False
        rem_r = start_state[0]
        rem_b = start_state[1]
        print(f"1 is open_card, 2 is show next")
        while not terminated:
            state = (rem_r,rem_b)
            key_with_max_value = max(self.q_policy[state], key=self.q_policy[state].get)
            print(f"RL suggest:{key_with_max_value} with value: {self.q_policy[state][key_with_max_value]:.3f}")
            action_text = input()
            if action_text == '1':
                action = 'open_card'
            elif action_text == '2':
                action = 'show_next'
            else:
                print('wrong input')
                exit(1)
            answer,reward,terminated = self.env.step(action)
            if 'Red' in answer:
                rem_r=rem_r -1
            else:
                rem_b=rem_b -1
            print(f"{answer}, current_reward:{reward}, current_state: {(rem_r,rem_b)}")
    
    def test_win_rate(self,num_tests,var_ep):
        start_state = (26,26)
        wins = 0
        for ep in range(num_tests):
            self.env.reset(start_state)
            terminated=False
            rem_r = start_state[0]
            rem_b = start_state[1]

            while not terminated:
                state = (rem_r,rem_b)

                action = self.take_action(state,var_ep)
                answer,reward,terminated = self.env.step(action)
                if 'Red' in answer:
                    rem_r=rem_r -1
                else:
                    rem_b=rem_b -1
                if reward >0:
                    wins=wins+1
        return wins/num_tests
    
    def write_q_policity(self,name_of_file):
        with open(name_of_file,'w') as f:
            for key,value in self.q_policy.items():
                f.write(f"{key}\n")
                for s_key,s_value in value.items():
                    f.write(f"{s_key}: {s_value:.3f}\t")
                f.write("\n")