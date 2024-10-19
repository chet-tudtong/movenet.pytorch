import numpy as np

# Load the .npy file
npy_file_path = 'lib/data/center_weight_origin.npy'
data = np.load(npy_file_path)

# Write the data to a .bin file
bin_file_path = 'lib/data/center_weight.bin'
data.tofile(bin_file_path)

print(f"Data from {npy_file_path} has been written to {bin_file_path}")