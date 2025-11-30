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