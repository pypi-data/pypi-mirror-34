import numpy as np

def get_by_condition(preds, truths, confidences, condition):
    indexed_confidences = np.where(condition(preds, truths))
    return confidences[indexed_confidences[0]]

def get_incorrect_confidences(preds, truths, confidences):
    return get_by_condition(preds,truths, confidences, np.not_equal)

def  get_correct_confidences(preds, truths, confidences):
    return get_by_condition(preds, truths, confidences, np.equal)

def get_error_confidences(truths, confidences):
    return get_by_condition(truths, 1,confidences, np.equal)

def get_non_error_confidences(truths, confidences):
    return get_by_condition(truths, 0, confidences, np.equal)