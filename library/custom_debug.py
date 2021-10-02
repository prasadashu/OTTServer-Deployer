#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from datetime import datetime
import json

def custom_debug_module():
    """Function to define the Ansible Custom Module"""
    
    # Define the fields which will act as the parameters for the Custom Module
    fields = {
        "debug_msg": {"required": True, "type": 'str'}
    }

    # Instantiate the module
    module = AnsibleModule(argument_spec = fields)

    # Get the 'debug_msg' parameter value
    debug_msg = module.params['debug_msg']

    # Print the output
    try:
        # Successful exit of module
        module.exit_json(changed = True, msg = str(datetime.now().strftime('%c')) + " - " + str(debug_msg))
        
    except Exception as exception:
        # Failed exit of module
        module.fail_json(msg = "Failed to execute module: " + str(exception))

    return

# Calling the main function
if __name__ == '__main__':
    # Call the Custom Module function
    custom_debug_module()