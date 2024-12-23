# OPC-UA

## unilogics setup

 * connect the PLC to the network with DHCP enabled, then for UPC you have to disable dhcp again, just take the same IP. Verify the connection with the router
 * make a project with OPC-UA enabled, and share the desired variables form the list of global variables

## Encryption options with certificates

open the folder in explorer, then type in cmd in the navbar to open the cmd console from this folder

openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
openssl req -new -key private_key.pem -out cert.csr -subj "/C=DE/ST=BW/L=Stuttgart/O=ChemTherm/OU=CW/CN=chem-therm.de"
openssl x509 -req -days 7300 -in cert.csr -signkey private_key.pem -out cert.pem -sha256
openssl pkcs8 -topk8 -inform PEM -outform DER -in private_key.pem -nocrypt -out private_key.der
openssl x509 -outform DER -in cert.pem -out cert.der



on the python side enter folowring lines
certificate_path = cwd.joinpath("cert.der")
private_key_path = cwd.joinpath("private_key.dem")

on the uaexpert side use the certificate
