"""A small Tkinter application for converting common length units."""

import tkinter as tk
from tkinter import messagebox


UNITS_IN_METERS = {
    "meter": 1.0,
    "foot": 0.3048,
    "yard": 0.9144,
    "inch": 0.0254,
}


def convert_length(value, from_unit, to_unit):
    """Convert a numeric length between two supported units."""
    if from_unit not in UNITS_IN_METERS:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in UNITS_IN_METERS:
        raise ValueError(f"Unsupported destination unit: {to_unit}")

    value_in_meters = float(value) * UNITS_IN_METERS[from_unit]
    return value_in_meters / UNITS_IN_METERS[to_unit]


class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Length Unit Converter")
        self.root.resizable(False, False)

        self.from_unit = tk.StringVar(value="meter")
        self.to_unit = tk.StringVar(value="foot")
        self.input_value = tk.StringVar()
        self.output_value = tk.StringVar(value="—")

        self._build_layout()

    def _build_layout(self):
        container = tk.Frame(self.root, padx=16, pady=16)
        container.grid(row=0, column=0)

        tk.Label(container, text="Value").grid(row=0, column=0, sticky="w")
        tk.Entry(container, textvariable=self.input_value, width=18).grid(
            row=1, column=0, padx=(0, 8), pady=(4, 12)
        )

        tk.Label(container, text="From").grid(row=0, column=1, sticky="w")
        tk.OptionMenu(container, self.from_unit, *UNITS_IN_METERS).grid(
            row=1, column=1, padx=8, pady=(4, 12), sticky="ew"
        )

        tk.Label(container, text="To").grid(row=0, column=2, sticky="w")
        tk.OptionMenu(container, self.to_unit, *UNITS_IN_METERS).grid(
            row=1, column=2, padx=(8, 0), pady=(4, 12), sticky="ew"
        )

        tk.Label(container, text="Result").grid(row=2, column=0, sticky="w")
        tk.Label(
            container,
            textvariable=self.output_value,
            width=24,
            anchor="w",
            borderwidth=2,
            relief="groove",
            padx=8,
            pady=6,
        ).grid(row=3, column=0, columnspan=3, sticky="ew", pady=(4, 12))

        tk.Button(container, text="Convert", command=self.convert).grid(
            row=4, column=0, sticky="ew", padx=(0, 8)
        )
        tk.Button(container, text="Clear", command=self.clear).grid(
            row=4, column=1, sticky="ew", padx=8
        )
        tk.Button(container, text="Exit", command=self.root.destroy).grid(
            row=4, column=2, sticky="ew", padx=(8, 0)
        )

    def convert(self):
        try:
            result = convert_length(
                self.input_value.get(), self.from_unit.get(), self.to_unit.get()
            )
        except ValueError:
            messagebox.showerror("Invalid input", "Enter a valid numeric value.")
            self.output_value.set("Invalid input")
            return

        self.output_value.set(f"{result:.6g} {self.to_unit.get()}")

    def clear(self):
        self.input_value.set("")
        self.output_value.set("—")


def main():
    root = tk.Tk()
    UnitConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
