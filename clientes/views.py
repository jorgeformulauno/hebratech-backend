from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrdenForm
from .models import Orden, Cliente, Producto


def registrar_orden(request):
    # Por ahora usamos el cliente #1 (Éxito) como cliente de sesión
    # Esto lo conectaremos al login en pasos posteriores
    cliente = Cliente.objects.get(idCliente=1)

    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            producto = form.cleaned_data['producto']

            orden = Orden(
                idCliente=cliente,
                cantidad=form.cleaned_data['cantidad'],
                precioUnitario=producto.precio,
                fechaEntregaEstimada=form.cleaned_data['fechaEntregaEstimada'],
                instrucciones=form.cleaned_data['instrucciones'] or '',
                prioridad=form.cleaned_data['prioridad'],
                estado='Pendiente'
            )
            orden.save()

            messages.success(request, f'Orden #{orden.idOrden} registrada exitosamente.')
            return redirect('orden_exitosa', idOrden=orden.idOrden)
    else:
        form = OrdenForm()

    return render(request, 'clientes/registrar_orden.html', {
        'form': form,
        'cliente': cliente
    })


def orden_exitosa(request, idOrden):
    orden = Orden.objects.get(idOrden=idOrden)
    return render(request, 'clientes/orden_exitosa.html', {'orden': orden})


def mis_ordenes(request):
    cliente = Cliente.objects.get(idCliente=1)
    ordenes = Orden.objects.filter(idCliente=cliente).order_by('-fechaCreacion')
    return render(request, 'clientes/mis_ordenes.html', {
        'ordenes': ordenes,
        'cliente': cliente
    })