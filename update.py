import re

SVG_ICON = '''<svg class="w-5 h-5 fill-current" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>'''

def update_html_file(filepath, theme):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update glass-card styling for better effect
    old_glass_card = """.glass-card {
            background: rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .glass-card:hover {
            border-color: rgba(212, 175, 55, 0.4);
            transform: translateY(-5px);
            box-shadow: 0 20px 40px -10px rgba(212, 17, 50, 0.2);
        }"""
    
    new_glass_card = """.glass-card {
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: inset 0 0 20px rgba(212, 17, 50, 0.05);
        }

        .glass-card:hover {
            border-color: rgba(212, 175, 55, 0.6);
            transform: translateY(-5px);
            box-shadow: 0 20px 40px -10px rgba(212, 17, 50, 0.6), inset 0 0 30px rgba(212, 17, 50, 0.2);
        }"""
    content = content.replace(old_glass_card, new_glass_card)

    # 2. Fix service 6 image (replace bg-slate-800 with image tags)
    old_bg_div = '<div class="w-full h-full bg-slate-800 opacity-40"></div>'
    if theme == 'amor':
        new_img = '<img alt="Limpias Espirituales" class="w-full h-full object-cover opacity-40 group-hover:opacity-60 group-hover:scale-110 transition duration-700" loading="lazy" src="recursos/amor/amor1.webp" />'
        content = content.replace(old_bg_div, new_img)
    elif theme == 'pactos':
        new_img = '<img alt="Destrucción de Bloqueos" class="w-full h-full object-cover opacity-40 group-hover:opacity-60 group-hover:scale-110 transition duration-700" loading="lazy" src="recursos/pactos/pactos1.webp" />'
        content = content.replace(old_bg_div, new_img)

    # 3. Add SVG and solid fill to specific buttons
    
    # Hero CTA
    content = content.replace('Consulta Gratuita\n                        <span class="material-symbols-outlined text-sm">chat</span>', f'{SVG_ICON}\n                        Consulta Gratuita')
    content = content.replace('shadow-[0_0_20px_rgba(212,17,50,0.5)] flex', 'shadow-[0_0_20px_rgba(212,17,50,0.5)] hover:shadow-[0_0_40px_rgba(212,17,50,0.8)] flex')

    # Authority Split CTA
    # From: <a class="wa-conversion-btn inline-flex items-center text-gold hover:text-white font-medium gap-2 group transition-colors"
    # To solid bg btn
    auth_span = 'Contáctanos Ahora\n                            <span\n                                class="material-symbols-outlined group-hover:translate-x-1 transition-transform">arrow_right_alt</span>'
    content = content.replace(auth_span, f'{SVG_ICON}\n                            Contáctanos Ahora\n                            <span class="material-symbols-outlined group-hover:translate-x-1 transition-transform">arrow_right_alt</span>')
    content = content.replace('inline-flex items-center text-gold hover:text-white font-medium gap-2 group transition-colors', 'inline-flex bg-primary hover:bg-red-700 text-white font-bold py-3 px-8 rounded-full shadow-[0_0_20px_rgba(212,17,50,0.5)] hover:shadow-[0_0_30px_rgba(212,17,50,0.7)] transition-all items-center gap-2 group')

    # Final CTA
    final_span_1 = 'href="https://wa.me/19123037943?text=Deseo%20ayuda%20inmediata%20con%20mi%20pareja." target="_blank">\n                Atención Inmediata Vía WhatsApp'
    final_span_2 = 'href="https://wa.me/19123037943?text=Deseo%20ayuda%20inmediata%20con%20mi%20pareja." target="_blank">\n                ' + SVG_ICON + '\n                Atención Inmediata Vía WhatsApp'
    if final_span_1 in content:
        content = content.replace(final_span_1, final_span_2)
        content = content.replace('hover:scale-105"', 'hover:scale-105 gap-3"')

    final_span_3 = 'href="https://wa.me/19123037943?text=Deseo%20ayuda%20inmediata%20para%20obtener%20riqueza%20y%20poder." target="_blank">\n                Iniciación Exclusiva Vía WhatsApp'
    final_span_4 = 'href="https://wa.me/19123037943?text=Deseo%20ayuda%20inmediata%20para%20obtener%20riqueza%20y%20poder." target="_blank">\n                ' + SVG_ICON + '\n                Iniciación Exclusiva Vía WhatsApp'
    if final_span_3 in content:
        content = content.replace(final_span_3, final_span_4)
        content = content.replace('hover:scale-105"', 'hover:scale-105 gap-3"')

    # Fix service card buttons (which have "text-primary" currently):
    # Need to convert them to fully filled buttons and ensure ALL 6 have one.
    # To do this safely, we will replace the inner text of service descriptions to append a button if they lack one. 
    # Alternatively, regex replace all end-of-service texts.
    
    # Existing buttons:
    content = content.replace('Consultar <span class="material-symbols-outlined text-sm ml-1">arrow_outward</span>', f'{SVG_ICON} Consultar')
    content = content.replace('Consultar Precio <span class="material-symbols-outlined text-sm ml-1">arrow_outward</span>', f'{SVG_ICON} Consultar Precio')
    content = content.replace('text-primary font-bold hover:text-white transition-colors', 'justify-center bg-primary hover:bg-red-700 text-white font-bold py-2 px-6 rounded-full shadow-[0_0_15px_rgba(212,17,50,0.4)] hover:shadow-[0_0_30px_rgba(212,17,50,0.7)] transition-all gap-2 mt-4 w-full md:w-fit')

    # Add buttons to those that lack it. We look for closed <p> tags inside relative z-10 inside glass-card that do NOT have a button.
    # This is slightly tricky, we can do it by finding <div class="relative z-10">...</div>
    import re
    def add_button_if_missing(match):
        block = match.group(0)
        # Check if it has a wa-conversion-btn already
        if "wa-conversion-btn" not in block:
            # We insert the button right before the closing </div>
            msg = "Quiero consultar este servicio."
            if "pactos" in theme:
                msg = "Quiero consultar este pacto."
            
            # Since the text is right inside a p block, we add it after </p>
            btn = f'''
                        <a class="wa-conversion-btn inline-flex items-center justify-center bg-primary hover:bg-red-700 text-white font-bold py-2 px-6 rounded-full shadow-[0_0_15px_rgba(212,17,50,0.4)] hover:shadow-[0_0_30px_rgba(212,17,50,0.7)] transition-all gap-2 mt-4 w-full md:w-fit"
                            href="https://wa.me/19123037943?text={msg}" target="_blank">
                            {SVG_ICON}
                            Consultar
                        </a>'''
            # Add some margin bottom to the <p> if it lacks it
            block = block.replace('text-xs">', 'text-sm mb-4">')
            return block.replace('</p>', '</p>' + btn)
        else:
            return block

    content = re.sub(r'<div class="relative z-10">([\s\S]*?)</div>', add_button_if_missing, content)

    # Quick logo patch for pactos
    if theme == 'pactos':
        content = content.replace('src="recursos/logos/logo.png"', 'src="recursos/pactos/pactos2.webp"')
        content = content.replace('alt="Símbolo místico de unión y amor incondicional"', 'alt="Símbolo de Riqueza y Poder"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

update_html_file(r'c:\Ankharot\jhon2-ank\index.html', 'amor')
update_html_file(r'c:\Ankharot\jhon2-ank\pactos.html', 'pactos')
