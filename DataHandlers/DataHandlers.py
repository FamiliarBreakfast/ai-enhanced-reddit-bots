

def validate(text):
		
		return text
	
def extract_response(text, prompt=None, eos_token='<|endoftext|>'):
	if prompt is None:
		return #todo: auto detect prompt
	else:
		response = text[len(prompt):text.rfind(eos_token)-1]
	return response