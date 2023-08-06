from data_reader.dataset import EmailDataset
from data_reader.operations import load_dataset
from random import seed
from adlib.learners.svm_restrained import SVMRestrained

dataset = EmailDataset(path='./data_reader/data/raw/trec05p-1/test-400', binary=False, raw=True)
# set a seed so we get the same output every time
seed(1)
training_, testing_ = dataset.split({'train': 60, 'test': 40})
training_data = load_dataset(training_)
testing_data = load_dataset(testing_)

# learning_model = svm.SVC(probability=True, kernel='linear')
# learner = SimpleLearner(learning_model, training_data)

learner = SVMRestrained({'c_f': 0.7, 'xmin': 0.25, 'xmax': 0.75},
                        training_data)
# learner = SimpleLearner(learning_model, training_data)

learner.train()

predictions = learner.predict(testing_data)
print(predictions)
print([testing_data[i].label for i in range(len(testing_data))])

pre_proba = learner.predict_proba(testing_data)
print(pre_proba)
