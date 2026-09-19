from pyscript import display, document


def create_order(e):
    document.getElementById("show").innerHTML = ""
    subtotal = 0

    if document.getElementById("item1").checked:
        subtotal += 120 #+120 on the subtotal value

    if document.getElementById("item2").checked:
        subtotal += 150 #+150 on the subtotal value

    if document.getElementById("item3").checked:
        subtotal += 180 #+180 on the subtotal value

    if document.getElementById("item4").checked:
        subtotal += 168 #+168 on the subtotal value

    if document.getElementById("item5").checked:
        subtotal += 130 #+130 on the subtotal value

    vat = subtotal * 0.12 #12% of subtotal
    total = subtotal + vat

    display(f"Subtotal: ₱{subtotal:.2f}", target="show")
    display(f"VAT: ₱{vat:.2f}", target="show")
    display(f"Total Amount: ₱{total:.2f}", target="show")


    #.checked --> value included in computaiton IF user ticked it (https://www.w3schools.com/jsref/prop_checkbox_checked.asp)

    #.2f = 2 decimal places (https://www.w3schools.com/python/trypython.asp?filename=demo_fstring_modifier_novar)

def generate_sku(e): 
    category = document["categories"].value
    product_name = document["prod_name"].value
    stock = document["stock"].value

    category = category[:3].upper()
    product_name = product_name[:3].upper()

    sku = category_code + "-" + product_code + "-" + stock document["sku"].innerText = sku