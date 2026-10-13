from pyscript import document

def checkNum(e):
    name_list1 = ["jeremy taruq", "jake tiangco", "juan nolasco", "jane sebastian", "emmanuel dizon"]
    firstname = document.getElementById("firstname").value
    lastname = document.getElementById("lastname").value
    fullname = (f'{firstname} {lastname}')
    con_name = fullname.lower() #coverts fullname variable into lowercase in order to confirm if the user's input is listed; acts as a decoy variable so that the user's original input will still be displayed
    confirm_name = con_name in name_list1 

    message = (f'Sorry {fullname}, your name is not found on the list.', f'Congrats {fullname}! You are now part of the Math Guild.')
    document.getElementById("output1").innerHTML = message[confirm_name]