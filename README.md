# Traffic-Tickets-Web-App
Steps to Execute Program (Web-Web):

1.	Bring up the Traffic-Tickets-Webapp directory into the IDE PyCharm as a project. 
2.	The server.py has the code for the webserver. Open that file in the IDE. 
3.	The IDE will install any libraries needed (bottle webserver library, pygame library, etc.). Python 3.7 (or higher most likely) may have to be setup under Project Structure (Module Libraries). 
4.	Run server.py to start the webserver. 
5.	Open the link ‘http://localhost:8080/’ that comes up in the IDE’s run window. 
6.	A browser window should open displaying a map of the Buffalo area with markers pointing to the locations were traffic tickets were issued. 


Architecture and Concepts:

The Project implements a web application that uses Mapbox JavaScript interface on the client-side to display the map and uses Buffalo Traffic Data returned from the server-side to show the markers. The project consists of the following:

1.	Server.py – the file implements a python webserver using the bottle library. Bottle’s static_file return function is used to show the default ‘index.html’ page which in-turn loads the JavaScript file ‘map.js’ and the application icon ‘favicon.ico’. 
2.	Index.html – the page downloads the mapbox JavaScript library code from mapbox server and JavaScript code map.js that implements a function getData() from the webserver. It then calls getData() in the body tag’s onload. getData() uses AJAX GET request (XMLHttpRequest) using the ‘/tickets’ path. The asynchronous code then calls the mapbox library code when the data about Buffalo Traffic Tickets comes back. The tickets data is then used to display markers in the map. Mapbox library has a container tag that is set to ‘map’ that connects it to the div ‘map’ tag in index.html. 
3.	Server.py handles the ‘/tickets’ path by calling the function tickets.get_ticket_data with the parameter of the URL to retrieve the data from - https://data.buffalony.gov/resource/ux3f-ypyc.json 
4.	tickets.get_ticket_data retrieves the JSON string from the URL and converts it to native Python data. 
5.	Note: changing any of the Javascript etc. files that the html accesses can result in the webserver still using the old files due to browser caching. The issue can be avoided by forcing the browser to do a “hard refresh” - Windows: Ctrl+F5, Mac: Cmd+Shift+R, Linux: Ctrl+Shift+R. Also, use “debug=True, reloader=True” as additional bottle.run parameters when developing code.
