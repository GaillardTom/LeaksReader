# Email Search in Files

This project allows you to search for a specific string (ex: email) within files or directories. It supports `.sql`, `.txt`, and `.csv` file formats but can be ajusted with the allowed_extensions list. Note: as most leaks are not sorted the script read the file line by line.
## Requirements

- Python 3.x
- `tqdm` library

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install tqdm to have clean progress bar: 
    ```sh
    pip install tqdm  
    ```
3. Have your leaks ready in a directory!

## Usage

1. Run the script:
    ```sh
    python readLeaks.py
    ```

2. Enter the email address you want to search for when prompted.

3. Enter the file or directory name to search in. If no path is provided it will look in the current directory.
## Example

```sh
Enter email to search: (No check for validity of email) example@example.com
Enter file or directory name to search in (default: ./): ./data
```

## TODO

- Accept Multiple strings 
- Instead of input pass arguments to the script? 
- Quick Timer ? 
- Clean up the console cleaning process