# ✨ Yazumimoon y sus Pequitas ✨

Un adorable generador interactivo de pequeñitas (freckles) para la imagen de Yazumimoon, con una beautiful interfaz tipo drawing app que te permite pintar el área donde quieres que aparezcan las pecas.

## 🌟 Características

- **Interfaz Drawing App**: Imagen grande como foco principal, controles en el sidebar
- **Pincel de Selección**: Pinta el área específica donde quieres que aparezcan las pequitas
- **Pequeñitas Lindas**: Diseño soft, cute y anime-style que se mezcla naturalmente con la piel
- **Tamaños Variados**: Cada pequeña tiene tamaño único para efecto natural
- **Colores Personalizables**: 5 tonos marrón pastel para elegir
- **Descarga de Imagen**: Guarda el resultado final con todas las pequeñitas

## 🚀 Uso Local (con Servidor Python)

### Requisitos
- Python 3.x
- Navegador web moderno

### Instalación y Ejecución

```bash
# 1. Clona el repositorio
git clone https://github.com/tu-usuario/yazumimoon-pecas.git
cd yazumimoon-pecas

# 2. Ejecuta el servidor Python
python server.py

# 3. Abre en tu navegador
# Ve a http://localhost:8000
```

### Características del Servidor Local
- Obtiene el conteo de seguidores de NicheProwler en tiempo real
- Genera pequeñitas dinámicamente basado en el conteo exacto de followers
- Mejor rendimiento para archivos locales

## 🌐 Uso en GitHub Pages (Versión Estática)

El proyecto también está disponible como sitio estático sin necesidad de servidor backend. El servidor local es opcional y solo se usa para obtener el conteo dinámico de followers.

**Demo en vivo**: [Tu GitHub Pages URL aquí]

## 📖 Cómo Usar la Aplicación

1. **Observa la imagen**: Yazumimoon aparece en grande en el lado izquierdo
2. **Selecciona el área**:
   - Haz clic en "🖌️ Pincel de Área"
   - Pinta el área de la cara donde quieres pequeñitas
   - Verás un área roja mientras pintas
   - Haz clic en "✓ Finalizar Pincel"
3. **Personaliza las pequeñitas**:
   - Elige color: 5 tonos marrón suave
   - Ajusta tamaño: 2-10px
   - Regenera si quieres variación diferente
4. **Descarga**: Haz clic en "💾 Descargar Imagen" para guardar el resultado

## 🎨 Paleta de Colores

- **Marrón Oscuro** (#A0704D): Tonalidad clásica
- **Siena** (#A0522D): Calidez suave
- **Perú** (#CD853F): Caramel suave
- **Chocolate** (#D2691E): Rico y tierno
- **Dorado Oscuro** (#8B6914): Tono natural

## 📁 Estructura del Proyecto

```
yazumimoon-pecas/
├── index.html              # Aplicación principal
├── server.py               # Servidor backend Python (opcional)
├── yazu cerrada.png        # Imagen de Yazumimoon
├── README.md               # Este archivo
├── LICENSE                 # MIT License
└── .gitignore              # Archivos a ignorar en git
```

## 🔧 Tecnologías Utilizadas

- **Frontend**: HTML5, CSS3, Canvas API, JavaScript vanilla
- **Backend**: Python (http.server, urllib)
- **API de Datos**: NicheProwler Twitch Follower Checker
- **Hosting**: GitHub Pages (versión estática) + Python Server (desarrollo local)

## 🎯 Características Técnicas

### Frontend
- Canvas 2D para rendering de pequeñitas
- Máscara de selección con ImageData
- Gradientes radiales para efecto soft
- Event handling para pincel interactivo
- Descarga de canvas a PNG

### Backend (Opcional)
- HTTP Server personalizado
- Scraping de datos con regex
- Endpoint `/api/followers` para datos dinámicos
- URL decoding para soportar espacios en nombres de archivo

## 📝 Notas de Desarrollo

### Para Modificar la Imagen
Reemplaza `yazu cerrada.png` con tu propia imagen. El canvas se ajustará automáticamente.

### Para Cambiar los Colores de Pequeñitas
Edita el array `freckleColors` en el JavaScript (alrededor de línea 410):
```javascript
const freckleColors = [
    '#A0704D', // Warm taupe
    '#B8845C', // Soft tan
    // ... más colores
];
```

### Para Ajustar Tamaños de Pequeñitas
Modifica estos valores en `generateFreckles()`:
```javascript
const size = 1.5 + Math.random() * 2.5; // Mín: 1.5, Máx: 4
const opacity = 0.4 + Math.random() * 0.4; // Mín: 0.4, Máx: 0.8
```

## 🐛 Troubleshooting

### El servidor Python no inicia
```bash
# Verifica que Python está instalado
python --version

# Intenta con python3
python3 server.py
```

### La imagen no carga en GitHub Pages
- Asegúrate de que `yazu cerrada.png` está en el repositorio
- Verifica que el nombre del archivo es exacto (las mayúsculas importan)
- Usa `/yazu%20cerrada.png` en la URL (espacio codificado)

### Los freckles no aparecen donde los pinté
- Asegúrate de pintar con el pincel activado (botón verde)
- El área debe ser lo suficientemente grande
- Intenta "Resetear Todo" y vuelve a pintar

## 📄 Licencia

MIT License - Siéntete libre de usar, modificar y compartir este proyecto.

## 👤 Autor

Creado con 💖 para Yazumimoon y sus fans

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📞 Contacto y Soporte

Si encuentras bugs o tienes sugerencias, abre un Issue en GitHub.

---

**Hecho con 💖 para Yazumimoon y sus fans** ✨
