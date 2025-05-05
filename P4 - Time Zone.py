import tkinter

class TimeZone:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title('Time Zones')
        self.main_window.configure(bg="#fce4ec")  # pastel pink background

        # Create the widgets.
        self.__build_prompt_label()
        self.__build_listbox()
        self.__build_output_frame()
        self.__build_quit_button()

        # Start the main loop.
        tkinter.mainloop()

    # This method creates the prompt_label widget.
    def __build_prompt_label(self):
        self.prompt_label = tkinter.Label(
            self.main_window, text='Select a City',
            bg="#fce4ec", fg="#7e57c2", font=("Arial", 12, "bold"))
        self.prompt_label.pack(padx=5, pady=5)

    # This method creates and populates the city_listbox widget.
    def __build_listbox(self):
        self.__cities = ['Denver', 'Honolulu', 'Minneapolis',
                         'New York', 'San Francisco']

        self.city_listbox = tkinter.Listbox(
            self.main_window, height=0, width=0,
            bg="#f3e5f5", fg="#6a1b9a", selectbackground="#ce93d8",
            font=("Arial", 11))
        self.city_listbox.pack(padx=5, pady=5)

        self.city_listbox.bind(
            '<<ListboxSelect>>', self.__display_time_zone)

        for city in self.__cities:
            self.city_listbox.insert(tkinter.END, city)

    # This method creates the output_frame and its contents.
    def __build_output_frame(self):
        self.output_frame = tkinter.Frame(self.main_window, bg="#fce4ec")
        self.output_frame.pack(padx=5)

        self.output_description_label = tkinter.Label(
            self.output_frame, text='Time Zone:',
            bg="#fce4ec", fg="#7e57c2", font=("Arial", 11, "bold"))
        self.output_description_label.pack(
            side='left', padx=(5, 1), pady=5)

        self.__timezone = tkinter.StringVar()

        self.output_label = tkinter.Label(
            self.output_frame, borderwidth=1, relief='solid',
            width=15, textvariable=self.__timezone,
            bg="#f3e5f5", fg="#4a148c", font=("Arial", 11))
        self.output_label.pack(side='right', padx=(1, 5), pady=5)

    # This method creates the Quit button.
    def __build_quit_button(self):
        self.quit_button = tkinter.Button(
            self.main_window, text='Quit',
            command=self.main_window.destroy,
            bg="#f8bbd0", fg="#4a148c", font=("Arial", 11, "bold"))
        self.quit_button.pack(padx=5, pady=10)

    # Callback function for the city_listbox widget.
    def __display_time_zone(self, event):
        index = self.city_listbox.curselection()
        city = self.city_listbox.get(index[0])

        if city == 'Denver':
            self.__timezone.set('Mountain')
        elif city == 'Honolulu':
            self.__timezone.set('Hawaii-Aleutian')
        elif city == 'Minneapolis':
            self.__timezone.set('Central')
        elif city == 'New York':
            self.__timezone.set('Eastern')
        elif city == 'San Francisco':
            self.__timezone.set('Pacific')


if __name__ == '__main__':
    time_zone = TimeZone()
