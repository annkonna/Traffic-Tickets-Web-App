import bottle
import tickets

@bottle.route('/')
def server_index():
    return bottle.static_file('index.html', root='')

@bottle.route('/favicon.ico')
def server_map():
    return bottle.static_file('favicon.ico', root='')

@bottle.route('/map.js')
def server_index():
    return bottle.static_file('/map.js', root='')

@bottle.route('/tickets')
def get_tickets():
    return tickets.get_ticket_data(
        "https://data.buffalony.gov/resource/ux3f-ypyc.json")


bottle.run(host="localhost", port=8080, debug=True, reloader=True)
# this line instead if running in codenvy - bottle.run(host="0.0.0.0", port=8080, debug=True)
