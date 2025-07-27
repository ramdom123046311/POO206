from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.albumModel import getAll, softDeleteAlbum, insertarAlbum, updateAlbum, getAlbumById

albumBP = Blueprint('albums', __name__)


@albumBP.route('/')
def home():
    try:
        albums = getAll()
        return render_template('formulario.html', errores={}, albums=albums)
    except Exception as e:
        print('Error al consultar todo:', str(e))
        flash('Error al cargar los álbumes', 'error')
        return render_template('formulario.html', errores={}, albums=[])

@albumBP.route('/guardarAlbum', methods=['POST'])
def guardar():
    errores = {}
    Vtitulo = request.form.get('txtTitulo', '').strip()
    Vartista = request.form.get('txtArtista', '').strip()
    Vanio = request.form.get('txtAnio', '').strip()

    if not Vtitulo:
        errores['txtTitulo'] = 'Nombre del álbum obligatorio'
    if not Vartista:
        errores['txtArtista'] = 'Nombre de artista obligatorio'
    if not Vanio:
        errores['txtAnio'] = 'Año obligatorio'
    elif not Vanio.isdigit() or int(Vanio) < 1800 or int(Vanio) > 2100:
        errores['txtAnio'] = 'Ingresa un año válido (entre 1800 y 2100)'

    if errores:
        return render_template('formulario.html', errores=errores, albums=getAll())

    try:
        insertarAlbum(Vtitulo, Vartista, Vanio)
        flash('Álbum guardado correctamente', 'success')
        return redirect(url_for('albums.home'))
    except Exception as e:
        flash(f'Error al guardar: {str(e)}', 'error')
        return redirect(url_for('albums.home'))

@albumBP.route('/eliminar/<int:id>', methods=['GET'])
def eliminar_confirmacion(id):
    try:
        album = getAlbumById(id)
        if not album or album.get('state') == 0:
            flash('Álbum no encontrado o ya eliminado', 'error')
            return redirect(url_for('albums.home'))
            
        return render_template('confirmDel.html', album=album)
    except Exception as e:
        print("Error al cargar confirmación:", str(e))
        flash('Error al cargar la confirmación: ' + str(e), 'error')
        return redirect(url_for('albums.home'))

@albumBP.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_album(id):
    try:
        softDeleteAlbum(id)
        flash('Álbum eliminado correctamente', 'success')
        return redirect(url_for('albums.home'))
    except Exception as e:
        print('Error al eliminar:', str(e))
        flash('Error al eliminar el álbum', 'error')
        return redirect(url_for('albums.home'))

@albumBP.route('/detalle/<int:id>')
def detalle(id):
    try:
        album = getAlbumById(id)
        if album:
            return render_template('consulta.html', album=album)
        else:
            flash('Álbum no encontrado', 'error')
            return redirect(url_for('albums.home'))
    except Exception as e:
        print('Error al consultar id:', str(e))
        flash('Error al cargar el detalle', 'error')
        return redirect(url_for('albums.home'))

@albumBP.route('/actualizar/<int:id>', methods=['GET'])
def actualizar(id):
    try:
        album = getAlbumById(id)
        if album:
            return render_template('actualizar.html', album=album, errores={})
        else:
            flash('Álbum no encontrado', 'error')
            return redirect(url_for('albums.home'))
    except Exception as e:
        print('Error al consultar para actualizar:', str(e))
        flash('Error al cargar el formulario', 'error')
        return redirect(url_for('albums.home'))

@albumBP.route('/guardarCambios/<int:id>', methods=['POST'])
def guardarCambios(id):
    Vtitulo = request.form.get('txtTitulo', '').strip()
    Vartista = request.form.get('txtArtista', '').strip()
    Vanio = request.form.get('txtAnio', '').strip()

    errores = {}
    if not Vtitulo:
        errores['txtTitulo'] = 'Título obligatorio'
    if not Vartista:
        errores['txtArtista'] = 'Artista obligatorio'
    if not Vanio:
        errores['txtAnio'] = 'Año obligatorio'
    elif not Vanio.isdigit() or int(Vanio) < 1800 or int(Vanio) > 2100:
        errores['txtAnio'] = 'Año inválido (1800-2100)'

    if errores:
        album = {
            'id': id,
            'album': Vtitulo,
            'artista': Vartista,
            'anio': Vanio
        }
        return render_template('actualizar.html', album=album, errores=errores)

    try:
        updateAlbum(id, Vtitulo, Vartista, Vanio)
        flash('Álbum actualizado correctamente', 'success')
        return redirect(url_for('albums.home'))
    except Exception as e:
        print('Error al actualizar:', str(e))
        flash('Error al actualizar el álbum', 'error')
        return redirect(url_for('albums.home'))