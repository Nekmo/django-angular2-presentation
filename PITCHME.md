@title[Introducción]
## Django y Angular 6 de la mano

Note:
Buenas, soy Juan José Oyagüe, en esta charla voy a contar mi experiencia usando Angular 6 junto con Django,

---
@title[acerca-tec]
## Tecnologías previas

* Django desde versión 1.1 (2009)
* AngularJS desde versión 1.1 (2013)

Note:
En mi caso, antes de usar Angular 4, tenía 8 años experiencia usando Django, y había estado usando AngularJS desde 
hace 5, por lo que el cambio de tecnología fue algo difícil. Tuve que cambiar mi forma de trabajar.

---
@title[requerido-django]


Note:
Así que esta presentación no va a ir sobre cómo volverse un profesional de Angular y Django en tan sólo 45 minutos... 
Sino sobre mis errores y experiencias

---
@title[mis-errores]

Note:
Y cómo aprendí conjuntar ambas tecnologías antes del deadline. Para esta presentación, se presupone que ya se cuenta 
con conocimientos al menos de Django, aunque no hace falta de Angular.


---
@title[contenido]

En esta presentación se va a ver:

* Comparación entre Angular y Django
* Formas de utilizar Angular
* Angular CLI
* Conectando Angular y Django
* Demo técnica
* Paso a producción

Note:
En esta presentación vamos a ver (...) pero antes, vamos a hacer una pequeña presentación de Django y Angular


---
@title[django]

Django es un framework web de servidor en Python. Algunas características:

* ORM propio
* Administración
* Middleware
* Sistema de rutas
* Lenguaje de plantillas
* Controlador (llamadas vistas)

Note:
(...) ahora veamos Angular

---
@title[angular]

Angular es un framework web de cliente en JS/TypeScript. Algunas características:

* Web Apps progresivas
* Multiplataforma (web, escritorio, móvil...)
* Optimización web (code splitting, Universal...)
* Sistema de rutas
* Lenguaje de plantillas
* Controlador (llamados componentes)

SystemJS ya no aparece en la documentación

Note:
(...) y... controlador. Como vemos, ambos frameworks tienen varios elementos en común.


---

TODO: diapositiva icono gracioso

---
@title[conflictos]

Elementos comunes entre ambos:

<table>
  <tr>
    <th>Django</th>
    <th>Angular</th>
  </tr>
  <tr>
    <td>...</td>
    <td>...</td>
  </tr>
  <tr>
    <td>Sistema de rutas</td>
    <td>Sistema de rutas</td>
  </tr>
  <tr>
    <td>Lenguaje de plantillas</td>
    <td>Lenguaje de plantillas</td>
  </tr>
  <tr>
    <td>Controladores</td>
    <td>Controladores</td>
  </tr>
</table>


Note:
Estos elementos son (...) ¿y ahora qué hacemos?


---
@title[clasico]

### Método clásico

Django se encarga de las rutas, las plantillas y los controladores (views).


Note:
Dejamos a Django encargarse de (...). Este método es muy popular en AngularJS, la primera versión de Angular.

---
@title[clasico-2]

Usado por Djangular (AngularJS). Se incluye AngularJS en templates de Django a demanda.

Este método puede usarse en Angular 2+ con SystemJS.


Note:
Es usado por ejemplo en Djangular, una biblioteca para AngularJS en Django. Ésta es la forma en que muchos 
nos encontrábamos acostumbrados. Un método similar se encontraba documentado para Angular 4 mediante SystemJS.  


---
@title[clasico-3]

```html
...

<!-- This SystemJS configuration loads umd packages 
     from the web -->
<script src="systemjs.config.server.js"></script>
 
 <script>
   System.import('main.js')
         .catch(function(err){ console.error(err); });
 </script>
```

Note:
Aquí encontramos un ejemplo.


---
@title[clasico-4]

Este método no es apropiado para Angular 2+:

* Su configuración y uso es complicada
* Requiere adaptación con cada módulo instalado
* Se pierden las características de Angular CLI
* Ya no se encuentra documentado

Note:
No obstante, este método puede ser frustrante si se está empezando con Angular, ya que (...). 
Eso nos deja una segunda opción.


---
@title[cli]

### Angular Cli

Angular se encarga de las rutas, las plantillas y los controladores (componentes).


Note:
Con este método, Angular se encarga de (...). Angular Cli es el método recomendado para Angular.


---
@title[cli-2]

### Características

* Gestión de configuración y paquetes
* Generar proyectos, componentes, servicios...
* Comprobación de código, tests
* Compilar (modos dev y prod.) y ejecución


Note:
Angular Cli tiene un montón de características interesantes. (...)


---
@title[cli-3]

### Guía rápida

1. Crear nuevo proyecto: `ng new my-app`
2. Iniciar proyecto: `ng serve --open`
3. ¡Listo!


Note:
Para crear un proyecto sólo tenemos que (...) e iniciamos el proyecto. Se compilará en tiempo real, se quedará 
el servidor de Angular escuchando a cambios y se abrirá un navegador con el proyecto.


---
@title[api]

### ¿Y dónde queda Django?

Ahora tenemos 2 servidores ejecutándose en desarrollo:

* `manage.py runserver` (Django) en el puerto 8000.
* `ng serve` (Angular) en el puerto 4200.

¿Cómo trabajar con ambas tecnologías a la vez?


Note:
Si antes sólo teníamos que ejecutar el servidor de Django, ahora también tenemos que tener en ejecución el de 
Angular mientras desarrollamos. ¿Pero cómo conectamos ambas tecnologías?

---
@title[api-2]

### Formas de conectar

* Django Rest Framework
* Django Channels
* Graphene Django (GraphQL)
* ... entre otros.


Note:
Django incluye varias bibiotecas para API, entre las que destacamos (...)

---
@title[drf]

### Django Rest Framework

* API Web navegable
* Potentes formas de serialización y autenticación
* Muy personalizable y adaptable
* Documentación automática
* Gran soporte y comunidad


Note:
Django Rest Framework es la biblioteca más popular por la comunidad. Ofrece una API REST, una 
solución fácil de usar y con buen soporte. Entre sus características destacamos (...)


---
@title[api-rest-ejemplo]

### Ejemplo

```typescript
export class HeroApiService {
    constructor(private http: HttpClient) { }

    // ...
    getHero(id: number): Observable<Hero> {
      const url = `/api/heroes/${id}/`;
      return this.http.get<Hero>(url).pipe(
        tap(_ => this.log(`fetched hero id=${id}`)),
        catchError(this.handleError<Hero>(`getHero id=${id}`))
      );
    }
}
```

Note:
Aquí podemos ver un ejemplo basado en el tutorial de Angular, de cómo obtener un objeto
Hero desde la API de Django. El código está en TypeScript, el lenguaje recomendado para 
Angular.


---
@title[proxy-1]

### Conectar cliente Angular a Django

El navegador ejecuta `http://localhost:4200`, pero la API de Django se encuentra accesible 
en `http://localhost:8000`. Para conectarlos de forma transparente, podemos usar proxies en 
el servidor de Angular.


---
@title[proxy-2]

---?code=src/proxy.conf.json&lang=json&title=Source: proxy.conf.json


---
@title[proxy-3]

---?code=src/package.json&lang=json&title=Source: package.json
