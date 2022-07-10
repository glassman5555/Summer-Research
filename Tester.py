from battle_environment import BattleEnvironment
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

cf = {
    'hit_base_reward': 1,
    'hit_plane_reward': 1,
    'miss_punishment': 0,
    'too_long_punishment': 0,
    'closer_to_base_reward': 0,
    'closer_to_plane_reward': 0,
    'lose_punishment': -1
}

model_dir = "models/PPO_1/final_model"

# Load trained agent and evaluate 1000 games
eval_env = BattleEnvironment(show=False, hit_base_reward=cf['hit_base_reward'], hit_plane_reward=cf['hit_plane_reward'], miss_punishment=cf['miss_punishment'], 
    too_long_punishment=cf['too_long_punishment'], closer_to_base_reward=cf['closer_to_base_reward'], closer_to_plane_reward=cf['closer_to_plane_reward'], lose_punishment=cf['lose_punishment'])
model = PPO.load(model_dir, env=eval_env)
print("Evaluating model...")
mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=1000, deterministic=True)
print(f"Mean reward: {mean_reward:.2f} +/- {std_reward}")
print(eval_env.wins())

# Evaluate with visuals (10 games)
eval_env = BattleEnvironment(show=True, hit_base_reward=cf['hit_base_reward'], hit_plane_reward=cf['hit_plane_reward'], miss_punishment=cf['miss_punishment'], 
    too_long_punishment=cf['too_long_punishment'], closer_to_base_reward=cf['closer_to_base_reward'], closer_to_plane_reward=cf['closer_to_plane_reward'], lose_punishment=cf['lose_punishment'], fps=30)
model.set_env(eval_env)
mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=10, deterministic=True)
print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")