import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo9-addons-oca-l10n-morocco",
    description="Meta package for oca-l10n-morocco Odoo addons",
    version=version,
    install_requires=[
        'odoo9-addon-l10n_ma_state',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 9.0',
    ]
)
