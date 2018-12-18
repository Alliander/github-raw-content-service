## Settings

# Flask settings
FLASK_PORT = 8080
FLASK_DEBUG = False  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# Prometheus settings
PROMETHEUS_METRIC_PORT = 9090

# Healthpoint settings
HEALTH_ENDPOINT_PORT = 5002
