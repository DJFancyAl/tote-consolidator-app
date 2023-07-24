from markersys import create_app
app = create_app()

if __name__ == "__main__":
    # Run the app on all network interfaces
    app.run(host='192.168.1.174')