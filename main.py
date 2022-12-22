import wascrapper

print ("""
_  _  _ _______ _______ _______  ______ _______  _____   _____  _______  ______
 |  |  | |_____| |______ |       |_____/ |_____| |_____] |_____] |______ |_____/
 |__|__| |     | ______| |_____  |    \_ |     | |       |       |______ |    \_
                                                                                
""")


print  (
    """
    Select one of the options below:
     [ 01 ] Extract links from WhatsApp domain.
     [ 02 ] Extract links from Facebook.
     [ 03 ] Extract links from site especific.
     [ 03 ] Check valid links.
     [ 04 ] Exit.
    """
)

option = input("Enter the selected option number:")
option = int(option)

if option == 1:
    print("Extract links from WhatsApp.")
    wascrapper.scrapperWa()

elif option == 2:
    print("Extract links from Google.")
    wascrapper.scrapperGo()

elif option == 3:
    print("Extract links from site especific.")
    wascrapper.scrapperOpt()

elif option == 4:
    print("Check valid links.")
    wascrapper.scrapperVal()

else:
    print("Exit")
