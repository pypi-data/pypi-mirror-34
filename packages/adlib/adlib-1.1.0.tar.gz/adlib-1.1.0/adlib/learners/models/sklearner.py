from typing import List, Dict
from data_reader.binary_input import Instance
from adlib.learners.models.model import BaseModel
from data_reader.operations import sparsify
from sklearn import svm


class Model(BaseModel):
    """Learner model wrapper around sklearn classifier

    Extends the BaseModel class to use the functionality of
    a user-supplied sklearn classifier in conjunction with
    the adversarial library.

    """

    def __init__(self, sklearn_object):
        """Creates new model from user-supplied sklearn function.

        Args:
            sklearn_object (sklearn classifier): Model for sklearn
            classification.

        """
        self.learner = sklearn_object

    def train(self, instances):
        """Train on the set of training instances using the underlying
        sklearn object.

        Args:
            instances (List[Instance]): training instances or emaildataset
            object.

        """
        if isinstance(instances, List):
            (y, X) = sparsify(instances)
            self.learner.fit(X.toarray(), y)
        else:
            self.learner.fit(instances.data[0], instances.data[1])

    def predict(self, instances):
        """Predict classification labels for the set of instances using
        the predict function of the sklearn classifier.

        Args:
            instances should be a Email Dataset
            instances (List[Instance]) or (Instance): training or test instances.

        Returns:
            label classifications (List(int))

        """
        if isinstance(instances, List):
            (y, X) = sparsify(instances)
            predictions = self.learner.predict(X.toarray())
        elif type(instances) == Instance:
            predictions = self.learner.predict(
                instances.get_feature_vector().get_csr_matrix().toarray())[0]
        else:
            predictions = self.learner.predict(instances.features)
        return predictions

    def predict_proba(self, instances):
        """Use the model to determine probability of adversarial classification.

        Args:
            instances (List[Instance]) or (Instance): training or test instances.
            instances should be a csr_matrix representation

        Returns:
            probability of adversarial classification (List(int))

        """
        if isinstance(instances, List):
            (y, X) = sparsify(instances)
            full_probs = self.learner.predict_proba(X.toarray())
            probs = [x[0] for x in full_probs]
        elif type(instances) == Instance:
            probs = self.learner.predict_proba(
                instances.get_feature_vector().get_csr_matrix())
        else:
            probs = self.learner.predict_proba(instances.features)
        return probs

    def predict_log_proba(self, instances):
        """Use the model to determine log probability of adversarial classification.

        Args:
            instances (List[Instance]) or (Instance): training or test instances.
            instances should be a csr_matrix representation

        Returns:
            probability of adversarial classification (List(int))

        """
        if isinstance(instances, List):
            (y, X) = sparsify(instances)
            full_probs = self.learner.predict_log_proba(X)
            probs = [x[0] for x in full_probs]
        elif type(instances) == Instance:
            matrix = instances.get_feature_vector().get_csr_matrix()
            probs = self.learner.predict_log_proba(matrix.toarray())
        else:
            probs = self.learner.predict_log_proba(instances.features)
        return probs

    def decision_function_(self, instances):
        """Use the model to determine the decision function for each instance.

        Args:
            instances (List[Instance]) or (Instance): training or test instances.

        Returns:
            decision values (List(int))

        """
        if isinstance(instances, List):
            (y, X) = sparsify(instances)
            f = self.learner.decision_function(X)
        elif type(instances) == Instance:
            f = self.learner.decision_function(
                instances.get_feature_vector().get_csr_matrix())[0]
        else:
            self.learner.dicision_function(instances.features)
        return f

    def set_params(self, params: Dict):
        """Set params for the model.

        Args:
            params (Dict): set of available params with updated values

        """
        param_map = {}
        if type(self.learner) == svm.SVC:
            if 'C' in params.keys():
                param_map['C'] = params['C']
            if 'kernel' in params.keys():
                param_map['kernel'] = params['kernel']
            if 'gamma' in params.keys():
                param_map['gamma'] = params['gamma']
            if 'coef0' in params.keys():
                param_map['coef'] = params['coef0']
            if 'probability' in params.keys():
                param_map['probability'] = params['probability']
            if 'class_weight' in params.keys():
                param_map['class_weight'] = params['class_weight']
        self.learner.set_params(**param_map)

    def get_params(self):
        return self.learner.get_params()

    def get_attributes(self):
        if type(self.learner) == svm.SVC:
            attribute_map = {"support_": self.learner.support_,
                             "support_vectors_": self.learner.support_vectors_,
                             "n_support_": self.learner.n_support_,
                             "dual_coef_": self.learner.dual_coef_,
                             "intercept_": self.learner.intercept_}
            if self.learner.kernel == "linear":
                attribute_map["coef_"] = self.learner.coef_
            return attribute_map
        return None

    def get_available_params(self) -> Dict:
        """Get the set of params defined in the model usage.

        These are generated by the sklearn module.

        Returns:
            dictionary mapping param names to current values

        """
        return self.learner.get_params()

    def get_alg(self):
        """Return the underlying model algorithm.

        Returns:
            algorithm used to train and test instances

        """
        return self.learner

    def get_weight(self):
        """
        Return the weight vector of the linear classifier
        :return:
        """
        print("weight vec shape from sklearner: {}".format(self.learner.coef_[0]))
        return self.learner.coef_[0]
