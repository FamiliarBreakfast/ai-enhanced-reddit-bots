from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import numpy as np

import json
import random

# logging
import sys
import logging

class ModelTextCasualLM:
	def __init__(self, model_path, tokenizer_path):
		logging.info('Loading model...')
		model = AutoModelForCausalLM.from_pretrained('gpt2', # replace with your model (path or huggingface model)
			##torch_dtype=torch.float16, # use float16 if on GPU
			low_cpu_mem_usage=True)
		logging.info('Loading tokenizer...')
		tokenizer = AutoTokenizer.from_pretrained('gpt2') # replace with your tokenizer (path or huggingface model)

	#todo: add logging
	#todo: pull from database

	def parse(self, text):
		tokens = self.tokenizer.encode(text)
		return tokens

	def generate(self, tokens):
		generate_tokens = self.model.generate(
			input_ids=tokens,
			max_length=200,
			temperature=1.0,
			do_sample=True,
		)

		return self.tokenizer.decode(generate_tokens, skip_special_tokens=False)
	
	def generate_tokens(self, tokens):
		generate_tokens = self.model.generate(
			input_ids=tokens,
			max_length=200,
			temperature=1.0,
			do_sample=True,
		)

		return generate_tokens