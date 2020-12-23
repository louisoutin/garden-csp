import connexion

app = connexion.App(__name__, specification_dir="swagger/")
app.run(port=8080)


if __name__ == "__main__":
    app.run(debug=True)
