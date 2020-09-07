from flask import Flask, jsonify, abort, request

app = Flask ( __name__ )

light = {'id': -1}
@app.route('/')
def index():
        return "Hello, Ganzin user"

@app.route('/light', methods=['GET'])
def get_light():
        return jsonify(light)

@app.route('/light', methods=['PUT'])
def update_light():
        if not request.json:
                abort(400)
        #if 'id' in request.json and type(request.json['id'])!=int:
        #       abort(400)

        light['id'] = request.json.get('id', light['id'])
        return jsonify(light)


if __name__ == '__main__':
        app.run(host='127.0.0.1',port=5000,debug=True)
