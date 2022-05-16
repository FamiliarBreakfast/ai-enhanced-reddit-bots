from transformers import AutoTokenizer, AutoModelForCausalLM
from DataHandlers.Memory import Memory
import torch

# logging
import sys
import logging

class ModelTextCausalLM:
	def __init__(self, model_path='gpt2', tokenizer_path='gpt2', device='cpu'):
		self.model_path = model_path
		self.tokenizer_path = tokenizer_path
		self.device = device

		logging.debug(f'Using device {device}')
		logging.debug(f'Loading model {model_path}')
		if device != 'cpu':
			self.model = AutoModelForCausalLM.from_pretrained(model_path,
				torch_dtype=torch.float16, # use float16 if on GPU
				low_cpu_mem_usage=True)
		else:
			self.model = AutoModelForCausalLM.from_pretrained(model_path, low_cpu_mem_usage=True)
		logging.debug(f'Loading tokenizer {tokenizer_path}')
		self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
		logging.info(f'Model and tokenizer loaded after ms')#todo: measure time
		logging.info(f'Memory usage: {Memory.get_memory_usage(2)}')

	def generate(self, input, tokenize=True): #todo: add batch processing
		if tokenize:
			logging.debug(f'Tokenizing with input {input}')
			tokens = self.tokenizer(input, return_tensors="pt").input_ids
		else:
			logging.debug(f'No tokenization')
			tokens = input

		logging.info(f'Generating for input {input}')
		logging.debug(f'Generating with tokens {tokens}')
		generate_tokens = self.model.generate(tokens, max_length=200, temperature=1.0, do_sample=True)#todo: custom config

		if not tokenize:
			return generate_tokens
		return self.tokenizer.batch_decode(generate_tokens, skip_special_tokens=False)[0]

class ModelTextSeq2Seq:
	pass

class ModelTextSequenceClassifier:
	def __init__(self, model_path='bert-base-uncased', tokenizer_path='bert-base-uncased', device='cpu'):
		self.model_path = model_path
		pass #todo: deal with this later