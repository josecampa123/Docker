from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy



class RegistrarView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registrar.html'

#def contraseña(request):
 #   if request.method == 'POST':
  #      form = PasswordChangeForm(request.user,request.post)
   #     if form.is_valid():
    #        user=form.save()
     #       update_session_auth_hash(request,user)
      #      return redirect('login')
       # else:
        #    pass
    #else: 
     #   form=PasswordChangeForm(request.user)
    #return render(request,'registrartion/password_change.html',{'form':form})

