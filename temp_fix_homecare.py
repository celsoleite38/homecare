from pathlib import Path

targets = {
    'config/urls.py': {
        'replace': "if settings.DEBUG:\n    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\n\nif settings.DEBUG:\n    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)",
        'with': "if settings.DEBUG:\n    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"
    }
}

base = Path('d:/python nutry-lab/projetos-python/homecare')
for relative, data in targets.items():
    path = base / relative
    text = path.read_text(encoding='utf-8')
    new_text = text.replace(data['replace'], data['with'])
    path.write_text(new_text, encoding='utf-8')
