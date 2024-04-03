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

    # Convert memory sizes from bytes to human-readable format (MB)
    total_memory_mb = total_memory / (1024 * 1024)
    available_memory_mb = available_memory / (1024 * 1024)
    used_memory_mb = used_memory / (1024 * 1024)

    # Convert memory in percentages %
    available_memory_percent = ((total_memory_mb-used_memory_mb)/total_memory_mb)*100
    
    # Print RAM utilization information
    print("Total Memory: {:.2f} MB".format(total_memory_mb))
    print("Available Memory: {:.2f} MB".format(available_memory_mb))
    print("Used Memory: {:.2f} MB".format(used_memory_mb))
    print("Used Memory Percentage: {:.2f}%".format(used_memory_percentage))
    print("Available Memory Percentage: {:.2f}%".format(available_memory_percent))

if __name__ == "__main__":
    # Call the function to get RAM utilization information
    get_ram_usage()

