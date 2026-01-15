import rl_agent
import rl_game_env
import random

if __name__ == '__main__':
    #  не скитайся бро

    
    random.seed(0)
    hyperparametrs = {}
    alpha = [0.01,0.05,0.1,0.15,0.2,0.25,0.30,0.35,0.40,0.45,0.5]
    string_alpha = [str(number) for number in alpha]

    hyperparametrs['alpha'] = alpha
    gamma = []
    for i in range(1,20):
        gamma.append(i/20)
    
    hyperparametrs['gamma'] = gamma
    hyperparametrs['num_of_episodes'] = 500

    n = 0
    n_all = len(gamma)*len(alpha)
    hyperparametrs_winrate_table = [[0] * len(alpha) for i in range(len(gamma))]
    epsilon_mode = [0]
    # epsilon_mode = [0,1,2]


# СЧИТАЕМ ЭЛЕМЕНТЫ
    ex = rl_agent.agent(rl_game_env.game_env)
    for g in range(len(gamma)):
        for a in range(len(alpha)):
            ex.make_q_policy()
            ex.q_learning(
                hyperparametrs['num_of_episodes'],
                alpha[a],
                gamma[g],
                0
                )
            hyperparametrs_winrate_table[g][a] = f"{ex.test_win_rate(10000):.2f}"
            n = n + 1
            print(f"{n/n_all*100:3.1f}%")


# ПИШЕМ В ФАЙЛ
    for ep in epsilon_mode:
        name = f"hyper_params_find_ep_{ep}.txt"
        with open(name, 'w') as f:
            f.write('\t')
            f.write(f"{'\t'.join(string_alpha)}\n")
            for g in range(len(gamma)):
                f.write(f"{gamma[g]:.2f}\t")
                row = [str(number) for number in hyperparametrs_winrate_table[g][:]]
                f.write('\t'.join(row))   
                f.write('\n')


