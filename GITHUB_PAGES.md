# 🚀 Guía de Despliegue en GitHub Pages

## Configuración Rápida

### Opción 1: Usando la carpeta `docs/` (Recomendado)

1. El archivo `docs/index.html` ya está configurado para GitHub Pages
2. Ve a tu repositorio en GitHub
3. Ve a **Settings → Pages**
4. En "Source", selecciona:
   - Branch: `main` (o la rama que uses)
   - Folder: `/docs`
5. Haz clic en "Save"
6. Tu sitio estará disponible en: `https://tu-usuario.github.io/yazumimoon-pecas`

### Opción 2: Usando la raíz del repositorio

1. Renombra `index.html` (en la raíz) o copia el contenido a la raíz
2. Ve a **Settings → Pages**
3. En "Source", selecciona:
   - Branch: `main`
   - Folder: `/ (root)`
4. Tu sitio estará disponible en: `https://tu-usuario.github.io/yazumimoon-pecas`

## Estructura del Proyecto para GitHub

```
tu-repositorio/
├── index.html              # Versión principal (interactiva)
├── docs/
│   └── index.html          # Versión para GitHub Pages
├── server.py               # Servidor Python (desarrollo local)
├── yazu cerrada.png        # Imagen principal
├── README.md               # Documentación
├── LICENSE                 # MIT License
├── .gitignore              # Archivos a ignorar
└── GITHUB_PAGES.md         # Este archivo
```

## Diferencias Entre Versiones

### `index.html` (Raíz)
- ✅ Funciona con servidor Python (`server.py`)
- ✅ Obtiene seguidores en tiempo real desde NicheProwler
- ✅ Mejor para desarrollo local
- ❌ No funciona en GitHub Pages (sin servidor)

### `docs/index.html`
- ✅ Funciona sin servidor (completamente estático)
- ✅ Perfecta para GitHub Pages
- ✅ Follower count hardcodeado a 207
- ⚠️ No se actualiza automáticamente

## Actualizar Follower Count en la Versión Static

Si el contador de seguidores cambia, edita `docs/index.html`:

```javascript
// Línea ~320
let followerCount = 207; // Cambia este número
```

O en el HTML:
```html
<!-- Línea ~68 -->
<span id="freckle-count">207</span> pequeñitas
```

## Cómo Clonar y Desplegar

### Para contribuidores:

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/yazumimoon-pecas.git
cd yazumimoon-pecas

# Desarrollo local
python server.py
# Abre http://localhost:8000

# Hacer cambios
git add .
git commit -m "Descrip de cambios"
git push origin main
```

### Para usuarios (solo GitHub Pages):
- Solo necesitan acceder a: `https://tu-usuario.github.io/yazumimoon-pecas`
- No requiere instalación local

## Actualizaciones Futuras

### Opción A: Usar GitHub Actions
Crear un workflow para actualizar automáticamente el contador:

```yaml
# .github/workflows/update-followers.yml
name: Update Follower Count
on:
  schedule:
    - cron: '0 */6 * * *' # Cada 6 horas
jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Update count
        run: |
          # Script para obtener follower count
          # y actualizar docs/index.html
```

### Opción B: Usar API externa
Reemplazar la lógica para obtener seguidores desde una API pública que soporte CORS.

## Troubleshooting

### "GitHub Pages no se actualiza después de push"
- Espera 1-2 minutos
- Verifica que el branch y folder correctos están seleccionados
- Limpia el caché del navegador (Ctrl+Shift+Del)

### "La imagen no carga en GitHub Pages"
- Verifica que `yazu cerrada.png` está en el repositorio
- El nombre debe ser exacto (mayúsculas importan)
- GitHub Pages respeta el nombre exacto del archivo

### "El CSS no se aplica"
- Verifica que los caminos relativos son correctos
- Limpia el caché del navegador
- Usa DevTools (F12) para verificar errores

## Configuración Personalizada

### Cambiar la URL del repositorio
En los archivos HTML y markdown, reemplaza:
- `tu-usuario` por tu usuario de GitHub real
- `yazumimoon-pecas` por el nombre de tu repositorio

### Cambiar la imagen
1. Reemplaza `yazu cerrada.png` con tu imagen
2. Actualiza la ruta en HTML si cambias el nombre:
   ```html
   <img id="main-image" src="tu-imagen.png" alt="Yazumimoon">
   ```

### Personalizar el footer
Edita el texto del footer en ambos archivos HTML

## Métricas y Monitoreo

### Ver estadísticas de GitHub Pages
1. Ve a **Settings → Pages**
2. Verás información sobre visitas y despliegue
3. Haz clic en "View deployment" para ver el historial

## Dominios Personalizados

Para usar un dominio personalizado:
1. Ve a **Settings → Pages**
2. En "Custom domain", ingresa tu dominio
3. Configura los registros DNS de tu proveedor
4. GitHub verificará automáticamente

## Buenas Prácticas

- ✅ Mantén el README.md actualizado
- ✅ Usa descriptiones claras en los commits
- ✅ Testa cambios localmente antes de pushear
- ✅ Documenta cambios en el CHANGELOG
- ✅ Responde issues y pull requests

## Soporte y Contacto

Si tienes problemas:
1. Revisa los logs de GitHub Actions (si usas)
2. Abre un Issue describiendo el problema
3. Incluye capturas de pantalla si es relevante

---

**¡Tu proyecto está listo para compartir con el mundo!** 🌍✨
