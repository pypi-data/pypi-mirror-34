Description
-----------

This module provide only one function: it check if domain is listed on http://blocklist.rkn.gov.ru
rkn can be obtained directly from PyPI, and can be installed with pip:

    pip install rkn

You need anti-captcha.com API key for using this module.

Example usage:

    >>> from rkn import check_rkn
    >>> result, found_in_reestr = check_rkn.query("domain.name", "YOUR_API_KEY_HERE")
    >>> if found_in_reestr:
	>>>     print (result)

