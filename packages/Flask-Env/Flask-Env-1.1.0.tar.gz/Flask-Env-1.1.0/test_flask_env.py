import os
import unittest

from flask_env import MetaFlaskEnv


class TestFlaskEnv(unittest.TestCase):
    def _get_test_configuration(self, env_prefix='', env_load_all=False, **kwargs):
        """Helper to define a new configuration class using our MetaFlaskEnv"""
        return MetaFlaskEnv('TestConfiguration', (object, ), dict(
            ENV_PREFIX=env_prefix,
            ENV_LOAD_ALL=env_load_all,
            **kwargs
        ))

    def test_default_env_load_all(self):
        """A test to ensure that we load all environment variables by default"""
        # Configure an environment variable not defined on the configuration class
        os.environ['TEST_SETTING'] = 'true'

        # Create our configuration object
        TestConfiguration = MetaFlaskEnv('TestConfiguration', (object, ), dict())

        # Assert that we loaded all environment variables
        self.assertTrue(TestConfiguration.TEST_SETTING)


    def test_default_settings(self):
        """A test to ensure that if no environment variable is set, we get the default value that is set"""
        TestConfiguration = self._get_test_configuration(DEFAULT_SETTING='default_value')
        self.assertEqual(TestConfiguration.DEFAULT_SETTING, 'default_value')

    def test_override_from_env(self):
        """A test to ensure that an environment variable will override the default setting"""
        # DEV: We have to set the environment variable first, since they get loaded into the class on definition
        os.environ['DEFAULT_SETTING'] = 'set_by_env'

        TestConfiguration = self._get_test_configuration(DEFAULT_SETTING='default_value')
        self.assertEqual(TestConfiguration.DEFAULT_SETTING, 'set_by_env')

    def test_only_set_on_env(self):
        """A test to ensure that a setting only defined by an environment variable is still available"""
        # DEV: We have to set the environment variable first, since they get loaded into the class on definition
        os.environ['NEW_SETTING'] = 'set_by_env'

        # When configured to load all environment variables
        TestConfiguration = self._get_test_configuration(env_load_all=True)
        self.assertEqual(TestConfiguration.NEW_SETTING, 'set_by_env')

        # When configured to not load all environment variables
        TestConfiguration = self._get_test_configuration(env_load_all=False)
        self.assertFalse(hasattr(TestConfiguration, 'NEW_SETTING'))

    def test_env_prefix(self):
        """A test to ensure that the ENV_PREFIX setting functions as needed"""
        # DEV: We have to set the environment variable first, since they get loaded into the class on definition
        os.environ['TEST_DEFAULT_SETTING'] = 'set_by_env'

        TestConfiguration = self._get_test_configuration(env_prefix='TEST_', DEFAULT_SETTING='default_value')
        self.assertEqual(TestConfiguration.DEFAULT_SETTING, 'set_by_env')

    def test_env_prefix_non_matching(self):
        """A test to ensure that the ENV_PREFIX setting does not allow non-matching settings in"""
        # DEV: We have to set the environment variable first, since they get loaded into the class on definition
        os.environ['DEFAULT_SETTING'] = 'set_by_env'

        TestConfiguration = self._get_test_configuration(env_prefix='MYAPP_', DEFAULT_SETTING='default_value')
        self.assertEqual(TestConfiguration.DEFAULT_SETTING, 'default_value')

    def test_parsing_boolean(self):
        """A test to ensure that we properly parse booleans"""
        # DEV: We have to set the environment variable first, since they get loaded into the class on definition
        os.environ['IS_TRUE'] = 'true'
        os.environ['IS_NOT_TRUE'] = 'true-ish'
        os.environ['IS_FALSE'] = 'FALSE'
        os.environ['IS_WACKY_FALSE'] = 'FaLSe'

        # DEV: Set `env_load_all=True` to keep from having to make default values for each variable
        TestConfiguration = self._get_test_configuration(env_load_all=True)
        self.assertEqual(TestConfiguration.IS_TRUE, True)
        self.assertEqual(TestConfiguration.IS_NOT_TRUE, 'true-ish')
        self.assertEqual(TestConfiguration.IS_FALSE, False)
        self.assertEqual(TestConfiguration.IS_WACKY_FALSE, False)

    def test_parsing_float(self):
        """A test to ensure that we properly parse floats"""
        # DEV: We have to set the environment variable first, since they get loaded into the class on definition
        os.environ['IS_FLOAT'] = '12.5'
        os.environ['TRAILING_DOT'] = '12.'
        os.environ['LEADING_DOT'] = '.12'
        os.environ['IS_NOT_FLOAT'] = 'This is 6.5'

        # DEV: Set `env_load_all=True` to keep from having to make default values for each variable
        TestConfiguration = self._get_test_configuration(env_load_all=True)
        self.assertEqual(TestConfiguration.IS_FLOAT, 12.5)
        self.assertEqual(TestConfiguration.TRAILING_DOT, 12.0)
        self.assertEqual(TestConfiguration.LEADING_DOT, 0.12)
        self.assertEqual(TestConfiguration.IS_NOT_FLOAT, 'This is 6.5')

    def test_parsing_int(self):
        """A test to ensure that we properly parse integers"""
        # DEV: We have to set the environment variable first, since they get loaded into the class on definition
        os.environ['IS_INT'] = '12'
        os.environ['IS_ZERO'] = '0'
        os.environ['IS_NOT_INT'] = '12fa'

        # DEV: Set `env_load_all=True` to keep from having to make default values for each variable
        TestConfiguration = self._get_test_configuration(env_load_all=True)
        self.assertEqual(TestConfiguration.IS_INT, 12)
        self.assertEqual(TestConfiguration.IS_ZERO, 0)
        self.assertEqual(TestConfiguration.IS_NOT_INT, '12fa')


if __name__ == '__main__':
    unittest.main()
