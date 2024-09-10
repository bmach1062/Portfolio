def allowed_ips():
    import_file = "allow_list.txt"
    remove_list = ['192.168.6.9', '192.168.52.90', '192.168.158.170', '192.168.203.198',
                    '192.168.201.40', '192.168.218.219', '192.168.52.37', '192.168.156.224']
    
    # Opening the allow_list file and reading it in to parse through IP addresses
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    """
    I need the read contents to be in the form of a list to find the ip 
    addresses that I need to remove 
    """
    ip_addresses = ip_addresses.split()
    

    """
    Now I am iterating through the remove_list and if the ip address that 
    I am currently on is in the allowed_list, then I need to remove it
    using .remove(). .remove() can be used because all ip addresses are unique
    """
    for ip in remove_list:
        if ip in ip_addresses:
            ip_addresses.remove(ip)

    """
    .join() converts the allowed_list back into a string. The \n separates 
    them into each line
    """
    ip_addresses = "\n".join(ip_addresses)

    #writing over the original allow_list and replacing it with the updated list 
    with open(import_file, "w") as file:
        file.write(ip_addresses)

allowed_ips()
