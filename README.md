# GetPhilo
a Python script to check the "Getting to Philosophy" law.
https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy

## Installation
- first use python 3

 

- ``` pip install -r requirements.txt ```
this command will install
requests ==2.20.1
beautifulsoup4 ==4.7.1

## Run
for example:
- python Main.py https://en.wikipedia.org/wiki/Football

## Test cases

- ### Ordinary test case (successful reached philosophy page)
- link : https://en.wikipedia.org/wiki/Egypt
- in egypt first non parenthized not red outgoing link is (north africa)
```
Egypt (/ˈiːdʒɪpt/ (About this soundlisten) EE-jipt; Arabic: مِصر‎ Miṣr, Egyptian Arabic: مَصر‎ Maṣr, Coptic: Ⲭⲏⲙⲓ Khēmi), officially the Arab Republic of Egypt, is a country spanning the northeast corner of Africa and southwest corner of Asia by a land bridge formed by the Sinai Peninsula. Egypt is a Mediterranean country bordered by the Gaza Strip and Israel to the northeast, the Gulf of Aqaba and the Red Sea to the east, Sudan to the south, and Libya to the west. Across the Gulf of Aqaba lies Jordan, across the Red Sea lies Saudi Arabia, and across the Mediterranean lie Greece, Turkey and Cyprus, although none share a land border with Egypt.
```
- result 
```
/wiki/North_Africa
/wiki/Africa
/wiki/Continent
/wiki/Landmass
/wiki/Land
/wiki/Earth
/wiki/Planet
/wiki/Astronomical_body
/wiki/Physical_body
/wiki/3-dimensional_space
/wiki/Dimension
/wiki/Physics
/wiki/Natural_science
/wiki/Branches_of_science
/wiki/Science
/wiki/Knowledge
/wiki/Fact
/wiki/Reality
/wiki/Object_of_the_mind
/wiki/Object_(philosophy)
/wiki/Philosophy
 we have reached philosophy
```
- ### test case (page with no outgoing links)
- link : https://en.wikipedia.org/wiki/Akeno_Observatory
```Akeno Observatory is a cosmic ray observatory located in Akeno, a town in Yamanashi prefecture, Japan. The observatory is run by the Institute for Cosmic Ray Research (ICRR), based at the University of Tokyo[1]. Akeno Observatory features AGASA, the Akeno Giant Air Shower Array, which studies the origins of very high energy cosmic rays[2].

Construction of the observatory began in 1975, and in 1977 it became the second attached institution with ICRR. Its accomplishments include the observation of a super high energy cosmic ray air shower in 1995 that was previously thought to be impossible[3].
```
- result 
```
page has no outgoing links
```
- ### test case (page with redlink as the first link)
- link : https://en.wikipedia.org/wiki/Wikipedia:Red_link
- first red link ignored and choose the link after it
```
A red link, like this one, signifies that the linked-to page does not exist‍—‌it either never existed, or previously existed but has been deleted. It is useful while editing articles to add a red link to indicate that a page will be created soon or that an article should be created for the topic because the subject is notable and verifiable. Red links help Wikipedia grow.[1] The creation of red links prevents new pages from being orphaned from the start.[2]
```
- result 
```
/wiki/Wikipedia:Viewing_deleted_content
/wiki/Wikipedia:ADMIN
/wiki/Wikipedia:BLOCK
/wiki/Wikipedia:Administrators
/wiki/Wikipedia:BLOCK
 we have stucked in a loop
```

- ### test case (page with external link as the first link(to wikidictionry not wikipedia))
- link : https://en.wikipedia.org/wiki/Physical_object
```
In common usage, a physical object or physical body (or simply a object or body) is a collection of matter within a defined contiguous boundary in 3-dimensional space.[citation needed] The boundary must be defined and identified by the properties of the material. 
```
- result 
```
/wiki/3-dimensional_space
/wiki/Dimension
/wiki/Physics
/wiki/Natural_science
/wiki/Branches_of_science
/wiki/Science
/wiki/Knowledge
/wiki/Fact
/wiki/Reality
/wiki/Object_of_the_mind
/wiki/Object_(philosophy)
/wiki/Philosophy
 we have reached philosophy
```

- ### test case (page with loop)
- link : https://en.wikipedia.org/wiki/Football
```
Football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal. Unqualified, the word football is understood to refer to whichever form of football is the most popular in the regional context in which the word appears. Sports commonly called football in certain places include association football (known as soccer in some countries); 
```
- result 
```
/wiki/Team_sport
/wiki/Sport
/wiki/Competition
/wiki/Rivalry
/wiki/Competitive
/wiki/Rivalry
 we have stucked in a loop
```
- ### test case (successfully reached philosophy)
- link : https://en.wikipedia.org/wiki/Muhammad_Ali
```
Muhammad Ali (/ɑːˈliː/;[4] born Cassius Marcellus Clay Jr.;[5] January 17, 1942 – June 3, 2016) was an American professional boxer, activist, and philanthropist. He is nicknamed "The Greatest" and is widely regarded as one of the most significant and celebrated sports figures of the 20th century and as one of the greatest boxers of all time.

Ali was born and raised in Louisville, Kentucky, and began training as an amateur boxer at age 12. At 18, he won a gold medal in the light heavyweight division at the 1960 Summer Olympics, and turned professional later that year. He converted to Islam and became a Muslim after 1961, and eventually took the name Muhammad Ali. He won the world heavyweight championship from Sonny Liston in a major upset at age 22 in 1964. In 1966, Ali refused to be drafted into 
```
- result 
```
/wiki/Louisville,_Kentucky
/wiki/List_of_cities_in_Kentucky
/wiki/Kentucky
/wiki/U.S._state
/wiki/United_States
/wiki/Country
/wiki/Political_geography
/wiki/Politics
/wiki/Decision-making
/wiki/Psychology
/wiki/Science
/wiki/Knowledge
/wiki/Fact
/wiki/Reality
/wiki/Object_of_the_mind
/wiki/Object_(philosophy)
/wiki/Philosophy
 we have reached philosophy
```
