from data import Data

def print_IP(data_obj: Data):
    """
    Main function to run the script's functionality.

    :param data_obj: An instance of the Data class.
    """
    data_obj.check_requirement()

    # Get the entire dictionary
    name_ip_dict = data_obj.get_all()
    print("Name-IP Dictionary:", name_ip_dict)
