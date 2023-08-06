#!/usr/bin/env python

# Python imports.
import sys

# Other imports.
import srl_example_setup
from simple_rl.agents import LinearQAgent, QLearningAgent, RandomAgent, DoubleQAgent
from simple_rl.tasks import ChainMDP
from simple_rl.run_experiments import run_agents_on_mdp, run_single_agent_on_mdp

def main(open_plot=True):
    # Setup MDP, Agents.
    mdp = ChainMDP()

    rand_agent = RandomAgent(actions=mdp.get_actions())

    _, _, value = run_single_agent_on_mdp(rand_agent, mdp, episodes=1, steps=100)

    # Run experiment and make plot.
    run_agents_on_mdp([lin_ql_agent, rbf_lin_ql_agent, ql_agent, rand_agent], mdp, instances=5, episodes=50, steps=1000, open_plot=open_plot)

if __name__ == "__main__":
    main(open_plot=not sys.argv[-1] == "no_plot")
