from django.contrib import admin , messages
from  .models import  *
# Register your models here.
class MemberShipInline(admin.StackedInline):
    model = MembershipInProject
    extra = 0

class StudentAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email')

class CoachAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email')

class Filter_Duree(admin.SimpleListFilter):
    title = ('Duree')
    parameter_name = 'duree'

    def lookups(self, request, model_admin):
        return (('1 mois', ("mois d'1 mois")),('3 mois', ("plus d'1 mois")))

    def queryset(self, request, queryset):
        if self.value() == '1 mois':
            return queryset.filter(duree_du_projet__lte=30)
        if self.value() == '3 mois':
            return queryset.filter(duree_du_projet__lte=90, duree_du_projet__gte=30)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('nom_du_projet', 'duree_du_projet', 'temps_alloue_par_le_createur','besoins','description','est_valide','createur','superviseur','total_allocated_by_members',)
    actions = ['set_to_valid','set_to_no_valide']




    def set_to_no_valide(self, request, queryset):
        no_valid = queryset.filter(est_valide=False)
        if no_valid.count()>0 :
            messages.error(request," %s projects est_valide=False"%no_valid.count())
        else:
            rows_update = queryset.update(est_valide=False)
            if rows_update == 1 :
                messages.info(request , " %s project est valide = True"%rows_update)
            else:
                message = " %s project est valide = True"%rows_update
                #messages.info(request,"%s projects were updated "%rows_update)
                self.message_user(request,message="%s successfullu "%message)
    def set_to_valid(self, request, queryset):
        queryset.update(est_valide=True)

    set_to_valid.short_description = "Valider"
    inlines =  (MemberShipInline,)
    fieldsets =  ( ('Etat', {'fields':('est_valide',)}) ,
                   ('A propos', {'fields':('nom_du_projet' ,
                                           ('createur' , 'superviseur') , 'besoins' , 'description')}) ,
                   ('Duree' , {'fields':('duree_du_projet' ,'temps_alloue_par_le_createur' )}),
                   )


    search_fields = ['nom_du_projet','createur__nom']
    list_filter = ['createur__prenom',Filter_Duree]
    actions_on_bottom = True
    actions_on_top = False
    list_per_page = 1
admin.site.register(Student,StudentAdmin)
admin.site.register(Coach ,CoachAdmin)
admin.site.register(Project,ProjectAdmin)