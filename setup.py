from pathlib import Path
from setuptools import setup

ROOT = Path(__file__).parent
FOLDERS = ['bin', 'input']
setup(
    name='vaspup2',
    version="0.0.0+archer2.20261015",
    description="Preserved customized vaspup2.0 command-line tools",
    python_requires=">=3.9",
    packages=['vaspup2_cli'],
    data_files=[
        ("share/vaspup2/" + folder,
         [str(p.relative_to(ROOT)) for p in sorted((ROOT / folder).iterdir()) if p.is_file()])
        for folder in FOLDERS
    ],
    entry_points={"console_scripts": [
        name + "=" + target for name, target in {'vaspup2': 'vaspup2_cli:main', 'checkforce': 'vaspup2_cli:main', 'data-converge': 'vaspup2_cli:main', 'data-converge-magnetic': 'vaspup2_cli:main', 'dfpt-data-converge': 'vaspup2_cli:main', 'generate-converge': 'vaspup2_cli:main', 'kgs_gen_kpts': 'vaspup2_cli:main', 'nbands-epsopt-data-converge': 'vaspup2_cli:main', 'nbands-generate-converge': 'vaspup2_cli:main', 'vaspup2-checkforce': 'vaspup2_cli:main', 'vaspup2-data-converge': 'vaspup2_cli:main', 'vaspup2-data-converge-magnetic': 'vaspup2_cli:main', 'vaspup2-dfpt-data-converge': 'vaspup2_cli:main', 'vaspup2-generate-converge': 'vaspup2_cli:main', 'vaspup2-kgs_gen_kpts': 'vaspup2_cli:main', 'vaspup2-nbands-epsopt-data-converge': 'vaspup2_cli:main', 'vaspup2-nbands-generate-converge': 'vaspup2_cli:main'}.items()
    ]},
)
