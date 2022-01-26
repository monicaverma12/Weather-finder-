def search():
    city = city_entry.get()
    #print(city)
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=88e88f570f80d0d47352c988b6e52865"
    result = requests.get(url).json()
    temperature = (result["main"]["temp"]) - 273.15
    temp_lbl['text'] = "Temperature at " + city + " is " + str(int(temperature))+ "°C"


def reset():
    city_entry.delete(0, tk.END)
    temp_lbl['text'] = ''


root = tk.Tk()
root.title("Weather App")
root.geometry("300x500")
root.configure(bg='powder blue')

head1 = tk.Label(root,
                 text="Enter your city",
                 font=("bold", 16),
                 fg="blue",
                 bg="powder blue")
head1.configure(bg='powder blue')
head1.pack(pady=10)

city = tk.StringVar()
city_entry = tk.Entry(root, textvariable=city)
city_entry.pack(pady=7)

search_btn = tk.Button(root,
                       text="Search Weather",
                       width=12,
                       command=search,
                       bg="navy blue",
                       fg="white")
search_btn.pack(pady=10)

reset_btn = tk.Button(root, text="Reset", command=reset, bg="yellow")
reset_btn.pack(pady=10)

temp_lbl = tk.Label(root, text="")
temp_lbl.configure(bg="powder blue")
temp_lbl.pack(padx=5, pady=3)

root.mainloop()
