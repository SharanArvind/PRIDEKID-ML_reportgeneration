import pickle
from pride_model import PRIDEModel

# Instantiate the model
pride_model = PRIDEModel()

# Save the model to a pickle file
with open('pride_model.pkl', 'wb') as f:
    pickle.dump(pride_model, f)

print("Model saved as 'pride_model.pkl'")
