from flask_frozen import Freezer
from kp_generator.app import app

freezer = Freezer(app)

@freezer.register_generator
def index():
    yield {}

if __name__ == '__main__':
    freezer.freeze() 