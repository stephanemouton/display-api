from flask import Flask, request

app = Flask(__name__)

global DISPLAYS


@app.route('/displays', methods=['GET'])
def get_available_displays():
    return DISPLAYS, 200


@app.route('/display/<int:display_id>/set_cursor', methods=['POST'])
def set_cursor(display_id):
    try:
        display = get_display(display_id)
        position = request.args.to_dict()
        validate_position(display)

        # send the message to the display
        send_cursor_position(display, position)
        return 'wilco', 202
    except ValueError as e:
        return str(e), 400

@app.route('/display/<int:display_id>/write', methods=['POST'])
def write_message(display_id):
    try:
        display = get_display(display_id)
        position = request.args.to_dict()
        validate_position(display)

        message = str(request.data)
        send_message_to_display(display, message, position)
        return 'wilco', 202
    except ValueError as e:
        return str(e), 400


@app.route('/screens/<int:display_id>/clear', methods=['POST'])
def clear_display(display_id):
    try:
        display = get_display(display_id)
        send_clear_command(display)
        return 'wilco', 202
    except ValueError as e:
        return str(e), 400


@app.route('/brew', methods=['POST', 'BREW'])
def brew():
    return "I'm a teapot", 418


def detect_displays():
    global DISPLAYS
    DISPLAYS = [{
        "id": 0,
        "max_x": 19,
        "max_y": 1
    }]

def send_cursor_position(display, position):
    pass

def send_message_to_display(display, message, position):
    pass

def send_clear_command(display):
    pass

def get_display(display_id):
    if display_id > len(DISPLAYS)-1:
        raise ValueError("Invalid display id")

    return DISPLAYS[display_id]

def validate_position(position: dict, display):
    if position.x < 0 or position.x > display.max_x or position.y < 0 or position.y > display.max_y:
        raise ValueError("Invalid position for this display")

if __name__ == '__main__':
    detect_displays()
    app.run()
