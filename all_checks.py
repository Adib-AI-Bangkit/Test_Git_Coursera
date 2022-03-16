#!/usr/bin/env python3
import os
import sys

def check_reboot():
    """Return True if the computer has a pending reboot.""" #Swadikap
    return os.path.exists("/run/reboot-required")
def main():
    if check_reboot():
        print("Print Reboot.")
        sys.exit(1)
    print("Everthing ok.")
    sys.exit(0)
main()
