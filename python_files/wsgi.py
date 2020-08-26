from app import app
import sys

flask_port = 5000

if len(sys.argv) == 2:
    print('input port from command line is: ', sys.argv[1])
    flask_port = sys.argv[1]


if __name__ == "__main__":
    app.run(port=flask_port)