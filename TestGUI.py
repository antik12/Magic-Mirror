import tkinter as tk

def create_gui():
    try:
        # Create the main window
        root = tk.Tk()
        root.title("Simple GUI")
        root.geometry("600x400")
        root.configure(bg="#f0f0f0")
        root.eval('tk::PlaceWindow . center')  # Ensure the window is visible

        # Create a canvas for layout
        canvas = tk.Canvas(root, width=600, height=400, bg="#f0f0f0", highlightthickness=0)
        canvas.pack()

        # Main square
        main_square_size = 200
        x0_main = (400 - main_square_size) // 2
        y0_main = (400 - main_square_size) // 2
        x1_main = x0_main + main_square_size
        y1_main = y0_main + main_square_size

        canvas.create_rectangle(x0_main, y0_main, x1_main, y1_main, fill="#ffffff", outline="#000000", width=2)
        canvas.create_text((x0_main + x1_main) // 2, (y0_main + y1_main) // 2,
                           text="ML Voice Model", font=("Helvetica", 16), fill="#000000")

        # Right-side squares
        right_square_width = 150
        right_square_height = 80
        x0_right = 450
        x1_right = x0_right + right_square_width
        spacing = 10

        labels = ["Weather", "Calendar", "Reminders"]
        for i, label in enumerate(labels):
            y0_right = 20 + (right_square_height + spacing) * i
            y1_right = y0_right + right_square_height
            canvas.create_rectangle(x0_right, y0_right, x1_right, y1_right, fill="#ffffff", outline="#000000", width=2)
            canvas.create_text((x0_right + x1_right) // 2, (y0_right + y1_right) // 2,
                               text=label, font=("Helvetica", 14), fill="#000000")

        # Run the application
        root.mainloop()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_gui()
