from pathlib import Path
import pyarrow as pa
import pyarrow.parquet as pq

ROOT = Path(__file__).resolve().parents[1]
input_path = ROOT / "data" / "raw" / "transactions.parquet"
output_path = ROOT / "data" / "processed" / "transactions.parquet"

if not input_path.exists():
    raise FileNotFoundError(input_path)

output_path.parent.mkdir(parents=True, exist_ok=True)

table = pq.read_table(input_path)
index = table.schema.get_field_index("t_dat")

if index < 0:
    raise ValueError("Không tìm thấy cột t_dat")

table = table.set_column(
    index,
    "t_dat",
    table["t_dat"].cast(pa.timestamp("us"))
)

pq.write_table(table, output_path)
print("Đã tạo:", output_path)
