import tkinter as tk
from random import randint

class DiceRoller:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Dice Roller")
        self.window.configure(bg="#B7B4A0")

        # Input 
        tk.Label(self.window, text="Number of Dice:").grid(row=0, column=0)
        self.dice_entry = tk.Entry(self.window, bg="#429C2D", fg="#DC143C")
        self.dice_entry.grid(row=0, column=1)

        tk.Label(self.window, text="Number of sides:").grid(row=1, column=0)
        self.sides_entry = tk.Entry(self.window, bg="#429C2D", fg="#DC143C")
        self.sides_entry.grid(row=1, column=1)

        # Roll button
        self.roll_button = tk.Button(self.window, text="Roll", bg="#0F52BA", fg="white", command=self.roll_dice)
        self.roll_button.grid(row=2, column=0, columnspan=2)

        # Output field
        self.output_label = tk.Label(self.window, text="", fg="#0F52BA")
        self.output_label.grid(row=3, column=0, columnspan=2)

        # Canvas for drawing dice
        self.canvas = tk.Canvas(self.window, width=500, height=300)
        self.canvas.grid(row=4, column=0, columnspan=2)

        # Ask again and quit buttons
        self.again_button = tk.Button(self.window, text="Roll Again", command=self.ask_again, bg="#0F52BA", fg="white")
        self.again_button.grid(row=5, column=0)

        self.quit_button = tk.Button(self.window, text="Quit", command=self.window.destroy, bg="blue", fg="white")
        self.quit_button.grid(row=5, column=1)

        # Roll log for last 10 rolls
        self.roll_log_label = tk.Label(self.window, text="Last 10 Rolls:", fg="#0F52BA")
        self.roll_log_label.grid(row=6, column=0, columnspan=2)

        self.roll_log = tk.Text(self.window, height=10, width=50, state='disabled')
        self.roll_log.grid(row=7, column=0, columnspan=2)

        self.roll_history = []

    def roll_dice(self):
        try:
            num_dice = int(self.dice_entry.get())
            num_sides = int(self.sides_entry.get())

            # Adjust canvas height dynamically based on number of dice
            canvas_height = max(200, (num_dice // 2 + 1) * 100)
            self.canvas.config(height=canvas_height)
            
            # Roll
            rolls = [randint(1, num_sides) for _ in range(num_dice)]

            # Results
            output = "You rolled: " + ", ".join(str(roll) for roll in rolls)
            self.output_label.config(text=output)

            # Draw dice
            self.canvas.delete("all")
            for i, roll in enumerate(rolls):
                x = 50 + (i % 3) * 100
                y = 50 + (i // 3) * 100
                self.draw_dice(x, y, roll)

            # Update roll history
            self.update_roll_log(output)
            
        except ValueError:
            self.output_label.config(text="Please enter only numbers.")

    def draw_dice(self, x, y, roll):
        self.canvas.create_rectangle(x, y, x+90, y+90, fill="#FFFFFF")
        self.canvas.create_rectangle(x+5, y+5, x+85, y+85, fill="#CCCCCC")
        if roll == 1:
            self.canvas.create_oval(x+40, y+40, x+50, y+50, fill="#000000")
        elif roll == 2:
            self.canvas.create_oval(x+20, y+20, x+30, y+30, fill="#000000")
            self.canvas.create_oval(x+60, y+60, x+70, y+70, fill="#000000")
        elif roll == 3:
            self.canvas.create_oval(x+20, y+20, x+30, y+30, fill="#000000")
            self.canvas.create_oval(x+40, y+40, x+50, y+50, fill="#000000")
            self.canvas.create_oval(x+60, y+60, x+70, y+70, fill="#000000")
        elif roll == 4:
            self.canvas.create_oval(x+20, y+20, x+30, y+30, fill="#000000")
            self.canvas.create_oval(x+20, y+60, x+30, y+70, fill="#000000")
            self.canvas.create_oval(x+60, y+20, x+70, y+30, fill="#000000")
            self.canvas.create_oval(x+60, y+60, x+70, y+70, fill="#000000")
        elif roll == 5:
            self.canvas.create_oval(x+20, y+20, x+30, y+30, fill="#000000")
            self.canvas.create_oval(x+20, y+60, x+30, y+70, fill="#000000")
            self.canvas.create_oval(x+40, y+40, x+50, y+50, fill="#000000")
            self.canvas.create_oval(x+60, y+20, x+70, y+30, fill="#000000")
            self.canvas.create_oval(x+60, y+60, x+70, y+70, fill="#000000")
        elif roll == 6:
            self.canvas.create_oval(x+20, y+20, x+30, y+30, fill="#000000")
            self.canvas.create_oval(x+20, y+40, x+30, y+50, fill="#000000")
            self.canvas.create_oval(x+20, y+60, x+30, y+70, fill="#000000")
            self.canvas.create_oval(x+60, y+20, x+70, y+30, fill="#000000")
            self.canvas.create_oval(x+60, y+40, x+70, y+50, fill="#000000")
            self.canvas.create_oval(x+60, y+60, x+70, y+70, fill="#000000")
    

    def update_roll_log(self, roll_result):
        # Add roll result to history
        self.roll_history.append(roll_result)
        
        # Keep only last 10 rolls
        if len(self.roll_history) > 10:
            self.roll_history.pop(0)

        # Update log text widget
        self.roll_log.config(state='normal')
        self.roll_log.delete(1.0, tk.END)
        self.roll_log.insert(tk.END, "\n".join(self.roll_history))
        self.roll_log.config(state='disabled')

    def ask_again(self):
        # Reset the dice roll results and clear canvas
        self.output_label.config(text="")
        self.canvas.delete("all")
        self.dice_entry.delete(0, tk.END)
        self.sides_entry.delete(0, tk.END)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = DiceRoller()
    app.run()
