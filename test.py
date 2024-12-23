from opcua import Client
from opcua import ua


''' 
# Encryption related and not used for now 

import os
from pathlib import Path

cwd = Path(os.getcwd())
certificate_path = cwd.joinpath("cert.der")
private_key_path = cwd.joinpath("private_key.pem")
print(f"{certificate_path.exists()}  {certificate_path.exists()}")

# when not using exncryption leave this out: client.set_security_string("None")
# client.set_security_string(f"Basic256Sha256,SignAndEncrypt,{certificate_path},{private_key_path}")
# not needed either iirc
# client.set_password("Password")
'''

client = Client("opc.tcp://192.168.2.37:48020")


node_id = "ns=4;s=Root.TestFolder.TestBool"
plc_root_node = "ns=4;s=Root"


def get_node(node_name):
    return client.get_node(node_name)


def set_node(node, value, data_type):
    data_value = ua.DataValue(ua.Variant(value, data_type))
    node.set_value(data_value)


def main():
    try:
        client.connect()
        node = get_node(plc_root_node)
        bool_node = get_node(node_id)
        print(bool_node.get_value())
        set_node(bool_node, False, ua.VariantType.Boolean)
        print(get_node(node_id).get_value())
        browse_node(node)
    finally:
        client.disconnect()


def browse_node(node, depth=0):
    indent = "  " * depth
    try:
        print(f"{indent}- Node: {node}, Display Name: {node.get_display_name().Text}")
        for child in node.get_children():
            browse_node(child, depth + 1)
    except Exception as e:
        print(f"{indent}Error browsing node: {e}")


main()
exit()

"""



try:
    # Get the root node
    node = client.get_node(node_id)
    value = node.get_value()
    print(f"Value of '{node_id}': {value}")

    # Write a value to the node

    root = client.get_root_node()
    print(f"Root node is: {root}")


finally:
    client.disconnect()

try:
    # Connect to the server
    client.connect()
    print("Connected to OPC-UA server")

    # Get the root node
    root = client.get_root_node()
    print(f"Root node: {root}")

    # Browse the root node
    print("Browsing server namespace:")
    objects = root.get_children()
    for obj in objects:
        print(f"Object: {obj}, Display Name: {obj.get_display_name().Text}")
finally:
    client.disconnect()

# Connect and browse from the root
try:
    client.connect()
    root = client.get_root_node()
    print("Browsing entire namespace:")
    browse_node(root)
finally:
    client.disconnect()

def browse_variables(node, depth=0):
    indent = "  " * depth
    try:
        for child in node.get_children():
            node_class = child.get_node_class()
            if node_class == ua.NodeClass.Variable:
                print(f"{indent}- Variable: {child}, Value: {child.get_value()}")
            else:
                browse_variables(child, depth + 1)
    except Exception as e:
        print(f"{indent}Error accessing variable: {e}")

# Connect and list variables
try:
    client.connect()
    objects_node = client.get_objects_node()
    print("Listing variables:")
    browse_variables(objects_node)
finally:
    client.disconnect()

exit()



"""