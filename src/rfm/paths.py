from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

ARTICLE_PATH = RAW_DIR / "article.parquet"
CUSTOMER_PATH = RAW_DIR / "customer.parquet"
TRANSACTIONS_PATH = RAW_DIR / "transactions.parquet"
