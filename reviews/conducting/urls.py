# coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('reviews.conducting.views',
    url(r'^generate_search_string/$', 'generate_search_string', name='generate_search_string'),
    url(r'^save_generic_search_string/$', 'save_generic_search_string', name='save_generic_search_string'),
    url(r'^import_bibtex/$', 'import_bibtex', name='import_bibtex'),
    url(r'^source_articles/$', 'source_articles', name='source_articles'),
    url(r'^article_details/$', 'article_details', name='article_details'),
    url(r'^save_article_details/$', 'save_article_details', name='save_article_details'),
    url(r'^save_quality_assessment/$', 'save_quality_assessment', name='save_quality_assessment'),
    url(r'^quality_assessment_detailed/$', 'quality_assessment_detailed', name='quality_assessment_detailed'),
    url(r'^quality_assessment_summary/$', 'quality_assessment_summary', name='quality_assessment_summary'),
)