import tld

def check(domain):

	res = domain.split('.')
	dom = tld.get_tld(domain, as_object = True)

	if res[-1] == dom.tld:
		return True
	else:
		return False
