
style centered_style:
    xalign 0.4
    yalign 0.4
    spacing 15

style patreon_text:
    color "#fff"
    selected_color "#ff0"

#screen for viewing inventory
screen inventory_screen(item_list,adj):
    modal True
    frame:
        xsize 400
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                style "centered_style"
                for item in item_list:
                    textbutton item:
                        action Return(item)


        bar adjustment adj style "vscrollbar"

        textbutton _("Exit Inventory."):
            xfill True
            action Return(False)
            top_margin 10




#screen for viewing Quests
screen quest_screen(quest_list, completed_list, adj):
    modal True
    frame:
        xsize 500
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                #style "centered_style"

                null height 10
                text "Current Quests"
                null height 5


                for item in quest_list:

                    textbutton item:
                        action Return(item)


                null height 10
                text "Completed Quests"
                null height 5

                for item in completed_list:
                    textbutton item

        bar adjustment adj style "vscrollbar"

        textbutton _("Exit."):
            xfill True
            action Return(False)
            top_margin 10


#screen for viewing and choosing player outfit
screen outfit_screen(item_list,adj):
    modal True
    frame:
        xsize 400
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                style "centered_style"
                for item in item_list:
                    textbutton item:
                        action Return(item)


        bar adjustment adj style "vscrollbar"

        textbutton _("Exit Inventory."):
            xfill True
            action Return(False)
            top_margin 10

#screen for giving someone something from yoiur inventory
screen inventory_screenGive(item_list,adj):
    modal True
    frame:
        xsize 400
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                style "centered_style"
                for item in item_list:
                    textbutton item:
                        action Return(item)


        bar adjustment adj style "vscrollbar"

        textbutton _("Exit Inventory."):
            xfill True
            action Return(False)
            top_margin 10

#screen for shopping from sarah
screen shop_screen(item_list,gold,adj):
    modal True
    frame:
        xsize 400
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                style "centered_style"
                for item in item_list:
                    textbutton item:
                        action Return(item)


        bar adjustment adj style "vscrollbar"


        textbutton _("Finish Looking."):
            xfill True
            action [ Hide("shop_screen"), Return(None)]
            top_margin 10

#screen for shopping from gliff
screen gliff_screen(item_list,adj):
    modal True
    frame:
        xsize 400
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                style "centered_style"
                for item in item_list:
                    textbutton item:
                        action Return(item)


        bar adjustment adj style "vscrollbar"


        textbutton _("Leave Store."):
            xfill True
            action [ Hide("gliff_screen"), Return(None)]
            top_margin 10


#screen for the clothes inventory of the girls
screen screen_clothes(clothes_list,adj):
    modal True
    frame:
        xsize 400
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                style "centered_style"
                for item in clothes_list:
                    textbutton item:
                        action Return(item)


        bar adjustment adj style "vscrollbar"

        textbutton _("That's enough for now."):
            xfill True
            action [ Hide("screen_clothes"), Return(None)]
            top_margin 10

screen girl_List(girl_list,adj):
    modal True
    frame:
        xsize 400
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                style "centered_style"
                for item in girl_list:
                    textbutton item:
                        action Return(item)


        bar adjustment adj style "vscrollbar"

        textbutton _("That's enough for now."):
            xfill True
            action [ Hide("girl_List"), Return(None)]
            top_margin 10

screen banquet_screen(girl_list,adj):
    modal True
    frame:
        xsize 400
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                style "centered_style"
                for item in girl_list:
                    textbutton item:
                        action Return(item)


        bar adjustment adj style "vscrollbar"

        textbutton _("No Banquet this week."):
            xfill True
            action [ Hide("girl_List"), Return(None)]
            top_margin 10

#screen to view and revisit past sex scenes
screen view_scenes(scene_list,adj):
    modal True
    frame:
        xsize 400
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                style "centered_style"
                for item in scene_list:
                    textbutton item:
                        action Return(item)


        bar adjustment adj style "vscrollbar"

        textbutton _("Go Back."):
            xfill True
            action [ Hide("scene_List"), Return(None)]
            top_margin 10



#patreon supporters screen, view only no functions
screen patreon_supporters(adj):
    modal True

    frame:
        xsize 350
        xalign .5
        ysize 600
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
               # style "patreon_text"

                null height 10
                text "Twentyfive Dollar Patrons"
                null height 5

                textbutton "Dal Vispu"

                null height 10
                text "Ten Dollar Patrons"
                null height 5


                textbutton "Davidjir"
                textbutton "citi96"
                textbutton "Nighthawkvibes"
                textbutton "No Fucking Way"
                textbutton "Thomas Pannier"
                textbutton "Kyle smithart"
                textbutton "Lederpusmaximus"
                textbutton "Matthew L Young"
                textbutton "realname_tba"
                textbutton "Stefan Kemske"
                textbutton "altherr martin"
                textbutton "Aurelien Adam"
                textbutton "Reegus Rockus"
                textbutton "Calabriel Atreides"
                textbutton "Dennes Diaz"
                textbutton "Emil Lind"
                textbutton "Aquis Hyperion"
                textbutton "Anthony Evett-beadon"
                textbutton "Marco Pedroso"
                textbutton "BigR"
                textbutton "Alex Bakker"
                textbutton "Bubonic"
                textbutton "Christian Dennis"
                textbutton "Daniel Cambell"
                textbutton "Ea7gign"
                textbutton "Helok"
                textbutton "Kyuca"
                textbutton "Queldroma32"
                textbutton "realname_tba"
                textbutton "Styrka"
                textbutton "Tyler Winningham"
                textbutton "Valtyr"
                textbutton "Andrew In"
                textbutton "Taylor Wilmore"
                textbutton "Dawjaw"
                textbutton "Aegis Linnear"
                textbutton "Scumknuckles"


                null height 10
                text "Five Dollar Patrons"
                null height 5

                textbutton "Kyle Jones"
                textbutton "LarryLaw"
                textbutton "jon"
                textbutton "Gregarwolf"
                textbutton "Aeryn Monet"
                textbutton "Warden Malice"
                textbutton "Roger McBigfan"
                textbutton "WakWaku"
                textbutton "The Dark Wanderer"
                textbutton "Chris father of Belle"
                textbutton "carrotz"
                textbutton "Cteno"
                textbutton "ANK Exposure"
                textbutton "DrCockroach"
                textbutton "Easton Honaker"
                textbutton "ScaredEnigma"
                textbutton "Baron Munchausan"
                textbutton "Abdul"
                textbutton "Ant"
                textbutton "Aquis Hyperion"
                textbutton "Awetcarrot"
                textbutton "Bob Russ"
                textbutton "Brian Tse"
                textbutton "Chandler Muehlberg"
                textbutton "dalton"
                textbutton "Frimann Haukur"
                textbutton "grgo"
                textbutton "Jeppe Risager"
                textbutton "Lan-Technology.de"
                textbutton "Maximuz Odtuhan"
                textbutton "william morton"
                textbutton "AbstractRude"
                textbutton "Alex"
                textbutton "Alexandre Monnier"
                textbutton "Barkior"
                textbutton "Baron Munchausan"
                textbutton "Bigup17"
                textbutton "BlattMeister"
                textbutton "Bubonic"
                textbutton "Chris Poole"
                textbutton "Dani Dener"
                textbutton "Danielle Campbell"
                textbutton "Darkkrow13"
                textbutton "Don Brown"
                textbutton "Dracyllion"
                textbutton "Gottmorder"
                textbutton "Heavenlyhell64"
                textbutton "Jimmylamtk"
                textbutton "Jonah"
                textbutton "Joseph Grantom"
                textbutton "Josh"
                textbutton "Josh Westwood"
                textbutton "Kiriba"
                textbutton "Kristopher"
                textbutton "Levone W."
                textbutton "Lonesommuffin"
                textbutton "lulno"
                textbutton "Lyon"
                textbutton "MajesticBeard"
                textbutton "Martin Johansen"
                textbutton "Master Blaster"
                textbutton "Moons"
                textbutton "Owen Craig"
                textbutton "Panpakapan!"
                textbutton "Poulopot"
                textbutton "PreorderBonus"
                textbutton "Quinn"
                textbutton "Raed Thg"
                textbutton "ray"
                textbutton "Ryan Velasquez"
                textbutton "Sierra Mercedes P..."
                textbutton "Simeon Meier"
                textbutton "slash"
                textbutton "Songin"
                textbutton "Steven michael go..."
                textbutton "ThatOneGuy"
                textbutton "Ty Weyland"
                textbutton "Vésteinn"
                textbutton "Whotitztwoya"
                textbutton "William Bull"
                textbutton "Xmagemania"
                textbutton "Yikan Ge"
                textbutton "Steven dunn"
                textbutton "Kazan"
                textbutton "Lord Hercules"
                textbutton "Paul"
                textbutton "Mark Anderson-Kahl"
                textbutton "Mbar38"
                textbutton "charles ross"
                textbutton "Arahtaz"
                textbutton "James Strahan"
                textbutton "Ditto"
                textbutton "TabuN"
                textbutton "Sigfred987"
                textbutton "Jack"
                textbutton "nightbladerz"
                textbutton "Allen Smith"
                textbutton "HWANG CHANHA"
                textbutton "Jacob Facemire"
                textbutton "Tyler Winningham"
                textbutton "Bar45"
                textbutton "Lawrence williams"
                textbutton "Borkbun"
                textbutton "Barry Wanyne Smith"
                textbutton "Christopher Gibson"
                textbutton "Ragdoll"
                textbutton "Phynix"
                textbutton "Declan"
                textbutton "Warsheef"
                textbutton "CryptoKing12"
                textbutton "marc"
                textbutton "ODYWILSON04"
                textbutton "bum93@o2.pl"
                textbutton "Vexa"
                textbutton "Normal Osborne"
                textbutton "Luke T"
                textbutton "Frederik Claumarch"
                textbutton "Aleksis Lindewall"
                textbutton "SuicidalTaco"
                textbutton "Brayden"
                textbutton "Alexander Faron"
                textbutton "glocknar"
                textbutton "Donglizard"
                textbutton "helge beras"
                textbutton "Biscuit"
                textbutton "Justin Guercia"
                textbutton "Nathaniel Wilson"
                textbutton "Jack"
                textbutton "Kewl"
                textbutton "Christian Dennis"
                textbutton "MerricWolfe"
                textbutton "Miles"
                textbutton "TImiddarkspy"
                textbutton "Scooter McCaffrey"
                textbutton "Marabow"
                textbutton "Glasol"
                textbutton "Anthony"
                textbutton "TVH"
                textbutton "Alistair Maher"
                textbutton "andrew trosper"
                textbutton "Anon"
                textbutton "Antoine Breton Lalancette"
                textbutton "blockperson"
                textbutton "boxzzz"
                textbutton "Cam Geary"
                textbutton "Chandler"
                textbutton "Chevy"
                textbutton "cottel anthony"
                textbutton "huntdog"
                textbutton "IMaster4001"
                textbutton "ITWeeb"
                textbutton "Jack"
                textbutton "JINYA NAKAMURA"
                textbutton "Joel Hubbard"
                textbutton "julian killet"
                textbutton "Kindasadbuthellarad"
                textbutton "Matthieu Bokota"
                textbutton "Mattricole"
                textbutton "NexFalx19"
                textbutton "Patrick Oliphant"
                textbutton "Red Runner"
                textbutton "Servius"
                textbutton "Seth"
                textbutton "SparkyBoomer"
                textbutton "Spencer"
                textbutton "Tenrou"
                textbutton "Thierry Bridet"
                textbutton "Wirglays"
                textbutton "yetie"
                textbutton "Kohlhaus Christopher"
                textbutton "AbstractRude"
                textbutton "Cthulhu"
                textbutton "Resz"
                textbutton "Lan222222"
                textbutton "Mad Lion"
                textbutton "Papito1999"
                textbutton "Firastos"
                textbutton "Joshua Dyer"
                textbutton "James T. Tackett"
                textbutton "Willim robert jones"
                textbutton "justin sepulveda"
                textbutton "Nerfguns Sitgarn"
                textbutton "Brandon Rose"
                textbutton "V Hays"
                textbutton "madnessoreilli"
                textbutton "gerado manuel marquez cardoso"
                textbutton "bigbagel12"
                textbutton "edeltoast"
                textbutton "Ted Leonard"
                textbutton "alexander scholl"
                textbutton "jordan tawse"
                textbutton "Ryan Murtaught"
                textbutton "holy shit just let me fucking sign in"
                textbutton "Davion nerd"
                textbutton "Marcel Köhler"
                textbutton "Harest"
                textbutton "Lukas Neander"
                textbutton "Adam Sun"
                textbutton "chaoticPopo"
                textbutton "DoomedInfidel"
                textbutton "ZeroMisanthrope241"
                textbutton "Rollo Resh"
                textbutton "Ryan Thomas"

                null height 10
                text "One Dollar Patrons"
                null height 5

                textbutton "L"
                textbutton "Steve C"
                textbutton "Tu"
                textbutton "Karan Verma"
                textbutton "Darth Revan"
                textbutton "Michael Simon"
                textbutton "KBH"
                textbutton "Goldenhand"
                textbutton "Gregarwolf"
                textbutton "Miles"
                textbutton "Aeryn Monet"
                textbutton "Stephan"
                textbutton "Michael York"
                textbutton "Jeppe Risager"
                textbutton "Peter Sarant"
                textbutton "4"
                textbutton "Venc"
                textbutton "Cteno"
                textbutton "Stephan"
                textbutton "Rink"
                textbutton "Void Walker"
                textbutton "carrotz"
                textbutton "Big Joe"
                textbutton "Gir"
                textbutton "G9mare"
                textbutton "Tebachi"
                textbutton "Easton Honaker"
                textbutton "Deekman"
                textbutton "Jeroen verboom"
                textbutton "Nope"
                textbutton "RedWizardVega"
                textbutton "Lonesommuffin"
                textbutton "Enno Kauker"
                textbutton "A Ch"
                textbutton "DemonFish"
                textbutton "Devan Raptor"
                textbutton "DrCockroach"
                textbutton "Enno Kauker"
                textbutton "Jebus Cable"
                textbutton "KBH"
                textbutton "Kevin R.J."
                textbutton "Miles"
                textbutton "SilenceDragon"
                textbutton "Aquis Hyperion"
                textbutton "helge berás"
                textbutton "Mr.Reinhardt"
                textbutton "nobody"
                textbutton "Tom Vu"
                textbutton "Will Burns"
                textbutton "Asgar15"
                textbutton "Vivek Sarkar"
                textbutton "Daniel Sanchez Flores"
                textbutton "Kenneth Chia"
                textbutton "Abc Def"
                textbutton "MitoShinigami"
                textbutton "Ice"
                textbutton "Jesse"
                textbutton "Jakkin Jakkin"
                textbutton "Tensei"
                textbutton "Artorias"
                textbutton "Razorhead"
                textbutton "Ceriond"
                textbutton "Arknea"
                textbutton "Red Infesto"
                textbutton "Benirax"
                textbutton "The Joester"
                textbutton "OGK"
                textbutton "diggab"
                textbutton "Christian Thomsen"
                textbutton "Helios"
                textbutton "nobody"
                textbutton "TV"
                textbutton "Vladislav Borodich"
                textbutton "claus sandgreen jensen"
                textbutton "Mike@patreon"
                textbutton "Drawen"
                textbutton "Hammerheadcruiser"
                textbutton "Will Burns"
                textbutton "A Ch"
                textbutton "Zengee"
                textbutton "Enno Kauker"
                textbutton "Craig Zlist"
                textbutton "Communist.Party"
                textbutton "Lauren"
                textbutton "Jeff Ellicott"
                textbutton "MonsieurLeRue"
                textbutton "Razorhead"
                textbutton "Artorias"
                textbutton "Temseo"
                textbutton "Jakkin Jakkin"
                textbutton "Ice"
                textbutton "Kenneth Chia"
                textbutton "dante dont give a shit"
                textbutton "Red infesto"
                textbutton "Kadell Jamieson"
                textbutton "OGK"
                textbutton "The Joester"
                textbutton "diggab"
                textbutton "Hammerheadcruiser"
                textbutton "claus sandgreen jensen"
                textbutton "Vladislav Borodich"
                textbutton "TV"
                textbutton "nobody"
                textbutton "The Joester"
                textbutton "Kyran Hayes"
                textbutton "Siegfred987"
                textbutton "Jesterspark"
                textbutton "Merlin1967"
                textbutton "DarkKnight"
                textbutton "Star123"
                textbutton "Hikaru"
                textbutton "Shugo"
                textbutton "Zee Poller"
                textbutton "Gabriell nicholis"
                textbutton "Jshock"
                textbutton "Dragoon48"
                textbutton "Randall"
                textbutton "Moises Gabriel Salas Aguilar Aquila"
                textbutton "altso"
                textbutton "Ucciuburdu"
                textbutton "Chad Thurman"
                textbutton "Greezzlies"
                textbutton "Vailor"
                textbutton "Anon Anonymous"
                textbutton "Richard"
                textbutton "Asterisk"
                textbutton "Elwood Blakk"
                textbutton "Anothony mulkey"
                textbutton "Pingo"
                textbutton "Blyss"
                textbutton ""
                textbutton ""
                textbutton ""



        bar adjustment adj style "vscrollbar"

        textbutton _("Finished Looking."):
            xfill True
            action [ Hide("patreon_supporters"), Return(None)]
            top_margin 10


# BARS AND BAR STUFF!

screen love_bar(love):
    text "{color=#00fa9a}Love{/color}":
        xpos 760 ypos 140
    frame:
        xalign 0.62 ypos 175
        xsize 23 ysize 500
        vbar:
            value StaticValue(love, 70)

screen cor_bar(corruption):
    text "{color=#dc143c}Corruption{/color}":
        xpos 820 ypos 140
    frame:
        xalign 0.68 ypos 175
        xsize 23 ysize 500
        vbar:
            value StaticValue(corruption, 70)

screen lilly_bar(lillylove):
    text "{color=#00008b}Lilly's Love{/color}":
        xpos 680 ypos 140
    frame:
        xalign 0.58 ypos 175
        xsize 23 ysize 500
        vbar:
            value StaticValue(lillylove, 20)


screen melony_bar(melresist):
    text "{color=#9400D3}Your Resistance{/color}":
        xpos 680 ypos 140
    frame:
        xalign 0.58 ypos 175
        xsize 23 ysize 500
        vbar:
            value StaticValue(melresist, 100)






























#textbutton "Close Inventory" action [ Hide("inventory_screen"), Show("inventory_button"), Return(None)]
