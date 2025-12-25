# LinkRunner Recovery

[![CI](https://github.com/krisarmstrong/linkrunner-recovery/actions/workflows/ci.yml/badge.svg)](https://github.com/krisarmstrong/linkrunner-recovery/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.14+-3776AB?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue)](CHANGELOG.md)

Recover and update MAC address, serial number, and option bits on NetAlly LinkRunner Pro/Duo devices.

## Features

- **Cross-platform** - Windows, Linux, and macOS support
- **Auto-detection** - Automatically finds connected LinkRunner device
- **MAC address recovery** - Update device MAC address
- **Serial number update** - Set device serial number
- **Option bits** - Configure 802.1x, Reports, and Reflector options
- **Logging** - Rotating log files for troubleshooting

## Installation

```bash
pip install linkrunner-recovery
```

Or run directly:

```bash
git clone https://github.com/krisarmstrong/linkrunner-recovery.git
cd linkrunner-recovery
python linkrunner_recovery.py --help
```

## Usage

Connect your LinkRunner Pro/Duo device in recovery mode, then run:

```bash
linkrunner-recovery --mac_address 00:11:22:33:44:55 --serial_number LR123456
```

### Options

| Option | Description |
|--------|-------------|
| `--mac_address` | MAC address (XX:XX:XX:XX:XX:XX format) - Required |
| `--serial_number` | Device serial number - Required |
| `--opt_8021x` | 802.1x option bit (0=disabled, 1=enabled) |
| `--opt_reports` | Reports option bit (0=disabled, 1=enabled) |
| `--opt_reflector` | Reflector option bit (0=disabled, 1=enabled) |
| `--verbose` | Enable verbose console output |
| `--logfile` | Path to log file |
| `--version` | Show version |

### Examples

```bash
# Basic recovery
linkrunner-recovery --mac_address 00:11:22:33:44:55 --serial_number LR123456

# Enable all options
linkrunner-recovery --mac_address 00:11:22:33:44:55 --serial_number LR123456 \
    --opt_8021x 1 --opt_reports 1 --opt_reflector 1

# Verbose with custom log file
linkrunner-recovery --mac_address 00:11:22:33:44:55 --serial_number LR123456 \
    --verbose --logfile /var/log/linkrunner.log
```

## How It Works

1. Detects the LinkRunner device mounted as a USB drive
2. Writes commands to `command.txt` on the device
3. Reads results from `results.txt`
4. Reports success or failure for each operation

### Device Detection

| Platform | Search Locations |
|----------|-----------------|
| Windows | All drive letters (A-Z) |
| Linux | `/mnt/*`, `/media/*` |
| macOS | `/Volumes/*` |

The tool looks for either:
- A volume labeled "LR"
- A `linkrunner.id` marker file

## License

MIT License - see [LICENSE](LICENSE)

## Contributing

Issues and pull requests welcome. See [CHANGELOG.md](CHANGELOG.md) for version history.
