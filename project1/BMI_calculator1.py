import tkinter as tk
from tkinter import messagebox
import json
import os
import matplotlib.pyplot as plt
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()

root.title('Tkinter.com - BMI Calculator')
root.iconbitmap('project1/bmi-icon-5.png')
root.geometry("300x500") 
root.resizable(False, False)


class BMI_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        
        self.w_label = tk.Label(root,
                                    text="weight In kilograms",
                                    width=20,
                                    height=3,
                                    borderwidth=1,
                                    relief="solid")
        self.w_label.grid(row=0, column=0, padx=10, pady=10)
        self.w_entry = tk.Entry(root)
        self.w_entry.grid(row=0, column=1, padx=10, pady=10)

        self.h_label = tk.Label(root,
                                      text="height In centimeter",
                                      width=20,
                                      height=3,
                                      borderwidth=1,
                                      relief="solid")
        self.h_label.grid(row=1, column=0, padx=10, pady=10)
        self.h_entry = tk.Entry(root)
        self.h_entry.grid(row=1, column=1, padx=10, pady=10)

        

        self.calculate_button = tk.Button(root, command=self.calculate_bmi,
                                           text="Calculate BMI",
                                           width=20,
                                           height=3,
                                           fg="#000000",
                                           bg="#FF1493")
        self.calculate_button.grid(row=2, columnspan=2, padx=10, pady=10)

        
        self.result_label = tk.Label(root, text="",
                                     height=3,
                                     fg="#000000",
                                     bg="#FF1493")
        self.result_label.grid(row=3, columnspan=2, padx=10, pady=10)

        self.save_data_button = tk.Button(root, text="Save Data", command=self.save_data, width=20,
                                           height=3,
                                           fg="#000000",
                                           bg="#FF1493")
        self.save_data_button.grid(row=4, columnspan=2, padx=10, pady=10)

        self.load_data_button = tk.Button(root, text="Load Data", command=self.load_data, width=20,
                                           height=3,
                                           fg="#000000",
                                           bg="#FF1493")
        self.load_data_button.grid(row=5, columnspan=2, padx=10, pady=10)
        
        self.visualize_data_button = tk.Button(root, text="Visualize Data", command=self.visualize_data, width=20,
                                           height=3,
                                           fg="#000000",
                                           bg="#FF1493")
        self.visualize_data_button.grid(row=6, columnspan=2, padx=10, pady=10)
        
        self.clear_data_button = tk.Button(root, text="Clear Data", command=self.clear_data, width=20,
                                           height=3,
                                           fg="#000000",
                                           bg="#FF1493")
        self.clear_data_button.grid(row=8, columnspan=2, padx=10, pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.w_entry.get())
            height = float(self.h_entry.get()) / 100  #in meters
            bmi = weight / (height * height)
            category = self.get_category(bmi)
            self.result_label.config(text=f"BMI: {bmi:.2f} ({category})")
            return bmi, category
        except ValueError:
            messagebox.showerror("Error", "Please enter valid weight and height.")
            return None, None

    def get_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def save_data(self):
        try:
            weight = float(self.w_entry.get())
            height = float(self.w_entry.get())
            bmi, category = self.calculate_bmi()
            if bmi is not None:
                data = {'weight': weight, 'height': height, 'bmi': bmi, 'category': category}
                with open('user_data.json', 'a') as f:
                    json.dump(data, f)
                    f.write('\n')

                try:
                        with open('user_data.json', 'r') as f_read:
                            entries = f_read.readlines()
                            entry_number = len(entries) + 1
                except FileNotFoundError:
                        entry_number = 1

                        f.write(f"{entry_number}. {json.dumps(data)}\n")

        except ValueError:
            messagebox.showerror("Error", "Please calculate BMI first.")
    
    def load_data(self):
        try:
            if os.path.exists('user_data.json'):
                with open('user_data.json', 'r') as f:
                    data = f.readlines()
                    for line in data:
                        entry = json.loads(line)
                        print(f"Weight: {entry['weight']}, Height: {entry['height']}, BMI: {entry['bmi']}, Category: {entry['category']}")
            else:
                messagebox.showinfo("Info", "No data available.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {str(e)}")

    def visualize_data(self):
        try:
            if os.path.exists('user_data.json'):
                with open('user_data.json', 'r') as f:
                    data = f.readlines()
                    weights = []
                    bmis = []
                    for line in data:
                        entry = json.loads(line)
                        weights.append(entry['weight'])
                        bmis.append(entry['bmi'])
                plt.plot(weights, bmis, marker='o', linestyle='-')
                plt.xlabel('Weight (kg)')
                plt.ylabel('BMI')
                plt.title('BMI vs. Weight')
                plt.grid(True)
                plt.show()
            else:
                messagebox.showinfo("Info", "No data available for visualization.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to visualize data: {str(e)}")

    def clear_data(self):
        self.w_entry.delete(0, tk.END)
        self.h_entry.delete(0, tk.END)
        self.result_label.config(text="")

def main():
    app = BMI_Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
