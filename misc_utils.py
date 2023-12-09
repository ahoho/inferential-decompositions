import ipywidgets as widgets
from IPython.display import display, HTML
import json 
import numpy as np
from sentence_transformers.util import cos_sim

def write_jsonl(data, fpath):
    with open(fpath, "w") as outfile:
        for index, line in enumerate(data): 
            s = json.dumps(line, ensure_ascii=False)
            if index == len(data) - 1:
                outfile.write(s)
            else: 
                outfile.write(f"{s}\n")


def read_jsonl(fpath):
    with open(fpath) as infile:
        return [json.loads(line) for line in infile if line]


def show_document(index, document_text): 
    return widgets.HTML(
    value=f"<h3 style='font-family: sans-serif; color:blue;'>Document {index+1}:</h3>"
          f"<p style='font-family: Verdana'>{document_text}</p>"
    )

def distance_func(x, y, mode="min") :
    """
    x is a set of vectors, so is y
    return the index i from x and j from y that 
    corresponds to the minimal possible distance 
    """
    dists = 1 - cos_sim(x, y)
    if mode == "min" :
        index1, index2 =  np.unravel_index(np.argmin(dists, axis=None), dists.shape)
        return index1, index2, dists[index1, index2]


def create_textboxes(value=None): 
    decomps = []

    if value is not None:
        text_area = widgets.Textarea(value=value, description='Decomps:', layout={'height': '200px', 'width': '1000px'})
    else: 
        text_area = widgets.Textarea(value=f'Add decompositions separated by newlines', description='Decomps:', layout={'height': '200px', 'width': '1000px'})
    
    #text_area = widgets.Text(value="Add newline separated decompositions here")
    #new_text_box = widgets.VBox([text_area])
    display(text_area)

    def get_all_text(button):
        text_values = text_area.value
        #print(text_values) 
        for elem in text_values.split('\n'): 
            decomps.append(elem)
        
            
    # Button to submit and retrieve text
    submit_button = widgets.Button(description="Submit")
    submit_button.on_click(get_all_text)
    
    # First, display the add text and the submit button 
    display(submit_button)
    
    
    return decomps 