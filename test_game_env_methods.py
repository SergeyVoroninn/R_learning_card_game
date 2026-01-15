import rl_game_env
def test_init():
    env = rl_game_env.game_env()
    assert len(env.deck) == 52
    assert env.reward == 0
    assert env.game_over ==0
    assert env.curr ==0

def test_step_method():
    env = rl_game_env.game_env()
    first_card = env.deck[0]

    answer, reward, game_over = env.step('open_card')
    assert reward != 0
    assert game_over == 1
    
    env2 = rl_game_env.game_env()
    first_card = env2.deck[0]
    answer, reward, game_over = env2.step('show_next')

    assert reward == 0
    assert game_over == 0
    

# СДЕСЬ БУДУТ ЮНИТ ТЕСТЫ ЕМАЕ
