import pandas as pd

chunk_size = 50000 
file_path = 'training_dataset/training_dataset.csv'

chunks = []

for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    chunks.append(chunk)

data_frame = pd.concat(chunks, ignore_index=True)
print(data_frame.head())


