import json
from django.http.response import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

def state_as_json_response(state):
	return HttpResponse(json.dumps(state), content_type="application/json")

def get_posted_state(request):
	return json.loads(request.body)

# may god have mercy on all our souls
GLOBAL_OBJECT_REPOSITORY = {}

# view: get
#@require_GET
def get_state(request, objname):
	if objname not in GLOBAL_OBJECT_REPOSITORY:
		raise Http404("No shared-state object named '%s'" % objname)
	return state_as_json_response(GLOBAL_OBJECT_REPOSITORY[objname])

# view: set
#@require_POST
@csrf_exempt # we're lazy
def set_state(request, objname):
	print "lalala"
	input_state = get_posted_state(request)
	GLOBAL_OBJECT_REPOSITORY[objname] = input_state
	return state_as_json_response(GLOBAL_OBJECT_REPOSITORY[objname])

# view: update
#@require_POST
@csrf_exempt # we're lazy
def update_state(request, objname):
	if objname not in GLOBAL_OBJECT_REPOSITORY:
		raise Http404("No shared-state object named '%s'" % objname)
	input_state = get_posted_state(request)
	GLOBAL_OBJECT_REPOSITORY[objname].update(input_state)
	return state_as_json_response(GLOBAL_OBJECT_REPOSITORY[objname])
