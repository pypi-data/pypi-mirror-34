# pylint: disable=all
import torch

class EpochMetric:
    def update(self, y_pred, y_true):
        raise NotImplementedError

    def compute(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

class FScore(EpochMetric):
    def __init__(self, num_classes=None, *, beta=1, average='micro'):
        self.num_classes = num_classes
        if self.num_classes is None:
            if average == 'binary':
                self.num_classes = 2
            else:
                raise ValueError("'num_classes' has to be specified when average mode is 'binary'.")
        self.beta = beta
        self.average = average
        if self.average not in ['binary', 'micro', 'macro', 'weighted']:
            raise ValueError("'%s' is not a valid average mode." % self.average)

        self.__name__ = 'f1score' if beta == 1 else 'fbetascore'
        self.initialized = False

    def _init_counts(self, dummy):
        self.true_pos = dummy.new_zeros(self.num_classes, dtype=torch.long)
        self.true_sum = dummy.new_zeros(self.num_classes, dtype=torch.long)
        self.pred_sum = dummy.new_zeros(self.num_classes, dtype=torch.long)
        self.class_range = dummy.new_empty(self.num_classes, dtype=torch.long)
        self.class_range = torch.arange(self.num_classes, out=self.class_range)
        self.initialized = True

    def update(self, y_pred, y_true):
        if not self.initialized:
            self._init_counts(y_pred)
        _, y_pred = y_pred.max(1)

        one_hot_pred = (y_pred.unsqueeze(-1) == self.class_range).long()
        one_hot_true = (y_true.unsqueeze(-1) == self.class_range).long()

        self.true_pos += (one_hot_true * one_hot_pred).sum(0)
        self.true_sum += one_hot_true.sum(0)
        self.pred_sum += one_hot_pred.sum(0)

    def compute(self):
        if not self.initialized:
            return 0.

        tp = self.true_pos.float()
        true_sum = self.true_sum.float()
        pred_sum = self.pred_sum.float()
        if self.average == 'micro':
            tp = tp.sum()
            true_sum = true_sum.sum()
            pred_sum = pred_sum.sum()

        precision = tp / pred_sum
        recall = tp / true_sum
        beta2 = self.beta ** 2
        f_score = ((1 + beta2) * precision * recall /
                   (beta2 * precision + recall))
        f_score[tp == 0] = 0.0

        if self.average == 'weighted':
            weights = true_sum / true_sum.sum()
            return (f_score * weights).sum()
        elif self.average == 'binary':
            return f_score[1]
        else:
            return f_score.mean()

    def reset(self):
        if self.initialized:
            self.true_pos.zero_()
            self.true_sum.zero_()
            self.pred_sum.zero_()

def main():
    num_classes = 2
    #y_true, y_pred = torch.LongTensor([1,2,3,4]), torch.LongTensor([2,2,3,5])
    y_true, y_pred = torch.LongTensor([0,1,1,1,0]), torch.LongTensor([0,0,1,0,0])
    #y_true, y_pred = torch.LongTensor([0, 1, 2, 0, 1, 2]), torch.LongTensor([0, 2, 1, 0, 0, 1])
    print(y_true, y_pred)

    class_range = torch.arange(num_classes, dtype=torch.long)
    one_hot_pred = (y_pred.unsqueeze(-1) == class_range).float()

    f = FScore(num_classes, average='binary')
    f.update(one_hot_pred, y_true)
    print(f.compute())
    f.reset()

if __name__ == '__main__':
    main()
