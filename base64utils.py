#Base64 Utils
#By rixa8

import base64

while True:
	mode = input("Mode.\n1.Encode\n2.Decode\n0.Exit\n")
	if mode == "1":
		e = input("To encode:")
		encoded_bytes = base64.b64encode(e.encode("utf-8"))
		encoded_string = encoded_bytes.decode("utf-8")
		print(encoded_string)
	elif mode == "2":
		d = input("To decode:")
		decoded_bytes = base64.b64decode(d.encode("utf-8"))
		decoded_string = decoded_bytes.decode("utf-8")
		print(decoded_string)
	elif mode == "0":
		print("Thanks for using!\nMade by:https://github.com/rixa8")
		quit
		break
	