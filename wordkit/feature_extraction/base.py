"""Base class for feature extractors."""
from itertools import chain


class BaseExtractor(object):
    """
    Base class for feature extractors.

    EXTRA STUFF HERE

    """

    def __init__(self, field=None):
        """Initialize the extractor."""
        self.features = {}
        self.field = field

    def extract(self, X):
        """Extract features from a set of words."""
        if self.field is not None:
            X = [x[self.field] for x in X]
        elif isinstance(X, dict):
            raise ValueError("You didn't pass a field value to the extractor "
                             "but also passed a dict.")

        if isinstance(X[0][0], str):
            all_symbols = set(chain.from_iterable(X))
        elif isinstance(X[0][0], tuple):
            x_ = [chain.from_iterable(x) for x in X]
            all_symbols = set(chain.from_iterable(x_))
        else:
            raise ValueError("Couldn't recognize type of data passed.")

        self.features = self._process(all_symbols)
        return self.features

    def _process(self, symbols):
        """Process the symbols and return features."""
        raise NotImplemented()
