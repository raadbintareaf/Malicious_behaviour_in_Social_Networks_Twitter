import numpy as np
from sklearn.ensemble import IsolationForest

from core.utils import normalize


class IsolationForestClassifier:
    def __init__(self):
        self.pos_features = []
        self.pos_weights = []
        self.classifier = IsolationForest()

    def train(self, pos_samples, neg_samples, weight=1):
        self.pos_features = pos_samples
        self.pos_weights = [weight] * len(pos_samples)

        self._train()

    def train_iteratively(self, pos_samples, neg_samples, weight=1):
        self.pos_features += pos_samples
        self.pos_weights += [weight] * len(pos_samples)

        self._train()

    def _train(self):
        self.classifier = self.classifier.fit(self.pos_features,
                                              sample_weight=np.array(self.pos_weights))

    def predict(self, samples):
        return [p == 1 for p in self.classifier.predict(samples)]

    def get_scores(self, samples):
        return normalize(self.classifier.decision_function(samples).tolist(),
                         absolute=True)
