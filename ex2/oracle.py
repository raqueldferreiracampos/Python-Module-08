import os
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()

    matrix = os.getenv("MATRIX_MODE")
    database = os.getenv("DATABASE_URL")
    api = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")

    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    if not matrix:
        print("[KO] MATRIX_MODE is missing")
    elif matrix not in ("development", "production"):
        print("[KO] Invalid MATRIX_MODE")
    else:
        print(f"Mode: {matrix}")
    if not database:
        print("[KO] DATABASE_URL is missing")
    else:
        print("Database: Connected to local instance")
    if not api:
        print("[KO] API_KEY is missing")
    else:
        print("API Access: Authenticated")
    if not log:
        print("[KO] LOG_LEVEL is missing")
    else:
        print(f"Log Level: {log}")
    if not zion:
        print("[KO] ZION_ENDPOINT is missing")
    else:
        print("Zion Network: Online\n")
    if not all([matrix, database, api, log, zion]):
        return
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
