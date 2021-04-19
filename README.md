### release


### backlog:

* Basic Documentation editorialize
* Email validation?
* Lock up user data
* Feedback
* Connection Visualization
* when learning queue is exhausted, we are currently just jumping back to root w/o explaination
* beim Bearbeiten von Notes: Zwischenspeichern ohne Edit-Modus zu verlassen
* Sendgrid
* First note does not show up in recent
* spellcheck für Texte
* Links immer in neuem Tab öffnen lassen
* einbauen von Latexformeln (pandoc?)
* die Größe beim Editieren einer Note sollte die selbe Größe behalten wie die Original Note
* color gradient over scrollable text
* disallow SSH by password

### wontfix

* zwei Notes sind nicht gleichzeitig bearbeitbar; jedwede andere Aktion schließt unwiderruflich den aktuellen Edit einer Note -> Warnhinweis öffnen
* Erlaube Markdown Formatierung von Code (zB Python)
* Notes in Kästen in der Sidebar: öffnen auch dann, wenn nur in den Kasten geklickt wird


### bugs:

* recent notes (check all cases)
* active users only counts logins, and includes temp users
* password forgot connection problem

### ideas:

* Hypercard
* needs attention button

### future:

* write HN dude

### notes:

* Docker Stuff

`docker-compose -f docker-compose.prod.yml up -d --build`

`docker-compose -f docker-compose.prod.yml logs -f`

* locally, use *testaccount4* for lots of generated notes.
* env is called `.virtualenv`

* The static files sometimes not loading has something to do with the static directory
* For some reason, the server tries to serve the files from an url dependent on the current url we are on

### deploy:

./chaoskasten3/deploy.sh
