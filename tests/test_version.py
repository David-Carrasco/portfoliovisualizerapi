import unittest

import portfoliovisualizerapi


class VersionTestCase(unittest.TestCase):
    """ Version tests """

    def test_version(self):
        """ check portfoliovisualizerapi exposes a version attribute """
        self.assertTrue(hasattr(portfoliovisualizerapi, "__version__"))
        self.assertIsInstance(portfoliovisualizerapi.__version__, str)


if __name__ == "__main__":
    unittest.main()
