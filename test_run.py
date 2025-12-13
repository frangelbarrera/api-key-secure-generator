import base64
import unittest
from unittest.mock import patch

import run

class TestKeyGen(unittest.TestCase):
    """Comprehensive unit tests for the secure key generation system."""

    def test_default_key_generation(self):
        """Verify key creation with standard 32-byte size."""
        key = run.generate_secure_key(32)
        decoded = base64.urlsafe_b64decode(key + '==')
        self.assertEqual(len(decoded), 32)

    @patch('run.os.getenv')
    def test_main_process(self, mock_env):
        """Validate main execution flow under controlled conditions."""
        mock_env.return_value = '32'
        with patch('builtins.print') as mock_output:
            run.main()
            mock_output.assert_called_once()

    def test_custom_key_generation(self):
        """Check key production for non-standard 64-byte size."""
        key = run.generate_secure_key(64)
        decoded = base64.urlsafe_b64decode(key + '==')
        self.assertEqual(len(decoded), 64)

    @patch('run.os.getenv')
    def test_main_with_custom_size(self, mock_env):
        """Test main with user-defined key size."""
        mock_env.return_value = '64'
        with patch('builtins.print') as mock_output:
            run.main()
            mock_output.assert_called_once()
            generated_key = mock_output.call_args[0][0]
            decoded = base64.urlsafe_b64decode(generated_key + '==')
            self.assertEqual(len(decoded), 64)

    @patch('run.os.getenv')
    def test_main_with_bad_input(self, mock_env):
        """Ensure proper error handling for incorrect inputs."""
        mock_env.return_value = 'invalid'
        with self.assertRaises(ValueError):
            run.main()