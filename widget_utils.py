import ipywidgets as widgets
from IPython.display import display, HTML
import time 


def show_document(index, document_text): 
    return widgets.HTML(
    value=f"<h4 style='font-family: sans-serif; color:blue;'>Document {index}:</h4>"
          f"<p style='font-family: Verdana'>{document_text}</p>"
    )

def create_textboxes(): 
    text_boxes = []
    decomps = []
    
    def add_text_box(button):
        new_text_box = widgets.Text(value=f'Decomposition {len(text_boxes) + 1} here', description=f'Box {len(text_boxes) + 1}:')
        text_boxes.append(new_text_box)
        display(new_text_box)
    
    def get_all_text(button):
        text_values = [textbox.value for textbox in text_boxes]
        decomps.append(text_values)
        waiting_to_submit = True
        
    
    # Button to add a new text box 
    add_button = widgets.Button(description="Add Decomposition")
    add_button.on_click(add_text_box)
    
    # Button to submit and retrieve text
    submit_button = widgets.Button(description="Submit")
    submit_button.on_click(get_all_text)
    
    # JavaScript to wait for button3 click
    
    # First, display the add text and the submit button 
    display(add_button)
    display(submit_button)
    
    # Start with 3 decompositions 
    for _ in range(5):
        add_text_box(None)
    
    return decomps 