from pyscript import document

def checkNum(e):
    name_list1 = ["Jeremy", "Jake", "Juan", "Jane", "John"].lower()
    name_list2 = ['Salazar','Nolasco','Dela Cruz','Rosario','Makabunga'].lower()
    firstname = document.getElementById("firstname").value
    lastname = document.getElementById("lastname").value
    message = (f'Sorry {firstname} {lastname}, your name is not found.', f'Yey! Salutations {firstname} {lastname}.')
    confirm_num = firstname in name_list1
    confirm_num2 = lastname in name_list2

    document.getElementById("output1").innerHTML = message[confirm_num & confirm_num2]