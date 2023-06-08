
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.db.models import Q
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from .forms import ClienteForm
from .models import Cliente
from .forms import IngenieroForm
from .models import Ingeniero
from .forms import ProyectoForm
from .models import Proyecto
from .forms import ActividadForm
from .models import Actividad
from .forms import BitacoraForm
from .models import Bitacora
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import shortuuid
from django.contrib.auth.decorators import user_passes_test





def admin_required(view_func):
    return user_passes_test(lambda u: u.is_superuser, login_url='acceso-no-autorizado')(view_func)
# Create your views here.

#Registrarse
def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # registro de usuario
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('inicio')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Las contraseñaas no coinciden'
        })
        
#iniciar sesion
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST
                            ['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecto'
            })
        else:
            login(request, user)
            return redirect('home')
        
#cerrar sesion
@login_required
def signout(request):
    logout(request)
    return redirect('inicio')

def inicio(request):
    return render(request, 'inicio.html')

@login_required
def home(request):
    return render(request, 'home.html')

# AQUI COMIENZA EL CRUD PARA CLIENTE
@login_required
def cliente(request):
    return render(request, 'cliente.html')

@login_required
def create_cliente(request):
    if request.method == 'GET':
        return render(request, 'create_cliente.html', {
            'form': ClienteForm
        })
    else:
        try:
            form = ClienteForm(request.POST)
            new_cliente = form.save(commit=False)
            new_cliente.user = request.user
            new_cliente.save()
            messages.success(request, "¡Cliente agregado correctamente!")
            return redirect('cliente')
        except ValueError:       
            return render(request, 'create_cliente.html', {
                'form': ClienteForm,
                'error': '¡Por favor proporcione datos validos!'
            })
 
@login_required            
def detalle_cliente(request, NID):
    if request.method == 'GET':
        cliente = get_object_or_404(Cliente, pk=NID)
        form = ClienteForm(instance=cliente)
        return render(request, 'detalle_cliente.html', {'cliente': cliente, 'form': form})
    else:
        try:
            cliente = get_object_or_404(Cliente, pk=NID)
            form = ClienteForm(request.POST,instance=cliente)
            form.save()
            messages.success(request, "¡Informacion actualizada correctamente!")
            return redirect('listaclientes')
        except ValueError:
            return render(request, 'detalle_cliente.html', {'cliente': cliente, 'form': form,
            'error': "No es posrible actualizar la informacion por error en los parametros"})

@login_required
def eliminar_cliente(request, NID):
    cliente = get_object_or_404(Cliente, pk=NID)
    if request.method == 'POST':
        if cliente.bitacora_set.exists():
           messages.error(request, 'No se permite la eliminación porque el cliente está asociado con un registro de bitacora')
           return redirect('listaclientes')
        else:
            cliente.delete()
            messages.success(request, "¡El cliente ha sido eliminado con exito!")
            return redirect('listaclientes')   

@login_required                
def vistacliente(request):
    return render(request, 'vistacliente.html')

@login_required
def listaclientes(request):
    busqueda = request.POST.get("buscar")
    clientes = Cliente.objects.all()
    page = request.GET.get('page', 1)
    
  
    paginator = Paginator(clientes, 5)
    clientes = paginator.page(page)
  
    
    if busqueda:
        clientes = Cliente.objects.filter(
            Q(NID__icontains = busqueda) | 
            Q(Razon_social__icontains = busqueda) 
        ).distinct()
        
    return render(request, 'listaclientes.html', {'clientes': clientes})

# AQUI TERMINA EL CRUD PARA CLIENTE

# AQUI COMIENZA EL CRUD PARA INGENIEROS
    
@login_required
def ingeniero(request):
    return render(request, 'ingeniero.html')

@login_required
def create_ingeniero(request):
    if request.method == 'GET':
        return render(request, 'create_ingeniero.html', {
            'form': IngenieroForm
        })
    else:
        try:
            form = IngenieroForm(request.POST)
            new_ingeniero = form.save(commit=False)
            new_ingeniero.user = request.user
            new_ingeniero.save()
            messages.success(request, "¡Ingeniero creado correctamente!")
            return redirect('ingeniero')
        except ValueError:       
            return render(request, 'create_ingeniero.html', {
                'form': IngenieroForm,
                'error': 'Por favor proporcione datos validos'
            })
            
@login_required            
def detalle_ingeniero(request, COD_ingeniero):
    if request.method == 'GET':
        ingeniero = get_object_or_404(Ingeniero, pk=COD_ingeniero)
        form = IngenieroForm(instance=ingeniero)
        return render(request, 'detalle_ingeniero.html', {'ingeniero': ingeniero, 'form': form})
    else:
        try:
            ingeniero = get_object_or_404(Ingeniero, pk=COD_ingeniero)
            form = IngenieroForm(request.POST,instance=ingeniero)
            form.save()
            messages.success(request, "¡Informacion actualizada correctamente!")
            return redirect('listaingenieros')
        except ValueError:
            return render(request, 'detalle_ingeniero.html', {'ingeniero': ingeniero, 'form': form,
            'error': "No es posrible actualizar la informacion por error en los parametros"})

@login_required
def eliminar_ingeniero(request, COD_ingeniero):
    ingeniero = get_object_or_404(Ingeniero, pk=COD_ingeniero)
    if request.method == 'POST':
        ingeniero.delete()
        messages.success(request, "¡El ingeniero ha sido eliminado con exito!")
        return redirect('listaingenieros')

@login_required
def listaingenieros(request):
    busqueda = request.POST.get("buscar")
    ingenieros = Ingeniero.objects.all()
    page = request.GET.get('page', 1)
    
  
    paginator = Paginator(ingenieros, 5)
    ingenieros = paginator.page(page)
  
    
    if busqueda:
        ingenieros = Ingeniero.objects.filter(
            Q(COD_ingeniero__icontains = busqueda) | 
            Q(Identificacion__icontains = busqueda) |
            Q(Nombres__icontains = busqueda) |
            Q(Apellidos__icontains = busqueda) 
        ).distinct()
        
    return render(request, 'listaingenieros.html', {'ingenieros': ingenieros})

# AQUI TERMINA EL CRUD PARA INGENIEROS

# AQUI EMPIEZA EL CRUD PARA PROYECTOS
@login_required
def proyecto(request):
    return render(request, 'proyecto.html')

@login_required
def create_proyecto(request):
    if request.method == 'GET':
        return render(request, 'create_proyecto.html', {
            'form': ProyectoForm
        })
    else:
        try:
            form = ProyectoForm(request.POST)
            new_proyecto = form.save(commit=False)
            new_proyecto.user = request.user
            new_proyecto.save()
            form.save_m2m()
            messages.success(request, "¡Proyecto creado correctamente!")
            return redirect('proyecto')
        except ValueError:       
            return render(request, 'create_proyecto.html', {
                'form': ProyectoForm,
                'error': 'Por favor proporcione datos validos'
            })

@login_required            
def detalle_proyecto(request, Codigo):
    if request.method == 'GET':
        proyecto = get_object_or_404(Proyecto, pk=Codigo)
        form = ProyectoForm(instance=proyecto)
        return render(request, 'detalle_proyecto.html', {'proyecto': proyecto, 'form': form})
    else:
        try:
            proyecto = get_object_or_404(Proyecto, pk=Codigo)
            form = ProyectoForm(request.POST,instance=proyecto)
            form.save()
            messages.success(request, "¡Informacion actualizada correctamente!")
            return redirect('listaproyectos')
        except ValueError:
            return render(request, 'detalle_proyecto.html', {'proyecto': proyecto, 'form': form,
            'error': "No es posible actualizar la informacion por error en los parametros"})

@login_required
def eliminar_proyecto(request, Codigo):
    proyecto = get_object_or_404(Proyecto, pk=Codigo)
    if request.method == 'POST':
        proyecto.delete()
        messages.success(request, "¡El proyecto ha sido eliminado con exito!")
        return redirect('listaproyectos')

@login_required
def listaproyectos(request):
    busqueda = request.POST.get("buscar")
    proyectos = Proyecto.objects.all()
    page = request.GET.get('page', 1)
    
  
    paginator = Paginator(proyectos, 5)
    proyectos = paginator.page(page)
  
    
    if busqueda:
        proyectos = Proyecto.objects.filter(
            Q(Codigo__icontains = busqueda) | 
            Q(Nombre__icontains = busqueda)  
        ).distinct()
        
    return render(request, 'listaproyectos.html', {'proyectos': proyectos})

# AQUI TERMINA EL CRUD PARA PROYECTOS

# AQUI EMPIEZA EL CRUD PARA ACTIVIDADES
@login_required
def actividad(request):
    return render(request, 'actividad.html')

@login_required
def create_actividad(request):
    if request.method == 'GET':
        return render(request, 'create_actividad.html', {
            'form': ActividadForm
        })
    else:
        try:
            form = ActividadForm(request.POST)
            new_actividad = form.save(commit=False)
            new_actividad.user = request.user
            new_actividad.save()
            messages.success(request, "¡Actividad agregada correctamente!")
            return redirect('actividad')
        except ValueError:       
            return render(request, 'create_actividad.html', {
                'form': ActividadForm,
                'error': 'Por favor proporcione datos validos'
            })

@login_required            
def detalle_actividad(request, COD_actividad):
    if request.method == 'GET':
        actividad = get_object_or_404(Actividad, pk=COD_actividad)
        form = ActividadForm(instance=actividad)
        return render(request, 'detalle_actividad.html', {'actividad': actividad, 'form': form})
    else:
        try:
            actividad = get_object_or_404(Actividad, pk=COD_actividad)
            form = ActividadForm(request.POST,instance=actividad)
            form.save()
            messages.success(request, "¡Informacion actualizada correctamente!")
            return redirect('listaactividades')
        except ValueError:
            return render(request, 'detalle_actividad.html', {'actividad': actividad, 'form': form,
            'error': "No es posrible actualizar la informacion por error en los parametros"})

@login_required
def eliminar_actividad(request, COD_actividad):
    actividad = get_object_or_404(Actividad, pk=COD_actividad)
    if request.method == 'POST':
        actividad.delete()
        messages.success(request, "¡La actividad ha sido eliminada con exito!")
        return redirect('listaactividades')

@login_required
def listaactividades(request):
    busqueda = request.POST.get("buscar")
    actividades = Actividad.objects.all()
    page = request.GET.get('page', 1)
    
  
    paginator = Paginator(actividades, 5)
    actividades = paginator.page(page)
    
    if busqueda:
        actividades = Actividad.objects.filter(
            Q(COD_actividad__icontains = busqueda) | 
            Q(Nombre__icontains = busqueda)  
        ).distinct()
        
    return render(request, 'listaactividades.html', {'actividades': actividades})

@login_required
def moneda(request):
    return render(request, 'moneda.html')

@login_required
def olvidemicontrasena(request):
    return render(request, 'olvidemicontrasena.html')
# AQUI TERMINA LA SECCION DE MONEDA

# AQUI EMPIEZAN LAS FUNCIONALIDADES DEL USUARIO REGULAR
def signiningeniero(request):
    if request.method == 'GET':
        return render(request, 'signiningeniero.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST
                            ['password'])
        if user is None:
            return render(request, 'signiningeniero.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecto'
            })
        else:
            login(request, user)
            return redirect('homeusuario')
        
#cerrar sesion
@login_required
def signout(request):
    logout(request)
    return redirect('inicio')

@login_required
def homeusuario(request):
    return render(request, 'homeusuario.html')

@login_required
def signupingeniero(request):
    
    if request.method == 'GET':
        return render(request, 'signupingeniero.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1']:
            try:
                # registro de usuario
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                #login(request, user)
                messages.success(request, "¡Credenciales creadas correctamente!")
                return redirect('signupingeniero')
            except IntegrityError:
                return render(request, 'signupingeniero.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
        return render(request, 'signupingeniero.html', {
            'form': UserCreationForm,
            "error": 'Las contraseñaas no coinciden'
        })

@login_required
def bitacora(request):
    return render(request, 'bitacora.html')

@login_required
def create_bitacora(request):
    if request.method == 'GET':
        form = BitacoraForm(initial={'user': request.user})
    else:
        form = BitacoraForm(request.POST)
        if form.is_valid():
            bitacora = form.save(commit=False)
            bitacora.user = request.user
            bitacora.save()
            messages.success(request, "¡Bitácora agregada correctamente!")
            return redirect('bitacora')

    return render(request, 'create_bitacora.html', {'form': form})


@login_required
def listabitacoras(request):
    busqueda = request.POST.get("buscar")
    user = request.user  # Obtener el usuario actualmente autenticado
    bitacoras = Bitacora.objects.filter(user=user)  # Filtrar por el usuario actual
    page = request.GET.get('page', 1)

    if busqueda:
        bitacoras = bitacoras.filter(
            Q(COD_bitacora__icontains=busqueda) |
            Q(Fecha__icontains=busqueda)
        ).distinct()

    # Ordenar las bitácoras por fecha de forma descendente (más reciente a más antigua)
    bitacoras = bitacoras.order_by('-Fecha__year', '-Fecha__month', '-Fecha__day')

    paginator = Paginator(bitacoras, 5)
    bitacoras = paginator.page(page)

    return render(request, 'listabitacoras.html', {'bitacoras': bitacoras})

@login_required
def detalle_bitacora(request, COD_bitacora):
    if request.method == 'GET':
        bitacora = get_object_or_404(Bitacora, pk=COD_bitacora)
        form = BitacoraForm(instance=bitacora)
        return render(request, 'detalle_bitacora.html', {'bitacora': bitacora, 'form': form})
    else:
        try:
            bitacora = get_object_or_404(Bitacora, pk=COD_bitacora)
            form = BitacoraForm(request.POST,instance=bitacora)
            form.save()
            return redirect('listabitacoras')
        except ValueError:
            return render(request, 'detalle_bitacora.html', {'bitacora': bitacora, 'form': form
            #'error': "No es posrible actualizar la informacion por error en los parametros"
            })
  
# GENERAR DE REPORTES          
@login_required
def generarreporte(request):
    return render(request, 'generarreporte.html')

def detallebitacoraregistrada(request, COD_bitacora):
    if request.method == 'GET':
        bitacora = get_object_or_404(Bitacora, pk=COD_bitacora)
        form = BitacoraForm(instance=bitacora)
        return render(request, 'detallebitacoraregistrada.html', {'bitacora': bitacora, 'form': form})
    else:
        try:
            bitacora = get_object_or_404(Bitacora, pk=COD_bitacora)
            form = BitacoraForm(request.POST,instance=bitacora)
            form.save()
            return redirect('bitacorasingeniero')
        except ValueError:
            return render(request, 'detallebitacoraregistrada.html', {'bitacora': bitacora, 'form': form
            #'error': "No es posrible actualizar la informacion por error en los parametros"
            })

@login_required
def balancegeneral(request):
    return render(request, 'balancegeneral.html')

@login_required
def cifrasproyecto(request):
    return render(request, 'cifrasproyecto.html')

@login_required
def cifrasactividad(request):
    return render(request, 'cifrasactividad.html')

@login_required
def novedadescolaborador(request):
    return render(request, 'novedadescolaborador.html')

@login_required
def buscarbitacoras(request):
    busqueda = request.POST.get("buscar")
    ingenieros = Ingeniero.objects.all()
    page = request.GET.get('page', 1)
    
  
    paginator = Paginator(ingenieros, 5)
    ingenieros = paginator.page(page)
  
    
    if busqueda:
        ingenieros = Ingeniero.objects.filter(
            Q(COD_ingeniero__icontains = busqueda) | 
            Q(Identificacion__icontains = busqueda) |
            Q(Nombres__icontains = busqueda) |
            Q(Apellidos__icontains = busqueda) 
        ).distinct()
        
    return render(request, 'buscarbitacoras.html', {'ingenieros': ingenieros})

@login_required
def productividad(request):
    return render(request, 'productividad.html')

#GESTIO DE PROYECTOS
@login_required
def registroIngeniero(request):
    return render(request, 'registroIngeniero.html')


@login_required
def bitacorasingeniero(request, COD_ingeniero):
    ingeniero = get_object_or_404(Ingeniero, COD_ingeniero=COD_ingeniero)
    bitacoras = Bitacora.objects.filter(user=request.user)
    busqueda = request.POST.get("buscar")
    bitacoras = Bitacora.objects.all()
    page = request.GET.get('page', 1)
    
  
    paginator = Paginator(bitacoras, 5)
    bitacoras = paginator.page(page)
    
    
    
    if busqueda:
        bitacoras = Bitacora.objects.filter(
            Q(COD_bitacora__icontains = busqueda) |
            Q(Fecha__icontains = busqueda) |
            Q(user__username__icontains=busqueda) 
            ).distinct()
        bitacoras = bitacoras.order_by('-Fecha')
        
    return render(request, 'bitacorasingeniero.html', {'ingeniero': ingeniero, 'bitacoras': bitacoras})

    
@login_required
def base(request):
    return render(request, 'base.html')

#ACESO NO AUTORIZADO
def accesonoautorizado(request):
    return render(request, 'accesonoautorizado.html')
