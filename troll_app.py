#!/usr/bin/env python3
"""
Fun Troll App - A harmless prank application
Nothing serious, just some playful trolling!
"""

import tkinter as tk
from tkinter import messagebox
import random
import time


class TrollApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Totally Normal App")
        self.root.geometry("400x300")

        self.click_count = 0
        self.message_count = 0

        self.setup_ui()

    def setup_ui(self):
        """Setup the main UI elements"""
        # Main container
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')

        # Title
        title_label = tk.Label(
            main_frame,
            text="Welcome to This App!",
            font=('Arial', 16, 'bold')
        )
        title_label.pack(pady=10)

        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="This is definitely a real application",
            font=('Arial', 10)
        )
        subtitle_label.pack(pady=5)

        # Main button
        self.main_button = tk.Button(
            main_frame,
            text="Click Me",
            font=('Arial', 12),
            command=self.on_button_click,
            width=15,
            height=2
        )
        self.main_button.pack(pady=20)

        # Counter label
        self.counter_label = tk.Label(
            main_frame,
            text=f"Clicks: {self.click_count}",
            font=('Arial', 10)
        )
        self.counter_label.pack(pady=5)

        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="Status: Ready",
            font=('Arial', 9),
            fg='gray'
        )
        self.status_label.pack(pady=10)

    def on_button_click(self):
        """Handle button clicks with trolling behavior"""
        self.click_count += 1
        self.counter_label.config(text=f"Clicks: {self.click_count}")

        # Different trolling behaviors based on click count
        behaviors = [
            self.behavior_1,
            self.behavior_2,
            self.behavior_3,
            self.behavior_4,
            self.behavior_5
        ]

        # Pick a behavior based on click count (cycling through)
        behavior = behaviors[self.click_count % len(behaviors)]
        behavior()

    def behavior_1(self):
        """Button moves away"""
        self.status_label.config(text="Status: 🎣 Catch me if you can!")
        x = random.randint(50, 300)
        y = random.randint(50, 200)
        self.main_button.place(x=x, y=y)

    def behavior_2(self):
        """Fun message box"""
        messages = [
            "Nice click!",
            "You clicked!",
            "Keep clicking!",
            "Very impressive!",
            "Wow, you're good at this!",
            "Have you tried not clicking?",
            "Interesting..."
        ]
        messagebox.showinfo("Info", random.choice(messages))
        self.status_label.config(text="Status: 📬 Message delivered!")

    def behavior_3(self):
        """Button changes text"""
        fake_texts = [
            "Don't Click",
            "Seriously, Stop",
            "Why?",
            "Please No",
            "I'm Tired",
            "🎮",
            "???",
            "Wait"
        ]
        self.main_button.config(text=random.choice(fake_texts))
        self.status_label.config(text="Status: 🔄 Button confused")

        # Reset button position
        self.main_button.pack_forget()
        self.main_button = tk.Button(
            self.root,
            text=self.main_button.cget('text'),
            font=('Arial', 12),
            command=self.on_button_click,
            width=15,
            height=2
        )
        self.main_button.pack(pady=20)

    def behavior_4(self):
        """Fake loading"""
        self.status_label.config(text="Status: ⏳ Loading...")
        self.root.update()

        original_text = self.main_button.cget('text')
        for i in range(3):
            self.main_button.config(text=f"Loading{'.' * (i + 1)}")
            self.root.update()
            time.sleep(0.3)

        self.main_button.config(text="Just Kidding!")
        self.root.update()
        time.sleep(0.5)

        self.main_button.config(text=original_text)
        self.status_label.config(text="Status: 😂 Gotcha!")

    def behavior_5(self):
        """Random popup"""
        popup = tk.Toplevel(self.root)
        popup.title("???")
        popup.geometry("200x100")
        popup.attributes('-topmost', True)

        label = tk.Label(
            popup,
            text=random.choice(["Hi!", "Hello!", "Hey!", "👋"]),
            font=('Arial', 14)
        )
        label.pack(expand=True)

        # Auto close after 1.5 seconds
        popup.after(1500, popup.destroy)

        # Position randomly
        x = random.randint(0, 500)
        y = random.randint(0, 400)
        popup.geometry(f"+{x}+{y}")

        self.status_label.config(text="Status: 🎉 Surprise!")


def main():
    root = tk.Tk()
    app = TrollApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
