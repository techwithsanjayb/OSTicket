from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.
def home(request):
    pass


def admin_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            UserLoginForm_obj = UserLoginForm(
                request=request, data=request.POST)
            if UserLoginForm_obj.is_valid():
                uname = UserLoginForm_obj.cleaned_data['username']
                passwd = UserLoginForm_obj.cleaned_data['password']
                user = authenticate(username=uname, password=passwd)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login Successfully")
                    return redirect('TKTAdmin:admin_dashboard')
                else:
                    messages.error(request, "User does not exist")
                    return redirect('TKTAdmin:admin_login')
            else:
                messages.error(
                    request, "Invalid Details . Please login with correct details")
                return redirect('TKTAdmin:admin_login')
        else:
            UserLoginForm_obj = UserLoginForm()
            return render(request, 'TKTAdmin/admin_login.html', {'UserLoginForm_obj': UserLoginForm_obj})
    else:
        return redirect('TKTAdmin:admin_login')


def admin_dashboard(request):
    return render(request, 'TKTAdmin/admin_dashboard.html')


def admin_logout(request):
    logout(request)
    return redirect('TKTAdmin:admin_login')


######################################################

def view_agent_role(request):
    Agent_Role_obj = Agent_Role.objects.all()
    return render(request, 'TKTAdmin/admin_view_agent_role.html', {'Agent_Role_obj': Agent_Role_obj})


def create_agent_role(request):
    if request.method == 'POST':
        AgentRoleForm_obj = AgentRoleForm(request.POST)
        if AgentRoleForm_obj.is_valid():
            AgentRoleForm_obj.save()
            messages.success(request, "Role Created Successfully")
            return redirect('TKTAdmin:view_agent_role')
        else:
            messages.error(request, "Invalid Data Entered")
            return render(request, 'TKTAdmin/admin_create_agent_role.html', {'AgentRoleForm_obj': AgentRoleForm_obj})

    else:
        AgentRoleForm_obj = AgentRoleForm()
        return render(request, 'TKTAdmin/admin_create_agent_role.html', {'AgentRoleForm_obj': AgentRoleForm_obj})


def edit_agent_role(request, id):
    if request.method == 'POST':
        print("POST CALLING")
        Agent_Role_obj = Agent_Role.objects.get(pk=id)
        AgentRoleForm_obj = AgentRoleForm(request.POST, instance=Agent_Role_obj)
        if AgentRoleForm_obj.is_valid():
            AgentRoleForm_obj.save()
            messages.success(request, "Role Edited Successfully")
            return redirect('TKTAdmin:view_agent_role')
        else:
            messages.error(request, "Invalid Data Entered")
            return render(request, 'TKTAdmin/admin_edit_agent_role.html', {'AgentRoleForm_obj': AgentRoleForm_obj})

    else:
        print("GET CALLING")
        Agent_Role_obj = Agent_Role.objects.get(pk=id)
        print(Agent_Role_obj)
        AgentRoleForm_obj = AgentRoleForm(instance=Agent_Role_obj)
        return render(request, 'TKTAdmin/admin_edit_agent_role.html', {'AgentRoleForm_obj': AgentRoleForm_obj})


#####################################################################

def view_category(request):
    Category_obj = Category.objects.all()
    return render(request, 'TKTAdmin/admin_view_category.html', {'Category_obj': Category_obj})


def create_category(request):
    if request.method == 'POST':
        CategoryForm_obj = CategoryForm(request.POST)
        if CategoryForm_obj.is_valid():
            CategoryForm_obj.save()
            messages.success(request, "Category Created Successfully")
            return redirect('TKTAdmin:view_category')
        else:
            messages.error(request, "Invalid Data Entered")
            return render(request, 'TKTAdmin/admin_create_category.html', {'CategoryForm_obj': CategoryForm_obj})

    else:
        CategoryForm_obj = CategoryForm()
        return render(request, 'TKTAdmin/admin_create_category.html', {'CategoryForm_obj': CategoryForm_obj})


def edit_category(request, id):
    if request.method == 'POST':
        print("POST CALLING")
        Category_obj = Category.objects.get(pk=id)
        CategoryForm_obj = CategoryForm(request.POST, instance=Category_obj)
        if CategoryForm_obj.is_valid():
            CategoryForm_obj.save()
            messages.success(request, "Category Edited Successfully")
            return redirect('TKTAdmin:view_category')
        else:
            messages.error(request, "Invalid Data Entered")
            return render(request, 'TKTAdmin/admin_edit_category.html', {'CategoryForm_obj': CategoryForm_obj})

    else:
        print("GET CALLING")
        Category_obj = Category.objects.get(pk=id)
        print(Category_obj)
        CategoryForm_obj = CategoryForm(instance=Category_obj)
        return render(request, 'TKTAdmin/admin_edit_category.html', {'CategoryForm_obj': CategoryForm_obj})


###############################################


def view_ticket_status_choice(request):
    Ticket_status_choice_obj = Ticket_status_choice.objects.all()
    return render(request, 'TKTAdmin/view_ticket_status_choice.html',
                  {'Ticket_status_choice_obj': Ticket_status_choice_obj})


def create_ticket_status_choice(request):
    if request.method == 'POST':
        Ticket_status_choiceForm_obj = Ticket_status_choiceForm(request.POST)
        if Ticket_status_choiceForm_obj.is_valid():
            Ticket_status_choiceForm_obj.save()
            messages.success(request, "Ticket Status Choice Created Successfully")
            return redirect('TKTAdmin:view_ticket_status_choice')
        else:
            messages.error(request, "Invalid Data Entered")
            return render(request, 'TKTAdmin/admin_create_ticket_status_choice.html',
                          {'Ticket_status_choiceForm_obj': Ticket_status_choiceForm_obj})

    else:
        Ticket_status_choiceForm_obj = Ticket_status_choiceForm()
        return render(request, 'TKTAdmin/admin_create_ticket_status_choice.html',
                      {'Ticket_status_choiceForm_obj': Ticket_status_choiceForm_obj})


def edit_ticket_status_choice(request, id):
    if request.method == 'POST':
        print("POST CALLING")
        Ticket_status_choice_obj = Ticket_status_choice.objects.get(pk=id)
        Ticket_status_choiceForm_obj = Ticket_status_choiceForm(request.POST, instance=Ticket_status_choice_obj)
        if Ticket_status_choiceForm_obj.is_valid():
            Ticket_status_choiceForm_obj.save()
            messages.success(request, "Ticket Status Choice Edited Successfully")
            return redirect('TKTAdmin:view_ticket_status_choice')
        else:
            messages.error(request, "Invalid Data Entered")
            return render(request, 'TKTAdmin/admin_edit_ticket_status_choice.html',
                          {'Ticket_status_choiceForm_obj': Ticket_status_choiceForm_obj})

    else:
        print("GET CALLING")
        Ticket_status_choice_obj = Ticket_status_choice.objects.get(pk=id)
        print(Ticket_status_choice_obj)
        Ticket_status_choiceForm_obj = Ticket_status_choiceForm(instance=Ticket_status_choice_obj)
        return render(request, 'TKTAdmin/admin_edit_ticket_status_choice.html',
                      {'Ticket_status_choiceForm_obj': Ticket_status_choiceForm_obj})


###############################################

def view_technology_stack(request):
    technology_stack_obj = technology_stack.objects.all()
    return render(request, 'TKTAdmin/view_technology_stack.html',
                  {'technology_stack_obj': technology_stack_obj})


def create_technology_stack(request):
    if request.method == 'POST':
        technology_stackForm_obj = technology_stackForm(request.POST)
        if technology_stackForm_obj.is_valid():
            technology_stackForm_obj.save()
            messages.success(request, "Ticket Status Choice Created Successfully")
            return redirect('TKTAdmin:view_technology_stack')
        else:
            messages.error(request, "Invalid Data Entered")
            return render(request, 'TKTAdmin/create_technology_stack.html',
                          {'technology_stackForm_obj': technology_stackForm_obj})

    else:
        technology_stackForm_obj = technology_stackForm()
        return render(request, 'TKTAdmin/create_technology_stack.html',
                      {'technology_stackForm_obj': technology_stackForm_obj})


def edit_technology_stack(request, id):
    if request.method == 'POST':
        print("POST CALLING")
        technology_stack_obj = technology_stack.objects.get(pk=id)
        technology_stackForm_obj = technology_stackForm(request.POST, instance=technology_stack_obj)
        if technology_stackForm_obj.is_valid():
            technology_stackForm_obj.save()
            messages.success(request, "Technology Stack Edited Successfully")
            return redirect('TKTAdmin:view_technology_stack')
        else:
            messages.error(request, "Invalid Data Entered")
            return render(request, 'TKTAdmin/edit_technology_stack.html',
                          {'technology_stackForm_obj': technology_stackForm_obj})

    else:
        print("GET CALLING")
        technology_stack_obj = technology_stack.objects.get(pk=id)
        print(technology_stack_obj)
        technology_stackForm_obj = technology_stackForm(instance=technology_stack_obj)
        return render(request, 'TKTAdmin/edit_technology_stack.html',
                      {'technology_stackForm_obj': technology_stackForm_obj})


###############################################


def view_Issue_Category(request):
    Issue_Category_obj = Issue_Category.objects.all()
    return render(request, 'TKTAdmin/view_Issue_Category.html',
                  {'Issue_Category_obj': Issue_Category_obj})


def create_Issue_Category(request):
    if request.method == 'POST':
        Issue_CategoryForm_obj = Issue_CategoryForm(request.POST)
        if Issue_CategoryForm_obj.is_valid():
            Issue_CategoryForm_obj.save()
            messages.success(request, "Issue CategoryCreated Successfully")
            return redirect('TKTAdmin:view_Issue_Category')
        else:
            messages.error(request, "Invalid Data Entered")
            return render(request, 'TKTAdmin/create_issue_category.html',
                          {'Issue_CategoryForm_obj': Issue_CategoryForm_obj})

    else:
        Issue_CategoryForm_obj = Issue_CategoryForm()
        return render(request, 'TKTAdmin/create_issue_category.html',
                      {'Issue_CategoryForm_obj': Issue_CategoryForm_obj})


def edit_Issue_Category(request, id):
    if request.method == 'POST':
        print("POST CALLING")
        Issue_Category_obj = Issue_Category.objects.get(pk=id)
        Issue_CategoryForm_obj = Issue_CategoryForm(request.POST, instance=Issue_Category_obj)
        if Issue_CategoryForm_obj.is_valid():
            Issue_CategoryForm_obj.save()
            messages.success(request, "Issue Category Successfully")
            return redirect('TKTAdmin:view_Issue_Category')
        else:
            messages.error(request, "Invalid Data Entered")
            return render(request, 'TKTAdmin/edit_issue_category.html',
                          {'Issue_CategoryForm_obj': Issue_CategoryForm_obj})

    else:
        print("GET CALLING")
        Issue_Category_obj = Issue_Category.objects.get(pk=id)
        print(Issue_Category_obj)
        Issue_CategoryForm_obj = Issue_CategoryForm(instance=Issue_Category_obj)
        return render(request, 'TKTAdmin/edit_issue_category.html',
                      {'Issue_CategoryForm_obj': Issue_CategoryForm_obj})


###################################################


def view_agent_list(request):
    Agent_obj = Agent.objects.all()
    # print(Agent_obj)
    # for value in Agent_obj:
    #     techexpert_obj = value.Agent_technology_expert.all()
    #     # print(techexpert_obj[0].technology_name)
    return render(request, 'TKTAdmin/view_agent_list.html',
                  {'Agent_obj': Agent_obj})


def create_agent_list(request):
    if request.method == 'POST':
        AgentForm_obj = AgentForm(request.POST)
        if AgentForm_obj.is_valid():
            AgentForm_obj.save()
            messages.success(request, "Agent Created Successfully")
            return redirect('TKTAdmin:view_agent_list')
        else:
            messages.error(request, "Invalid Data Entered")
            return render(request, 'TKTAdmin/create_agent.html',
                          {'AgentForm_obj': AgentForm_obj})
    else:
        AgentForm_obj = AgentForm()
        return render(request, 'TKTAdmin/create_agent.html',
                      {'AgentForm_obj': AgentForm_obj})


def edit_agent_list(request,id):
    if request.method == 'POST':
        Agent_obj = Agent.objects.get(pk=id)
        AgentForm_obj = AgentForm(request.POST, instance=Agent_obj)
        if AgentForm_obj.is_valid():
            AgentForm_obj.save()
            messages.success(request, "Edited Successfully")
            return redirect('TKTAdmin:view_agent_list')
        else:
            messages.error(request, "Invalid Data Entered")
            return render(request, 'TKTAdmin/edit_agent.html',
                          {'AgentForm_obj': AgentForm_obj})
    else:
        Agent_obj = Agent.objects.get(pk=id)
        AgentForm_obj = AgentForm(instance=Agent_obj)
        return render(request, 'TKTAdmin/edit_agent.html',
                      {'AgentForm_obj': AgentForm_obj})


###################################################


def view_tickets_list(request):
    TicketDetail_obj = TicketDetail.objects.all()
    Ticket_status_obj = Ticket_status.objects.all()
    return render(request, 'TKTAdmin/view_TicketDetail.html',
                  {'TicketDetail_obj': TicketDetail_obj,'Ticket_status_obj':Ticket_status_obj})