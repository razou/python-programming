
import functools
import importlib
import numpy as np
from typing import Optional, Union
from sklearn.metrics import precision_score, recall_score, roc_auc_score, accuracy_score, top_k_accuracy_score

def _score(
    metric: str, 
    y_true: list, 
    y_pred: Optional[list] = None, 
    y_score: Optional[list] = None, 
    average: Optional[str] = 'micro', 
    k: Optional[int] = 3
) -> Union[float, np.ndarray]:
    
    VALID_METRICS = ["precision_score", "recall_score", "roc_auc_score", "accuracy_score", 
                     "top_k_accuracy_score"]

    if metric not in VALID_METRICS:
        raise ValueError(f"Expecting one of {VALID_METRICS} but found '{metric}'")


    try:
        scorer_function = importlib.import_module("sklearn.metrics")
        objective_scorer = getattr(scorer_function, metric)
    except (ModuleNotFoundError, AttributeError):
        raise ValueError(f"Unable to find the metric '{metric}' in sklearn.metrics")


    if metric in ["precision_score", "recall_score", "roc_auc_score"]:
        objective_scorer = functools.partial(objective_scorer, average=average)

    if metric in ['top_k_accuracy_score']:
        objective_scorer = functools.partial(objective_scorer, k=k)


    if metric in ["top_k_accuracy_score", "roc_auc_score"]:
        if y_score is None:
            raise ValueError(f"The parameter 'y_score' is missing")
        scores = objective_scorer(y_true=y_true, y_score=y_score)
    else:
        scores = objective_scorer(y_true=y_true, y_pred=y_pred)

    
    return scores

if __name__ == "__main__":
        # More advanced (with sklearn metrics)
    
    y_true = [1, 1, 0, 1, 0]
    y_pred = [1, 0, 0, 1, 1]
    y_score = [0.8, 0.6, 0.3, 0.9, 0.7]

    metrics = ["precision_score", "recall_score", "roc_auc_score", "accuracy_score", "top_k_accuracy_score"]
    n_classes = len(set(y_true))

    for metric in metrics:
        try:
            if metric == "top_k_accuracy_score":
                k = min(n_classes - 1, 2)  # Adjust the value of k based on the number of classes
                score = _score(metric, y_true, y_pred, y_score, k=k)
            else:
                score = _score(metric, y_true, y_pred, y_score)
            print(f"{metric}: {score:.3}")
        except ValueError as e:
            print(f"Error: {e}")
