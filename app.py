# coding: utf-8
import web
import datetime
import model
import json
from web import form

### Url mappings

urls = (
    '/', 'Index',
    '/view/(\d+)', 'View',
    '/cuentas', 'Cuentas',
    '/new', 'New',
    '/delete/(\d+)', 'Delete',
    '/edit/(\d+)', 'Edit',
    '/consultas', 'Consultas',
    '/login', 'Login',
    '/informacion','Informacion')


### Templates
t_globals = {
    'datestr': web.datestr
}
render = web.template.render('views', base='base', globals=t_globals)

class Cuentas:
    def GET(self):
        posts1= model.get_posts()
        return render.cuentas(posts1)

class Index:
    def GET(self):
        posts = model.get_posts()
        return render.index(posts)

class Informacion:
     def GET(self):
        bariavle = 'Francisco Javier Heredia Tellez'
        bariavle2 = 'Frankcisco-xavier@live.com.mx'
        bariavle4 = 'ITI-71'
        bariavle5 = '1714110251'
        return render.informacion(bariavle, bariavle2, bariavle4, bariavle5)

        
class Consultas:
     def GET (datos):
         
        datos=[]
        with open("registros.json","r")as file:
            datos=json.load(file)
        return render.consultas(datos)

class Login:
    def GET(self):
        bariavle = 'INICIO DE SECION'
        return render.login(bariavle)



class View:
    def GET(self, id):
        """ View single post """
        post = model.get_post(int(id))
        return render.view(post)


class New:
    form = web.form.Form(
        web.form.Textbox('nombre', web.form.notnull, 
            size=30,
            description="Pueblo:"),
        web.form.Textbox('telefono', web.form.notnull, 
            size=30,
            description="Telefono :"),
        web.form.Textbox('email', web.form.notnull, 
            size=30,
            description="Email:"),
        web.form.Textbox('sitio_web', web.form.notnull, 
            size=30,
            description="web:"),
        web.form.Textarea('informacion', web.form.notnull, 
            rows=15, cols=32,
            description="informacion:"),
        web.form.Textbox('guia_turistico', web.form.notnull, 
            size=30,
            description="Guia Turistico:"),
        web.form.Textbox('telefono_guia', web.form.notnull, 
            size=30,
            description="Telefono Guia:"),
        web.form.Button('Guardar'),
    )

    def GET(self):
        form = self.form()
        return render.new(form)

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.new(form)
        model.new_post(form.d.nombre, form.d.telefono, form.d.email, form.d.sitio_web, form.d.informacion, form.d.guia_turistico, form.d.telefono_guia )
        raise web.seeother('/')


class Delete:

    def POST(self, id):
        model.del_post(int(id))
        raise web.seeother('/')


class Edit:

    def GET(self, id):
        post = model.get_post(int(id))
        form = New.form()
        form.fill(post)
        return render.edit(post, form)


    def POST(self, id):
        form = New.form()
        post = model.get_post(int(id))
        if not form.validates():
            return render.edit(post, form)
        model.update_post(int(id), form.d.nombre, form.d.telefono, form.d.email, form.d.sitio_web, form.d.informacion, form.d.guia_turistico, form.d.telefono_guia)
        raise web.seeother('/')


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()