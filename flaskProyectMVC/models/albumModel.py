from extensions import mysql

def getAll():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tb_albums WHERE state = 1")
    albums = cursor.fetchall()
    
    # Convertir a lista de diccionarios
    result = []
    for album in albums:
        result.append({
            'id': album[0],
            'album': album[1],
            'artista': album[2],
            'anio': album[3],
            'state': album[4]
        })
    return result

def softDeleteAlbum(id):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE tb_albums SET state = 0 WHERE id = %s", (id,))
    mysql.connection.commit()
    cursor.close()

def updateAlbum(id, titulo, artista, anio):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE tb_albums 
        SET album = %s, artista = %s, anio = %s 
        WHERE id = %s
    """, (titulo, artista, anio, id))
    mysql.connection.commit()
    cursor.close()

def insertarAlbum(titulo, artista, anio):
    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO tb_albums(album, artista, anio, state) 
        VALUES (%s, %s, %s, 1)
    """, (titulo, artista, anio))
    mysql.connection.commit()
    cursor.close()

def getAlbumById(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tb_albums WHERE id = %s", (id,))
    album = cursor.fetchone()
    cursor.close()
    
    if not album:
        return None
        
    return {
        'id': album[0],
        'album': album[1],
        'artista': album[2],
        'anio': album[3],
        'state': album[4]
    }
    
    