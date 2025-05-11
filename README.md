# DbConvert

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.41-blue.svg)](https://www.sqlalchemy.org/)
[![Typer](https://img.shields.io/badge/Typer-0.15.4-blue.svg)](https://typer.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Convert your PostgreSQL or MySQL database to an SQLite file with ease.

## Features

- Convert PostgreSQL databases to SQLite
- Convert MySQL databases to SQLite
- Command-line interface for easy usage
- Preserves table structures and data
- Supports all common data types
- Rich progress display and error reporting

## Installation

You can install DbConvert using pip:

```bash
pip install dbconvert
```

## Requirements

- Python 3.8 or higher
- PostgreSQL or MySQL database to convert from

## Usage

### Command Line Options

```bash
dbconvert [COMMAND] [OPTIONS]

Commands:
  convert              Convert a database to SQLite
  supported-databases  Show supported database types

Options for convert:
  --source TEXT    Source database type (postgresql, mysql)  [required]
  --conn TEXT      Source database connection string         [required]
  --sqlite TEXT    Target SQLite database file path         [required]
  --help          Show this help message and exit
```

### Connection String Format

#### PostgreSQL
```
postgresql://[user[:password]@][host][:port][/dbname]
```

#### MySQL
```
mysql://[user[:password]@][host][:port][/dbname]
```

### Examples

1. Convert a PostgreSQL database:
```bash
dbconvert convert --source postgresql --conn "postgresql://user:password@dbhost:5432/mydb" --sqlite mydb.sqlite
```

1. Convert a MySQL database:
```bash
dbconvert convert --source mysql --conn "mysql://user:password@dbhost:3306/production" --sqlite prod_backup.sqlite
```

1. List supported database types:
```bash
dbconvert supported-databases
```

## Development

### Setup Development Environment

1. Clone the repository:
```bash
git clone https://github.com/ysskrishna/dbconvert.git
cd dbconvert
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -e .
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/ysskrishna/dbconvert/issues) on GitHub.  