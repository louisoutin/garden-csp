import logging

import connexion

app = connexion.App(__name__, specification_dir="./swagger")
app.add_api('api.yaml')
app.run(port=8080)

logging.basicConfig(level=logging.INFO)
application = app.app

if __name__ == "__main__":
    app.run(debug=True)
