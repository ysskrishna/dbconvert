import typer
from dbconvert.core.loggingsetup import LoggerManager
from dbconvert.converters.converter_factory import ConverterFactory
from dbconvert.writers.sqlite_writer import SQLiteWriter
from dbconvert.core.enums import DatabaseType
import os

app = typer.Typer()
logger = LoggerManager.get_logger()

@app.command(name="gui")
def launch_gui():
    """
    Launch the graphical user interface.
    """
    try:
        from dbconvert.gui.app import main
        main()
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise typer.Exit(1)

@app.command(name="supported-databases")
def supported_databases():
    """
    Show supported database types for conversion.
    """
    logger.info("Supported database types:")
    for db_type in DatabaseType.values():
        logger.info(f"  • {db_type}")

@app.command()
def convert(
    source: str = typer.Option(..., help=f"Source database type ({', '.join(DatabaseType.values())})"),
    conn: str = typer.Option(..., help="Source database connection string"),
    sqlite: str = typer.Option(..., help="Target SQLite database file path")
):
    """
    Convert a PostgreSQL or MySQL database to SQLite.
    """
    try:
        # Validate source database type
        if source not in DatabaseType.values():
            raise ValueError(f"Unsupported source database type: {source}")
        
        # Validate connection string
        if not conn:
            raise ValueError("Connection string cannot be empty")
        
        # Validate SQLite path
        sqlite_dir = os.path.dirname(sqlite)
        if sqlite_dir and not os.path.exists(sqlite_dir):
            os.makedirs(sqlite_dir)
        
        # Create converter using factory
        converter = ConverterFactory.create_converter(source, conn)
        
        # Read source database
        logger.info("Reading source database...")
        tables = converter.read_all_tables()
        
        # Write to SQLite
        logger.info("Writing to SQLite database...")
        writer = SQLiteWriter(sqlite)
        writer.write_all_tables(tables)
        
        logger.info("✅ Conversion completed successfully!")
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise typer.Exit(1)

if __name__ == "__main__":
    app()