import pandas as pd
import numpy as np

# Set the number of samples
num_samples = 100

# Generate dummy data
data = {
    'id': np.arange(1, num_samples + 1),
    'name': [f'Name_{i}' for i in range(1, num_samples + 1)],
    'age': np.random.randint(18, 70, size=num_samples),
    'salary': np.random.randint(30000, 100000, size=num_samples)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('dummy_data.csv', index=False)

print("Dummy data generated and saved to 'dummy_data.csv'")