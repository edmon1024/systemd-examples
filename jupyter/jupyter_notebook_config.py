## The full path to an SSL/TLS certificate file.
#c.NotebookApp.certfile = ''
c.NotebookApp.certfile = 'jupyter.pem'

## The IP address the notebook server will listen on.
#c.NotebookApp.ip = 'localhost'
c.NotebookApp.ip = '0.0.0.0'

## The full path to a private key file for usage with SSL/TLS.
#c.NotebookApp.keyfile = ''
c.NotebookApp.keyfile = 'jupyter.key'

## Whether to open in a browser after starting. The specific browser used is
#  platform dependent and determined by the python standard library `webbrowser`
#  module, unless it is overridden using the --browser (NotebookApp.browser)
#  configuration option.
#c.NotebookApp.open_browser = True
c.NotebookApp.open_browser = False

## Hashed password to use for web authentication.
#  
#  To generate, type in a python/IPython shell:
#  
#    from notebook.auth import passwd; passwd()
#  
#  The string should be of the form type:salt:hashed-password.
c.NotebookApp.password = u'sha1:password.11010102020'

## The port the notebook server will listen on.
c.NotebookApp.port = 8888
