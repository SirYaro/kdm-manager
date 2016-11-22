#!/usr/bin/python2.7

male = [
    "Aaron",
    "Adam",
    "Aeneas",
    "Alexander",
    "Alucard",
    "Alister",
    "Anchises",
    "Artorias",
    "Arthur",
    "Asher",
    "Atreyu",
    "Atticus",
    "Amos",
    "Benedict",
    "Borris",
    "Brian",
    "Brooks",
    "Caliban",
    "Calvin",
    "Cecil",
    "Clint",
    "Cole",
    "Conan",
    "Cyril",
    "Cyrus",
    "Damon",
    "Dante",
    "Dashiell",
    "Declan",
    "Demetrius",
    "Demarcus",
    "Delita",
    "Diego",
    "Draco",
    "Duncan",
    "Edward",
    "Eirik",
    "Eli",
    "Elvis",
    "Esteban",
    "Ezekiel",
    "Ezra",
    "Felix",
    "Fidel",
    "Foster",
    "Francis",
    "Gabriel",
    "Gerald",
    "Giovanni",
    "Griffith",
    "Gustavo",
    "Guy",
    "Hadrian",
    "Haakon",
    "Hector",
    "Hideo",
    "Hipolito",
    "Hiram",
    "Hobbes",
    "Hugh",
    "Humberto",
    "Hunter",
    "Ian",
    "Ignacio",
    "Ike",
    "Irving",
    "Israel",
    "Isaac",
    "Jacob",
    "Jacinto",
    "Jeremy",
    "Jesse",
    "Jaoquin",
    "Jon",
    "Jonah",
    "Jorge",
    "Jude",
    "Kalameet",
    "Kane",
    "Karl",
    "Khalil",
    "Kieran",
    "Klaus",
    "Kris",
    "Kyle",
    "Lance",
    "Lazaro",
    "Leif",
    "Logan",
    "Liam",
    "Lincoln",
    "Link",
    "Locke",
    "Lucas",
    "Lucien",
    "Lucius",
    "Luther",
    "Lyman",
    "Malcolm",
    "Malik",
    "Malvolio",
    "Marcus",
    "Mason",
    "Maximo",
    "Maxwell",
    "Maynard",
    "Merlin",
    "Modesto",
    "Mohammed",
    "Moshe",
    "Micah",
    "Nathan",
    "Nestor",
    "Nils",
    "Norman",
    "Noah",
    "Oliver",
    "Orlando",
    "Owen",
    "Paul",
    "Peter",
    "Petrus",
    "Piotr",
    "Preston",
    "Puck",
    "Pug",
    "Quentin",
    "Ramza",
    "Rashad",
    "Ravn",
    "Reuben",
    "Reed",
    "Robb",
    "Robert",
    "Reinhardt",
    "Reinaldo",
    "Rico",
    "Royal",
    "Raynaldo",
    "Roland",
    "Rolondo",
    "Rolo",
    "Royce",
    "Ryu",
    "Sean",
    "Sergei",
    "Setzer",
    "Silas",
    "Shane",
    "Simon",
    "Santiago",
    "Solomon",
    "Sylvester",
    "Sang",
    "Seth",
    "Tetsuo",
    "Thanh",
    "Theron",
    "Timon",
    "Timothy",
    "Titus",
    "Tobias",
    "Trey",
    "Trent",
    "Trevor",
    "Ulf",
    "Ulysses",
    "Umberto",
    "Victor",
    "Vincenzo",
    "Vlad",
    "Valentine",
    "Virgil",
    "Ward",
    "Wallace",
    "William",
    "Wilfred",
    "Xavier",
    "Xerxes",
    "Yang",
    "Zachary",
    "Zane",
    "Zeke",
]

female = [
    "Anna",
    "Arabella",
    "Aria",
    "Athena",
    "Aurora",
    "Ava",
    "Avalon",
    "Beatrice",
    "Belit",
    "Brianne",
    "Bridget",
    "Brooke",
    "Caitlyn",
    "Celes",
    "Camelia",
    "Camilla",
    "Carmen",
    "Casca",
    "Celeste",
    "Charlotte",
    "Cheree",
    "Delphine",
    "Demeter",
    "Desdemona",
    "Diana",
    "Eir",
    "Eirwen",
    "Elena",
    "Eliza",
    "Emilia",
    "Erica",
    "Erza",
    "Esmerelda",
    "Esti",
    "Eve",
    "Fern",
    "Fiona",
    "Frances",
    "Freya",
    "Gabrielle",
    "Genevieve",
    "Gillian",
    "Gloria",
    "Goneril",
    "Grace",
    "Gwen",
    "Haifa",
    "Harper",
    "Heidrun",
    "Hilary",
    "Hope",
    "Igraine",
    "Iman",
    "Ingrid",
    "Iphigeneia",
    "Ira",
    "Irina",
    "Isabella",
    "Isolde",
    "Jaclyn"
    "Janet",
    "Jayne",
    "Jaimie",
    "Jennifer",
    "Juliet",
    "Kalliope",
    "Kara",
    "Katarina",
    "Kendall",
    "Kendra",
    "Kestrel",
    "Kira",
    "Kumiko",
    "Kyra",
    "Lavender",
    "Laverne",
    "Lavinia",
    "Leigh",
    "Libby",
    "Lily",
    "Lucy",
    "Lydia",
    "Maeve",
    "Magdalena",
    "Maleficent",
    "Mallory",
    "Mary",
    "Maria",
    "Maya",
    "Michiko",
    "Minerva",
    "Miranda"
    "Monika",
    "Nadia",
    "Narcissa",
    "Nia",
    "Naomi",
    "Nyx",
    "Odette",
    "Ophelia",
    "Olive",
    "Olivia",
    "Olwen",
    "Opal",
    "Paetra",
    "Paige",
    "Patricia",
    "Pauline",
    "Pearl",
    "Phaedra",
    "Phoebe",
    "Quinn",
    "Quirina",
    "Rachna",
    "Rachel",
    "Rada",
    "Raina",
    "Rasha",
    "Regan",
    "Regina",
    "Renee",
    "Rhea",
    "Rhianon",
    "Rosa",
    "Rosalind",
    "Rosaria",
    "Rosario",
    "Samantha",
    "Sansa",
    "Sara",
    "Scarlett",
    "Scheherazade",
    "Serafina",
    "Shannon",
    "Sophia",
    "Sibyl",
    "Sif",
    "Sigrun",
    "Simone",
    "Sonja",
    "Skyy",
    "Stella",
    "Summer",
    "Tamara",
    "Tamiko",
    "Tara",
    "Thalia",
    "Themis",
    "Ume",
    "Undine",
    "Unice",
    "Valencia",
    "Valeriya",
    "Vena",
    "Velka",
    "Veronica",
    "Viola",
    "Winona",
    "Wiola",
    "Wynter",
    "Xandra",
    "Xiu",
    "Yana",
    "Ylva",
    "Yoko",
    "Zelda",
]

other = [
    "Ghost",
    "Jones",
    "Scout",
    "Shadow",
    "Robin",
    "Quinn",
]
