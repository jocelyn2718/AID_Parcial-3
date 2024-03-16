import pywhatkit

try:
# 18,13 es la hora se debe modificar a la hora que se quiera enviar 
# pywhatkit.sendwhatmsg("+4446390477", "Holi desde python", 18, 23)
#   pywhatkit.sendwhatmsg_instantly("+4445149668", "Hola bola")

# Envia un mensaje de whatsapp a un grupo instantaneamente
#    pywhatkit.sendwhatmsg_to_group_instantly("HMSd7sLfFPy4ivP0YtAqvE", "Hey All!")

# Envia una imagen a un grupo con un mensaje 
    pywhatkit.sendwhats_image("HMSd7sLfFPy4ivP0YtAqvE", "C:/Users/jocel/Desktop/descarga.jpeg")

# Send an Image to a Contact with the no Caption
#    pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")  

    print ("Mensaje enviado")
except:
    print("Error")


    