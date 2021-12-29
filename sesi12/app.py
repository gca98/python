# def test_sum():
#     assert sum([1, 2, 3]) == 6, "Should be 6"
 
# def test_sum_tuple():
    
#     assert sum((1, 2, 3)) == 6, "Should be 6"


from flask import Flask
from handler.routes import configure_routes

app = Flask(__name__)

configure_routes(app)

if __name__ == '__main__':
    app.run()