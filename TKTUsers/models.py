from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

##########################################################

class Category(models.Model):
    Category_title = models.CharField(max_length=500)
    Category_created_date = models.DateField(auto_now_add=True, blank=True)
    Category_update_date = models.DateField(auto_now=True, blank=True)

    class Meta:
        verbose_name_plural = 'Category Title'

    def __str__(self):
        return self.Category_title


##########################################################

class technology_stack(models.Model):
    technology_name = models.CharField(max_length=500)
    technology_stack_created_date = models.DateField(auto_now_add=True, blank=True)
    technology_stack_update_date = models.DateField(auto_now=True, blank=True)

    class Meta:
        verbose_name_plural = 'Technology Name'

    def __str__(self):
        return self.technology_name


##########################################################

class Issue_Category(models.Model):
    Issue_Category_name = models.CharField(max_length=500)
    Issue_Category_created_date = models.DateField(auto_now_add=True, blank=True)
    Issue_Category_update_date = models.DateField(auto_now=True, blank=True)

    class Meta:
        verbose_name_plural = 'Issue Category Name'

    def __str__(self):
        return self.Issue_Category_name


##########################################################


class TicketDetail(models.Model):
    websitename = models.TextField()
    websiteurl = models.TextField()
    website_technology = models.ManyToManyField(
        technology_stack, related_name="website_technology")
    website_description = models.TextField()
    website_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Issue_Related_To = models.ForeignKey(Issue_Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Ticket For ' + 'websiteurl'

    def __str__(self):
        return self.websiteurl


##########################################################

class Ticket_status_choice(models.Model):
    status_name = models.CharField(max_length=100)
    Ticket_status_created_date = models.DateField(auto_now_add=True, blank=True)
    Ticket_status_update_date = models.DateField(auto_now=True, blank=True)

    class Meta:
        verbose_name_plural = 'Ticket Status Choice'

    def __str__(self):
        return self.status_name


##########################################################

class Agent_Role(models.Model):
    Agent_Role_name = models.CharField(max_length=500)
    Agent_Role_created_date = models.DateField(auto_now_add=True, blank=True)
    Agent_Role_update_date = models.DateField(auto_now=True, blank=True)

    class Meta:
        verbose_name_plural = 'Agent_Role_name'

    def __str__(self):
        return self.Agent_Role_name


##########################################################

class Agent(models.Model):
    Agent_name = models.TextField()
    Agent_role = models.ForeignKey(Agent_Role, on_delete=models.CASCADE)
    Agent_created_date = models.DateField(auto_now_add=True, blank=True, null=True)
    Agent_status_choice = (
        ('Active', 'ACTIVE'), ('Deactivated', 'DEACTIVATED'))
    Agent_status = models.CharField(
        choices=Agent_status_choice, max_length=20, )
    Agent_expert = models.ForeignKey(
        technology_stack, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Agent_name'

    def __str__(self):
        return self.Agent_name


##########################################################


class Ticket_status(models.Model):
    ticket_token_id = models.ForeignKey(TicketDetail, on_delete=models.CASCADE)
    ticket_remark = models.TextField()
    ticket_raised_by = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket_assigned_to = models.ForeignKey(Agent, on_delete=models.CASCADE)
    ticket_raised_date = models.DateField(
        auto_now_add=True, blank=True, null=True)
    ticket_last_updated_date = models.DateField(
        auto_now=True, blank=True, null=True)
    ticket_status = models.ForeignKey(
        Ticket_status_choice, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'ticket_token_id' + 'ticket_raised_by'

    def __str__(self):
        return self.ticket_token_id + self.ticket_raised_by

##########################################################


