

# may  need to -pip install kivy in your terminal
# command: pip install kivy

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button

from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout
        

class MyCalculator(App):
    def build(self):  # this is the function to help buid the function
        root_widget = BoxLayout(orientation='vertical')
        # this adds a boxlayout to the class which is the main layout in all of the class

        output_label = Label(size_hint_y=1)
        # this creates a label 

        button_symbols = ('1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '0', '*', '/', '', '')
        # this is just a list of values that are strign currently

        button_grid = GridLayout(cols=4, size_hint_y=2)
        # this creates a grid layuot 

        for symbol in button_symbols:
            button_grid.add_widget(Button(text=symbol))
            # this for loop goes through every index in the list of button_symbols and adds it as a button in the button grid layout

        clear_button = Button(text='clear', size_hint_y=None, height=100)
        # this just creates a button
        
        def print_button_text(instance):
            output_label.text += instance.text
        
        for button in button_grid.children[1:]:
            button.bind(on_press=print_button_text)

        def resize_label_text(label, new_height):
            label.font_size = .5 * label.height

        output_label.bind(height=resize_label_text)

        def evaluate_result(instance):
            try:
                output_label.text = str(eval(output_label.text))
            except SyntaxError:
                output_label.text = 'Python syntax error!'
        # button_grid.bind(on_press=evaluate_result)

        equal_button = Button(text='=')

        equal_button.bind(on_press=evaluate_result)
    
        def clear_label(instance):
            output_label.text = ''

        clear_button.bind(on_press=clear_label)

        root_widget.add_widget(output_label)

        root_widget.add_widget(button_grid)

        root_widget.add_widget(equal_button)

        root_widget.add_widget(clear_button)

        return root_widget


if __name__ == "__main__":
    MyCalculator().run()