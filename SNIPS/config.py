import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
total_epoch = 50
max_len = 50
batch = 16
learning_rate = 0.001
DROPOUT = 0.2 # 0.2, 0.3, 0.4


embedding_size = 300
lstm_hidden_size = 200


train_file = 'data/snips/train_dev'
test_file = 'data/snips/test'

vocab_intent_file = 'data/snips/vocab.intent'
vocab_slot_file = 'data/snips/vocab.slot'
