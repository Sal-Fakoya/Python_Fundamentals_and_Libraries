# Import libraries
import numpy as np
import pandas as pd
import pymc as pm
import matplotlib.pyplot as plt

# Set random seed
np.random.seed(42)

# Generate some fake data
n_populations = 3 # Number of populations
n_individuals = 100 # Number of individuals per population
n_behaviors = 2 # Number of behaviors (0: pro-social, 1: anti-social)
n_interactions = 10 # Number of interactions per individual
n_outcomes = 2 # Number of outcomes (0: negative, 1: positive)
n_feedbacks = 2 # Number of feedbacks (0: no, 1: yes)

# Generate population sizes
pop_sizes = np.random.randint(100, 1000, size=n_populations)

# Generate propensities to punish and correct for each population
punish_probs = np.random.beta(2, 2, size=n_populations)
correct_probs = np.random.beta(2, 2, size=n_populations)

# Generate behaviors for each individual
behaviors = np.random.binomial(1, 0.5, size=(n_populations, n_individuals))

# Generate interactions for each individual
interactions = np.random.randint(0, n_populations, size=(n_populations, n_individuals, n_interactions))

# Generate outcomes for each interaction
outcomes = np.zeros((n_populations, n_individuals, n_interactions), dtype=int)
for i in range(n_populations):
    for j in range(n_individuals):
        for k in range(n_interactions):
            # If the behavior is pro-social and the interaction is with the same population, the outcome is positive
            if behaviors[i, j] == 0 and interactions[i, j, k] == i:
                outcomes[i, j, k] = 1
            # If the behavior is anti-social and the interaction is with a different population, the outcome is negative
            elif behaviors[i, j] == 1 and interactions[i, j, k] != i:
                outcomes[i, j, k] = 0
            # Otherwise, the outcome is random
            else:
                outcomes[i, j, k] = np.random.binomial(1, 0.5)

# Generate feedback for each interaction
feedbacks = np.zeros((n_populations, n_individuals, n_interactions), dtype=int)
for i in range(n_populations):
    for j in range(n_individuals):
        for k in range(n_interactions):
            # If the outcome is negative and the interaction is with the same population, the feedback is yes with the punish probability
            if outcomes[i, j, k] == 0 and interactions[i, j, k] == i:
                feedbacks[i, j, k] = np.random.binomial(1, punish_probs[i])
            # If the outcome is positive and the interaction is with the same population, the feedback is yes with the correct probability
            elif outcomes[i, j, k] == 1 and interactions[i, j, k] == i:
                feedbacks[i, j, k] = np.random.binomial(1, correct_probs[i])
            # Otherwise, the feedback is no
            else:
                feedbacks[i, j, k] = 0

# Reshape the data into a long format
data = pd.DataFrame({
    'population': np.repeat(np.arange(n_populations), n_individuals * n_interactions),
    'individual': np.tile(np.repeat(np.arange(n_individuals), n_interactions), n_populations),
    'behavior': np.tile(behaviors.ravel(), n_interactions),
    'interaction': interactions.ravel(),
    'outcome': outcomes.ravel(),
    'feedback': feedbacks.ravel()
})

# Define the Bayesian network model
with pm.Model() as model:
    # Define the priors for the population sizes
    pop_sizes = pm.Dirichlet('pop_sizes', a=np.ones(n_populations))

    # Define the priors for the propensities to punish and correct
    punish_probs = pm.Beta('punish_probs', alpha=2, beta=2, shape=n_populations)
    correct_probs = pm.Beta('correct_probs', alpha=2, beta=2, shape=n_populations)

    # Define the priors for the behaviors
    behavior_probs = pm.Beta('behavior_probs', alpha=2, beta=2, shape=n_populations)
    behaviors = pm.Bernoulli('behaviors', p=behavior_probs[data['population']], observed=data['behavior'])

    # Define the priors for the interactions
    interaction_probs = pm.Dirichlet('interaction_probs', a=np.ones(n_populations), shape=n_populations)
    interactions = pm.Categorical('interactions', p=interaction_probs[data['population']], observed=data['interaction'])

    # Define the priors for the outcomes
    outcome_probs = pm.Beta('outcome_probs', alpha=2, beta=2, shape=(n_populations, n_behaviors, n_populations))
    outcomes = pm.Bernoulli('outcomes', p=outcome_probs[data['population'], data['behavior'], data['interaction']], observed=data['outcome'])

    # Define the priors for the feedbacks
    feedback_probs = pm.Beta('feedback_probs', alpha=2, beta=2, shape=(n_populations, n_outcomes, n_populations))
    feedbacks = pm.Bernoulli('feedbacks', p=feedback_probs[data['population'], data['outcome'], data['interaction']], observed=data['feedback'])

# Sample from the posterior distribution
with model:
    trace = pm.sample(1000, tune=1000, return_inferencedata=True)

# Plot the posterior distributions
pm.plot_posterior(trace, var_names=['pop_sizes', 'punish_probs', 'correct_probs', 'behavior_probs', 'interaction_probs', 'outcome_probs', 'feedback_probs'])
plt.show()

