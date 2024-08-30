import os
from collections import defaultdict

def find_duplicates(static_dirs):
    file_map = defaultdict(list)
    for static_dir in static_dirs:
        for root, _, files in os.walk(static_dir):
            for file in files:
                relative_path = os.path.relpath(os.path.join(root, file), static_dir)
                file_map[relative_path].append(static_dir)
    
    duplicates = {path: dirs for path, dirs in file_map.items() if len(dirs) > 1}

    if duplicates:
        for path, dirs in duplicates.items():
            print(f'Arquivo "{path}" está presente em:')
            for d in dirs:
                print(f'  - {d}')
            print()
    else:
        print("Nenhum arquivo duplicado encontrado nas pastas estáticas de origem.")

if __name__ == "__main__":
    # Liste aqui todas as pastas estáticas do seu projeto
    static_dirs = [
        '/home/fabianosf/Desktop/asbjj_django/accounts/static',
        '/home/fabianosf/Desktop/asbjj_django/contact/static',
        '/home/fabianosf/Desktop/asbjj_django/core/static',
        # Adicione outras pastas estáticas conforme necessário
    ]

    find_duplicates(static_dirs)
