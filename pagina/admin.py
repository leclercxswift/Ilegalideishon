from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    actions = ['set_pdf_file']

    def set_pdf_file(self, request, queryset):
        # Esta función establece el archivo PDF para los usuarios seleccionados en el panel de administración
        # Puedes personalizar esto según tus necesidades
        for user_profile in queryset:
            # Ruta al archivo PDF deseado
            pdf_path = '/ruta/al/pdf/chimbo.pdf'
            user_profile.pdf_file.name = 'pdfs/chimbo.pdf'
            user_profile.save()

        self.message_user(request, 'PDF file set successfully.')

    set_pdf_file.short_description = 'Set PDF file for selected users'

admin.site.register(UserProfile, UserProfileAdmin)