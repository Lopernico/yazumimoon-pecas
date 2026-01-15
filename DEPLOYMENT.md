# 📦 Instrucciones de Deployment a GitHub

## Paso 1: Preparar tu Repositorio

### A. Limpiar archivos innecesarios

Elimina estos archivos que son solo de desarrollo:
- `debug_api.html`
- `debug_livecounts.html`
- `debug_twitchtracker.html`
- `pipo.html`

Estos no son necesarios en GitHub.

### B. Verificar la estructura

Tu carpeta debe tener esta estructura:

```
yazumimoon-pecas/
├── index.html              ← Versión con servidor Python
├── docs/
│   └── index.html          ← Versión para GitHub Pages
├── server.py               ← Backend Python
├── yazu cerrada.png        ← Imagen principal
├── README.md               ← Documentación principal
├── QUICKSTART.md           ← Guía rápida
├── GITHUB_PAGES.md         ← Guía de deployment
├── LICENSE                 ← MIT License
└── .gitignore              ← Archivos a ignorar
```

## Paso 2: Crear el Repositorio en GitHub

1. Ve a [github.com/new](https://github.com/new)
2. **Repository name**: `yazumimoon-pecas`
3. **Description**: `Adorable freckles generator for Yazumimoon - Interactive drawing app`
4. **Public** (para que GitHub Pages sea gratuito)
5. NO inicialices con README (ya lo tienes)
6. Haz clic en "Create repository"

## Paso 3: Subir tu Código

```bash
# Navega a tu carpeta del proyecto
cd "c:\Users\oswal\Downloads\Yazumimoon y sus pecas"

# Inicializa git si no está ya hecho
git init

# Agrega todos los archivos
git add .

# Haz el primer commit
git commit -m "Initial commit: Yazumimoon freckles generator"

# Conecta con tu repositorio remoto
git remote add origin https://github.com/tu-usuario/yazumimoon-pecas.git

# Sube a GitHub
git branch -M main
git push -u origin main
```

**Reemplaza `tu-usuario` con tu nombre de usuario de GitHub**

## Paso 4: Configurar GitHub Pages

1. Ve a tu repositorio en GitHub
2. Haz clic en **Settings** (esquina superior derecha)
3. En el menú izquierdo, selecciona **Pages**
4. En "Source":
   - **Branch**: `main`
   - **Folder**: `/docs` (importante!)
5. Haz clic en **Save**

## Paso 5: Esperar al Despliegue

1. Espera 1-2 minutos
2. GitHub Pages te mostrará un mensaje: "Your site is published at..."
3. Haz clic en el link para ver tu sitio en vivo

**Tu URL será**: `https://tu-usuario.github.io/yazumimoon-pecas`

## Paso 6: Actualizar tu README

En GitHub, edita el archivo README.md para agregar:

```markdown
## 🌐 Demo en Vivo

**Juega ahora**: [https://tu-usuario.github.io/yazumimoon-pecas](https://tu-usuario.github.io/yazumimoon-pecas)
```

## Verificación Final

- [ ] Repositorio creado en GitHub
- [ ] Código subido (git push)
- [ ] GitHub Pages configurado en `/docs`
- [ ] El sitio está disponible en tu URL
- [ ] La imagen carga correctamente
- [ ] El pincel funciona
- [ ] Se pueden descargar las imágenes

## Cambios Futuros

Para hacer cambios:

```bash
# 1. Haz tus cambios
# 2. Comprueba localmente (si tienes servidor)
# 3. Sube a GitHub

git add .
git commit -m "Descripción de los cambios"
git push origin main

# GitHub Pages se actualizará automáticamente en 1-2 minutos
```

## Opciones Avanzadas

### Usar un dominio personalizado

Si tienes un dominio (ej: pequitas.com):

1. En Settings → Pages → Custom domain
2. Ingresa tu dominio
3. Actualiza los registros DNS de tu registrador
4. GitHub verificará automáticamente

### Configurar CNAME (DNS)

Para que GitHub Pages reconozca tu dominio:
- **A**: Señala a `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
- **CNAME**: `tu-usuario.github.io`

## Solución de Problemas

### "GitHub Pages no aparece"
- Verifica que está en `/docs`
- Espera 2-3 minutos
- Limpia el caché (Ctrl+Shift+Del)
- Recarga: Ctrl+F5

### "Imagen en 404"
- Verifica que `yazu cerrada.png` está en el repositorio
- El nombre debe ser exacto (incluidas mayúsculas y espacios)
- Usa URL encoded: `/yazu%20cerrada.png`

### "Mi sitio no se ve bien"
- Abre DevTools (F12)
- Verifica errores en la consola
- Comprueba que todos los archivos cargan

## Compartir tu Proyecto

¡Ahora puedes compartir!

```
¡Mira lo que hice! 🎨✨
https://tu-usuario.github.io/yazumimoon-pecas

Generador adorable de pequeñitas para Yazumimoon
```

## Próximos Pasos

- Comparte en redes sociales
- Envía el link en Discord
- Contribuye mejoras
- Agrega más características

---

**¡Felicidades! Tu proyecto está en GitHub Pages!** 🎉

Para más info, lee:
- [README.md](README.md) - Documentación completa
- [QUICKSTART.md](QUICKSTART.md) - Guía rápida
- [GITHUB_PAGES.md](GITHUB_PAGES.md) - Detalles técnicos
