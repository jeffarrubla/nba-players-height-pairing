### Mach Eight Sample Project

Thank you for taking the time to complete this sample project. We're a tech
first company and we value our engineers tremendously. We're are looking for
hard working, smart engineers with either excellent experience or lots of
potential.


## Project

The project is to write a function that searches through NBA player heights
based on user input. The raw data is taken from
[here](https://www.openintro.org/data/index.php?data=nba_heights).  The data is
served in json format by the endpoint
[here](https://mach-eight.uc.r.appspot.com/).

The task is to create an application that takes a single integer input. The
application will download the raw data from the website above
(https://mach-eight.uc.r.appspot.com) and print a list of all pairs of players
whose height in inches adds up to the integer input to the application. If no
matches are found, the application will print "No matches found"

Sample output is as follows:
```
> app 139

- Brevin Knight         Nate Robinson
- Nate Robinson         Mike Wilks
```

The algorithm to find the pairs must be faster than O(n^2). All edge cases
should be handled appropriately. This is _not_ a closed book test. You are
encouraged to reach out with any questions that you come across.

## Evaluation

All candidates who submit an algorithm that is efficient and correct will pass
to the next step of the interview process. We define "efficient" as faster than
O(n^2) and "correct" as returning the correct results for all possible inputs.
Any assignment that doesn't return the correct answer for the sample input
above (139) will fail.

If you feel the need to impress us by going above and beyond, we're impressed
by good unit tests as well as clean and readable code. We're less interested in
your knowledge of any particular framework (react, django, etc.). You're
welcome to create a full featured web app with pretty graphics if you want, but
that will not improve your chances of passing. There have been passing
assignments written in under 30 lines of python.


## Submission

The preferred form of submission is by publishing a public repo on github with
your code and a README file explaining how to run the code. I also can accept
an emailed zip file with the same contents. 
#json = [{"first_name":"Alex","h_in":"77","h_meters":"1.96","last_name":"Acker"},{"first_name":"Hassan","h_in":"76","h_meters":"1.93","last_name":"Adams"},{"first_name":"Arron","h_in":"77","h_meters":"1.96","last_name":"Afflalo"},{"first_name":"Maurice","h_in":"77","h_meters":"1.96","last_name":"Ager"},{"first_name":"Alexis","h_in":"84","h_meters":"2.13","last_name":"Ajinca"},{"first_name":"LaMarcus","h_in":"83","h_meters":"2.11","last_name":"Aldridge"},{"first_name":"Joe","h_in":"80","h_meters":"2.03","last_name":"Alexander"},{"first_name":"Malik","h_in":"82","h_meters":"2.08","last_name":"Allen"},{"first_name":"Ray","h_in":"77","h_meters":"1.96","last_name":"Allen"},{"first_name":"Tony","h_in":"76","h_meters":"1.93","last_name":"Allen"},{"first_name":"Morris","h_in":"78","h_meters":"1.98","last_name":"Almond"},{"first_name":"Rafer","h_in":"74","h_meters":"1.88","last_name":"Alston"},{"first_name":"Louis","h_in":"81","h_meters":"2.06","last_name":"Amundson"},{"first_name":"Chris","h_in":"82","h_meters":"2.08","last_name":"Andersen"},{"first_name":"Ryan","h_in":"82","h_meters":"2.08","last_name":"Anderson"},{"first_name":"Carmelo","h_in":"80","h_meters":"2.03","last_name":"Anthony"},{"first_name":"Joel","h_in":"81","h_meters":"2.06","last_name":"Anthony"},{"first_name":"Gilbert","h_in":"76","h_meters":"1.93","last_name":"Arenas"},{"first_name":"Trevor","h_in":"80","h_meters":"2.03","last_name":"Ariza"},{"first_name":"Hilton","h_in":"83","h_meters":"2.11","last_name":"Armstrong"},{"first_name":"Ron","h_in":"79","h_meters":"2.01","last_name":"Artest"},{"first_name":"Darrell","h_in":"81","h_meters":"2.06","last_name":"Arthur"},{"first_name":"Chucky","h_in":"71","h_meters":"1.8","last_name":"Atkins"},{"first_name":"D.J.","h_in":"72","h_meters":"1.83","last_name":"Augustin"},{"first_name":"Kelenna","h_in":"77","h_meters":"1.96","last_name":"Azubuike"},{"first_name":"Renaldo","h_in":"80","h_meters":"2.03","last_name":"Balkman"},{"first_name":"Marcus","h_in":"74","h_meters":"1.88","last_name":"Banks"},{"first_name":"Leandro","h_in":"75","h_meters":"1.91","last_name":"Barbosa"},{"first_name":"Jose","h_in":"72","h_meters":"1.83","last_name":"Barea"},{"first_name":"Andrea","h_in":"84","h_meters":"2.13","last_name":"Bargnani"},{"first_name":"Matt","h_in":"79","h_meters":"2.01","last_name":"Barnes"},{"first_name":"Brent","h_in":"79","h_meters":"2.01","last_name":"Barry"},{"first_name":"Brandon","h_in":"80","h_meters":"2.03","last_name":"Bass"},{"first_name":"Maceo","h_in":"82","h_meters":"2.08","last_name":"Baston"},{"first_name":"Tony","h_in":"83","h_meters":"2.11","last_name":"Battie"},{"first_name":"Shane","h_in":"80","h_meters":"2.03","last_name":"Battier"},{"first_name":"Nicolas","h_in":"80","h_meters":"2.03","last_name":"Batum"},{"first_name":"Jerryd","h_in":"75","h_meters":"1.91","last_name":"Bayless"},{"first_name":"Michael","h_in":"81","h_meters":"2.06","last_name":"Beasley"},{"first_name":"Marco","h_in":"77","h_meters":"1.96","last_name":"Belinelli"},{"first_name":"Charlie","h_in":"75","h_meters":"1.91","last_name":"Bell"},{"first_name":"Raja","h_in":"77","h_meters":"1.96","last_name":"Bell"},{"first_name":"Mike","h_in":"74","h_meters":"1.88","last_name":"Bibby"},{"first_name":"Andris","h_in":"83","h_meters":"2.11","last_name":"Biedrins"},{"first_name":"Chauncey","h_in":"75","h_meters":"1.91","last_name":"Billups"},{"first_name":"Steve","h_in":"75","h_meters":"1.91","last_name":"Blake"},{"first_name":"Andray","h_in":"83","h_meters":"2.11","last_name":"Blatche"},{"first_name":"Mark","h_in":"84","h_meters":"2.13","last_name":"Blount"},{"first_name":"Keith","h_in":"77","h_meters":"1.96","last_name":"Bogans"},{"first_name":"Andrew","h_in":"84","h_meters":"2.13","last_name":"Bogut"},{"first_name":"Matt","h_in":"82","h_meters":"2.08","last_name":"Bonner"},{"first_name":"Josh","h_in":"82","h_meters":"2.08","last_name":"Boone"},{"first_name":"Calvin","h_in":"83","h_meters":"2.11","last_name":"Booth"},{"first_name":"Carlos","h_in":"81","h_meters":"2.06","last_name":"Boozer"},{"first_name":"Chris","h_in":"82","h_meters":"2.08","last_name":"Bosh"},{"first_name":"Bruce","h_in":"79","h_meters":"2.01","last_name":"Bowen"},{"first_name":"Ryan","h_in":"81","h_meters":"2.06","last_name":"Bowen"},{"first_name":"Elton","h_in":"81","h_meters":"2.06","last_name":"Brand"},{"first_name":"Corey","h_in":"81","h_meters":"2.06","last_name":"Brewer"},{"first_name":"Ronnie","h_in":"79","h_meters":"2.01","last_name":"Brewer"},{"first_name":"Aaron","h_in":"72","h_meters":"1.83","last_name":"Brooks"},{"first_name":"Andre","h_in":"81","h_meters":"2.06","last_name":"Brown"},{"first_name":"Bobby","h_in":"74","h_meters":"1.88","last_name":"Brown"},{"first_name":"Dee","h_in":"72","h_meters":"1.83","last_name":"Brown"},{"first_name":"Devin","h_in":"77","h_meters":"1.96","last_name":"Brown"},{"first_name":"Kwame","h_in":"83","h_meters":"2.11","last_name":"Brown"},{"first_name":"Shannon","h_in":"76","h_meters":"1.93","last_name":"Brown"},{"first_name":"Kobe","h_in":"78","h_meters":"1.98","last_name":"Bryant"},{"first_name":"Greg","h_in":"76","h_meters":"1.93","last_name":"Buckner"},{"first_name":"Caron","h_in":"79","h_meters":"2.01","last_name":"Butler"},{"first_name":"Rasual","h_in":"79","h_meters":"2.01","last_name":"Butler"},{"first_name":"Andrew","h_in":"84","h_meters":"2.13","last_name":"Bynum"},{"first_name":"Will","h_in":"72","h_meters":"1.83","last_name":"Bynum"},{"first_name":"Jose","h_in":"75","h_meters":"1.91","last_name":"Calderon"},{"first_name":"Marcus","h_in":"83","h_meters":"2.11","last_name":"Camby"},{"first_name":"Brian","h_in":"80","h_meters":"2.03","last_name":"Cardinal"},{"first_name":"Rodney","h_in":"79","h_meters":"2.01","last_name":"Carney"},{"first_name":"Matt","h_in":"78","h_meters":"1.98","last_name":"Carroll"},{"first_name":"Anthony","h_in":"74","h_meters":"1.88","last_name":"Carter"},{"first_name":"Vince","h_in":"78","h_meters":"1.98","last_name":"Carter"},{"first_name":"Sam","h_in":"75","h_meters":"1.91","last_name":"Cassell"},{"first_name":"Mario","h_in":"73","h_meters":"1.85","last_name":"Chalmers"},{"first_name":"Tyson","h_in":"85","h_meters":"2.16","last_name":"Chandler"},{"first_name":"Wilson","h_in":"80","h_meters":"2.03","last_name":"Chandler"},{"first_name":"Speedy","h_in":"71","h_meters":"1.8","last_name":"Claxton"},{"first_name":"Jarron","h_in":"83","h_meters":"2.11","last_name":"Collins"},{"first_name":"Jason","h_in":"84","h_meters":"2.13","last_name":"Collins"},{"first_name":"Mardy","h_in":"78","h_meters":"1.98","last_name":"Collins"},{"first_name":"Nick","h_in":"82","h_meters":"2.08","last_name":"Collison"},{"first_name":"Mike","h_in":"73","h_meters":"1.85","last_name":"Conley"},{"first_name":"Brian","h_in":"81","h_meters":"2.06","last_name":"Cook"},{"first_name":"Daequan","h_in":"77","h_meters":"1.96","last_name":"Cook"},{"first_name":"Jamal","h_in":"77","h_meters":"1.96","last_name":"Crawford"},{"first_name":"Javaris","h_in":"77","h_meters":"1.96","last_name":"Crittenton"},{"first_name":"Austin","h_in":"82","h_meters":"2.08","last_name":"Croshere"},{"first_name":"Eddy","h_in":"83","h_meters":"2.11","last_name":"Curry"},{"first_name":"Samuel","h_in":"83","h_meters":"2.11","last_name":"Dalembert"},{"first_name":"Erick","h_in":"83","h_meters":"2.11","last_name":"Dampier"},{"first_name":"Antonio","h_in":"76","h_meters":"1.93","last_name":"Daniels"},{"first_name":"Marquis","h_in":"78","h_meters":"1.98","last_name":"Daniels"},{"first_name":"Baron","h_in":"75","h_meters":"1.91","last_name":"Davis"},{"first_name":"Glen","h_in":"81","h_meters":"2.06","last_name":"Davis"},{"first_name":"Paul","h_in":"83","h_meters":"2.11","last_name":"Davis"},{"first_name":"Ricky","h_in":"79","h_meters":"2.01","last_name":"Davis"},{"first_name":"Luol","h_in":"81","h_meters":"2.06","last_name":"Deng"},{"first_name":"Boris","h_in":"80","h_meters":"2.03","last_name":"Diaw"},{"first_name":"Yakhouba","h_in":"79","h_meters":"2.01","last_name":"Diawara"},{"first_name":"Travis","h_in":"73","h_meters":"1.85","last_name":"Diener"},{"first_name":"Ike","h_in":"81","h_meters":"2.06","last_name":"Diogu"},{"first_name":"DeSagana","h_in":"84","h_meters":"2.13","last_name":"Diop"},{"first_name":"Juan","h_in":"75","h_meters":"1.91","last_name":"Dixon"},{"first_name":"Keyon","h_in":"75","h_meters":"1.91","last_name":"Dooling"},{"first_name":"Joey","h_in":"80","h_meters":"2.03","last_name":"Dorsey"},{"first_name":"Quincy","h_in":"75","h_meters":"1.91","last_name":"Douby"},{"first_name":"Chris","h_in":"79","h_meters":"2.01","last_name":"Douglas-Roberts"},{"first_name":"Goran","h_in":"76","h_meters":"1.93","last_name":"Dragic"},{"first_name":"Jared","h_in":"79","h_meters":"2.01","last_name":"Dudley"},{"first_name":"Chris","h_in":"73","h_meters":"1.85","last_name":"Duhon"},{"first_name":"Tim","h_in":"83","h_meters":"2.11","last_name":"Duncan"},{"first_name":"Mike","h_in":"81","h_meters":"2.06","last_name":"Dunleavy"},{"first_name":"Kevin","h_in":"81","h_meters":"2.06","last_name":"Durant"},{"first_name":"Francisco","h_in":"84","h_meters":"2.13","last_name":"Elson"},{"first_name":"Melvin","h_in":"82","h_meters":"2.08","last_name":"Ely"},{"first_name":"Maurice","h_in":"77","h_meters":"1.96","last_name":"Evans"},{"first_name":"Reggie","h_in":"80","h_meters":"2.03","last_name":"Evans"},{"first_name":"Jordan","h_in":"74","h_meters":"1.88","last_name":"Farmar"},{"first_name":"Desmon","h_in":"77","h_meters":"1.96","last_name":"Farmer"},{"first_name":"Raymond","h_in":"73","h_meters":"1.85","last_name":"Felton"},{"first_name":"Rudy","h_in":"78","h_meters":"1.98","last_name":"Fernandez"},{"first_name":"Kyrylo","h_in":"85","h_meters":"2.16","last_name":"Fesenko"},{"first_name":"Michael","h_in":"79","h_meters":"2.01","last_name":"Finley"},{"first_name":"Derek","h_in":"73","h_meters":"1.85","last_name":"Fisher"},{"first_name":"T.J.","h_in":"72","h_meters":"1.83","last_name":"Ford"},{"first_name":"Jeff","h_in":"83","h_meters":"2.11","last_name":"Foster"},{"first_name":"Randy","h_in":"76","h_meters":"1.93","last_name":"Foye"},{"first_name":"Adonal","h_in":"82","h_meters":"2.08","last_name":"Foyle"},{"first_name":"Steve","h_in":"75","h_meters":"1.91","last_name":"Francis"},{"first_name":"Channing","h_in":"83","h_meters":"2.11","last_name":"Frye"},{"first_name":"Dan","h_in":"83","h_meters":"2.11","last_name":"Gadzuric"},{"first_name":"Danilo","h_in":"82","h_meters":"2.08","last_name":"Gallinari"},{"first_name":"Francisco","h_in":"79","h_meters":"2.01","last_name":"Garcia"},{"first_name":"Thomas","h_in":"77","h_meters":"1.96","last_name":"Gardner"},{"first_name":"Kevin","h_in":"83","h_meters":"2.11","last_name":"Garnett"},{"first_name":"Marc","h_in":"85","h_meters":"2.16","last_name":"Gasol"},{"first_name":"Pau","h_in":"84","h_meters":"2.13","last_name":"Gasol"},{"first_name":"Rudy","h_in":"80","h_meters":"2.03","last_name":"Gay"},{"first_name":"Devean","h_in":"80","h_meters":"2.03","last_name":"George"},{"first_name":"Daniel","h_in":"74","h_meters":"1.88","last_name":"Gibson"},{"first_name":"J.R.","h_in":"77","h_meters":"1.96","last_name":"Giddens"},{"first_name":"Manu","h_in":"78","h_meters":"1.98","last_name":"Ginobili"},{"first_name":"Ryan","h_in":"79","h_meters":"2.01","last_name":"Gomes"},{"first_name":"Drew","h_in":"82","h_meters":"2.08","last_name":"Gooden"},{"first_name":"Ben","h_in":"75","h_meters":"1.91","last_name":"Gordon"},{"first_name":"Eric","h_in":"75","h_meters":"1.91","last_name":"Gordon"},{"first_name":"Marcin","h_in":"83","h_meters":"2.11","last_name":"Gortat"},{"first_name":"Joey","h_in":"79","h_meters":"2.01","last_name":"Graham"},{"first_name":"Stephen","h_in":"78","h_meters":"1.98","last_name":"Graham"},{"first_name":"Danny","h_in":"80","h_meters":"2.03","last_name":"Granger"},{"first_name":"Aaron","h_in":"84","h_meters":"2.13","last_name":"Gray"},{"first_name":"Gerald","h_in":"80","h_meters":"2.03","last_name":"Green"},{"first_name":"Jeff","h_in":"81","h_meters":"2.06","last_name":"Green"},{"first_name":"Willie","h_in":"75","h_meters":"1.91","last_name":"Green"},{"first_name":"Donte","h_in":"83","h_meters":"2.11","last_name":"Greene"},{"first_name":"Hamed","h_in":"86","h_meters":"2.18","last_name":"Haddadi"},{"first_name":"Richard","h_in":"79","h_meters":"2.01","last_name":"Hamilton"},{"first_name":"Matt","h_in":"79","h_meters":"2.01","last_name":"Harpring"},{"first_name":"Al","h_in":"81","h_meters":"2.06","last_name":"Harrington"},{"first_name":"Devin","h_in":"75","h_meters":"1.91","last_name":"Harris"},{"first_name":"Jason","h_in":"75","h_meters":"1.91","last_name":"Hart"},{"first_name":"Udonis","h_in":"80","h_meters":"2.03","last_name":"Haslem"},{"first_name":"Trenton","h_in":"77","h_meters":"1.96","last_name":"Hassell"},{"first_name":"Spencer","h_in":"84","h_meters":"2.13","last_name":"Hawes"},{"first_name":"Chuck","h_in":"78","h_meters":"1.98","last_name":"Hayes"},{"first_name":"Jarvis","h_in":"80","h_meters":"2.03","last_name":"Hayes"},{"first_name":"Brendan","h_in":"84","h_meters":"2.13","last_name":"Haywood"},{"first_name":"Luther","h_in":"75","h_meters":"1.91","last_name":"Head"},{"first_name":"Richard","h_in":"81","h_meters":"2.06","last_name":"Hendrix"},{"first_name":"Walter","h_in":"81","h_meters":"2.06","last_name":"Herrmann"},{"first_name":"Roy","h_in":"86","h_meters":"2.18","last_name":"Hibbert"},{"first_name":"J.J.","h_in":"81","h_meters":"2.06","last_name":"Hickson"},{"first_name":"George","h_in":"74","h_meters":"1.88","last_name":"Hill"},{"first_name":"Grant","h_in":"80","h_meters":"2.03","last_name":"Hill"},{"first_name":"Steven","h_in":"84","h_meters":"2.13","last_name":"Hill"},{"first_name":"Kirk","h_in":"75","h_meters":"1.91","last_name":"Hinrich"},{"first_name":"Ryan","h_in":"84","h_meters":"2.13","last_name":"Hollins"},{"first_name":"Al","h_in":"82","h_meters":"2.08","last_name":"Horford"},{"first_name":"Eddie","h_in":"73","h_meters":"1.85","last_name":"House"},{"first_name":"Dwight","h_in":"83","h_meters":"2.11","last_name":"Howard"},{"first_name":"Josh","h_in":"79","h_meters":"2.01","last_name":"Howard"},{"first_name":"Larry","h_in":"77","h_meters":"1.96","last_name":"Hughes"},{"first_name":"Kris","h_in":"81","h_meters":"2.06","last_name":"Humphries"},{"first_name":"Othello","h_in":"80","h_meters":"2.03","last_name":"Hunter"},{"first_name":"Steven","h_in":"84","h_meters":"2.13","last_name":"Hunter"},{"first_name":"Andre","h_in":"78","h_meters":"1.98","last_name":"Iguodala"},{"first_name":"Zydrunas","h_in":"87","h_meters":"2.21","last_name":"Ilgauskas"},{"first_name":"Didier","h_in":"84","h_meters":"2.13","last_name":"Ilunga-Mbenga"},{"first_name":"Allen","h_in":"72","h_meters":"1.83","last_name":"Iverson"},{"first_name":"Royal","h_in":"76","h_meters":"1.93","last_name":"Ivey"},{"first_name":"Jarrett","h_in":"75","h_meters":"1.91","last_name":"Jack"},{"first_name":"Bobby","h_in":"73","h_meters":"1.85","last_name":"Jackson"},{"first_name":"Darnell","h_in":"81","h_meters":"2.06","last_name":"Jackson"},{"first_name":"Stephen","h_in":"80","h_meters":"2.03","last_name":"Jackson"},{"first_name":"Jerome","h_in":"85","h_meters":"2.16","last_name":"James"},{"first_name":"LeBron","h_in":"80","h_meters":"2.03","last_name":"James"},{"first_name":"Mike","h_in":"74","h_meters":"1.88","last_name":"James"},{"first_name":"Antawn","h_in":"81","h_meters":"2.06","last_name":"Jamison"},{"first_name":"Marko","h_in":"79","h_meters":"2.01","last_name":"Jaric"},{"first_name":"Nathan","h_in":"82","h_meters":"2.08","last_name":"Jawai"},{"first_name":"Al","h_in":"82","h_meters":"2.08","last_name":"Jefferson"},{"first_name":"Richard","h_in":"79","h_meters":"2.01","last_name":"Jefferson"},{"first_name":"Jared","h_in":"83","h_meters":"2.11","last_name":"Jeffries"},{"first_name":"Linton","h_in":"80","h_meters":"2.03","last_name":"Johnson III"},{"first_name":"Amir","h_in":"81","h_meters":"2.06","last_name":"Johnson"},{"first_name":"Anthony","h_in":"75","h_meters":"1.91","last_name":"Johnson"},{"first_name":"Joe","h_in":"79","h_meters":"2.01","last_name":"Johnson"},{"first_name":"Dahntay","h_in":"78","h_meters":"1.98","last_name":"Jones"},{"first_name":"Damon","h_in":"75","h_meters":"1.91","last_name":"Jones"},{"first_name":"James","h_in":"80","h_meters":"2.03","last_name":"Jones"},{"first_name":"Solomon","h_in":"82","h_meters":"2.08","last_name":"Jones"},{"first_name":"DeAndre","h_in":"83","h_meters":"2.11","last_name":"Jordan"},{"first_name":"Chris","h_in":"84","h_meters":"2.13","last_name":"Kaman"},{"first_name":"Jason","h_in":"80","h_meters":"2.03","last_name":"Kapono"},{"first_name":"Jason","h_in":"76","h_meters":"1.93","last_name":"Kidd"},{"first_name":"Tarence","h_in":"78","h_meters":"1.98","last_name":"Kinsey"},{"first_name":"Andrei","h_in":"81","h_meters":"2.06","last_name":"Kirilenko"},{"first_name":"Linas","h_in":"80","h_meters":"2.03","last_name":"Kleiza"},{"first_name":"Brevin","h_in":"70","h_meters":"1.78","last_name":"Knight"},{"first_name":"Kyle","h_in":"79","h_meters":"2.01","last_name":"Korver"},{"first_name":"Kosta","h_in":"84","h_meters":"2.13","last_name":"Koufos"},{"first_name":"Rob","h_in":"81","h_meters":"2.06","last_name":"Kurz"},{"first_name":"Raef","h_in":"83","h_meters":"2.11","last_name":"LaFrentz"},{"first_name":"Carl","h_in":"81","h_meters":"2.06","last_name":"Landry"},{"first_name":"Acie","h_in":"75","h_meters":"1.91","last_name":"Law"},{"first_name":"Courtney","h_in":"77","h_meters":"1.96","last_name":"Lee"},{"first_name":"David","h_in":"81","h_meters":"2.06","last_name":"Lee"},{"first_name":"Rashard","h_in":"82","h_meters":"2.08","last_name":"Lewis"},{"first_name":"Shaun","h_in":"79","h_meters":"2.01","last_name":"Livingston"},{"first_name":"Brook","h_in":"84","h_meters":"2.13","last_name":"Lopez"},{"first_name":"Robin","h_in":"84","h_meters":"2.13","last_name":"Lopez"},{"first_name":"Kevin","h_in":"82","h_meters":"2.08","last_name":"Love"},{"first_name":"Kyle","h_in":"72","h_meters":"1.83","last_name":"Lowry"},{"first_name":"Tyronn","h_in":"72","h_meters":"1.83","last_name":"Lue"},{"first_name":"Mark","h_in":"81","h_meters":"2.06","last_name":"Madsen"},{"first_name":"Corey","h_in":"78","h_meters":"1.98","last_name":"Maggette"},{"first_name":"Jamaal","h_in":"83","h_meters":"2.11","last_name":"Magloire"},{"first_name":"Ian","h_in":"83","h_meters":"2.11","last_name":"Mahinmi"},{"first_name":"Stephon","h_in":"74","h_meters":"1.88","last_name":"Marbury"},{"first_name":"Shawn","h_in":"79","h_meters":"2.01","last_name":"Marion"},{"first_name":"Sean","h_in":"82","h_meters":"2.08","last_name":"Marks"},{"first_name":"Donyell","h_in":"81","h_meters":"2.06","last_name":"Marshall"},{"first_name":"Kenyon","h_in":"81","h_meters":"2.06","last_name":"Martin"},{"first_name":"Kevin","h_in":"79","h_meters":"2.01","last_name":"Martin"},{"first_name":"Desmond","h_in":"77","h_meters":"1.96","last_name":"Mason"},{"first_name":"Roger","h_in":"77","h_meters":"1.96","last_name":"Mason"},{"first_name":"Jason","h_in":"79","h_meters":"2.01","last_name":"Maxiell"},{"first_name":"Sean","h_in":"81","h_meters":"2.06","last_name":"May"},{"first_name":"O.J.","h_in":"76","h_meters":"1.93","last_name":"Mayo"},{"first_name":"Luc","h_in":"80","h_meters":"2.03","last_name":"Mbah a Moute"},{"first_name":"Rashad","h_in":"76","h_meters":"1.93","last_name":"McCants"},{"first_name":"Antonio","h_in":"81","h_meters":"2.06","last_name":"McDyess"},{"first_name":"JaVale","h_in":"84","h_meters":"2.13","last_name":"McGee"},{"first_name":"Tracy","h_in":"80","h_meters":"2.03","last_name":"McGrady"},{"first_name":"Dominic","h_in":"81","h_meters":"2.06","last_name":"McGuire"},{"first_name":"Josh","h_in":"82","h_meters":"2.08","last_name":"McRoberts"},{"first_name":"Chris","h_in":"84","h_meters":"2.13","last_name":"Mihm"},{"first_name":"C.J.","h_in":"78","h_meters":"1.98","last_name":"Miles"},{"first_name":"Darko","h_in":"84","h_meters":"2.13","last_name":"Milicic"},{"first_name":"Andre","h_in":"74","h_meters":"1.88","last_name":"Miller"},{"first_name":"Brad","h_in":"84","h_meters":"2.13","last_name":"Miller"},{"first_name":"Mike","h_in":"80","h_meters":"2.03","last_name":"Miller"},{"first_name":"Paul","h_in":"80","h_meters":"2.03","last_name":"Millsap"},{"first_name":"Cuttino","h_in":"76","h_meters":"1.93","last_name":"Mobley"},{"first_name":"Nazr","h_in":"82","h_meters":"2.08","last_name":"Mohammed"},{"first_name":"Jamario","h_in":"80","h_meters":"2.03","last_name":"Moon"},{"first_name":"Mikki","h_in":"84","h_meters":"2.13","last_name":"Moore"},{"first_name":"Randolph","h_in":"83","h_meters":"2.11","last_name":"Morris"},{"first_name":"Adam","h_in":"80","h_meters":"2.03","last_name":"Morrison"},{"first_name":"Anthony","h_in":"77","h_meters":"1.96","last_name":"Morrow"},{"first_name":"Troy","h_in":"83","h_meters":"2.11","last_name":"Murphy"},{"first_name":"Ronald","h_in":"75","h_meters":"1.91","last_name":"Murray"},{"first_name":"Eduardo","h_in":"80","h_meters":"2.03","last_name":"Najera"},{"first_name":"Steve","h_in":"75","h_meters":"1.91","last_name":"Nash"},{"first_name":"DeMarcus","h_in":"76","h_meters":"1.93","last_name":"Nelson"},{"first_name":"Jameer","h_in":"72","h_meters":"1.83","last_name":"Nelson"},{"first_name":"NA","h_in":"83","h_meters":"2.11","last_name":"Nene"},{"first_name":"Rasho","h_in":"84","h_meters":"2.13","last_name":"Nesterovic"},{"first_name":"Demetris","h_in":"80","h_meters":"2.03","last_name":"Nichols"},{"first_name":"Joakim","h_in":"83","h_meters":"2.11","last_name":"Noah"},{"first_name":"Andres","h_in":"79","h_meters":"2.01","last_name":"Nocioni"},{"first_name":"Steve","h_in":"82","h_meters":"2.08","last_name":"Novak"},{"first_name":"Dirk","h_in":"84","h_meters":"2.13","last_name":"Nowitzki"},{"first_name":"Patrick","h_in":"84","h_meters":"2.13","last_name":"O'Bryant"},{"first_name":"Jermaine","h_in":"83","h_meters":"2.11","last_name":"O'Neal"},{"first_name":"Shaquille","h_in":"85","h_meters":"2.16","last_name":"O'Neal"},{"first_name":"Fabricio","h_in":"82","h_meters":"2.08","last_name":"Oberto"},{"first_name":"Greg","h_in":"84","h_meters":"2.13","last_name":"Oden"},{"first_name":"Lamar","h_in":"82","h_meters":"2.08","last_name":"Odom"},{"first_name":"Emeka","h_in":"82","h_meters":"2.08","last_name":"Okafor"},{"first_name":"Mehmet","h_in":"83","h_meters":"2.11","last_name":"Okur"},{"first_name":"Kevin","h_in":"74","h_meters":"1.88","last_name":"Ollie"},{"first_name":"Travis","h_in":"81","h_meters":"2.06","last_name":"Outlaw"},{"first_name":"Zaza","h_in":"83","h_meters":"2.11","last_name":"Pachulia"},{"first_name":"Anthony","h_in":"78","h_meters":"1.98","last_name":"Parker"},{"first_name":"Tony","h_in":"74","h_meters":"1.88","last_name":"Parker"},{"first_name":"Chris","h_in":"72","h_meters":"1.83","last_name":"Paul"},{"first_name":"Aleksandar","h_in":"79","h_meters":"2.01","last_name":"Pavlovic"},{"first_name":"Oleksiy","h_in":"84","h_meters":"2.13","last_name":"Pecherov"},{"first_name":"Kendrick","h_in":"82","h_meters":"2.08","last_name":"Perkins"},{"first_name":"Morris","h_in":"79","h_meters":"2.01","last_name":"Peterson"},{"first_name":"Johan","h_in":"84","h_meters":"2.13","last_name":"Petro"},{"first_name":"Paul","h_in":"79","h_meters":"2.01","last_name":"Pierce"},{"first_name":"Mickael","h_in":"78","h_meters":"1.98","last_name":"Pietrus"},{"first_name":"James","h_in":"80","h_meters":"2.03","last_name":"Posey"},{"first_name":"Leon","h_in":"80","h_meters":"2.03","last_name":"Powe"},{"first_name":"Josh","h_in":"81","h_meters":"2.06","last_name":"Powell"},{"first_name":"Ronnie","h_in":"74","h_meters":"1.88","last_name":"Price"},{"first_name":"Tayshaun","h_in":"81","h_meters":"2.06","last_name":"Prince"},{"first_name":"Gabe","h_in":"76","h_meters":"1.93","last_name":"Pruitt"},{"first_name":"Joel","h_in":"85","h_meters":"2.16","last_name":"Przybilla"},{"first_name":"Chris","h_in":"74","h_meters":"1.88","last_name":"Quinn"},{"first_name":"Vladimir","h_in":"82","h_meters":"2.08","last_name":"Radmanovic"},{"first_name":"Anthony","h_in":"82","h_meters":"2.08","last_name":"Randolph"},{"first_name":"Shavlik","h_in":"82","h_meters":"2.08","last_name":"Randolph"},{"first_name":"Zach","h_in":"81","h_meters":"2.06","last_name":"Randolph"},{"first_name":"Theo","h_in":"82","h_meters":"2.08","last_name":"Ratliff"},{"first_name":"Michael","h_in":"78","h_meters":"1.98","last_name":"Redd"},{"first_name":"J.J.","h_in":"76","h_meters":"1.93","last_name":"Redick"},{"first_name":"Jason","h_in":"78","h_meters":"1.98","last_name":"Richardson"},{"first_name":"Jeremy","h_in":"79","h_meters":"2.01","last_name":"Richardson"},{"first_name":"Quentin","h_in":"78","h_meters":"1.98","last_name":"Richardson"},{"first_name":"Luke","h_in":"74","h_meters":"1.88","last_name":"Ridnour"},{"first_name":"Anthony","h_in":"74","h_meters":"1.88","last_name":"Roberson"},{"first_name":"Nate","h_in":"69","h_meters":"1.75","last_name":"Robinson"},{"first_name":"Sergio","h_in":"75","h_meters":"1.91","last_name":"Rodriguez"},{"first_name":"Rajon","h_in":"73","h_meters":"1.85","last_name":"Rondo"},{"first_name":"Derrick","h_in":"75","h_meters":"1.91","last_name":"Rose"},{"first_name":"Malik","h_in":"79","h_meters":"2.01","last_name":"Rose"},{"first_name":"Quinton","h_in":"78","h_meters":"1.98","last_name":"Ross"},{"first_name":"Brandon","h_in":"78","h_meters":"1.98","last_name":"Roy"},{"first_name":"Michael","h_in":"80","h_meters":"2.03","last_name":"Ruffin"},{"first_name":"Brandon","h_in":"78","h_meters":"1.98","last_name":"Rush"},{"first_name":"Kareem","h_in":"78","h_meters":"1.98","last_name":"Rush"},{"first_name":"John","h_in":"78","h_meters":"1.98","last_name":"Salmons"},{"first_name":"Cheikh","h_in":"85","h_meters":"2.16","last_name":"Samb"},{"first_name":"Brian","h_in":"81","h_meters":"2.06","last_name":"Scalabrine"},{"first_name":"Luis","h_in":"81","h_meters":"2.06","last_name":"Scola"},{"first_name":"Thabo","h_in":"79","h_meters":"2.01","last_name":"Sefolosha"},{"first_name":"Mouhamed","h_in":"83","h_meters":"2.11","last_name":"Sene"},{"first_name":"Ramon","h_in":"75","h_meters":"1.91","last_name":"Sessions"},{"first_name":"Walter","h_in":"81","h_meters":"2.06","last_name":"Sharpe"},{"first_name":"Bobby","h_in":"78","h_meters":"1.98","last_name":"Simmons"},{"first_name":"Cedric","h_in":"81","h_meters":"2.06","last_name":"Simmons"},{"first_name":"Sean","h_in":"72","h_meters":"1.83","last_name":"Singletary"},{"first_name":"James","h_in":"80","h_meters":"2.03","last_name":"Singleton"},{"first_name":"Brian","h_in":"81","h_meters":"2.06","last_name":"Skinner"},{"first_name":"Craig","h_in":"79","h_meters":"2.01","last_name":"Smith"},{"first_name":"J.R.","h_in":"78","h_meters":"1.98","last_name":"Smith"},{"first_name":"Jason","h_in":"84","h_meters":"2.13","last_name":"Smith"},{"first_name":"Joe","h_in":"82","h_meters":"2.08","last_name":"Smith"},{"first_name":"Josh","h_in":"81","h_meters":"2.06","last_name":"Smith"},{"first_name":"Eric","h_in":"75","h_meters":"1.91","last_name":"Snow"},{"first_name":"Will","h_in":"73","h_meters":"1.85","last_name":"Solomon"},{"first_name":"Darius","h_in":"81","h_meters":"2.06","last_name":"Songaila"},{"first_name":"Marreese","h_in":"82","h_meters":"2.08","last_name":"Speights"},{"first_name":"Jerry","h_in":"78","h_meters":"1.98","last_name":"Stackhouse"},{"first_name":"DeShawn","h_in":"77","h_meters":"1.96","last_name":"Stevenson"},{"first_name":"Peja","h_in":"82","h_meters":"2.08","last_name":"Stojakovic"},{"first_name":"Amar'e","h_in":"82","h_meters":"2.08","last_name":"Stoudemire"},{"first_name":"Rodney","h_in":"77","h_meters":"1.96","last_name":"Stuckey"},{"first_name":"NA","h_in":"81","h_meters":"2.06","last_name":"Sun Yue"},{"first_name":"Robert","h_in":"85","h_meters":"2.16","last_name":"Swift"},{"first_name":"Stromile","h_in":"82","h_meters":"2.08","last_name":"Swift"},{"first_name":"Wally","h_in":"79","h_meters":"2.01","last_name":"Szczerbiak"},{"first_name":"Mike","h_in":"74","h_meters":"1.88","last_name":"Taylor"},{"first_name":"Sebastian","h_in":"72","h_meters":"1.83","last_name":"Telfair"},{"first_name":"Jason","h_in":"74","h_meters":"1.88","last_name":"Terry"},{"first_name":"Etan","h_in":"82","h_meters":"2.08","last_name":"Thomas"},{"first_name":"Kenny","h_in":"79","h_meters":"2.01","last_name":"Thomas"},{"first_name":"Kurt","h_in":"81","h_meters":"2.06","last_name":"Thomas"},{"first_name":"Tim","h_in":"82","h_meters":"2.08","last_name":"Thomas"},{"first_name":"Tyrus","h_in":"81","h_meters":"2.06","last_name":"Thomas"},{"first_name":"Jason","h_in":"83","h_meters":"2.11","last_name":"Thompson"},{"first_name":"Al","h_in":"80","h_meters":"2.03","last_name":"Thornton"},{"first_name":"Jamaal","h_in":"75","h_meters":"1.91","last_name":"Tinsley"},{"first_name":"Anthony","h_in":"80","h_meters":"2.03","last_name":"Tolliver"},{"first_name":"Alando","h_in":"78","h_meters":"1.98","last_name":"Tucker"},{"first_name":"Ronny","h_in":"82","h_meters":"2.08","last_name":"Turiaf"},{"first_name":"Hedo","h_in":"82","h_meters":"2.08","last_name":"Turkoglu"},{"first_name":"Ime","h_in":"77","h_meters":"1.96","last_name":"Udoka"},{"first_name":"Beno","h_in":"75","h_meters":"1.91","last_name":"Udrih"},{"first_name":"Roko","h_in":"77","h_meters":"1.96","last_name":"Ukic"},{"first_name":"Anderson","h_in":"83","h_meters":"2.11","last_name":"Varejao"},{"first_name":"Jacque","h_in":"73","h_meters":"1.85","last_name":"Vaughn"},{"first_name":"Charlie","h_in":"83","h_meters":"2.11","last_name":"Villanueva"},{"first_name":"Sasha","h_in":"79","h_meters":"2.01","last_name":"Vujacic"},{"first_name":"Dwyane","h_in":"76","h_meters":"1.93","last_name":"Wade"},{"first_name":"Von","h_in":"77","h_meters":"1.96","last_name":"Wafer"},{"first_name":"Antoine","h_in":"81","h_meters":"2.06","last_name":"Walker"},{"first_name":"Bill","h_in":"78","h_meters":"1.98","last_name":"Walker"},{"first_name":"Ben","h_in":"81","h_meters":"2.06","last_name":"Wallace"},{"first_name":"Gerald","h_in":"79","h_meters":"2.01","last_name":"Wallace"},{"first_name":"Rasheed","h_in":"83","h_meters":"2.11","last_name":"Wallace"},{"first_name":"Luke","h_in":"80","h_meters":"2.03","last_name":"Walton"},{"first_name":"Hakim","h_in":"81","h_meters":"2.06","last_name":"Warrick"},{"first_name":"C.J.","h_in":"74","h_meters":"1.88","last_name":"Watson"},{"first_name":"Earl","h_in":"73","h_meters":"1.85","last_name":"Watson"},{"first_name":"Kyle","h_in":"78","h_meters":"1.98","last_name":"Weaver"},{"first_name":"Martell","h_in":"79","h_meters":"2.01","last_name":"Webster"},{"first_name":"Sonny","h_in":"78","h_meters":"1.98","last_name":"Weems"},{"first_name":"David","h_in":"81","h_meters":"2.06","last_name":"West"},{"first_name":"Delonte","h_in":"75","h_meters":"1.91","last_name":"West"},{"first_name":"Mario","h_in":"77","h_meters":"1.96","last_name":"West"},{"first_name":"Russell","h_in":"75","h_meters":"1.91","last_name":"Westbrook"},{"first_name":"D.J.","h_in":"81","h_meters":"2.06","last_name":"White"},{"first_name":"Chris","h_in":"82","h_meters":"2.08","last_name":"Wilcox"},{"first_name":"Damien","h_in":"78","h_meters":"1.98","last_name":"Wilkins"},{"first_name":"Mike","h_in":"70","h_meters":"1.78","last_name":"Wilks"},{"first_name":"Deron","h_in":"75","h_meters":"1.91","last_name":"Williams"},{"first_name":"Jawad","h_in":"81","h_meters":"2.06","last_name":"Williams"},{"first_name":"Louis","h_in":"74","h_meters":"1.88","last_name":"Williams"},{"first_name":"Marcus","h_in":"75","h_meters":"1.91","last_name":"Williams"},{"first_name":"Marvin","h_in":"81","h_meters":"2.06","last_name":"Williams"},{"first_name":"Mo","h_in":"73","h_meters":"1.85","last_name":"Williams"},{"first_name":"Sean","h_in":"82","h_meters":"2.08","last_name":"Williams"},{"first_name":"Shawne","h_in":"81","h_meters":"2.06","last_name":"Williams"},{"first_name":"Shelden","h_in":"81","h_meters":"2.06","last_name":"Williams"},{"first_name":"Antoine","h_in":"79","h_meters":"2.01","last_name":"Wright"},{"first_name":"Brandan","h_in":"82","h_meters":"2.08","last_name":"Wright"},{"first_name":"Dorell","h_in":"81","h_meters":"2.06","last_name":"Wright"},{"first_name":"Julian","h_in":"80","h_meters":"2.03","last_name":"Wright"},{"first_name":"Lorenzen","h_in":"83","h_meters":"2.11","last_name":"Wright"},{"first_name":"Yao","h_in":"90","h_meters":"2.29","last_name":"Ming"},{"first_name":"Yi","h_in":"84","h_meters":"2.13","last_name":"Jianlian"},{"first_name":"Nick","h_in":"78","h_meters":"1.98","last_name":"Young"},{"first_name":"Thaddeus","h_in":"80","h_meters":"2.03","last_name":"Young"}]
