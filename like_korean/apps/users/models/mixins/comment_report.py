# Django
from django.db import models

# Models
from template.apps.reports.models import CommentReport


# Class Section
class CommentReportModelMixin(models.Model):
    class Meta:
        abstract = True

    def report_comment(self, comment, profile, **data):
        comment_report = CommentReport.objects.create(comment=comment, profile=profile, **data)
        return comment_report
