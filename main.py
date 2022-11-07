from subprocess import check_output
import tkinter as tk


def cmd(command):
    return check_output(command, shell=False)


def main():

    close_lid_template = "powercfg -set{}valueindex SCHEME_CURRENT 4f971e89-eebd-4455-a8de-9e59040e7347 5ca83367-6e45-459f-a27b-476b1d01c936 {}"
    
    # First param
    on_battery = "dc"
    plugged_in = "ac"

    # Second param
    nothing = 0
    sleep = 1

    cmd(close_lid_template.format(on_battery, nothing))

    root = tk.Tk()


if __name__ == '__main__':
    main()