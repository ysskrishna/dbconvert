# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2025-05-31

### Added
- Introduced a GUI version of dbconvert, including a new `dbconvert.gui` package and application window.
- Added GUI assets: application icon and logo.
- Added optional dependencies for GUI support.
- Implemented reset and clear output buttons in the GUI.
- Added ASCII logo for CLI.
- Added author and repository links in both CLI and GUI.
- Created custom logging setup for CLI and GUI.

### Changed
- Refactored GUI code into a dedicated `dbconvert.gui` package.
- Enhanced CLI help text and improved user guidance.
- Improved project metadata handling and pyproject metadata extraction.
- Enhanced README with GUI usage details.

## [1.1.1] - 2025-05-24

### Added
- Add `RELEASE.md` documentation
- Create script for release automation

### Fixed
- Missing import errors of subpackages
- Issue with setuptools packaging
- Update README documentation

## [1.0.0] - 2025-05-24

### Added
- Initial release of the `dbconvert` package
- Support for converting PostgreSQL and MySQL databases to SQLite
- Command-line interface (CLI) built with Typer
- Support for PostgreSQL and MySQL connection strings
- Handling of common SQL data types during conversion
- Progress indicators and status messages using Rich
- Error reporting for invalid inputs and failed conversions

[1.2.0]: https://github.com/ysskrishna/dbconvert/compare/v1.1.1...v1.2.0
[1.1.1]: https://github.com/ysskrishna/dbconvert/compare/v1.0.0...v1.1.1
[1.0.0]: https://github.com/ysskrishna/dbconvert/releases/tag/v1.0.0 