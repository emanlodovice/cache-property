from django.shortcuts import render
from django.views.generic import TemplateView
from django.db import connection, reset_queries

from models import Profile, Project


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        context = {
            'total_profile': Profile.objects.count()
        }
        reset_queries()
        cached_result = []
        for p in Profile.objects.all():
            c = p.cached_project_count
            cached_result.append((p.full_name, c))
        context['total_queries_with_caching'] = len(connection.queries)
        context['cached_results'] = cached_result
        reset_queries()
        not_cached_result = []
        for p in Profile.objects.all():
            c = p.project_count
            not_cached_result.append((p.full_name, c))
        context['total_queries_without_caching'] = len(connection.queries)
        context['noncached_results'] = not_cached_result
        return context
