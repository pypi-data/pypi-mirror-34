from os.path import dirname


class TrainTestCase(object):

    def test_fit_without_valid_ratio_0(self):
        self.model.fit(
            subtrain_x=self.x_train,
            subtrain_seqlen=self.seqlen_train,
            valid_ratio=0.0,
            epochs=2,
        )

    def test_fit_without_valid_ratio_01(self):
        self.model.fit(
            subtrain_x=self.x_train,
            subtrain_seqlen=self.seqlen_train,
            valid_ratio=0.1,
            epochs=2,
            output_dir=dirname(self.model_path),
        )

    def test_fit_and_encode(self):
        self.model.fit(
            subtrain_x=self.x_train,
            subtrain_seqlen=self.seqlen_train,
            valid_ratio=0.1,
            epochs=2,
        )
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
                    single_result[0].shape,
                )
                self.assertEqual(
                    (self.model.latent_size,),
                    single_result[1].shape,
                )

    def test_fit_and_get_latent_vector(self):
        self.model.fit(
            subtrain_x=self.x_train,
            subtrain_seqlen=self.seqlen_train,
            valid_ratio=0.1,
            epochs=2,
        )
        result = self.model.get_latent_vector(
            x=self.x_test,
            seqlen=self.seqlen_test,
            batch_size=1,
        )
        for i, single_result in enumerate(result):
            with self.subTest(i=i):
                self.assertEqual(
                    (self.model.latent_size,),
                    single_result[0].shape,
                )

    def test_fit_and_evaluate(self):
        self.model.fit(
            subtrain_x=self.x_train,
            subtrain_seqlen=self.seqlen_train,
            valid_ratio=0.1,
            epochs=2,
        )
        self.model.evaluate(
            x=self.x_test,
            seqlen=self.seqlen_test,
            batch_size=2,
        )

    def test_fit_save_and_restore(self):
        self.model.fit(
            subtrain_x=self.x_train,
            subtrain_seqlen=self.seqlen_train,
            valid_ratio=0.1,
            epochs=2,
        )
        self.model.save(path=self.model_path)
        del self.model
        self.model = self.model_class.load(self.model_path)
        result = self.model.get_latent_vector(
            x=self.x_test,
            seqlen=self.seqlen_test,
            batch_size=1,
        )
        for i, single_result in enumerate(result):
            with self.subTest(i=i):
                self.assertEqual(
                    (self.model.latent_size,), single_result[0].shape)

    def test_fit_save_and_restore_and_refit(self):
        self.model.fit(
            subtrain_x=self.x_train,
            subtrain_seqlen=self.seqlen_train,
            valid_ratio=0.1,
            epochs=2,
        )
        self.model.save(path=self.model_path)
        del self.model
        # restore
        self.model = self.model_class.load(self.model_path)
        # retrain
        self.model.fit(
            subtrain_x=self.x_train,
            subtrain_seqlen=self.seqlen_train,
            valid_ratio=0.1,
            epochs=2,
        )

    def test__train_on_batch(self):
        result = self.model._train_on_batch(
            x_batch=self.x_train,
            seqlen_batch=self.seqlen_train,
            learning_rate=0.001,
        )
        self.assertAllEqual(
            set(["decoder_output_indices", "reconstruction_loss",
                 "kl_divergent", "vae_loss", "total_loss"]),
            set(result[1].keys()),
        )

    def test__get_latent_vector_on_batch(self):
        result = self.model._get_latent_vector_on_batch(
            x_batch=self.x_train,
            seqlen_batch=self.seqlen_train,
        )
        self.assertEqual(5, len(result))
        self.assertEqual((self.model.latent_size, ), result[0][0].shape)

    def test__encode_on_batch(self):
        result = self.model._encode_on_batch(
            x_batch=self.x_train,
            seqlen_batch=self.seqlen_train,
        )
        self.assertEqual(5, len(result))
        for i, single_result in enumerate(result):
            with self.subTest(i=i):
                self.assertEqual((self.model.latent_size,),
                                 single_result[0].shape)
                self.assertEqual((self.model.latent_size,),
                                 single_result[1].shape)

    def test__evaluate_on_batch(self):
        result = self.model._evaluate_on_batch(
            x_batch=self.x_train,
            seqlen_batch=self.seqlen_train,
        )
        self.assertEqual(result[0], result[1]["total_loss"])
        self.assertEqual(
            set(["decoder_output_indices", "reconstruction_loss",
                 "kl_divergent", "vae_loss", "total_loss"]),
            set(result[1].keys()),
        )
