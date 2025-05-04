from pathlib import Path

SQL_DIR = Path("sql")


def load_sql(table: str) -> dict:
    sqls_table = SQL_DIR / f"{table}"

    return { \
        sql_file.stem: sql_file.read_text(encoding="utf-8") \
        for sql_file in sqls_table.glob("*.sql") \
        }
