import logging
from os.path import join, dirname, isdir
import pickle as pkl

from serving_utils import Saver
from mkdir_p import mkdir_p
from bistiming import SimpleTimer

LOGGER = logging.getLogger(__name__)


class StorageManager(object):

    @classmethod
    def _gen_hyper_param_path(cls, output_path: str):
        hyper_param_path = "{}_{}-param.pkl".format(
            output_path,
            cls.__name__,
        )
        return hyper_param_path

    @classmethod
    def _gen_variable_path(cls, output_path: str):
        variable_path = "{}_{}-variable.model".format(
            output_path,
            cls.__name__,
        )
        return variable_path

    def save(
            self,
            path: str,
            hyper_params: dict,
        ) -> None:
        """
        hyper_params = {
            "input_dim": 300,
            "output_dim": 10,
        }
        """
        mkdir_p(dirname(path))
        with SimpleTimer(
            "Saving model to {}".format(path),
            logger=self.logger,
        ):
            if not self.hyper_params_saved:
                self.save_hyper_params(
                    hyper_params=hyper_params,
                    output_path=path,
                )
            self.save_model(path)

    def save_hyper_params(
            self,
            hyper_params: dict,
            output_path: str,
        ) -> None:

        hyper_param_path = self._gen_hyper_param_path(output_path)
        self.logger.info("Saving parameters from {}".format(hyper_param_path))
        with open(hyper_param_path, "wb") as fw:
            pkl.dump(hyper_params, fw)

        self.hyper_params_saved = True

    def save_model(
            self,
            output_path: str,
        ) -> None:

        variable_path = self._gen_variable_path(output_path)
        self.logger.info("Saving model to {}".format(variable_path))
        self.saver.save(self.sess, variable_path)

    def set_tf_serving_saver(
            self,
            output_dir: str,
        ) -> Saver:

        with SimpleTimer(
            'Setting tensorflow serving saver to {}'.format(output_dir),
            logger=self.logger,
        ):
            if not isdir(output_dir):
                mkdir_p(output_dir)
            saver = Saver(
                session=self.sess,
                output_dir=output_dir,
                signature_def_map=self.define_signature(),
            )

        return saver

    def save_tf_serving(
            self,
            tf_serving_saver: Saver,
        ) -> None:

        # if not self.hyper_params_saved:
        #     self.save_hyper_params(
        #         hyper_params=self.hyper_params,
        #         output_path=join(tf_serving_saver.output_dir, ''),
        #     )

        next_version_dir = tf_serving_saver.save()
        self.logger.info(
            'Saving serving models to {}'.format(next_version_dir),
        )

    @classmethod
    def load(
            cls,
            path: str,
            logger: logging.Logger = LOGGER,
        ) -> object:
        """Load trained parameters.
        Use this method when load model to the cache.
        >>> clf = XXX.load("path/to/model")
        >>> y = clf.predict(x)
        """
        cls.model_name = cls.__name__
        params = cls.load_hyper_params(
            output_path=path,
            logger=logger,
        )
        model = cls.load_model(
            output_path=path,
            hyper_params=params,
            logger=logger,
        )
        return model

    @classmethod
    def load_hyper_params(
            cls,
            output_path: str,
            logger: logging.Logger = LOGGER,
        ) -> dict:

        # case: tensorflow serving
        if isdir(output_path):
            output_path = join(output_path, '')

        hyper_param_path = cls._gen_hyper_param_path(output_path)
        with SimpleTimer(
            "Loading hyper parameters from {}".format(hyper_param_path),
            logger=logger,
        ):
            with open(hyper_param_path, "rb") as f:
                params = pkl.load(f)
        return params

    @classmethod
    def load_model(
            cls,
            output_path: str,
            hyper_params: dict,
            logger: logging.Logger = LOGGER,
        ) -> object:

        variable_path = cls._gen_variable_path(output_path)
        with SimpleTimer(
            "Loading model {}".format(variable_path),
            logger=logger,
        ):
            model = cls(**hyper_params)
            model.saver.restore(model.sess, variable_path)
        return model
