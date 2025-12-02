import re

class Validaciones:  

    # Validaciones de login
    @classmethod
    def validarNumeroDeTelefono(cls,numero):
        if numero == '':
            return 'Campo obligatorio: Numero de telefono.'
        return numero
    
    @classmethod
    def validarPassword(cls,pwrd):
        if pwrd == '':
            return 'Contrasena no ingresada.'
        return pwrd
    
    # Validaciones del registro
    @classmethod
    def validarPhone(cls,phone):
        if phone == '':
            return 'Campo obligatorio: Numero de telefono.'
        if len(phone) != 10:
            return 'El numero de telefono debe tener 10 digitos.'
        return phone
    
    @classmethod
    def validarContrasena(cls,pwrd):
        if pwrd == '':
            return 'Contrasena no ingresada.'
        if len(pwrd) <= 7:
            return 'La contrasena debe tener al menos 8 caracteres.'
        if len(pwrd) >= 21:
            return 'La contrasena debe tener menos de 21 caracteres.'
        return pwrd
    

    ''' Validaciones para reservaciones '''
    @classmethod
    def validar_id(self,valor):
        valor = str(valor).strip()

        if valor == "":
            return "Todo"   # si quieres que un campo vacío signifique "Todo"
    
        # Solo números positivos, 1 a 4 dígitos
        patron = r'^[0-9]{1,4}$'
        return bool(re.match(patron, valor))

    @classmethod
    def validar_ciudad(self,ciudad):
        ciudad = str(ciudad).strip()

        if ciudad == "":
            return "Ciudad no ingresada."   # si quieres que un campo vacío signifique "Todo"
    
        # Solo letras y espacios, 1 a 20 caracteres
        patron = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{1,20}$'
        return bool(re.match(patron, ciudad))