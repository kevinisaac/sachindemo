from flask import Flask, render_template, request, jsonify, abort

app = Flask('My project')

@app.route('/')
def home_route():
    response_object = jsonify({
        'hello': 'world',
    })

    return response_object

@app.route('/settings')
def settings_route():
    return 'User settings page'
    
