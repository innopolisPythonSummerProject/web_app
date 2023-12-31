from browser import document, html, window, ajax
import random
import json

#main doby
main = html.DIV(id="main")
holiday = "birthday"
url = "error"
text = "error"

#Picture part
# header
picture_title_container = html.DIV(Class="headers", id="firstHeader")
picture_title_container <= html.H3("Generate your picture:")
main <= picture_title_container

# Kittens checkbox
label = html.LABEL()
checkbox1 = html.INPUT(type="checkbox", id="KittensCheckbox")
label_text = "Kittens"
label <= checkbox1
label <= label_text

# Sparkles checkbox
checkbox2 = html.INPUT(type="checkbox", name="myCheckbox", id="SparklesCheckbox")
label2 = html.LABEL()
label2 <= checkbox2
label2 <= "Sparkles"


# div for all checkboxes
all_checkboxes_div = html.DIV(Class="checkboxes", style={"border-radius": "10px","padding-top": "10px", "padding-bottom": "10px", "width": "280px","display":"flex", "flex-direction":"row", "gap": "25%",  "width": "300px"}) #"background-color": "#ffffff", 
all_checkboxes_div <= label
all_checkboxes_div <= label2
main <= all_checkboxes_div


# Image container witha a picture
container = html.DIV(id="picture_container")

loading_text = html.SPAN("Here will be the picture generated for you!", id="loadingText", style={"opacity":"0.5"})
picture_text_container = html.DIV(id="picture_text_container")
picture_text_container <= loading_text
container <= picture_text_container
main <= container


# the poup window openning
def popup_new_generation(event):

    overlay = html.DIV(id="overlay")
    document <= overlay

    # Create custom pop-up window
    popup_window = html.DIV(Class="popup-window", id="popup_window_id")
    popup_content = html.DIV(Class="popup-content")
    popup_text_1 = html.SPAN("Are you sure?", style={"font-weight": "bolder", "border": "0px solid #000000"})        
    popup_text_2 = html.SPAN("Your latest generation will be deleted", style={"font-size":"14px", "border": "0px solid #000000"})

    popup_close_button = html.DIV(id="close_button_div")
    popup_no = html.BUTTON(Class="newButon", id="popup-no") 
    svg_code = '''<svg xmlns="http://www.w3.org/2000/svg" class="close-svg" viewBox="0 -960 960 960"><path d="m249-207-42-42 231-231-231-231 42-42 231 231 231-231 42 42-231 231 231 231-42 42-231-231-231 231Z"/></svg>'''
    div = html.DIV()
    div.innerHTML = svg_code
    popup_no <= div
    popup_close_button <= popup_no
    popup_content <= popup_close_button

    popup_content <= popup_text_1
    popup_content <= popup_text_2
    popup_yes_button = html.BUTTON("Generate new", Class="newButtom", id="popup-yes")
    yes_button_div = html.DIV(id="yes_button_div")
    yes_button_div <=  popup_yes_button
    popup_content <= yes_button_div
    popup_window <= popup_content        
    document <= popup_window
    overlay <= popup_window
    
# Function to handle the picture button click event
def handle_picture_generate_button_click(event):

    picture_button.remove()
    picture_button_div <= new_button
    new_button.bind("click", handle_picture_popup_generate_click)

    picture_loading_only(event)
    
def picture_loading_only(event):

    def handle_image_load():
        
        # Make an HTTP GET request using ajax.ajax()
        req = ajax.ajax()
        req.bind("complete", lambda req: process_response(req))


        def handle_image_error(event):
            # when the image fails to load
            status_code = event.target.status  # Get the HTTP status code
            error_message = status_code  # Function to get error message based on status code
            loading_text.text = f"Failed: {error_message}"
            new_button.disabled = False


        req.bind("error", handle_image_error)
        req.bind("abort", handle_image_error)
        req.bind("timeout", handle_image_error)
        
        checkbox1_checked = document["KittensCheckbox"].checked
        checkbox2_checked = document["SparklesCheckbox"].checked


        req.open("GET", f'https://well-wisher.onrender.com/image?prompt={holiday}&kitty={checkbox1_checked}&Sparkles={checkbox2_checked}')
        req.timeout = 20000
        req.send()
        

    def process_response(req):
        global url
        
        response_data = req.text
        response_data = json.loads(response_data)
        url = response_data["data"][0]["url"]
                
        image = html.IMG(src=url, style={"height": "100%"})
        loading_text.remove()
        container.clear()
        container <= image
        new_button.disabled = False

    
    new_button.disabled = True 
    container.clear()
    loading_text = html.SPAN("Loading...", id="loadingText", style={"opacity":"0.5"})
    container <= loading_text
    
    handle_image_load()
    

def overlay_off_and_picture_loading(event):
    picture_loading_only(event)

    document["overlay"].remove()

# Function to handle the "Generate new" button click event or regeneration
def handle_picture_popup_generate_click(event):

    popup_new_generation(event) # open a popup window

    popup_no_button = document["popup-no"]
    popup_yes_button = document["popup-yes"]
    popup_yes_button.bind("click", overlay_off_and_picture_loading)
    popup_no_button.bind("click", handle_popup_no_click)

# Function to handle the close button click event
def handle_popup_no_click(event):
    document["overlay"].remove()


# "Generate!" picture button
picture_button_div = html.DIV(Class="NewButtonDiv", id="new_picture_button")
picture_button = html.BUTTON("Generate!", Class="NewButton", id="firstPictureButton")
picture_button.bind("click", handle_picture_generate_button_click)
picture_button_div <= picture_button
main <= picture_button_div

# Regenerate picture button
new_button = html.BUTTON(Class="regeneraring_button", id="newPictureButton", disabled=False)
svg_code = '''<svg xmlns="http://www.w3.org/2000/svg" class="regenerate-svg" viewBox="0 -960 960 960" >
<path d="M480-160q-133 0-226.5-93.5T160-480q0-133 93.5-226.5T480-800q85 0 149 34.5T740-671v-129h60v254H546v-60h168q-38-60-97-97t-137-37q-109 0-184.5 75.5T220-480q0 109 75.5 184.5T480-220q83 0 152-47.5T728-393h62q-29 105-115 169t-195 64Z"/>
</svg>'''
div = html.DIV()
div.innerHTML = svg_code
new_button <= div


# text section
text_title_container = html.DIV(Class="headers", id="secondHeader")
text_title_container <= html.H3("Generate your text:", style={"position": "relative", "bottom": "-24px"})
main <= text_title_container

text_container = html.DIV(id="textContainer")
initial_text = html.SPAN("Here will be the text generated for you!", style={"opacity": "0.5"}) 
text_container <= initial_text
main <= text_container


# text "Generate!" and Regenerate buttons functionality
def handle_text_generate_button_click(event):
    global text_button_clicked
    text_button.remove()
        
    text_button_div <= new_text_button
    new_text_button.bind("click", handle_text_popup_yes_click)
    text_button_clicked = True
    
    text_loading_only(event)
    

def text_loading_only(event):
    def handle_text_error():
        loading_text.text = "Failed to load the text"

    new_text_button.disabled = True
    text_container.clear()
    loading_text = html.SPAN("Loading...", id="loadingText", style={"opacity": "0.5"})
    text_container <= loading_text

    try:
        def process_response(req):
            global text
            random_text = req.text  # Retrieve the response text
            response_data = json.loads(random_text)
            
            random_text = response_data["choices"][0]["text"]
            text = html.SPAN(random_text, id="GeneratedText")
            loading_text.remove()
            text_container <= text
            new_text_button.disabled = False

        def handle_text_error():
            loading_text.text = "Failed to load the text"
            new_text_button.disabled = False

        req = ajax.ajax()
        req.bind("complete", process_response)
        req.bind("error", handle_text_error)
        req.bind("abort", handle_text_error)
        req.bind("timeout", handle_text_error)

        #get holidays
        payload = {"holiday": "название праздника"}
        req.open("GET", f'https://well-wisher.onrender.com/greeting?holiday={holiday}')
        req.timeout = 20000
        req.send()

    except Exception as e:
        handle_text_error()
        raise e


def overlay_off_and_text_loading(event):
    text_loading_only(event)

    document["overlay"].remove()
 
# Function to handle the "Yes" button click event
def handle_text_popup_yes_click(event):

    popup_new_generation(event) # Call the poput_new_generation function here
        
    popup_no_button = document["popup-no"]
    popup_yes_button = document["popup-yes"]
    popup_yes_button.bind("click", overlay_off_and_text_loading)
    popup_no_button.bind("click", handle_popup_no_click)
   

# Generate! text button
text_button_div = html.DIV(Class="NewButtonDiv")
text_button = html.BUTTON("Generate!", Class="NewButton", id="firstTextButton")
text_button.bind("click", handle_text_generate_button_click)
text_button_div <= text_button
main <= text_button_div

# Regenerae text button
new_text_button = html.BUTTON(Class="regeneraring_button", id="newTextButton", disabled=False)
svg_code = '''<svg xmlns="http://www.w3.org/2000/svg" class="regenerate-svg" viewBox="0 -960 960 960" >
<path d="M480-160q-133 0-226.5-93.5T160-480q0-133 93.5-226.5T480-800q85 0 149 34.5T740-671v-129h60v254H546v-60h168q-38-60-97-97t-137-37q-109 0-184.5 75.5T220-480q0 109 75.5 184.5T480-220q83 0 152-47.5T728-393h62q-29 105-115 169t-195 64Z"/>
</svg>'''
div = html.DIV()
div.innerHTML = svg_code
new_text_button <= div


# "Send my wishes!" button functionality
def handle_last_button_click(event):

    overlay = html.DIV(id="overlay")
    document <= overlay

    # Create custom pop-up window
    popup_window = html.DIV(Class="popup-window", id="popup_window_id")
    popup_content = html.DIV(Class="popup-content")
    popup_text_1 = html.SPAN("Are you sure?", style={"font-weight": "bolder", "border": "0px solid #000000"})
    popup_text_2 = html.SPAN("The window will be closed", style={"font-size":"14px", "border": "0px solid #000000"})


    popup_close_button = html.DIV(id="close_button_div")
    popup_no = html.BUTTON(id="popup-no") 
    svg_code = '''<svg xmlns="http://www.w3.org/2000/svg" class="close-svg" viewBox="0 -960 960 960"><path d="m249-207-42-42 231-231-231-231 42-42 231 231 231-231 42 42-231 231 231 231-42 42-231-231-231 231Z"/></svg>'''
    div = html.DIV()
    div.innerHTML = svg_code
    popup_no <= div
    popup_close_button <= popup_no
    popup_content <= popup_close_button

    popup_content <= popup_text_1
    popup_content <= popup_text_2
    send_button_div = html.DIV(id="send_button_div")
    popup_yes_button = html.BUTTON("Send!", id="popup-send-button")
    send_button_div <= popup_yes_button
    popup_content <= send_button_div
    popup_window <= popup_content
    document <= popup_window
    overlay <= popup_window

    # Bind events to the buttons in the pop-up window
    popup_no_button = document["popup-no"]
    popup_yes_button.bind("click", handle_last_yes_click)
    popup_no_button.bind("click", handle_last_no_click)

# actual loading
def handle_last_yes_click(event):
    global text, url

    payload = {
        "picture_src": url,
        "text_content": text if isinstance(text, str) else text.text
    }

    # Convert the payload to a JSON string
    payload_json = json.dumps(payload)
    

    js_code = f'''
    console.log("start js");
    window.Telegram.WebApp.sendData("{payload_json.replace('"', '\\"')}");
    console.log("end.js");
    '''

    window.eval(js_code)

# Function to handle the "No" button click event
def handle_last_no_click(event):
    document["overlay"].remove()


div = html.DIV(id="send_my_wishes_button_div")
submit_button = html.BUTTON("Send my wishes!", id="send_my_wishes_button")
submit_button.bind("click", handle_last_button_click)
div <= submit_button
main <= div
document <= main
