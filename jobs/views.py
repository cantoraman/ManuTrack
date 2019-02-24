from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Job, Manufacturer, Designer


def index(request):
    active_jobs = Job.objects.filter(is_completed=False)
    context = {
        'active_jobs_list': active_jobs,
    }
    return render(request, 'jobs/index.html', context)


def job_detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
    except Job.DoesNotExist:
        raise Http404('The job you are looking for does not exist')
    return render(request, 'jobs/job_detail.html', {'job': job,
                                                    })


def designers_list(request):
    designers = Designer.objects.all()
    context = {
        'designers': designers,
    }
    return render(request, 'jobs/designers.html', context)


def designer_detail(request, designer_id):
    designer = get_object_or_404(Designer, pk=designer_id)
    return render(request, 'jobs/designer_details.html', {'designer': designer,
                                                          })


def job_edit(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/job_edit.html', {'job': job,
                                                  })


def job_update(request, job_id):
    pass

# def manufacturers_list(request):
#    return HttpResponse('List of Manufacturers')


# def manufacturer_detail(request, manufacturer_id):
#   return HttpResponse('placeholder')
