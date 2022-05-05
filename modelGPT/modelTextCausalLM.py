from lib2to3.pgen2.tokenize import generate_tokens, tokenize
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import numpy as np

import json
import random

# logging
import sys
import logging

class ModelTextCausalLM:
	def __init__(self, model_path='gpt2', tokenizer_path='gpt2', device='cpu'):
		self.model_path = model_path
		self.tokenizer_path = tokenizer_path
		self.device = device

		logging.info('Loading model...')
		self.model = AutoModelForCausalLM.from_pretrained(model_path,
			##torch_dtype=torch.float16, # use float16 if on GPU
			low_cpu_mem_usage=True)
		logging.info('Loading tokenizer...')
		self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)

	#todo: add logging
	#todo: pull from database
	
	def tokenize(self, text):
		tokens = self.tokenizer(text, return_tensors="pt").input_ids
		return tokens

	def generate(self, tokens, no_decode=False):
		generate_tokens = self.model.generate(
			input_ids=tokens,
			max_length=200,
			temperature=1.0,
			do_sample=True
		)

		if no_decode:
			return generate_tokens
		else:
			return self.tokenizer.batch_decode(generate_tokens, skip_special_tokens=False)