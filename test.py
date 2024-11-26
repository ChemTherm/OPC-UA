from opcua import Client

# Connect to the OPC-UA server
# client = Client("opc.tcp://127.0.0.1:48020")
client = Client("opc.tcp://192.168.2.37:48020")
# client.set_password("ChemTherm2024!")
try:
    client.connect()
except Exception as err:
    exit(err)

node_id = "ns=4;s=Root.TestFolder.TestBool"

try:
    # Get the root node
    node = client.get_node(node_id)
    value = node.get_value()
    print(f"Value of '{node_id}': {value}")

    # Write a value to the node
    new_value = True  # Boolean value
    node.set_value(new_value)  # For simple types, directly pass the value

    # Alternatively, use the DataValue class for more control
    # data_value = ua.DataValue(ua.Variant(new_value, ua.VariantType.Boolean))
    # node.set_value(data_value)
    exit()
    root = client.get_root_node()
    print(f"Root node is: {root}")

    # Read a variable value (e.g., "Temperature")
    temp_node = client.get_node("ns=2;s=MyDevice.Temperature")
    temperature = temp_node.get_value()
    print(f"Temperature: {temperature}")

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


def browse_node(node, depth=0):
    indent = "  " * depth
    try:
        print(f"{indent}- Node: {node}, Display Name: {node.get_display_name().Text}")
        for child in node.get_children():
            browse_node(child, depth + 1)
    except Exception as e:
        print(f"{indent}Error browsing node: {e}")

# Connect and browse from the root
try:
    client.connect()
    root = client.get_root_node()
    print("Browsing entire namespace:")
    browse_node(root)
finally:
    client.disconnect()

from opcua import ua

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


