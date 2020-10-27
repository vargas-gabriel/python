from flask import Flask

result = "First Python GET request. Good Job"

api = Flask(__name__)

@api.route('/result', methods=['GET'])

def get_result():
  return result

if __name__ == '__main__':
    api.run()

