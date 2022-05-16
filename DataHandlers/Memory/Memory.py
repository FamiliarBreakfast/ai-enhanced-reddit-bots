import psutil
import json

def get_memory_usage(index):
	# index: 0 = total, 1 = available, 2 = percent, 3 = used, 4 = free
	if index != None:
		return psutil.virtual_memory()[index]
	return psutil.virtual_memory()

def can_handle(model, device='cpu'):
	memory = get_memory_usage(1)
	if device != 'cpu':
		pass

