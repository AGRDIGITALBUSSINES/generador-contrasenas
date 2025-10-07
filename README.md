# 🔐 Generador de Contraseñas Flexibles

Un generador de contraseñas seguras con interfaz gráfica y modo consola, diseñado para ser compatible con diferentes sitios web y sus diversos requisitos de contraseñas.

## ✨ Características

- 🖥️ **Interfaz gráfica intuitiva** con tkinter
- 💻 **Modo consola** para uso desde terminal
- 🎛️ **Longitud personalizable** (10-50 caracteres)
- 📁 **Selección de ruta** de guardado
- 📋 **Copia al portapapeles** con un clic
- 🔒 **Seguridad criptográfica** usando `secrets`
- 🌐 **Compatible universalmente** con diferentes sitios web

## 🎯 Tipos de Caracteres Incluidos

- **Mayúsculas:** A-Z
- **Minúsculas:** a-z
- **Números:** 0-9
- **Símbolos:** * + - / @ _ ? ! ; . > < ~ ° ^ & $ #

## 🚀 Uso

### Interfaz Gráfica (Por defecto)
```bash
python generador_contrasena.py
```

### Modo Consola
```bash
python generador_contrasena.py --console
```

## 📋 Requisitos

- Python 3.6+
- tkinter (incluido en Python)
- Módulos estándar: `secrets`, `string`, `datetime`, `os`

## 💾 Funcionalidades

### 🖥️ Interfaz Gráfica
- Selector de longitud con spinbox
- Selección de carpeta de guardado
- Vista previa de resultados
- Botones para copiar, generar nueva y abrir carpeta
- Validación únicamente por longitud

### 💻 Modo Consola
- Generación rápida de contraseñas
- Guardado automático en `password.txt`
- Información detallada de la contraseña generada

## 📁 Archivos Generados

El programa crea un archivo `password.txt` con:
- La contraseña generada
- Longitud y fecha de generación
- Características de la contraseña
- Información de compatibilidad

## 🛡️ Seguridad

- Utiliza el módulo `secrets` de Python para generación criptográficamente segura
- Generación completamente aleatoria
- No almacena contraseñas en memoria después del uso

## 📖 Ejemplo de Salida

```
🔑 CONTRASEÑA GENERADA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contraseña: 4k&OSLEAR?
Longitud: 10 caracteres
Generada: 2025-10-06 20:31:39

📊 CARACTERÍSTICAS:
• Incluye mayúsculas, minúsculas, números y símbolos
• Generación completamente aleatoria
• Compatible con diferentes sitios web

🔐 ¡Contraseña lista para usar!
```

## 📝 Licencia

Este proyecto está disponible bajo la Licencia MIT.

## 👨‍💻 Autor

**Andrés G. Rodríguez**
- Web: [agrdb.com](https://agrdb.com)

---
⭐ ¡Si te resulta útil, no olvides darle una estrella al repositorio!