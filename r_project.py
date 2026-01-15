import random
# random.seed(123123)
import rl_agent
import rl_game_env



if __name__=='__main__':
    exemplar = rl_agent.agent(rl_game_env.game_env)
    exemplar.make_q_policy()
    hyper_parametrs = {
        'num_episodes':500,
        # кол-во эпизодов обучения (не трогать)
        # таргетное обучение. num_episodes на каждое состояние
        # метод обучения - e-greedy 
        'alpha':0.1, # скорость обучения, множитель который формирует величину значения при заполнением результатом (типо чтобы большие цифры по политике не формировались)
        # Optimal values (typically small, e.g., 0.01 to 0.5)
        'gamma':0.8, # по сути это множитель который уменьшает или увеличивает награду на следующем шаге.
        # от 0 до 1
        # ближе к 1 - принимает решения на основе награды в долгострочном режиме
        # ближе к 0 - принимает решения на основе моментальных наград
        'epsilon_mode' : 2
        # ОПИСАНИЕ ПОМЕНЯТЬ)
        # 'epsilon':1 # скорость обучения
        # 1 - по умолчанию на рандоме исследует все возможности
        # по мере обучения становится все меньше полагатся на рандом и эпсилон уменьшается
    }
    exemplar.q_learning(
        hyper_parametrs['num_episodes'],
        hyper_parametrs['alpha'],
        hyper_parametrs['gamma'],
        hyper_parametrs['epsilon_mode']
    )
    exemplar.write_q_policity('q_policy.txt')
    # exemplar.hand_mode_operations()
    # num_tests = 10**5
    # print(f"RL win rate: {exemplar.test_win_rate(num_tests):.3f} over {num_tests}")
    
