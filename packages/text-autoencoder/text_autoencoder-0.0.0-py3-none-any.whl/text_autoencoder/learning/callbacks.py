
from os.path import join

from bistiming import SimpleTimer
from mkdir_p import mkdir_p


def get_improvement(current_loss, min_loss, epsilon=1e-3):
    diff = abs(min_loss - current_loss)
    if (current_loss < min_loss) & (diff > epsilon):
        return current_loss, True
    else:
        return min_loss, False


class ModelCheckpoint(object):

    def __init__(self, sess, saver,
                 output_dir, period=1,
                 save_best_only=False):
        self.sess = sess
        self.saver = saver
        self.output_dir = output_dir
        self.period = period
        self.save_best_only = save_best_only
        if save_best_only:
            print('save best model only !!!!')
        else:
            print('save model per {} epoches'.format(period))

    def __call__(self, epoch, model_name, improvement):
        save_model = self.should_save(epoch, improvement)
        if save_model is True:
            if self.save_best_only is True:
                self.save(model_name, 0)
            else:
                self.save(model_name, epoch)

    def should_save(self, epoch, improvement):
        save_model = False
        if self.save_best_only is True:
            if improvement is True:
                save_model = True
        else:
            if (epoch > 0) & (epoch % self.period == 0):
                save_model = True
        return save_model

    def save(self, model_name, epoch):
        mkdir_p(self.output_dir)
        if epoch == 0:
            announcement = 'Saving best model...'
        else:
            announcement = 'Saving model at epoch {}'.format(epoch)
        with SimpleTimer(announcement):
            self.saver.save(self.sess, join(
                self.output_dir, model_name), global_step=epoch)


class EarlyStopping(object):

    def __init__(self, patience):
        if isinstance(patience, int):
            self.patience = patience
            self.count = 0
        else:
            raise TypeError(
                'The datatype of patience is {}, it must be INTEGER !!!'.format(
                    type(patience)))

    def __call__(self, improvement):
        if improvement is True:
            self.count = 0
        else:
            self.count += 1
            if self.count > self.patience:
                return True
        return False


class ReduceLearningRate(object):

    def __init__(self, reduce_rate, patience, cooldown,
                 min_learning_rate):
        self.reduce_rate = reduce_rate
        self.patience = patience
        self.cooldown = cooldown
        self.min_learning_rate = min_learning_rate
        self.count_unimprovement = 0
        self.count_improvement = 0
        self.history = []

    def __call__(self, improvement, learning_rate):

        output = self.reduce_learning_rate(False, learning_rate)
        reduce_or_not = False

        if improvement is False:
            # from state imp to unimp
            if self.count_improvement > 0:
                self.count_improvement = 0
                self.count_unimprovement = 0

            self.count_unimprovement += 1
            if self.count_unimprovement > self.patience:
                output = self.reduce_learning_rate(True, learning_rate)
                reduce_or_not = True

        elif (improvement is True) & (self.count_unimprovement > 0):
            self.count_improvement += 1
            if ((self.count_improvement < (self.cooldown + 1)) &
                    (self.count_unimprovement > self.patience)):
                output = self.reduce_learning_rate(True, learning_rate)
                reduce_or_not = True

        if output < self.min_learning_rate:
            self.store_history(learning_rate)
            return learning_rate, not reduce_or_not
        else:
            self.store_history(output)
            return output, reduce_or_not

    def reduce_learning_rate(self, reduce_or_not, learning_rate):
        if reduce_or_not is True:
            return learning_rate * self.reduce_rate
        else:
            return learning_rate

    def store_history(self, learning_rate):
        self.history.append(learning_rate)
