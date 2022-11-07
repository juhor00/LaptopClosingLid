from subprocess import check_output
import tkinter as tk


def close_lid(power_mode, action):

    close_lid_template = "powercfg -set{}valueindex SCHEME_CURRENT 4f971e89-eebd-4455-a8de-9e59040e7347 5ca83367-6e45-459f-a27b-476b1d01c936 {}"
    command = close_lid_template.format(power_mode, action)

    return check_output(command, shell=False)


def main():

    
    
    # First param
    on_battery = "dc"
    plugged_in = "ac"

    # Second param
    nothing = 0
    sleep = 1

    root = tk.Tk()

    root.title("Lid settings")

    tk.Label(root, text="When I close the lid").grid(row=0, column=0, columnspan=4)

    battery_label = tk.Label(root, text="On battery")
    plugged_label = tk.Label(root, text="Plugged in")

    battery_label.grid(column=0, row=1, columnspan=2)
    plugged_label.grid(column=2, row=1, columnspan=2)

    battery_nothing = tk.Button(
        root,
        text="Do nothing",
        command=lambda: [
            close_lid(on_battery, nothing),
            battery_nothing.config(bg="green", fg="white"),
            battery_sleep.config(bg="red", fg="white")
        ]
    )

    battery_sleep = tk.Button(
        root,
        text="Sleep",
        command=lambda: [
            close_lid(on_battery, sleep),
            battery_sleep.config(bg="green", fg="white"),
            battery_nothing.config(bg="red", fg="white")
        ]
    )

    battery_nothing.grid(row=2, column=0, padx=10)
    battery_sleep.grid(row=2, column=1, padx=10)


    plugged_nothing = tk.Button(
        root,
        text="Do nothing",
        command=lambda: [
            close_lid(plugged_in, nothing),
            plugged_nothing.config(bg="green", fg="white"),
            plugged_sleep.config(bg="red", fg="white")
        ]
    )

    plugged_sleep = tk.Button(
        root,
        text="Sleep",
        command=lambda: [
            close_lid(plugged_in, sleep),
            plugged_sleep.config(bg="green", fg="white"),
            plugged_nothing.config(bg="red", fg="white")
        ]
    )

    plugged_nothing.grid(row=2, column=2, padx=10)
    plugged_sleep.grid(row=2, column=3, padx=10)


    tk.mainloop()


if __name__ == '__main__':
    main()