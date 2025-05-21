from morss.morss import init_app

app = init_app()
print("Starting Morss.it server...")
app.run(debug=True, host='0.0.0.0', port=5000)
