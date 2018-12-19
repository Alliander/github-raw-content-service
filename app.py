from flask import Flask
from github import Github
import base64
import os
import settings
from flask import request
from logzero import logger
from prometheus_client import start_http_server


app = Flask(__name__)

@app.route('/<repo>')
def index(repo):

    org_param = request.args.get("org")
    if org_param is None:
       print ("Argument org not provided")

    filepathparam = request.args.get("filepath")
    if filepathparam is None:
        print ("Argument filepath not provided")

    filepathparam  = request.args.get('filepath', None)
    org_param  = request.args.get('org', None)

    print (org_param)

    # First create a Github instance:
    g = Github(os.environ['TOKEN'])
    org = g.get_organization(org_param)
    repo = org.get_repo(repo)

    file_contents= repo.get_file_contents(filepathparam)

    decoded_content = base64.decodestring(file_contents.content.encode())

    return decoded_content, 200, {'Content-Type': 'text/plain; charset=utf-8'}


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    logger.info("Start metrics endpoint on port %s",
                int(os.getenv('PROMETHEUS_METRIC_PORT',
                              settings.PROMETHEUS_METRIC_PORT)))
    start_http_server(int(os.getenv('PROMETHEUS_METRIC_PORT',
                                    settings.PROMETHEUS_METRIC_PORT)))

    app.run(debug=settings.FLASK_DEBUG,
            host='0.0.0.0', port=os.getenv('FLASK_PORT', settings.FLASK_PORT))
