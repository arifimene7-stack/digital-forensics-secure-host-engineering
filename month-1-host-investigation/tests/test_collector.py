import unittest

import security_collector


class TestSecurityCollector(unittest.TestCase):

    def test_redaction_password(self):
        value = "password=mySecret123"
        result = security_collector.redact_text(value)

        self.assertNotIn("mySecret123", result)
        self.assertIn("[REDACTED]", result)

    def test_redaction_token(self):
        value = "token=ABC123SECRET"
        result = security_collector.redact_text(value)

        self.assertNotIn("ABC123SECRET", result)
        self.assertIn("[REDACTED]", result)

    def test_run_command_success(self):
        result = security_collector.run_command(
            ["printf", "security-test"]
        )

        self.assertEqual(result["return_code"], 0)
        self.assertEqual(
            result["stdout"],
            "security-test"
        )

    def test_run_command_failure(self):
        result = security_collector.run_command(
            ["command-that-does-not-exist"]
        )

        self.assertIsNone(result["return_code"])
        self.assertNotEqual(
            result["stderr"],
            ""
        )


if __name__ == "__main__":
    unittest.main()
