def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # пропустити порожні рядки
            operation, value = line.split(",")
            value = int(value)
            if operation == "supply":
                supply_total += value
            elif operation == "buy":
                buy_total += value

    result = supply_total - buy_total

    with open(report_file_name, "w", encoding="utf-8") as f:
        f.write(f"supply,{supply_total}\n")
        f.write(f"buy,{buy_total}\n")
        f.write(f"result,{result}\n")
