# DbConvert

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.41-blue.svg)](https://www.sqlalchemy.org/)
[![Typer](https://img.shields.io/badge/Typer-0.15.4-blue.svg)](https://typer.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/dbconvert)](https://pypi.org/project/dbconvert/)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/dbconvert?period=total&units=INTERNATIONAL_SYSTEM&left_color=GREY&right_color=BLUE&left_text=downloads)](https://pepy.tech/projects/dbconvert)
[![Author site](https://img.shields.io/badge/author-ysskrishna.space-informational)](https://ysskrishna.space)
[![Context7](https://img.shields.io/badge/Context7-docs-18181B)](https://context7.com/ysskrishna/dbconvert)
[![Ask DeepWiki](https://img.shields.io/badge/DeepWiki-ask-18181B)](https://deepwiki.com/ysskrishna/dbconvert)


Convert your PostgreSQL or MySQL database to an SQLite file with ease. DbConvert provides both a modern Command-Line Interface (CLI) and a user-friendly Graphical User Interface (GUI).

## Features

- Convert PostgreSQL databases to SQLite
- Convert MySQL databases to SQLite
- Command-line interface for fast, scriptable usage
- Graphical user interface for easy, no-code conversion
- Preserves table structures and data
- Supports all common data types
- Rich progress display and error reporting

## Installation

You can install DbConvert using pip:

```bash
pip install dbconvert
```

To use the GUI, install with the extra dependencies:

```bash
pip install dbconvert[gui]
```

## Requirements

- Python 3.8 or higher
- PostgreSQL or MySQL database to convert from
- (For GUI) Pillow >= 10.0.0

## Usage

<a id="command-line-interface-cli"></a>

<details>
<summary><b>Command Line Interface (CLI)</b></summary>

```bash
dbconvert [COMMAND] [OPTIONS]

Commands:
  convert              Convert a database to SQLite
  supported-databases  Show supported database types
  gui                  Launch the graphical user interface

Options for convert:
  --source TEXT    Source database type (postgres, mysql)  [required]
  --conn TEXT      Source database connection string         [required]
  --sqlite TEXT    Target SQLite database file path         [required]
  --help          Show this help message and exit
```

#### Connection String Format

##### PostgreSQL
```
postgresql://[user[:password]@][host][:port][/dbname]
```

##### MySQL
```
mysql://[user[:password]@][host][:port][/dbname]
```

#### CLI Examples

1. Convert a PostgreSQL database:
```bash
dbconvert convert --source postgres --conn "postgresql://user:password@dbhost:5432/mydb" --sqlite mydb.sqlite
```

2. Convert a MySQL database:
```bash
dbconvert convert --source mysql --conn "mysql://user:password@dbhost:3306/production" --sqlite prod_backup.sqlite
```

3. List supported database types:
```bash
dbconvert supported-databases
```

4. Launch the GUI:
```bash
dbconvert gui
```

</details>

<a id="graphical-user-interface-gui"></a>

<details>
<summary><b>Graphical User Interface (GUI)</b></summary>

After installing with GUI support, launch the GUI with:

```bash
dbconvert gui
```

- Select your source database type, enter the connection string, and choose the target SQLite file path.
- Click "Convert" to start the conversion process.
- The GUI provides progress and error reporting, and allows you to reset or clear output easily.

</details>

## Development

<details>
<summary><b>Set up a development environment</b></summary>

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

4. Install development dependencies with GUI support:
```
pip install -e ".[gui]"
```

</details>

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Built and maintained by

DbConvert is built and maintained by:

| | Name | GitHub | Role |
|---|------|--------|------|
| <img src="https://github.com/ysskrishna.png?size=120" width="60" height="60" alt="Y. Siva Sai Krishna"> | **Y. Siva Sai Krishna** | [@ysskrishna](https://github.com/ysskrishna) | Creator |

## Changelog

See [CHANGELOG](CHANGELOG.md) for release history.

## Support

If you find this library helpful:

- ⭐ Star the repository
- 🐛 [Report issues](https://github.com/ysskrishna/dbconvert/issues)
- 🔀 Submit pull requests
- 💝 [Sponsor on GitHub](https://github.com/sponsors/ysskrishna)

## License

MIT © [Y. Siva Sai Krishna](https://github.com/ysskrishna) — see [LICENSE](LICENSE) for details.

---

<p align="left">
  <a href="https://github.com/ysskrishna">Author's GitHub</a> •
  <a href="https://linkedin.com/in/ysskrishna">Author's LinkedIn</a> •
  <a href="https://ysskrishna.space">Author's site</a> •
  <a href="https://pypi.org/project/dbconvert/">Package on PyPI</a> •
  <a href="https://github.com/ysskrishna/dbconvert/issues">Report Issues</a>
</p>
