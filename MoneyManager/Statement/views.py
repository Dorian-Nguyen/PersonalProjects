from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import StatementUploadForm
from django.core.files.storage import default_storage
from .Reader import citiReader


def index(request):
    template = loader.get_template('Statement/ChooseStatement.html')
    context = None
    return HttpResponse(template.render(context, request))


def citi(request):

    if request.method == 'POST':

        form = StatementUploadForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES['citiStatement_raw']
            file_name = default_storage.save("test.csv", csv_file)
            a = citiReader()
            a.citiParse(default_storage.url(file_name))
            return render(request, 'Statement/success.html')
    else:
        form = StatementUploadForm()

    #this is the default screen
    return render(request, 'Statement/UploadScreen.html')