import sys
from pathlib import Path
from collections import Counter

# Parse a log line and return a dictionary with keys: date, time, level, message.
# Returns None if the line is malformed or incomplete.
# The level is converted to uppercase for consistency.

def parse_log_line(line: str) -> dict:
    parts = line.strip().split(maxsplit=3)
    if len(parts) < 4:
        return None    
    date, time, level, message = parts

    return {
        "date": date,
        "time": time,
        "level": level.upper(),
        "message": message
    }
    

# Load a log file and return a list of parsed log entries.
# Skips malformed lines and handles FileNotFoundError and other I/O errors.
def load_logs(file_path: str) -> list:
    logs = []
    try:
        # Uses the walrus operator (:=) to filter out lines that cannot be parsed.
        with open(file_path,"r",encoding="utf-8") as file:
            logs = [parsed for line in file if (parsed := parse_log_line(line))] 

    except FileNotFoundError:
        print("File is not found")
        sys.exit(1)

    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    return logs
    
#Filter the list by log level
def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper() 
    return [log for log in logs if log["level"] == level]

# Count the number of logs per level
def count_logs_by_level(logs: list) -> dict:
    level = [log["level"] for log in logs]
    return dict(Counter(level))

# Display the counts of logs in a table format
def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level.upper():<16} | {count:<8}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py <path_to_log_file> [log_level]")
        sys.exit(1)
    log_file = Path(sys.argv[1])
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    # Load and parse the logs
    logs = load_logs(log_file)

    # Count and display logs per level
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # If a specific level is provided, display detailed entries
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\n Деталі логів для рівня '{log_level.upper()}':")
        if filtered_logs:
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print("Немає записів цього рівня.")




if __name__ == "__main__":
    main()
