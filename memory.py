import psutil

def get_ram_usage():
    """
    Function to get RAM (memory) utilization information.
    """
    # Get memory usage statistics
    memory = psutil.virtual_memory()

    # Total physical memory (RAM) in bytes
    total_memory = memory.total
    # Available memory in bytes
    available_memory = memory.available
    # Used memory in bytes
    used_memory = memory.used
    # Percentage of used memory
    used_memory_percentage = memory.percent

    # Convert memory sizes from bytes to human-readable format (GB)
    GB_conveter = 1024 ** 3 # bytes to kb, kb to mb, mb to GB
    total_memory_gb = total_memory / GB_conveter
    available_memory_gb = available_memory / GB_conveter
    used_memory_gb = used_memory / GB_conveter

    # Convert memory in percentages %
    available_memory_percent = ((total_memory_gb-used_memory_gb)/total_memory_gb)*100
    
    # Print RAM utilization information
    print("Total Memory: {:.2f} GB".format(total_memory_gb))
    print("Available Memory: {:.2f} GB".format(available_memory_gb))
    print("Used Memory: {:.2f} GB".format(used_memory_gb))
    print("Used Memory Percentage: {:.2f}%".format(used_memory_percentage))
    print("Available Memory Percentage: {:.2f}%".format(available_memory_percent))

if __name__ == "__main__":
    # Call the function to get RAM utilization information
    get_ram_usage()
