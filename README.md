# Math-and-AI

Choose between two envelopes, each containing two balls. If you select the envelope with only black, you get nothing; if you select the envelope with one red and one black, you get a payout.

Functions
pick_envelope(switch, verbose) — this function expects two boolean parameter (whether you switch envelopes or not, and whether you want to see the printed explanation of the simulation) and returns True or False based on whether you selected the correct envelope
run_simulation(n) — this function runs n simulations of envelope picking under both strategies (switch n times, don't switch n times) and prints the percent of times the correct envelope was chosen for each

This next part is where things will get interesting: we'll be reading in a corpus (a collection of documents) with two possible true labels and training a classifier to determine which label a query document is more likely to have.


Functions

train(training_directory, cutoff) -- loads the training data, estimates the prior distribution P(label) and class conditional distributions LaTeX: P\left(word\mid label\right)P ( w o r d ∣ l a b e l ), return the trained model
create_vocabulary(training_directory, cutoff) -- create and return a vocabulary as a list of word types with counts >= cutoff in the training directory
create_bow(vocab, filepath) -- create and return a bag of words Python dictionary from a single document
load_training_data(vocab, directory) -- create and return training set (bag of words Python dictionary + label) from the files in a training directory
prior(training_data, label_list) -- given a training set, estimate and return the prior probability p(label) of each label
p_word_given_label(vocab, training_data, label) -- given a training set and a vocabulary, estimate and return the class conditional distribution LaTeX: P\left(word\mid label\right)P ( w o r d ∣ l a b e l ) over all words for the given label using smoothing
classify(model, filepath) -- given a trained model, predict the label for the test document (see below for implementation details including return value)
this high-level function should also use create_bow(vocab, filepath)
