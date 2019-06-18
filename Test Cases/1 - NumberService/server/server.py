from flask import Flask, request, Response
from random import randint

app = Flask(__name__.split('.')[0])	#See flask's docummentation about the Flask object at http://flask.pocoo.org/docs/1.0/api/ for an explanation of this

@app.route('/random', methods=['GET'])
def random():
	lower_bound = request.args.get('l')
	upper_bound = request.args.get('u')

	if lower_bound is None or upper_bound is None:
		return Response(response='"Missing lower or upper bound in request."', status=400, mimetype='application/json')

	try:
		lower_bound = int(lower_bound)
		upper_bound = int(upper_bound)
	except ValueError:
		return Response(response='"Lower and upper bound must be integers."', status=400, mimetype='application/json')

	val = randint(lower_bound, upper_bound)
	return Response(response=str(val), status=200, mimetype='application/json')
