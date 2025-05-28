# Show My Wifis

![Show My Wifis Banner](https://i.imgur.com/FofEhUJ.png)

A Python script to display and manage saved Wi-Fi networks on Linux systems.

## Features

- Display all saved Wi-Fi networks with their passwords
- Search networks by name
- Export network information to a text file
- Show last connection date for each network
- Colorful terminal interface
- Interactive menu system

## Requirements

- Python 3.x
- Linux operating system
- NetworkManager
- Superuser privileges (sudo)

## Dependencies

The script requires the following Python packages:
- tabulate
- colorama

## Installation

1. Clone this repository or download the files:
```bash
git clone https://github.com/yourusername/showmywifis.git
cd showmywifis
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script with superuser privileges:
```bash
sudo python3 showmywifis.py
```

### Menu Options

1. **Show all networks**
   - Displays a table with all saved Wi-Fi networks
   - Shows network name, password, and last connection date

2. **Search network by name**
   - Allows searching for specific networks
   - Case-insensitive search
   - Shows matching networks in a table format

3. **Export to file**
   - Exports all network information to a text file
   - Default filename: `wifi_networks.txt`
   - Custom filename can be specified

4. **Exit**
   - Closes the program

## Security Notice

⚠️ **IMPORTANT**: This script requires superuser privileges to access Wi-Fi credentials. Use it responsibly and only on systems you own or have permission to access.

## File Structure

```
showmywifis/
├── showmywifis.py    # Main script
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a new branch
3. Making your changes
4. Submitting a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Created by Br3noAraujo

## Disclaimer

This tool is for educational and legitimate purposes only. Always respect privacy and security laws when using this script. 
