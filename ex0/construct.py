import sys
import os
import site


def in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def get_directory_path() -> None:
    try:
        return (site.getsitepackages()[0])
    except AttributeError:
        return os.path.join(
            sys.prefix,
            "lib",
            f"python{sys.version_info.major}.{sys.version_info.minor}",
            "site-packages",
        )


def py_env() -> None:
    if in_venv():
        venv_name = os.path.basename(sys.prefix)
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting \n the global system.\n")
        print("Package installation path:\n")
        print(get_directory_path())
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")
        print()
        print("Then run this program again.")


def main() -> None:
    py_env()


if __name__ == "__main__":
    main()
