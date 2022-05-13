#from transformers import ...

class ModelTextSequenceClassifier:
	def __init__(self, model_path='bert-base-uncased', tokenizer_path='bert-base-uncased', device='cpu'):
		self.model_path = model_path
		pass #todo: deal with this later
		#should this be in a seperate file?