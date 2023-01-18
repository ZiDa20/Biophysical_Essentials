from qt_material import export_theme


if __name__ == '__main__':
    export_theme(theme='light_blue.xml',
                 qss='light_blue.qss',
                 rcc='resources.rcc',
                 output='theme',
                 prefix='icon:/',
                 invert_secondary=False,
                 )