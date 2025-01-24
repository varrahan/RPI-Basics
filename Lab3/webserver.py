from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import json
from sense_hat import SenseHat

colors = [[10,10,10] for i in range(64)]
sense: SenseHat = SenseHat()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

# Converts a RGB color expressed in HEX to RGB. HEX comes 
# from the server, and RGB array used by SenseHAT.
def hex_to_rgb_color(color: str):
    color = color.strip('#')
    rgb = [int(color[i:i+2], 16) for i in (0, 2, 4)]
    return rgb

# Button ids on html are integers. 
# This function maps the led index to x and y.
def map_index_to_xy(led_index: int):
    return int(led_index%8), int(led_index/8)

@app.route('/')
def index():
    return render_template('Lab3-Colour-Picker.html')

# When users connect to the server using a webbrowser, a websocket is opened 
# and this function is called to send the current LED colors
@socketio.on('connect')
def send_led_colors():
    print (f"sending colors.. {json.dumps(dict(colors=colors))}")
    emit('current_colors', json.dumps(dict(colors=colors)))

# When user clicks on a <div> in the webpage, the javascript sends a 
# message encoded as update_led, where data contains the id of the <div>
# and the color of set in the <colorpicker>.
# Once the color is set, the server sends a broadcast message to all 
# connected clients, which updates the LED color at each webbrowser screen. 
@socketio.on('update_led')
def update_led_color(data):
    data = json.loads(data)
    color_rgb = hex_to_rgb_color(data['color'])
    colors[int(data['id'])] = color_rgb
    # Sends broadcast message to connected users and sets the colour on the sensehat.
    sense.set_pixels(colors)     
    emit('update_led', 
         json.dumps(dict(
            id=data['id'],
            color=data['color'])), 
         broadcast=True)
         
@socketio.on('clear_leds')
def clear_leds():
    # Sets the default colour of the board
    for i in range(64): 
        colors[i] = [10,10,10]
    # Uses the current_colors javascript function to clear the RGB
    # By setting the current colour into the default colour
    emit('current_colors', json.dumps(dict(colors=colors)))
    # Clear sensehat scripts
    sense.clear()
    
if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", debug=True)
