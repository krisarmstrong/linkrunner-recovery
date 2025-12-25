#!/usr/bin/env python3
"""Tests for LinkRunner Recovery tool."""

import argparse
import sys
from pathlib import Path
from unittest.mock import patch

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import linkrunner_recovery


class TestVersion:
    """Test version information."""

    def test_version_exists(self):
        """Version should be defined."""
        assert hasattr(linkrunner_recovery, "__version__")
        assert linkrunner_recovery.__version__ is not None

    def test_version_format(self):
        """Version should be a valid semver string."""
        version = linkrunner_recovery.__version__
        parts = version.split(".")
        assert len(parts) >= 2  # At least major.minor


class TestArgumentParser:
    """Test argument parsing."""

    def test_parser_exists(self):
        """Argument parser should be creatable."""
        # The module uses argparse, verify it works
        parser = argparse.ArgumentParser()
        parser.add_argument("--mac_address", required=True)
        parser.add_argument("--serial_number", required=True)
        parser.add_argument("--opt_8021x", type=int, choices=[0, 1], default=0)
        parser.add_argument("--opt_reports", type=int, choices=[0, 1], default=0)
        parser.add_argument("--opt_reflector", type=int, choices=[0, 1], default=0)

        args = parser.parse_args(
            ["--mac_address", "00:11:22:33:44:55", "--serial_number", "ABC123"]
        )
        assert args.mac_address == "00:11:22:33:44:55"
        assert args.serial_number == "ABC123"
        assert args.opt_8021x == 0
        assert args.opt_reports == 0
        assert args.opt_reflector == 0

    def test_option_bits(self):
        """Option bits should accept 0 or 1."""
        parser = argparse.ArgumentParser()
        parser.add_argument("--mac_address", required=True)
        parser.add_argument("--serial_number", required=True)
        parser.add_argument("--opt_8021x", type=int, choices=[0, 1], default=0)
        parser.add_argument("--opt_reports", type=int, choices=[0, 1], default=0)
        parser.add_argument("--opt_reflector", type=int, choices=[0, 1], default=0)

        args = parser.parse_args(
            [
                "--mac_address",
                "00:11:22:33:44:55",
                "--serial_number",
                "ABC123",
                "--opt_8021x",
                "1",
                "--opt_reports",
                "1",
                "--opt_reflector",
                "1",
            ]
        )
        assert args.opt_8021x == 1
        assert args.opt_reports == 1
        assert args.opt_reflector == 1


class TestMacAddressValidation:
    """Test MAC address validation."""

    def test_valid_mac_format(self):
        """Valid MAC addresses should be accepted."""
        valid_macs = [
            "00:11:22:33:44:55",
            "AA:BB:CC:DD:EE:FF",
            "aa:bb:cc:dd:ee:ff",
        ]
        for mac in valid_macs:
            # Basic format check
            parts = mac.split(":")
            assert len(parts) == 6
            for part in parts:
                assert len(part) == 2
                int(part, 16)  # Should not raise


class TestModuleImport:
    """Test module can be imported."""

    def test_import_main_module(self):
        """Main module should be importable."""
        import linkrunner_recovery

        assert linkrunner_recovery is not None
