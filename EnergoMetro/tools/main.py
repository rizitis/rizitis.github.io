from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import webbrowser

class ColorWebApp(App):
    def build(self):
        # Create a BoxLayout with a vertical orientation
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Add a banner at the top
        banner = Label(
            text='ΠΑTΑΣ ΣΤΟ ΧΡΩΜΜΑ & ΒΛΕΠΕΙΣ ΤΙΜΕΣ',
            size_hint_y=None,
            height=40
        )
        layout.add_widget(banner)

        # Define labels and corresponding web pages
        labels_and_urls = {
            'ΠΡΑΣΙΝΟ': 'https://rizitis.github.io/EnergoMetro/green.html',
            'ΜΠΛΕ': 'https://rizitis.github.io/EnergoMetro/blue.html',
            'ΠΟΡΤΟΚΑΛΙ': 'https://rizitis.github.io/EnergoMetro/orange.html',
            'ΚΙΤΡΙΝΟ': 'https://rizitis.github.io/EnergoMetro/yellow.html',
        }

        # Create buttons for each color with custom text labels
        for label, url in labels_and_urls.items():
            button = Button(
                text=label,
                background_color=self.get_color_by_label(label),
                on_press=self.on_button_press(url)
            )
            layout.add_widget(button)

        # Add a button as a link to terms and conditions
        terms_button = Button(
            text="Oροι και Προϋποθέσεις χρήσης",
            markup=True,
            background_color=(1, 1, 1, 0),  # Transparent background
            border=(0, 0, 0, 0)  # No border
        )
        terms_button.bind(on_press=self.on_terms_button_press)
        layout.add_widget(terms_button)

        return layout

    def get_color_by_label(self, label):
        # Return the corresponding color based on the label
        color_mapping = {
            'ΠΡΑΣΙΝΟ': (0, 1, 0),
            'ΜΠΛΕ': (0, 0, 1),
            'ΠΟΡΤΟΚΑΛΙ': (255, 0, 0),  # RGB for orange
            'ΚΙΤΡΙΝΟ': (100, 100, 0),  # RGB for yellow
        }
        return color_mapping.get(label, (1, 1, 1))

    def on_button_press(self, url):
        # Callback function for button press
        def callback(instance):
            # Open the web page in the default web browser
            webbrowser.open(url)
        return callback

    def on_terms_button_press(self, instance):
        # Callback function for terms button press
        webbrowser.open("https://github.com/rizitis/EnergoMetro/blob/main/EnergoMetro_LICENSE.pdf")

if __name__ == '__main__':
    ColorWebApp().run()

