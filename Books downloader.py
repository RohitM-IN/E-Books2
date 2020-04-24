import wget

print('Beginning file download with wget module')

url = 'http://link.springer.com/content/pdf/10.1007%2F978-3-319-44127-6.pdf'
wget.download(url, 'Food Analysis Laboratory Manual.pdf')
