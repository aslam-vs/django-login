from django.shortcuts import render_to_response
from django.template import RequestContext



from django.contrib.auth.models import User

from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from cgi import escape
import cStringIO as StringIO
import ho.pisa as pisa
# For Convert PDF

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


		# return render_to_pdf(
  #           'super_admin/address_list.html',
  #           {
  #               'pagesize':'A4',
  #               'sub_stock':sub_stock,
  #               'subscribers': assigned_sub,
  #           }
  #       )



def home(request):

	variables = RequestContext(request, {})
	return render_to_response('index.html', variables)
		

def signup(request):
	if request.POST:
		name = request.POST.get('first_name')
		print name

	variables = RequestContext(request, {})
	return render_to_response('signup.html', variables)