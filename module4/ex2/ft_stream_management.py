import sys


if __name__ == "__main__":
    """*)sys.stdin is where your program reads input from.
        By default, this is the keyboard
        *)sys.stdout is where normal output goes.
        By default, this is the screen/terminal..
        *)sys.stderr is where error messages go.
        By default, it also shows on the screen, but it is
        separate from normal output.
        """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    print("Input Stream active. Enter archivist ID: ", end="", flush=True)
    stream_active_id = sys.stdin.readline()
    print("Input Stream active. Enter status report: ", end="", flush=True)
    stream_active2 = sys.stdin.readline()
    print("")
    sys.stdout.write(f"{{[}}STANDARD{{]}} Archive status from "
                     f"{stream_active_id.strip()}: "
                     f"{stream_active2.strip()}\n")
    sys.stderr.write("{[}ALERT{]} System diagnostic: "
                     "Communication channels verified\n")
    sys.stdout.write("{[}STANDARD{]} Data transmission complete")
    print("")
    print("")
    print("Three-channel communication test successful")
