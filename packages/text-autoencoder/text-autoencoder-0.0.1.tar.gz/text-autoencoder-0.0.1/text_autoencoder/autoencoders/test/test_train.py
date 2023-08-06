from os.path import join, dirname
from glob import glob

import tensorflow as tf

from batching.batch_generator import BatchGenerator
from batching.batch_loader import BatchLoader


class TrainTestCase(object):

    def serving_output_test(self, output_dir):
        self.assertEqual(
            set(
                [
                    join(
                        output_dir,
                        '0',
                        filename,
                    ) for filename in [
                        'saved_model.pb',
                        'variables',
                        'variables/variables.data-00000-of-00001',
                        'variables/variables.index',
                    ]
                ],
            ),
            set(
                glob(output_dir + '/*/*') +
                glob(output_dir + '/*/*/*'),
            ),
        )

    def test_fit(self):
        self.model.fit(
            x=self.x_train,
            seqlen=self.seqlen_train,
            valid_ratio=0.0,
            epochs=2,
            output_path=self.model_path,
        )
        self.model.fit(
            x=self.x_train,
            seqlen=self.seqlen_train,
            valid_ratio=0.3,
            epochs=2,
            output_path=self.model_path,
        )

    def test_fit_generator(self):
        subtrain_batch_generator = BatchGenerator(
            [self.x_train, self.seqlen_train],
            batch_size=2,
        )
        valid_loader = BatchLoader(
            [self.x_test, self.seqlen_test],
            batch_size=2,
        )

        self.model.fit_generator(
            subtrain_batch_generator=subtrain_batch_generator,
            valid_batch_loader=valid_loader,
            output_path=self.model_path,
            max_iter=2,
            assist_max_iter=2,
            display_period=1,
        )

    def test_encode(self):
        result = self.model.encode(
            x=self.x_test,
            seqlen=self.seqlen_test,
            batch_size=1,
        )
        self.assertEqual(2, len(result))
        for i, single_result in enumerate(result):
            with self.subTest(i=i):
                self.assertEqual(
                    (self.model.latent_size,),
                    single_result.shape,
                )

    def test_evaluate(self):
        loss, info = self.model.evaluate(
            x=self.x_test,
            seqlen=self.seqlen_test,
            batch_size=2,
        )
        self.assertEqual((), loss.shape)

    def test_save(self):
        self.model.save(path=self.model_path)
        self.assertEqual(
            set(
                [
                    self.model_path + '_{}'.format(
                        self.model.__class__.__name__) + filename
                    for filename in [
                        '-param.pkl',
                        '-variable.model.data-00000-of-00001',
                        '-variable.model.index',
                        '-variable.model.meta',
                    ]
                ],
            ),
            set(glob(self.model_path + '*')),
        )

    def test_load(self):
        self.model.save(path=self.model_path)
        del self.model
        self.model = self.model_class.load(self.model_path)

    def test_load_then_fit(self):
        self.model.save(path=self.model_path)
        del self.model
        self.model = self.model_class.load(self.model_path)
        self.model.fit(
            x=self.x_train,
            seqlen=self.seqlen_train,
            valid_ratio=0.0,
            epochs=2,
            output_path=self.model_path,
        )

    def test_save_tf_serving(self):
        output_dir = dirname(self.model_path)
        saver = self.model.set_tf_serving_saver(
            output_dir=output_dir,
        )
        self.model.save_tf_serving(saver)
        self.serving_output_test(output_dir=output_dir)

        # load
        with tf.Session(graph=tf.Graph()) as sess:
            meta_graph_def = tf.saved_model.loader.load(
                sess=sess,
                tags=[tf.saved_model.tag_constants.SERVING],
                export_dir=join(output_dir, '0'),
            )
            encode_graph = meta_graph_def.signature_def['encode']
            vector = sess.run(
                sess.graph.get_tensor_by_name(
                    encode_graph.outputs['vector'].name),
                feed_dict={
                    sess.graph.get_tensor_by_name(
                        encode_graph.inputs['x'].name):
                    self.x_train,
                    sess.graph.get_tensor_by_name(
                        encode_graph.inputs['seqlen'].name):
                    self.seqlen_train,
                },
            )
            self.assertEqual((5, self.latent_size), vector.shape)

    def test_fit_n_save_tf_serving(self):
        self.model.fit(
            x=self.x_train,
            seqlen=self.seqlen_train,
            valid_ratio=0.0,
            epochs=2,
            output_path=self.model_path,
            save_tf_serving=True,
        )
        output_dir = dirname(self.model_path)
        self.serving_output_test(output_dir=output_dir)

    def test_fit_generator_n_save_tf_serving(self):
        subtrain_batch_generator = BatchGenerator(
            [self.x_train, self.seqlen_train],
            batch_size=2,
        )
        valid_loader = BatchLoader(
            [self.x_test, self.seqlen_test],
            batch_size=2,
        )
        self.model.fit_generator(
            subtrain_batch_generator=subtrain_batch_generator,
            valid_batch_loader=valid_loader,
            output_path=self.model_path,
            max_iter=1,
            assist_max_iter=1,
            display_period=1,
            save_tf_serving=True,
        )
        output_dir = dirname(self.model_path)
        self.serving_output_test(output_dir=output_dir)
