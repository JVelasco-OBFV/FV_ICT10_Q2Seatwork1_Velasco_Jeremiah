from pyscript import document

def checkNum(e):
    name_list1 = ["jeremy taruq", "jake tiangco", "juan nolasco", "jane sebastian", "emmanuel dizon"] #dummy names
    firstname = document.getElementById("firstname").value 
    lastname = document.getElementById("lastname").value
    fullname = (f'{firstname} {lastname}') #combines both firstname and lastname together
    con_name = fullname.lower() #coverts fullname variable into lowercase in order to confirm if the user's input is listed; acts as a decoy variable so that the user's original input will still be displayed
    confirm_name = con_name in name_list1 #confirms if name is in list

    message = (f'Sorry {fullname}, your name is not found on the list.', f'Congrats {fullname}! You are now part of the Math Guild.') #displays result if person either listed within selected individuals or not
    document.getElementById("output1").innerHTML = message[confirm_name]
